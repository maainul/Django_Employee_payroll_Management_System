from django.db import models


class Grade(models.Model):
	name 				     = models.CharField(max_length=10)
	basic_salary 		     = models.IntegerField()
	house_rent  		     = models.IntegerField()
	medical_allowance 		 = models.IntegerField()
	lunch_bill 		         = models.IntegerField()
	transportation_allowance = models.IntegerField()
	net_salary				 = models.IntegerField()

	def __str__(self):
		return self.name


# class Salary(models.Model):
# 	grade 			     = models.ForeignKey(Grade, on_delete=models.CASCADE,default=0)
	

