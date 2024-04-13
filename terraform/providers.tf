terraform {
  required_providers {
    postgresql = {
      source  = "cyrilgdn/postgresql"
      version = ">= 1.0"
    }
  }
}

provider "google" {
  region = "europe-west1"
  zone   = "europe-west1-b"
}

provider "postgresql" {
  host            = google_sql_database_instance.this.public_ip_address
  port            = 5432
  username        = google_sql_user.admin.name
  password        = google_sql_user.admin.password
  sslmode         = "require"
  connect_timeout = 15
  alias           = "db"
}
