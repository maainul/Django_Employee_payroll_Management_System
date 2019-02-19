from django import forms
#from .models import Employee,Department,Section,Designation,Grade
from .models import (
			Department,
			Section,
			Designation,
			Team,
			Grade,
			Employee,
			EmployeeDepartment,
			EmployeeSection,
			EmployeeDesignation,
			Salary,
		)
class EmployeeForm(forms.ModelForm):
	class Meta:
		model = Employee
		fields = [
			'name',
			'father_name',
			'mother_name',
			'nid',
			'phone',
			'present_address',
			'permanent_address',
			'image',
		]
class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = ('dept_name',)

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = ('section_name',)

class DesignationForm(forms.ModelForm):
	class Meta:
		model = Designation
		fields = ('designation_name',)
class TeamForm(forms.ModelForm):
	class Meta:
		model = Team
		fields = ('team_name',)

class GradeForm(forms.ModelForm):
	class Meta:
		model = Grade
		fields = ('grade_no','basic_salary','medical_allowance','lunch_allowance',)

