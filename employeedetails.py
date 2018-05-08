# Lets create a class to get the details of employee from organisation

class Employee(object):
	def __init__(self,employeeName,ID,city,salary,designation):
		self.employeeName = employeeName
		self.ID=ID
		self.city=city
		self.salary=salary
		self.designation=designation
		## Add other basic details of employee
		
	
	def department(self):
		employeeDepartment = list()
		for i in range('HR','Testing','Coding'):
			employeeDepartment[i]=i
			print('employeeDepartment: {}', self.department)
		## create the departments the employee worked with the organisation,
		## EX: create 3 departments: HR, TESTING AND CODING.
		## It should PRINT that list.

	def personalDetails(self):
                ## Create a key value pair of personal details.
                ## ex:{'age':32}
                ## It should PRINT that dictionary of all the personal details.

