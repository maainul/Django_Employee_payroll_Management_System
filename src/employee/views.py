from django.shortcuts import render,get_object_or_404,redirect
from .models import (
			Department,
            Attendance,
			#Section,
			Designation,
			#Team,
			#Grade,
			Employee,
			#Salary,
		)
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView
from django.urls import reverse_lazy
from .models import Employee, Designation
from .forms import EmployeeForm,AttendanceForm


class EmployeeListView(ListView):
    model = Employee
    context_object_name = 'employee'


class EmployeeCreateView(CreateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_changelist')


class EmployeeUpdateView(UpdateView):
    model = Employee
    form_class = EmployeeForm
    success_url = reverse_lazy('employee_changelist')


def load_designations(request):
    department_id = request.GET.get('department')
    designations = Designation.objects.filter(department_id=department_id).order_by('name')
    return render(request, 'employee/designation_dropdown_list_options.html', {'designations': designations})

class AttendanceCreateView(CreateView):
    model = Attendance
    form_class = AttendanceForm
    success_url = reverse_lazy('employee_changelist')

# class AttendanceCreateView(CreateView):
#     model = Attendance
#     form_class = AttendanceForm
#     context_object_name = 'Attendance'

class AttdenceListView(ListView):
    model = Attendance
    context_object_name = 'attendance'

# def department_create(request):
# 	form = DepartmentForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = DepartmentForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'form/form.html',context)


# def department_list(request):
# 	department = Department.objects.all()
# 	context = {
# 		'department':department
# 	}
# 	return render(request,'department/department_list.html',context)


# def department_delete(request,id):
# 	obj = get_object_or_404(Department,id=id)
# 	if request.method == "POST":
# 		obj.delete()
# 		return redirect('department_list')
# 	context = {
# 		"objects":obj
# 	}
# 	#return render(request,'department/department_detete.html',context)
# 	return render(request,'delete/delete.html',context)


# #
# # Team 
# #

# def team_create(request):
# 	form = DepartmentForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = DepartmentForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'form/form.html',context)


# def team_list(request):
# 	team = Department.objects.all()
# 	context = {
# 		'team':team
# 	}
# 	return render(request,'team/department_list.html',context)


# def team_delete(request,id):
# 	obj = get_object_or_404(Department,id=id)
# 	if request.method == "POST":
# 		obj.delete()
# 		return redirect('department_list')
# 	context = {
# 		"objects":obj
# 	}
# 	#return render(request,'team/department_detete.html',context)
# 	return render(request,'delete/delete.html',context)


# #
# # Section Site
# #

# def section_create(request):
# 	form = SectionForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = DepartmentForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'form/form.html',context)


# def section_list(request):
# 	section = Section.objects.all()
# 	context = {
# 		'section':section
# 	}
# 	return render(request,'section/section_list.html',context)


# def section_delete(request,id):
# 	obj = get_object_or_404(Section,id=id)
# 	if request.method == "POST":
# 		obj.delete()
# 		return redirect('section_list')
# 	context = {
# 		"objects":obj
# 	}
# 	return render(request,'delete/delete.html',context)

# 	#return render(request,'section/section_detete.html',context)

# #
# #Designation site
# #

# def designation_create(request):
# 	form = DesignationForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = DesignationForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request, 'form/form.html',context)


# def designation_list(request):
# 	designation = Designation.objects.all()
# 	context = {
# 		'designation':designation
# 	}
# 	return render(request,'designation/designation_list.html',context)


# def designation_delete(request,id):
# 	obj = get_object_or_404(Designation,id=id)
# 	if request.method == "POST":
# 		obj.delete()
# 		return redirect('../')
# 	context = {
# 		"objects":obj
# 	}
# 	return render(request,'delete/delete.html',context)

	#return render(request,'designation/designation_delete.html',context)

#
# Employee site
#

# def employee_create_view(request):
# 	form = EmployeeForm(request.POST,request.FILES or None)
# 	if form.is_valid():
# 		form.save()
# 		form = EmployeeForm()
# 		return redirect('../')
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'form/form.html',context)

# def employee_create_view(request):
#     if request.method == 'POST':
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             employee = form.save(commit=False)
#             # employee.user = request.user
#             employee.save()
#             return redirect('employee_list')
#     else:
#         form = EmployeeForm()
#     return render(request, 'form/form.html', {'form': form})



# def employee_list(request):
# 	all_employee = Employee.objects.all()
# 	# department = Department.objects.all()
# 	# section = Section.objects.all()
# 	# designation = Designation.objects.all()
# 	context = {
# 		'all_employee':all_employee,
# 		# 'department':department,
# 		# 'section':section,
# 		# 'designation':designation
# 		}
# 	return render(request,'employee_list.html',context)


# class EmployeeUpdateView(UpdateView):
# 	model = Employee
# 	form_class = EmployeeForm
# 	template_name = 'employee_update.html'
# 	success_url = reverse_lazy('employee_list')


# def employee_detail(request,id):
# 	employee = get_object_or_404(Employee,id=id)
# 	context = {'employee':employee}
# 	return render(request,'employee_details.html',context)

# def employee_delete(request,id):
# 	obj = get_object_or_404(Employee,id=id)
# 	if request.method == "POST":
# 		obj.delete()
# 		return redirect('employee_list')
# 	context = {
# 		"objects":obj
# 	}
# 	return render(request,'delete/delete.html',context)

	#return render(request,'employee_detete.html',context)


# class EmployeeDeleteView(DeleteView):
# 	template_name = 'employee_detete.html'

# 	def get_object(self):
# 		id_ = self.kwargs.get("id")
# 		return get_object_or_404(Employee,id = id_)

# 	def get_success_url(self):
# 		return reverse('employee_list')


# def employee_edit(request):
#     EmployeeFormSet = modelformset_factory(Product,
# 		fields = (
#         	'name',
# 			'father_name',
# 			'mother_name',
# 			'nid',
# 			'phone',
# 			'present_address',
# 			'permanent_address',
# 			'department',
# 			'designation',
# 			'section' ),extra=0)

#     data = request.POST or None
#     formset = EmployeeFormSet(data=data, queryset=Employee.objects.filter())
#     for form in formset:
#         form.fields['department'].queryset  = Department.objects.filter()
#     for form in formset:
#         form.fields['designation'].queryset = Designation.objects.filter()
#     for form in formset:
#         form.fields['department'].queryset  = Section.objects.filter()
#     for form in formset:
#         form.fields['department'].queryset  = Team.objects.filter()    

#     if request.method == 'POST' and formset.is_valid():
#         formset.save()
#         return redirect('employee_list')

#     return render(request, 'form/form.html', {'formset': formset})
def attendance_list(request):
	all_employee = Employee.objects.all()
	context = {
		'all_employee':all_employee
		}
	return render(request,'attendance/attendance_list.html',context)






























# class EmployeeListView(ListView):
# 	model = Employee
# 	context_object_name = 'employee'
# 	success_url = reverse_lazy('employee_list')


# class AuthorListView(ListView):
#     model = Author
#     context_object_name = 'book'


# class AuthorCreateView(CreateView):
#     model = Author
#     fields = ('name', 'email', 'phone')
#     success_url = reverse_lazy('author_list')


# class AuthorUpdateView(UpdateView):
#     model = Author
#     form_class = AuthorForm
#     template_name = 'book/author_update_form.html'
#     success_url = reverse_lazy('author_list')






























#class based view 
#from django.views.generic import ListView,CreateView,UpdateView,DetailView
# class WorderCreateView(CreateView):
# 	model = Worker 
# 	fields = (
#         	'name',
#         	'father_name',
# 			'mother_name',
# 			'nid',
# 			'present_address',
# 			'permanent_address',
# 			'phone',
# 			'image',
# 			'card_number'
# 			)
# 	success_url = reverse_lazy('worker_list')


# def func(request, id):

#     object = Model.objects.get(id=id)
#     form = ModelForm(instance=object)

#     return render(request, 'my_template.html', {'form':form})


# def employee_update(request, id):
#     employee = Employee.objects.get(id=id)
#     form = EmployeeForm(instance=employee)
#     return render(request, 'employee_update.html', {'form':form})

#Update info by classbased view
#class based list
# class EmployeeListView(ListView):
# 	model = Employee
# 	context_object_name = 'employee'


# Class Based Detail
# class EmployeeDetailView(DetailView):
#     model = Employee
#     template_name = 'employee_details.html'
#     context_object_name = 'employee'