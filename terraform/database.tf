resource "google_sql_database_instance" "this" {
  name                = "instance-name"
  database_version    = "POSTGRES_15"
  deletion_protection = false
  project             = google_project.this.project_id

  settings {
    tier = "db-f1-micro"

    ip_configuration {
      ipv4_enabled = true
      require_ssl  = false
      authorized_networks {
        name  = "VM-to-SQL"
        value = "${google_compute_address.vm_address.address}/32"
      }
    }
  }
}

resource "google_sql_database" "this" {
  name     = "CloudComputingDatabase"
  instance = google_sql_database_instance.this.name
  project  = google_project.this.project_id
}

resource "google_sql_user" "admin" {
  name     = "Admin"
  instance = google_sql_database_instance.this.name
  password = "TestPa$$word123"
  project  = google_project.this.project_id
}

resource "google_dns_managed_zone" "this" {
  project  = google_project.this.project_id
  name     = "django-postgresql-zone"
  dns_name = "djangopostgresql.com."

  depends_on = [google_project_service.dns]
}

resource "google_dns_record_set" "this" {
  project      = google_project.this.project_id
  name         = "db.djangopostgresql.com."
  type         = "A"
  ttl          = 300
  managed_zone = google_dns_managed_zone.this.name

  rrdatas = [google_sql_database_instance.this.public_ip_address]
}
