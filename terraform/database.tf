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

# data "external" "initialize_database" {
#   program = ["bash", "${path.module}/schema.sh"]

#   query = {
#     host     = google_sql_database_instance.this.private_ip_address
#     user     = google_sql_user.admin.name
#     password = google_sql_user.admin.password
#     dbname   = google_sql_database.this.name
#   }
# }

# PGPASSWORD="TestPa$$word123" psql -h "34.77.56.42" -U "Admin" -d "CloudComputingDatabase" -c "SELECT 1"
