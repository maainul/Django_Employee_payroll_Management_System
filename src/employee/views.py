from django.shortcuts import render,get_object_or_404
from .models import Employee
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
	context = {'all_employee':all_employee}
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