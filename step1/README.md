# Exercise 1
[(_back to main readme_)](../README.md)
For this walkthrough, we have created a CodeCatalyst Space with projects for each individual. The projects are named with your 'panda' name and include the following:
* A code repository called Dev
* A non-prod deployment environment linked to an AWS account. Those accounts have an associated IAM role allowing us to deploy infrastructure into the account, including
  * a S3 bucket which can be used to hold terraform statefiles
  * a dynamodb table which will be used by the code we deploy to track how many time our code is called (we could have used a CloudWatch metric, but that can take time to reflect a real count.)
## Accessing CodeCatalyst
***You should have a builder ID and password - if not, please shout.***
1. Login to https://codecatalyst.aws - click Sign In and provide details
2. Select the project with your panda name, then click on `Code` in the nav. column, then `Source Repositories`.
   _You should see a main README.md, several step folders with more READMEs and sample code. If you get lost, follow these_
3. Click on `CI/CD` and select `Workflows` - this section should initially be empty, but we're going to create a workflow visually.
4. Click `Create workflow` button, and change the selector from `YAML` to `Visual` (_we'll use YAML in the next exercise_).
5. Click `Workflow properties` on the top RHS of the screen, under the `Commit` button. Change the workflow to something appropriate, then click the tick. Click the `X` to close the properties.
6. Click on the blue box in the center of the screen with the words `Source` and `Triggers`. _This defines where our code comes from and how the workflow will be triggered_.
7. Click on the pen to the right of `Push`. Click `Remove` button next to `main`. Click the `Update` button. _This tells the workflow that it will be triggered on a push to any branch_.
8. Click on the `+ Actions` underneath the name of the workflow. Choose `Build`. Click `Add to workflow` _This adds an action to the workflow that we'll use to initialise our working environment_
9. You'll see `WorkflowSource` is already in place, _this means the workflow will use the same repo that contains the workflow code_. 
10. Click on `Configuration` and change the action name to `Init`. or similar. _Review the options but don't change anything_.
11. Scroll down to Shell commands and paste this code:
```
- Run: |
    echo "Install required environment libraries on ${HOSTNAME}"
    pip install --user -r env_requirements.txt
- Run: |
    echo "Install required code libraries"
    cd src
    pip install --user -r requirements.txt
```
_This YAML code defines what actions this step will carry out_
12.  Click on `Outputs`, scroll down Reports and click the toggle. _This disables automatic discovery of reports (our sample code includes some example test reports)_
13.  Click the `X` to close the action. Click `Validate` at the top of the screen and make sure it comes back with valid code.
14.  Click `Commit` at the top of the screen.
  * Specify a name to use for the yaml file that will hold the workflow definition
  *   Add an appropriate commit message
  *   Choose the repo and `main` for the branch name from the drop-down
  *   Click on the `Commit` button.

15.   After a short delay, you'll be returned to the main Workflow screen and you should see a Run listed under your workflow name. You'll see the run has an id, a reference to the commit id, repo and branch.
16.   Click on the id (_something like `Run-d0ca1`_), and you'll see a visual representation of the run. Click on the action you added
17. Review the `Logs` section.   
18. Click on `Overiew` to return the project summary.

**Congratulations, you've created and executed your first workflow in CodeCatalyst.**

[(Jump to the 2nd exercise)](../step2/README.md) or [(_back to main readme_)](../README.md)