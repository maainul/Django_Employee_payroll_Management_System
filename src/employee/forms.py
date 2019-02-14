from django import forms
from .models import Employee,Department,Section,Designation


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
			'department',
			'section',
			'designation',
		]
class DepartmentForm(forms.ModelForm):
	class Meta:
		model = Department
		fields = ('name',)

class SectionForm(forms.ModelForm):
	class Meta:
		model = Section
		fields = ('name',)

class DesignationForm(forms.ModelForm):
	class Meta:
		model = Designation
		fields = ('name',)

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'email', 'phone')