# DevOps Playground - January 2023
## Hands-on with Amazon CodeCatalyst

In this playground, we'll be exploring [Amazon CodeCatalyst](https://codecatalyst.aws), a new development/collaboration
tool announced by AWS at re:Invent 2022. (The keynote announcement can be viewed [here](https://youtu.be/RfvL_423a-I?t=3486)).

We'll walkthrough various components of CodeCatalyst and try to deploy some python code, building a pipeline in CodeCatalyst
to test and deploy the code as an AWS Lambda using Terraform.

## Accessing the playground
Assuming you registered for the PlayGround, you should be able to login to https://lab.devopsplayground.org/ using your 
meetup username. (Internal GlobalLogic UK&I users should be able to access with 'firstname lastname' if you accepted the internal invite.)

## Agenda
The session should take approximately 60 minutes. Attendees do not need to have any previous experience with CodeCatalyst, Python or Terraform
as example code will be provided.

### Step 1. Creating a workflow to build our environment
 - where's our code
 - creating a workflow
 - adding build
 - running the workflow

### Step 2. Testing our code
 - accessing a dev environment
 - editing workflow via dev environment & Cloud9
 - adding tests
 - fixing missing files with artifacts
 - running workflow

### Step 3. Deploying code to AWS
 - adding workflow step