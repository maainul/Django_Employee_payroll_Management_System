from django.db import models
role_choices = (
    ("A","Absent"),
    ("P","Present"),
    ("L","Leave"),
    )

class Department(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Designation(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    birthdate = models.DateField(null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True)
    designation = models.ForeignKey(Designation, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name

class Attendance(models.Model):
    employee = models.ForeignKey(Employee,on_delete=models.CASCADE,null=True)
    date = models.DateField()
    # status= models.CharField(max_length=1)
    status= models.CharField(max_length=10,choices=role_choices,default="P")
    

    def __str__(self):
        return self.employee.name























# class Section(models.Model):
#     section_name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.section_name 

# class Team(models.Model):
#     team_name = models.CharField(max_length=50)
    
#     def __str__(self):
#         return self.team_name
# class Salary(models.Model):
#     employee  = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no')
#     grade     = models.ForeignKey(Grade, on_delete=models.CASCADE, db_column='grade_no')
#     from_date = models.DateField(('from'))
#     to_date   = models.DateField(('to'))
#     def __str__(self):
#     	return self.grade


# role_choices = (
#     ("A","Absent"),
#     ("P","Present"),
#     ("L","Leave"),
#     )
# class Grade(models.Model):
#     grade_no = models.CharField(max_length=10,primary_key=True)
#     basic_salary = models.IntegerField()
#     medical_allowance = models.IntegerField()
#     lunch_allowance = models.IntegerField()
    
#     def __str__(self):
#         return self.basic_salary



# class Attendance(models.Model):
#     employee  = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no')
#     date = models.DateField(('attendance_date'))
#     attendance_status = models.CharField(choices=ATTENDANCE_STATUS,max_length=1)	

	#attendance_status = models.CharField(choices=ATTENDANCE_STATUS,max_length=1)

# ATTENDANCE_STATUS = (
# #       ('A','Absent'),
# #       ('P','Present'),
# #       ('L','Leave'),
# #       )


# class Designation(models.Model):
#   designation_name = models.CharField(max_length=50)

#   def __str__(self):
#       return self.designation_name 


# class Department(models.Model):
#   dept_name = models.CharField(max_length=50)
    
#   def __str__(self):
#       return self.dept_name


# class Category(models.Model):
#     name = models.CharField(max_length=30)
    

# class Product(models.Model):
#     name = models.CharField(max_length=30)
#     price = models.DecimalField(decimal_places=2, max_digits=10)
#     category = models.ForeignKey(Category)






 #    class Meta:
 #    	verbose_name = _('department')
 #        verbose_name_plural = _('departments')
 #        db_table = 'departments'
 #        ordering = ['dept_no']
	# def __str__(self):
	# 	return self.dept_name

	# validation logic
    # def clean(self):
    #     # Don't allow 'San Diego' city entries that have state different than 'CA'
    #     if self.city == 'San Diego' and self.state != 'CA':
    #     	raise ValidationError('Wait San Diego is CA!, are you sure there is another San Diego in %s ?' % self.state)
    
    # def latitude_longitude(self):
    #     # Call remote service to get latitude & longitude
    #     latitude, longitude = geocoding_method(self.address, self.city, self.state)
    #     return latitude, longitude

	
	# class Meta:
	# 	verbose_name = _('section')
 #    	verbose_name_plural= _('sections')
 #    	db_table = 'sections'
 #    	ordering = ['id']
 #    def __str__(self):
 #    	return self.section_name


	
	# class Meta:
 #        verbose_name = _('designation')
 #        verbose_name_plural = _('designations')
 #        db_table = 'designations'
 #        ordering = ['id']

 #    def __str__(self):
 #        return self.designation_name


	
	# class Meta:
 #        verbose_name = _('team')
 #        verbose_name_plural = _('teams')
 #        db_table = 'teams'
 #        ordering = ['id']

 #    def __str__(self):
 #        return self.team_name


	
	# class Meta:
	# 	verbose_name = _('grade')
	# 	verbose_name_plural= _('grades')
	# 	db_table = 'grades'

	# def __str__(self):
	# 	return "{}".format(self.basic_salary)




    # class Meta:
    #     verbose_name = _('employee')
    #     verbose_name_plural = _('employees')
    #     db_table = 'employees'

    # def __str__(self):
    #     return "{}".format(self.name)

 # employee -----> Employee
 # deparment ------> department
# class EmployeeDepartment(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no')
#     department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no')
    # class Meta:
    #     verbose_name = _('department employee')
    #     verbose_name_plural = _('department employees')
    #     db_table = 'employeedepartments'

    # def __str__(self):
    #     return "{} - {}".format(self.employee, self.department)


# class EmployeeSection(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no')
#     section = models.ForeignKey(Section, on_delete=models.CASCADE, db_column='section_no')


    # class Meta:
    #     verbose_name = _(' sectionemployee')
    #     verbose_name_plural = _('sectionemployees')
    #     db_table = 'sectionemployees'

    # def __str__(self):
    #     return "{} - {}".format(self.employee, self.section)


# class EmployeeDesignation(models.Model):
#     employee    = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no')
#     designation = models.ForeignKey(Designation, on_delete=models.CASCADE, db_column='designation_no')


    # class Meta:
    #     verbose_name = _('employeedesignation')
    #     verbose_name_plural = _('employeedesignations')
    #     db_table = 'employeedesignations'

    # def __str__(self):
    #     return "{} - {}".format(self.employee, self.designation_name)





 #    def net_salary(basic_salary,medical_allowance,lunch_allowance):
	# 	 wages = basic_salary + medical_allowance + lunch_allowance
	# 	 return wages
	# wages = models.IntegerField()
	
    # class Meta:
    #     db_table = 'salaries'
    #     ordering = ['-from_date']
    #     verbose_name = _('salary')
    #     verbose_name_plural = _('salaries')

    # def __str__(self):
    #     return "{} - {}".format(self.employee, self.grade)











	# department 			     = models.ForeignKey(Department, on_delete=models.CASCADE,default=0,blank=True)
	# section 			     = models.ForeignKey(Section, on_delete=models.CASCADE,default=0,blank=True)
	# designation 		     = models.ForeignKey(Designation, on_delete=models.CASCADE,default=0,blank=True)
	# # departmentanddesignation = models.ForeignKey(DepartmentAndDesignation, on_delete=models.CASCADE,default=0,blank=True)
	# # departmentandsection     = models.ForeignKey(DepartmentAndSection, on_delete=models.CASCADE,default=0,blank=True)
	# # sectionandteam 		   = models.ForeignKey(SectionAndTeam, on_delete=models.CASCADE,default=0,blank=True)
	
	# team 		             = models.ForeignKey(Team, on_delete=models.CASCADE,default=0,blank=True)
	# #team 		             = models.ForeignKey(SectionAndTeam, on_delete=models.CASCADE,default=0,blank=True)
	# grade					 = models.ForeignKey(Grade,on_delete=models.CASCADE,default=0)


# 	class Meta:
# 		ordering = ('name',)
# 		#verbose_name = 'category'
# 		#verbose_name_plural = 'categories'

# 	def __str__(self):
# 		return self.name

# from __future__ import unicode_literals

# from django.db import models
# from django.utils.encoding import python_2_unicode_compatible
# from django.utils.translation import ugettext_lazy as _


# class Department(models.Model):
#     dept_no = models.CharField(_('dept_no'), primary_key=True, max_length=4)
#     dept_name = models.CharField(_('name'), unique=True, max_length=40)

#     class Meta:
#         verbose_name = _('department')
#         verbose_name_plural = _('departments')
#         db_table = 'departments'
#         ordering = ['dept_no']

#     def __str__(self):
#         return self.dept_name


# class Designation(models.Model):
#     designation_no = models.CharField(_('designation_no'), primary_key=True, max_length=4)
#     designation_name = models.CharField(_('designation_name'), unique=True, max_length=40)

#     class Meta:
#         verbose_name = _('designation')
#         verbose_name_plural = _('designations')
#         db_table = 'designations'
#         ordering = ['designation_no']

#     def __str__(self):
#         return self.designation_name

# class DepartmentEmployee(models.Model):
#     employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
#     department = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))


#     class Meta:
#         verbose_name = _('department employee')
#         verbose_name_plural = _('department employees')
#         db_table = 'employeedepartments'

#     def __str__(self):
#         return "{} - {}".format(self.employee, self.department)


# class Employee(models.Model):
#     emp_no = models.IntegerField(_('employee_number'), primary_key=True)
#     birth_date = models.DateField(_('birthday'))
#     first_name = models.CharField(_('first name'), max_length=14)
#     last_name = models.CharField(_('last name'), max_length=16)
#     gender = models.CharField(_('gender'), max_length=1)
#     hire_date = models.DateField(_('hire date'))

#     class Meta:
#         verbose_name = _('employee')
#         verbose_name_plural = _('employees')
#         db_table = 'employees'

#     def __str__(self):
#         return "{} {}".format(self.first_name, self.last_name)


# class Grade(models.Model):
# 	grade_no = models.CharField(max_length=10,primary_key=True)
# 	basic_salary = models.IntegerField()
# 	medical_allowance = models.IntegerField()
# 	lunch_allowance = models.IntegerField()
	
# 	class Meta:
# 		verbose_name = _('grade')
# 		verbose_name_plural= _('grades')
# 		db_table = 'grades'

# 	def __str__(self):
# 		return "{}".format(self.basic_salary)


# class Salary(models.Model):
#     employee = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
#     grade    = models.ForeignKey(Grade, on_delete=models.CASCADE, db_column='grade_no', verbose_name=_('grade'))
#     from_date = models.DateField(_('from'))
#     to_date = models.DateField(_('to'))


#  #    def net_salary(basic_salary,medical_allowance,lunch_allowance):
# 	# 	 wages = basic_salary + medical_allowance + lunch_allowance
# 	# 	 return wages
# 	# wages = models.IntegerField()
	
#     class Meta:
#         db_table = 'salaries'
#         ordering = ['-from_date']
#         verbose_name = _('salary')
#         verbose_name_plural = _('salaries')

#     def __str__(self):
#         return "{} - {}".format(self.employee, self.grade)




# class EmployeeDesignation(models.Model):
#     employee    = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
#     designation = models.ForeignKey(Designation, on_delete=models.CASCADE, db_column='designation_no', verbose_name=_('designation'))


#     class Meta:
#         verbose_name = _('employeedesignation')
#         verbose_name_plural = _('employeedesignations')
#         db_table = 'employeedesignations'

#     def __str__(self):
#         return "{} - {}".format(self.employee, self.title)



# # class DeptManager(models.Model):
# #     employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
# #     department = models.ForeignKey(Department, on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))
# #     from_date = models.DateField(_('from'))
# #     to_date = models.DateField(_('to'))

# #     objects = TemporalQuerySet.as_manager()

# #     class Meta:
# #         verbose_name = _('department manager')
# #         verbose_name_plural = _('department managers')
# #         db_table = 'dept_manager'
# #         ordering = ['-from_date']

# #     def __str__(self):
# #         return "{} - {}".format(self.employee, self.department)
