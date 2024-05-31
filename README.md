# Cloud Computing repo
Project on "Cloud Computing". </br>
The main task was to create a program using terraform and Google Cloud. </br>
The project must have a database/storage and some sort of virtual machines/microservices.

## Repo tree
```
.
├───documentation       
│   └───README.md       <- project diagrams documentation
│
├───shared_notes        <- django (backend+fronted)
│   └───api             <- backend
│       └───README.md   <- documentation of endpoints
│
├───terraform           <- terraform code
│   └───README.md       <- terraform resources documentation
│
└───README.md           <- project documentation
```

## How to run project
#### 1. Install requirements
* Terraform: https://developer.hashicorp.com/terraform/install
* Google Cloud: https://cloud.google.com/sdk/docs/install

#### 2. Authenticate yourself
Google Cloud:
```bash
gcloud auth login
gcloud auth application-default login
```

SSH key:
```bash
ssh-keygen
```

#### 3. Get the project files
Cone repo:
```bash
git clone https://github.com/LJaremek/CloudComputing-MINI.git
```

Enter the terraform directory:
```bash
cd CloudComputing-MINI/terraform
```

#### 4. Build project
Run terraform init and apply
```bash
terraform init
terraform apply
```
