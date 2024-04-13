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

resource "google_project_service" "this" {
  project = google_project.this.project_id
  service = "compute.googleapis.com"  # auto set: https://console.cloud.google.com/apis/dashboard
}
