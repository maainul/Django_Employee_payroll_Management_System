from django.shortcuts import render,get_object_or_404
from .models import Employee,Department,Section,Designation
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView


def department_list(request):
	department = Department.objects.all()
	context = {
		'department':department
	}
	return render(request,'department/department_list.html',context)