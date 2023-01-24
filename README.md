# DevOps Playground - January 2023
## Hands-on with Amazon CodeCatalyst

In this playground, we'll be exploring [Amazon CodeCatalyst](https://codecatalyst.aws), a new development/collaboration tool announced by AWS at re:Invent 2022. (The keynote announcement can be viewed [here](https://youtu.be/RfvL_423a-I?t=3486)).

We'll walk through various components of CodeCatalyst and try to deploy some python code, building a pipeline in CodeCatalyst to test and deploy the code as an AWS Lambda using Terraform.

## Accessing the playground
Assuming you registered for the PlayGround, you should be able to log in to https://lab.devopsplayground.org/ using your meetup username. (Internal GlobalLogic UK&I users should be able to access with 'firstname lastname' if you accepted the internal invite.)

## Agenda
The session should take approximately 60 minutes. Attendees do not need to have any previous experience with CodeCatalyst, Python or Terraform as example code will be provided.

### [Step 1. Creating a workflow to build our environment (_click_)](step1/README.md)
 - exploring CodeCatalyst
 - creating a workflow
 - adding build action
 - running the workflow

### [Step 2. Testing our code (_click_)](step2/README.md)
 - accessing a dev environment
 - editing workflow via dev environment & Cloud9
 - fixing missing files with artifacts
 - adding tests
 - running workflow

### [Step 3. Capturing test results (_click_)](step3/README.md)
 - adding reports
 - setting success criteria

### [Step 4. Deploying code to AWS (_click_)](step4/README.md)
 - adding workflow step
 - installing terraform
 - terraform init and plan
 - deploy
 - testing live (use restninja.io or https://www.site24x7.com/tools/restapi-tester.html)


# Final Architecture
The final deployment will deploy something that looks like
![deployed architecture](./images/architecture.png)