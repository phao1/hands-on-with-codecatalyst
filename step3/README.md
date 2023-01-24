# Exercise 3
[(_back to main readme_)](../README.md)

So far we've created an action to build our environment, and one to test it.
However, while we can see that we've run some tests, we don't know if they worked. In this exercise, we'll capture the test data we generated and use it set success criteria.

We'll continue to edit in the IDE.

1. Open the tab containing your IDE, or click `Code` in the navigation column, then `Dev Environments`. Each project should have a single dev environment called `coderepo/main`. Click on the link in the IDE column titled `Resume in AWS Cloud9`.
2. Open the workflow under `.codecatalyst/workflows` in the editor.
3. Scroll down to the `Outputs` section in the test action. It should look like
```
    Outputs:
      AutoDiscoverReports:
        Enabled: false
        ReportNamePrefix: rpt
```
4. Add these sections directly underneath - first, let's grab the results of our unittests (add these drectly underneath the lines above):
```
      Reports:
        TestReport:
          Format: JUNITXML
          IncludePaths:
            - src/junit/results.xml
          SuccessCriteria:
            PassRate: 100
        CoverageReport:
          Format: COBERTURAXML
          IncludePaths:
            - src/junit/coverage.xml
          SuccessCriteria:
            LineCoverage: 90
```
5. Then we'll grab the results from bandit
```
        PythonVulnerabilityReport:
          Format: SARIFSCA
          IncludePaths:
            - src/junit/bandit.sarif
          SuccessCriteria:
            Vulnerabilities:
              Severity: HIGH
              Number: 0
```
6. And finally, we'll capture our results from tfsec
```
        TerraformVulnerabilityReport:
          Format: SARIFSCA
          IncludePaths:
            - src/junit/tfsec.sarif
          SuccessCriteria:
            Vulnerabilities:
              Severity: HIGH
              Number: 0
```
7. Save your workflow, stage. commit and sync the changes back to our repository.
8. This will trigger a new run of our workflow (possibly after a short delay). Monitor this until it completes.
9. Once complete, review the `Reports` section of the run where you will see 4 reports.
10. If you can't get the workflow working, use [example_workflow_with_test_reports.yaml](example_with_test_reports.yaml)



[(Jump to the 4th exercise)](../step4/README.md) or [(_back to main readme_)](../README.md)