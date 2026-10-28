# SauceDemo - E2E Test Automation

End-to-end test suite for [SauceDemo](https://www.saucedemo.com), a demo online store made for testing practice.

The scenarios are written in Gherkin and run with pytest-bdd and Playwright. The suite runs in GitHub Actions on every push, in Chromium and Firefox.

## Tools

- Python 3.12
- Playwright with pytest-playwright
- pytest-bdd (Gherkin scenarios)
- pytest-html (HTML report)
- GitHub Actions (CI)

## Project structure

|Directory|Description|
|:--:|:--:|
|features/|Gherkin scenarios, one file per feature|
|pages/|Page Object Model: one class per page|
|tests/|Step definitions|
|tests/conftest.py|Page object fixtures and steps shared by several features|
|conftest.py|Hook that marks known defects as expected failures|
|pytest.ini|Base URL, test paths and evidence options|
|.github/|CI pipeline|

The page objects keep the locators and actions of each page in one place. The step definitions only call the page objects, so if the page changes, the fix is made in one file.

## Test scope

- Login: valid user, locked user, wrong password, empty username and empty password
- Product sorting: by name and by price, in both directions
- Cart: add products, remove products, check the cart content
- Checkout: complete purchase from login to confirmation, and required fields
- Known defects: three scenarios with problem_user (see below)

In total there are 19 tests: 16 for the expected behavior and 3 for known defects.

## Known defects

SauceDemo has a user called problem_user with intentional defects. These scenarios check the correct behavior, so they fail. They are tagged in the feature file with @known_bug_ and the bug ID.

The hook in conftest.py marks these scenarios as expected failures (xfail) with strict mode:

- While the defect exists, the test fails and the pipeline stays green.
- If the defect is fixed, the test passes and the pipeline fails, so the scenario must be reviewed and updated.

The same approach is used in my API testing project, with the known defects kept visible in the report.

## Evidence of failures

When a test fails, Playwright saves a screenshot, a video and a trace in the test-results folder. In GitHub Actions these files are uploaded as artifacts, together with the HTML report of each browser.

## Results

Execution on 2026-10-28 against saucedemo.com: 19 tests, 16 passed and 3 expected failures (known defects).

| Bug | Title | Severity |
| --- | --- | --- |
| [SD-01](bugs/SD-01.md) | All products show the same image for problem_user | Minor |
| [SD-02](bugs/SD-02.md) | Product sorting does not work for problem_user | Minor |
| [SD-03](bugs/SD-03.md) | problem_user cannot continue from checkout step one | Critical |

## Related projects

- [Manual testing on ParaBank](https://github.com/trip-rich-15/manual_test_case)
- [API testing on Restful-Booker](https://github.com/trip-rich-15/booker-api-testing)

## Author

Richard Tripodi - Manual QA | Functional Analyst | API Testing & Test Automation | richardtripodi15@gmail.com
