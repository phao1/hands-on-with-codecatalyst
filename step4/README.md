# Exercise 4
[(_back to main readme_)](../README.md)

We now have validated code in our workflow, we're ready for the final step which is to add an action to deploy the code to our AWS account.

We have already linked an AWS account to our CodeCatalyst environment, so we can add a new action which will deploy our code.

We'll continue to edit in the IDE.

1. Open the tab containing your IDE, or click `Code` in the navigation column, then `Dev Environments`. Each project should have a single dev environment called `coderepo/main`. Click on the link in the IDE column titled `Resume in AWS Cloud9`.
2. Open the file `coderepo/terraform/aws.tf` which should look like
```
provider "aws" {
    region = "eu-west-1"
    default_tags {
        tags = {
            Project = "DevOps PlayGround Jan 2023"
        }
    }
}

terraform {
  backend "s3" {
    bucket         = "204521158369-eu-west-1-terraform-state"
    key            = "devops-playground.tfstate"
    region         = "eu-west-1"
  }
}
```
3. Modify the `key` field and add your panda name in front of the key, so it looks like `funky-panda-devops-playground.tstate`
4. Open your workflow file, scroll to the bottom and add this text
```
  Deploy_Terraform_to_DEV:
    Identifier: aws/build@v1
    Inputs:
      Sources:
        - WorkflowSource
    Outputs:
      AutoDiscoverReports:
        Enabled: true
        ReportNamePrefix: rpt
    Configuration:
      Steps:
        - Run: |
            echo "Hello, World! - ready to deploy"
        - Run: |
            echo "Installing Terraform"
            sudo yum install -y yum-utils shadow-utils
            sudo yum-config-manager --add-repo https://rpm.releases.hashicorp.com/AmazonLinux/hashicorp.repo
            sudo yum -y --nogpgcheck install terraform
        - Run: |
            echo "Initialising Terraform"
            cd terraform
            terraform init
        - Run: |
            echo "Running Terraform Plan"
            terraform plan
        - Run: |
            echo "Running Terraform Apply"
            terraform apply --auto-approve -no-color
    Compute:
      Type: EC2
```
_This will add 5 steps that install terraform, initialise an environment, run a plan, and finally deploy the code_
5. Now we need to connect this to our AWS environment. Add the following lines directly below the lines above
```
    Environment:
      Connections:
        - Role: CodeCatalystDeploymentRole
          Name: "204521158369"
      Name: DevTest
```
_This will allow the workflow to connect to the AWS Account `204521158369`, using the IAM Role `CodeCatalystDeploymentRole`
6. Finally add a `DependsOn` section to ensure this runs after our test action is complete. Add these lines
```
    DependsOn:
      - Test_Phase
```
***Make sure you use the name of your test action.***
8. Again, save your changes, stage, commit and push.


[(_back to main readme_)](../README.md)