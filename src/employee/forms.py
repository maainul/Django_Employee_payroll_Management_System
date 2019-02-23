from django import forms
from .models import (
			Department,
			Section,
			Designation,
			Team,
			Grade,
			Employee,
			#Attendance,
			Salary,
		)
# class EmployeeForm(forms.ModelForm):
# 	class Meta:
# 		model = Employee
# 		fields = [
# 			'name',
# 			'father_name',
# 			'mother_name',
# 			'nid',
# 			'phone',
# 			'present_address',
# 			'permanent_address',
# 			'image',
# 			'designation_name',
# 			'dept_name',
# 			'section_name',
# 			'team_name',
# 		]



class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = (
        	'name',
			'father_name',
			'mother_name',
			'nid',
			'phone',
			'present_address',
			'permanent_address',
			'department',
			'designation',
			'section' )

        def __init__(self,*args,**kwargs):
        	super(EmployeeForm,self).__init__(*args,**kwargs)
        	

# def __init__(self,*args,**kwargs):
# 	super(EmployeeForm,self).__init__(*args,**kwargs)

	# def clean(self):
 #        cleaned_data = super(EmployeeForm, self).clean()super
 #        name = cleaned_data.get('name')
 #        father_name = cleaned_data.get('father_name')
 
 #        if not name and not father_name:
 #            raise forms.ValidationError('You have to write something!')

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


# class AttendanceForm(forms.ModelForm):
# 	class Meta:
# 		model = Attendance
# 		fields = ('employee','date','attendance_status',)

        # def __init__(self,*args,**kwargs):
        #     super(EmployeeForm,self).__init__(*args,**kwargs)
            

# class ContactForm(forms.ModelForm):
#       class Meta:      
#             model = Contact
#             fields = '__all__'
# views.py method to process model form
# def contact(request):
#     if request.method == 'POST':
#         # POST, generate bound form with data from the request
#         form = ContactForm(request.POST)
#         # check if it's valid:
#         if form.is_valid():
#             # Insert into DB
#             form.save()
#             # redirect to a new URL:
#             return HttpResponseRedirect('/about/contact/thankyou')
#     else:
#         # GET, generate unbound (blank) form
#         form = ContactForm()
#     return render(request,'about/contact.html',{'form':form})
