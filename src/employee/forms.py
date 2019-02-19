from django import forms
#from .models import Employee,Department,Section,Designation,Grade
from .models import (
			Department,
			Section,
			Designation,
			Team,
			Grade,
			Employee,
			# EmployeeDepartment,
			# EmployeeSection,
			# EmployeeDesignation,
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

	def clean_name(self):
          # Get the field value from cleaned_data dict
          value = self.cleaned_data['name']
          # Check if the value is all upper case
          if value.isupper():
             # Value is all upper case, raise an error
          	raise forms.ValidationError("Please don't use all upper case for your name, uselower case",code='uppercase')
          # Always return value
          return value

      # def clean_email(self):
      #     # Get the field value from cleaned_data dict
      #     value = self.cleaned_data['email']
      #     # Check if the value end in @hotmail.com
      #     if value.endswith('@hotmail.com'):
      #        # Value ends in @hotmail.com, raise an error
      #     	raise forms.ValidationError("Please don't use a hotmail email, we simply don't like it",code='hotmail')
      #     # Always return

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

