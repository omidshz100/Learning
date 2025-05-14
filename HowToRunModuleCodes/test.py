#from Imports.grade_average_service import calculate_average
import Imports.grade_average_service as gas
homework_assignment_grades = {
    "homework1": 95,
    "homework2": 64.9,
    "homework3": 87.36,
}

gas.calculate_average(homework_assignment_grades)


# to run code with modules use these commands
#------------------------------------------------
# PYTHONPATH=$PYTHONPATH:. python HowToRunModuleCodes/test.py 
# python -m HowToRunModuleCodesy.test
#------------------------------------------------
