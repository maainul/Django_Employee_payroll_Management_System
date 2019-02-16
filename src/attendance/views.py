from django.shortcuts import render
from django.shortcuts import render,get_object_or_404,redirect
from employee.models import Employee,Department,Section,Designation

# def section_create(request):
# 	form = SectionForm(request.POST or None)
# 	if form.is_valid():
# 		form.save()
# 		form = DepartmentForm()
# 	context = {
# 		'form':form
# 	}
# 	return render(request,'form/form.html',context)


# def attendance_create(request):
# 	employee = Employee.objects.all()
# 	context = {
# 		'employee':employee
# 	}
# 	return render(request,'attendance_form.html',{})


def attendance_create(request):
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
	return render(request,'attendance_form.html',context)

# def department_list(request):
# 	department = Department.objects.all()
# 	context = {
# 		'department':department
# 	}
# 	return render(request,'department/department_list.html',context)

def attendance_view(request):
	return render(request,'attendance_view.html',{})

