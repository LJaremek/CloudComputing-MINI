data "google_compute_zones" "this" {
  project = google_project.this.project_id
  region  = "europe-west1"
  # status  = "UP"

  depends_on = [google_project_service.this]
}

data "google_client_openid_userinfo" "me" {
}

resource "google_compute_instance" "this" {
  name         = "django-vm"
  # All Compute Engines: https://cloud.google.com/compute/all-pricing
  machine_type = "c2d-highcpu-2"  # "e2-medium"
  zone         = data.google_compute_zones.this.names[0]
  project      = google_project.this.project_id

  depends_on = [google_project_service.this]

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
    "enable-oslogin" = "FALSE",  # To connecting with ssh
    # ssh-keys = "root:${file("~/.ssh/id_rsa.pub")}"
    ssh-keys = "root:${file("C:/Users/Studia/.ssh/id_rsa.pub")}"
  }

  # I know it is ugly. However it works only in this way
  metadata_startup_script = "sudo apt-get update;sudo apt-get install -y python3-pip python3-dev git;sudo pip3 install virtualenv;sudo git clone https://github.com/LJaremek/CloudComputing-MINI.git /opt/CloudComputing-MINI;cd /opt/CloudComputing-MINI/shared_notes;sudo python3 -m virtualenv venv;source venv/bin/activate;sudo pip3 install -r requirements.txt;sudo nohup python3 manage.py runserver 0.0.0.0:8000 &"

  service_account {
    scopes = ["userinfo-email", "compute-ro", "storage-ro", "sql-admin"]
  }
}

resource "google_compute_firewall" "this" {
  name    = "allow-http-https"
  network = "default"
  project = google_project.this.project_id

  depends_on = [google_project_service.this]

  allow {
    protocol = "tcp"
    ports    = ["80", "443", "8000"]
  }

  source_ranges = ["0.0.0.0/0"]  # Pozwala na ruch z dowolnego adresu IP
}
