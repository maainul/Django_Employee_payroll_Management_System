from django.shortcuts import render,get_object_or_404
from .models import Employee,Department,Section,Designation
from django.http import HttpResponseRedirect
from .forms import EmployeeForm
from django.urls import reverse_lazy
from django.views.generic import UpdateView

def section_list(request):
	section = Section.objects.all()
	context = {
		'section':section
	}
	return render(request,'section/section_list.html',context)

