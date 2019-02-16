from django.db import models
from employee.models import Employee


class Attendance(models.Model):
	employee 	= models.ForeignKey(Employee,on_delete=models.CASCADE)
	date 		= models.DateTimeField(auto_now_add=True)
	status		= models.CharField(max_length=1)
