from django.shortcuts import render,get_object_or_404
from .models import Employee
from django.http import HttpResponseRedirect
from .forms import EmployeeForm


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
	context = {'all_employee':all_employee}
	return render(request,'employee_list.html',context)

def employee_detail(request,id):
	employee = get_object_or_404(Employee,id=id)
	context = {'employee':employee}
	return render(request,'employee_details.html',context)

