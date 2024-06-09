# Terraform resources
### Files
providers.tf
- google
- postgresql

main.tf
- google_project (this) - creating google project
- google_project_service (compute) - enabling Computer Engine API
- google_project_service (sqladmin) - enabling SQL API
- google_project_service (dns) - enabling cloud DNS API
- random_string (project_id) - project id generator

database.tf
- google_sql_database_instance (this) - creating sql server
- google_sql_database (this) - creating sql database
- google_sql_user (admin) - creating sql admin account
- google_dns_managed_zone (this) - enabling connect to database
- google_dns_record_set (this) - creating dns name for database

vm.tf
- google_compute_address (this) - creating vm address for dependencies
- google_compute_instance (this) - creating virtual machine with django server
- google_compute_firewall (this) - creating vm firewall settings

# Main terraform commands
### 1. terraform init
Initialize terraform environment

### 2. terraform plan
Check what will be created, changed and deleted after applying the code

### 3. terraform apply
Apply all changes from code

### 4. terraform destroy
Delete all objects from the code


# Database connection
From your local machine set gcloud project id:
```bash
gcloud config set project <PROJECT-ID>
```

Then check database IP (second one result after semicolon):
```bash
gcloud sql instances describe instance-name --format="get(ipAddresses.ipAddress)"
```

From VM type command:
```bash
psql -h <DATABASE-IP> -d CloudComputingDatabase -U Admin -p 5432
```
