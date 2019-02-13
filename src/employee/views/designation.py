from django.shortcuts import render,get_object_or_404
from .models import Employee,Department,Section,Designation
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

def designation_list(request):
	designation = Designation.objects.all()
	context = {
		'designation':designation
	}
	return render(request,'designation/designation_list.html',context)



