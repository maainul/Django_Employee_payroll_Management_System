 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager
from salary.models import Grade


class Department(models.Model):
	dept_name = models.CharField(max_length=50)
	class Meta:
		verbose_name = _('department')
        verbose_name_plural = _('departments')
        db_table = 'departments'
        ordering = ['id']

    def __str__(self):
        return self.dept_name


class Section(models.Model):
	section_name = models.CharField(max_length=50)
	class Meta:
		verbose_name = _('section')
        verbose_name_plural = _('sections')
        db_table = 'sections'
        ordering = ['id']

    def __str__(self):
        return self.dept_name

class Designation(models.Model):
	designation_name = models.CharField(max_length=50)
	class Meta:
        verbose_name = _('designation')
        verbose_name_plural = _('designations')
        db_table = 'designations'
        ordering = ['id']

    def __str__(self):
        return self.designation_name

class Team(models.Model):
	team_name = models.CharField(max_length=50)
	class Meta:
        verbose_name = _('team')
        verbose_name_plural = _('teams')
        db_table = 'teams'
        ordering = ['id']

    def __str__(self):
        return self.team_name

class Grade(models.Model):
	grade_no = models.CharField(max_length=10,primary_key=True)
	basic_salary = models.IntegerField()
	medical_allowance = models.IntegerField()
	lunch_allowance = models.IntegerField()
	
	class Meta:
		verbose_name = _('grade')
		verbose_name_plural= _('grades')
		db_table = 'grades'

	def __str__(self):
		return "{}".format(self.basic_salary)



class Employee(models.Model):
	name 				     = models.CharField(max_length=50)
	father_name 		     = models.CharField(max_length=50)
	mother_name 		     = models.CharField(max_length=50)
	nid 				     = models.IntegerField()
	present_address 	     = models.TextField(max_length=150)
	permanent_address 	     = models.TextField(max_length=150)
	phone 				     = models.IntegerField()
	image         		     = models.ImageField(upload_to='employee/%Y/%m/%d', blank=True)
    class Meta:
        verbose_name = _('employee')
        verbose_name_plural = _('employees')
        db_table = 'employees'

    def __str__(self):
        return "{}".format(self.name)


class EmployeeDepartment(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    department = models.ForeignKey('Department', on_delete=models.CASCADE, db_column='dept_no', verbose_name=_('department'))


    class Meta:
        verbose_name = _('department employee')
        verbose_name_plural = _('department employees')
        db_table = 'employeedepartments'

    def __str__(self):
        return "{} - {}".format(self.employee, self.department)


class EmployeeSection(models.Model):
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    section = models.ForeignKey('Section', on_delete=models.CASCADE, db_column='section_no', verbose_name=_('section'))


    class Meta:
        verbose_name = _(' sectionemployee')
        verbose_name_plural = _('sectionemployees')
        db_table = 'sectionemployees'

    def __str__(self):
        return "{} - {}".format(self.employee, self.section)


class EmployeeDesignation(models.Model):
    employee    = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    designation = models.ForeignKey(Designation, on_delete=models.CASCADE, db_column='designation_no', verbose_name=_('designation'))


    class Meta:
        verbose_name = _('employeedesignation')
        verbose_name_plural = _('employeedesignations')
        db_table = 'employeedesignations'

    def __str__(self):
        return "{} - {}".format(self.employee, self.designation_name)



class Salary(models.Model):
    employee  = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='emp_no', verbose_name=_('employee'))
    grade     = models.ForeignKey(Grade, on_delete=models.CASCADE, db_column='grade_no', verbose_name=_('grade'))
    from_date = models.DateField(_('from'))
    to_date   = models.DateField(_('to'))


 #    def net_salary(basic_salary,medical_allowance,lunch_allowance):
	# 	 wages = basic_salary + medical_allowance + lunch_allowance
	# 	 return wages
	# wages = models.IntegerField()
	
    class Meta:
        db_table = 'salaries'
        ordering = ['-from_date']
        verbose_name = _('salary')
        verbose_name_plural = _('salaries')

    def __str__(self):
        return "{} - {}".format(self.employee, self.grade)











	# department 			     = models.ForeignKey(Department, on_delete=models.CASCADE,default=0,blank=True)
	# section 			     = models.ForeignKey(Section, on_delete=models.CASCADE,default=0,blank=True)
	# designation 		     = models.ForeignKey(Designation, on_delete=models.CASCADE,default=0,blank=True)
	# # departmentanddesignation = models.ForeignKey(DepartmentAndDesignation, on_delete=models.CASCADE,default=0,blank=True)
	# # departmentandsection     = models.ForeignKey(DepartmentAndSection, on_delete=models.CASCADE,default=0,blank=True)
	# # sectionandteam 		   = models.ForeignKey(SectionAndTeam, on_delete=models.CASCADE,default=0,blank=True)
	# # department 			   = models.ForeignKey(Department, on_delete=models.CASCADE,default=0,blank=True)
	# # designation              = models.ForeignKey(DepartmentAndDesignation, on_delete=models.CASCADE,default=0,blank=True)
	# # section     			 = models.ForeignKey(DepartmentAndSection, on_delete=models.CASCADE,default=0,blank=True)
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
