provider "google" {
  region  = "europe-west1"
#   zone    = "europe-west1-b"
}

resource "random_string" "project_id" {
  length   = 16 
  special  = false
  upper    = false
  numeric  = true
}

resource "google_project" "this" {
  name            = "CloudComputingProject"
  project_id      = "ccp-${random_string.project_id.result}"
  billing_account = "019369-8CFC89-7725FB"
}

resource "google_sql_database_instance" "this" {
  name                = "instance-name"
  database_version    = "POSTGRES_15"
  deletion_protection = false
  project             = google_project.this.project_id

  settings {
    tier = "db-f1-micro"
  }
}

resource "google_sql_database" "this" {
  name     = "CloudComputingDatabase"
  instance = google_sql_database_instance.this.name
  project  = google_project.this.project_id
}

resource "google_sql_user" "users" {
  name     = "Admin"
  instance = google_sql_database_instance.this.name
  password = "TestPa$$word123"
  project  = google_project.this.project_id
}
