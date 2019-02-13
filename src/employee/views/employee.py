from django.shortcuts import render,get_object_or_404
from .models import Employee,Department,Section,Designation
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView


def employee_create_view(request):
	form = EmployeeForm(request.POST,request.FILES or None)
	if form.is_valid():
		form.save()
		form = EmployeeForm()

	context = {
		'form':form
	}
	return render(request,'employee_create.html',context)


def employee_list(request):
	all_employee = Employee.objects.all()
	department = Department.objects.all()
	section = Section.objects.all()
	designation = Designation.objects.all()
	context = {
		'all_employee':all_employee,
		'department':department,
		'section':section,
		'designation':designation
		}
	return render(request,'employee_list.html',context)


class EmployeeUpdateView(UpdateView):
	model = Employee
	form_class = EmployeeForm
	template_name = 'employee_update.html'
	success_url = reverse_lazy('employee_list')

# class EmployeeListView(ListView):
# 	model = Employee
# 	context_object_name = 'employee'
# 	success_url = reverse_lazy('employee_list')



def employee_detail(request,id):
	employee = get_object_or_404(Employee,id=id)
	context = {'employee':employee}
	return render(request,'employee_details.html',context)



