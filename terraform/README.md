# Terraform resources
### Files
providers.tf
- google
- postgresql

main.tf
- google_project (this) - creating google project
- google_project_service (this) - enabling Computer Engine API
- random_string (project_id) - project id generator

database.tf
- google_sql_database_instance (this) - creating sql server
- google_sql_database (this) - creating sql database
- google_sql_user (admin) - creating sql admin account
- something for building tables - TODO

vm.tf
- google_compute_instance (this) - creating virtual machine with django server
- google_compute_firewall (this) - creating vm firewall settings

schema.sh
- users create table query
- notes create table query
- shared_notes create table query


# Main terraform commands
### 1. terraform init
Initialize terraform environment

### 2. terraform plan
Check what will be created, changed and deleted after applying the code

### 3. terraform apply
Apply all changes from code

### 4. terraform destroy
Delete all objects from the code
