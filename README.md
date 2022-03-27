# tivix-automation
Automation of the test Tivix webpage.

### Test scenario
```
Feature: Car rent

  @critical_test
  Scenario: Rent a car successfully
    Given that I am on the main rent page
    When I do the process to rent a car
    Then I rent a car successfully
```


### Installation guide

```
# Close the repository
git clone https://github.com/anggelomos/tivix-automation.git

# Create virtual environment (optional)
python -m venv tivix-automation

# Activate virtual environment
source tivix-automation/bin/activate

# Move to the folder and install requirements
cd tivix-automation
pip install -r requirements.txt
```

### Run test
Once the requirements are installed, you can run the test using the following command:
```
python -m pytest test_automation_tivix_steps.py
```
