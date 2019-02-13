from django import forms
from .models import Employee


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

# class AuthorForm(forms.ModelForm):
#     class Meta:
#         model = Author
#         fields = ('name', 'email', 'phone')