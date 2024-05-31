data "google_compute_zones" "this" {
  project = google_project.this.project_id
  region  = "europe-west1"

  depends_on = [google_project_service.compute]
}

data "google_client_openid_userinfo" "me" {
}

resource "google_compute_address" "vm_address" {
  name   = "vm-static-ip"
  region = "europe-west1"
  project = google_project.this.project_id

  depends_on = [google_project_service.compute]
}

resource "google_compute_instance" "this" {
  name         = "django-vm"
  machine_type = "c2d-highcpu-2"  # All Compute Engines: https://cloud.google.com/compute/all-pricing
  zone         = data.google_compute_zones.this.names[0]
  project      = google_project.this.project_id

  depends_on = [google_project_service.compute]

  boot_disk {
    initialize_params {
      image = "debian-10-buster-v20240312"
    }
  }

 network_interface {
    network = "default"
    access_config {
      nat_ip = google_compute_address.vm_address.address
    }
  }

  metadata = {
    "enable-oslogin" = "FALSE",  # To connecting with ssh
    # ssh-keys = "root:${file("~/.ssh/id_rsa.pub")}"
    ssh-keys = "root:${file("C:/Users/Studia/.ssh/id_rsa.pub")}"
  }

  # I know it is ugly. However it works only in this way
  metadata_startup_script = "sudo apt-get update;sudo apt-get install -y python3-pip python3-dev git libpq-dev;sudo pip3 install virtualenv;sudo apt-get install -y postgresql-client;PGPASSWORD='TestPa$$word123' psql -h ${google_sql_database_instance.this.public_ip_address} -d CloudComputingDatabase -U Admin -p 5432 -c \"CREATE TABLE IF NOT EXISTS users (id_user SERIAL PRIMARY KEY,username TEXT NOT NULL,email TEXT NOT NULL,pass_hash TEXT NOT NULL);CREATE TABLE IF NOT EXISTS notes (id_note SERIAL PRIMARY KEY,id_user INT NOT NULL REFERENCES users(id_user),content TEXT NOT NULL,created_at TIMESTAMP NOT NULL DEFAULT now(),updated_at TIMESTAMP NOT NULL DEFAULT now());CREATE TABLE IF NOT EXISTS shared_notes (id_shared SERIAL PRIMARY KEY,id_user INT NOT NULL REFERENCES users(id_user),id_note INT NOT NULL REFERENCES notes(id_note),shared_at TIMESTAMP NOT NULL DEFAULT now(),permission_type TEXT NOT NULL);\";sudo git clone https://github.com/LJaremek/CloudComputing-MINI.git /opt/CloudComputing-MINI;cd /opt/CloudComputing-MINI/shared_notes;sudo python3 -m virtualenv venv;source venv/bin/activate;sudo pip3 install -r requirements.txt;echo '${google_sql_database_instance.this.public_ip_address} db.djangopostgresql.com' | sudo tee -a /etc/hosts;sudo nohup python3 manage.py runserver 0.0.0.0:8000 &"
  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro", "sql-admin"]
  }
}

resource "google_compute_firewall" "this" {
  name    = "allow-http-https"
  network = "default"
  project = google_project.this.project_id

  depends_on = [google_project_service.compute]

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "8000", "5432"]
  }

  source_ranges = ["0.0.0.0/0"]  # Pozwala na ruch z dowolnego adresu IP
}
