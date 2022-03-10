# VAMSTER BMI SERVICE

## Description

This applications takes in relevant data ( heights and weight) and calculates BMI. Based on continous BMI values, it also categorizes the BMI in various levels called BMI Category and Health Indicator through HealthRisk Parameter. The current set of application takes in raw hard coded data and splits out the relevant information mentioned above.

## How to run the application

*1.* Create virtual environment
        `conda create -n <venv_name> python=3.8`

*2.* Build the egg file for distribution:
        `python setup.py bdist_wheel`

*3.* Install the egg file for installation:
        `pip install .\dist\VAMSTER_BMI_SERVICE-1.0.1-py3-none-any.whl`

*4.* Run tests:
        `python setup.py test`

*5.* Run the application:
        `python -m bmi_service`

## Sample Application Output

|    | Gender   |   HeightCm |   WeightKg |   BMI | BMI Category     | HealthRisk    |
|---:|:---------|-----------:|-----------:|------:|:-----------------|:--------------|
|  0 | Male     |        171 |         96 |  32.8 | Moderately obese | Medium risk   |
|  1 | Male     |        161 |         85 |  32.8 | Moderately obese | Medium risk   |
|  2 | Male     |        180 |         77 |  23.8 | Normal Weight    | Low risk      |
|  3 | Female   |        166 |         62 |  22.5 | Normal Weight    | Low risk      |
|  4 | Female   |        150 |         70 |  31.1 | Moderately obese | Medium risk   |
|  5 | Female   |        167 |         82 |  29.4 | Overweight       | Enhanced risk |

Total Number of overweight people: 1

## TODO / FUTURE IMPROVMENTS

1. Create a command line argument to take input data and emit out bmi, category and health indicator
2. Create more stringent and edge test cases
3. Read the data from an external source ( right now it is hardcoded in the service)
4. Run the linter ( e.g. black/flake8) to follow python programing guidelines based on PEP-8





