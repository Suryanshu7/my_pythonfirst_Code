class SalaryError(Exception):
    pass


# raise SalaryError('Invalid salary')

def check_salary(salary):
    if salary < 0:
        raise SalaryError('Salary can not be negative')
    else:
         bonus = 1.3 *  salary
         return salary + bonus

salary = int(input('Enter your salary: '))
final_check =  check_salary(salary)
print(final_check)

#
# transaction

