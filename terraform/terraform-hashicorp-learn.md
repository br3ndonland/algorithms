# HashiCorp Learn: Terraform - Get started (AWS)

https://learn.hashicorp.com/collections/terraform/aws-get-started

## Lessons

### Introduction to Infrastructure as Code with Terraform

> Terraform is the infrastructure as code tool from HashiCorp. It is a tool for building, changing, and managing infrastructure in a safe, repeatable way. Operators and Infrastructure teams can use Terraform to manage environments with a configuration language called the HashiCorp Configuration Language (HCL) for human-readable, automated deployments.
>
> #### Infrastructure as Code
>
> If you are new to infrastructure as code as a concept, it is the process of managing infrastructure in a file or files rather than manually configuring resources in a user interface. A resource in this instance is any piece of infrastructure in a given environment, such as a virtual machine, security group, network interface, etc.
>
> At a high level, Terraform allows operators to use HCL to author files containing definitions of their desired resources on almost any provider (AWS, GCP, GitHub, Docker, etc) and automates the creation of those resources at the time of apply.
>
> #### Workflows
>
> A simple workflow for deployment will follow closely to the steps below. We will go over each of these steps and concepts more in-depth throughout these tutorials, so don't panic if you don't understand the concepts immediately.
>
> 1. Scope - Confirm what resources need to be created for a given project.
> 2. Author - Create the configuration file in HCL based on the scoped parameters
> 3. Initialize - Run terraform init in the project directory with the configuration files. This will download the correct provider plug-ins for the project.
> 4. Plan & Apply - Run terraform plan to verify creation process and then terraform apply to create real resources as well as state file that compares future changes in your configuration files to what actually exists in your deployment environment.
>
> #### Advantages of Terraform
>
> While many of the current tools for infrastructure as code may work in your environment, Terraform aims to have a few advantages for operators and organizations of any size.
>
> 1. Platform Agnostic
> 2. State Management
> 3. Operator Confidence
>
> #### Platform Agnostic
>
> In a modern datacenter, you may have several different clouds and platforms to support your various applications. With Terraform, you can manage a heterogenous environment with the same workflow by creating a configuration file to fit the needs of your project or organization.
>
> #### State Management
>
> Terraform creates a state file when a project is first initialized. Terraform uses this local state to create plans and make changes to your infrastructure. Prior to any operation, Terraform does a refresh to update the state with the real infrastructure. This means that Terraform state is the source of truth by which configuration changes are measured. If a change is made or a resource is appended to a configuration, Terraform compares those changes with the state file to determine what changes result in a new resource or resource modifications.
>
> #### Operator Confidence
>
> The workflow built into Terraform aims to instill confidence in users by promoting easily repeatable operations and a planning phase to allow users to ensure the actions taken by Terraform will not cause disruption in their environment. Upon terraform apply, the user will be prompted to review the proposed changes and must affirm the changes or else Terraform will not apply the proposed plan.

### Install Terraform

> Install Terraform on Mac, Linux, or Windows by downloading the binary or using a package manager (Homebrew or Chocolatey). Then create a Docker container locally by following a quick-start tutorial to check that Terraform installed correctly.

Docker demo:

```sh
mkdir terraform-docker-demo && cd $_
touch main.tf
```

```hcl
terraform {
  required_providers {
    docker = {
      source = "terraform-providers/docker"
    }
  }
}

provider "docker" {}

resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

resource "docker_container" "nginx" {
  image = docker_image.nginx.latest
  name  = "tutorial"
  ports {
    internal = 80
    external = 8000
  }
}

```

### Build Infrastructure

> Authenticate to AWS, and create an EC2 instance under the AWS free tier. You will write and validate Terraform configuration, initialize a configuration directory, and plan and apply a configuration to create infrastructure.

[Configure the AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-quickstart.html) with `aws configure`.

```sh
mkdir terraform-aws-demo && cd $_
touch example.tf
```

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = "us-west-2"
}

resource "aws_instance" "example" {
  ami           = "ami-830c94e3"
  instance_type = "t2.micro"
}

```

```sh
terraform init
terrraform fmt
terraform validate
terraform apply
terraform show
terraform state list
```

### Change Infrastructure

> Modify EC2-instance configuration to use a different Ubuntu version. Plan and apply the changes to re-provision a new instance that reflects the new configuration. Learn how Terraform handles infrastructure change management.

Update the AMI from `ami-830c94e3` to `ami-08d70e59c07c61a3a`, run `terraform apply` again, then verify with `terraform show`.

### Destroy Infrastructure

> Completely destroy the AWS infrastructure that Terraform manages in a configuration with a single command. Evaluate the plan and confirm the destruction.

Destroy with `terraform destroy`.

### Define Input Variables

> Declare your AWS region as a variable. Reference the variable in Terraform configuration. Define variables using command line flags, environment variables, .tfvars files or default values.
>
> You now have enough Terraform knowledge to create useful configurations, but we're still hard-coding access keys, AMIs, etc. To become truly shareable and version controlled, we need to parameterize the configurations. This page introduces input variables as a way to do this.

Add a file _variables.tf_, or add variables directly to _example.tf_.

```hcl
variable "region" {
  default = "us-west-2"
}

variable "ami" {
  default = "ami-08d70e59c07c61a3a"
}

```

_example.tf_

```hcl
resource "aws_instance" "example" {
  ami           = var.ami
  instance_type = "t2.micro"
}

```

Maps can also be set up.

```hcl
variable "region" {
  default = "us-west-2"
}

variable "amis" {
  type = map(string)
  default = {
    "us-east-1" = "ami-b374d5a5"
    "us-west-2" = "ami-fc0b939c"
  }
}

```

_example.tf_

```hcl
resource "aws_instance" "example" {
  ami           = var.amis[var.region]
  instance_type = "t2.micro"
}

```

### Query Data with Output Variables

> Declare output variables to display the public IP address of an EC2 instance. Display all outputs and query specific outputs. Define what data stored in Terraform state is relevant to the operator or end user.

```hcl
resource "aws_eip" "ip" {
  vpc      = true
  instance = aws_instance.example.id
}

output "ip" {
  value = aws_eip.ip.public_ip
}

```

After running `terraform apply`, view output with `terraform output ip`.

### Store Remote State

> Configure Terraform to store state in Terraform Cloud remote backend. Add a remote state block directly to configuration or set an environment variable to load remote state configuration when Terraform initializes.
>
> Now you have built, changed, and destroyed infrastructure from your local machine. This is great for testing and development, but in production environments you should keep your state secure and encrypted, where your teammates can access it to collaborate on infrastructure. The best way to do this is by running Terraform in a remote environment with shared access to state.
>
> Terraform [remote backends](https://www.terraform.io/docs/backends/index.html) allow Terraform to use a shared storage space for state data. The [Terraform Cloud](https://www.terraform.io/cloud) remote backend also allows teams to easily version, audit, and collaborate on infrastructure changes. Terraform Cloud also securely stores variables, including API tokens and access keys. It provides a safe, stable environment for long-running Terraform processes.
>
> In this tutorial you will migrate your state to Terraform Cloud.

Add a backend to the _example.tf_ file:

```hcl
terraform {
  backend "remote" {
    organization = "br3ndonland"
    workspaces {
      name = "HashiCorp-Learn"
    }
  }
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 2.70"
    }
  }
}

provider "aws" {
  profile = "default"
  region  = var.region
}

resource "aws_instance" "example" {
  ami           = var.amis[var.region]
  instance_type = "t2.micro"
}

resource "aws_eip" "ip" {
  vpc      = true
  instance = aws_instance.example.id
}

```

Generate an API token and log in with `terraform login`, initialize the backend with `terraform init`, and then run `terraform apply`. It may complain about lack of AWS credentials, and you may need to delete the local state file _terraform.tfstate_. To move the state back to local state, delete the `backend` block, and run `terraform apply` again. Finally, run `terraform destroy` to remove the resources.
