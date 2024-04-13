resource "google_compute_instance" "this" {
  name         = "django-vm"
  machine_type = "f1-micro"
  zone         = "europe-west1-b"
  project      = google_project.this.project_id

  boot_disk {
    initialize_params {
      image = "debian-10-buster-v20240312"
    }
  }

  network_interface {
    network = "default"
    access_config {
    }
  }

  metadata = {
    ssh-keys = "root:${file("~/.ssh/id_rsa.pub")}"
  }

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro", "sql-admin"]
  }
}

resource "google_compute_firewall" "this" {
  name    = "allow-http-https"
  network = "default"
  project = google_project.this.project_id

  allow {
    protocol = "tcp"
    ports    = ["80", "443"]
  }

  source_ranges = ["0.0.0.0/0"]  # Pozwala na ruch z dowolnego adresu IP
}

# resource "google_sql_database_instance" "this" {
#   name             = "instance-name"
#   database_version = "POSTGRES_15"
#   region           = "europe-west1"
#   project          = google_project.this.project_id

#   settings {
#     tier = "db-f1-micro"

#     ip_configuration {
#       ipv4_enabled = true
#       require_ssl  = true
#     }
#   }
# }
