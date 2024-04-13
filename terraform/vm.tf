resource "google_compute_instance" "this" {
  name         = "django-vm"
  machine_type = "f1-micro"
  zone         = "europe-west1-b"
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
    ssh-keys = "root:${file("~/.ssh/id_rsa.pub")}"
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    exec > /var/log/startup.log 2>&1  # Przekierowanie stdout i stderr do pliku logów

    echo "Aktualizacja listy pakietów..."
    sudo apt-get update

    echo "Instalacja Pythona i Git..."
    sudo apt-get install -y python3-pip python3-dev git

    echo "Instalacja i konfiguracja virtualenv..."
    sudo pip3 install virtualenv

    echo "Klonowanie repozytorium..."
    sudo git clone https://github.com/LJaremek/CloudComputing-MINI.git /opt/CloudComputing-MINI
    cd /opt/CloudComputing-MINI/shared_notes

    echo "Tworzenie środowiska wirtualnego i jego aktywacja..."
    sudo python3 -m virtualenv venv
    source venv/bin/activate

    echo "Instalacja zależności..."
    sudo pip3 install -r requirements.txt

    echo "Uruchamianie serwera Django..."
    sudo nohup python3 manage.py runserver 0.0.0.0:8000 &
  EOF

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
