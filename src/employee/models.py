 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Manager
from salary.models import Grade


class Department(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Section(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Designation(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name


class Team(models.Model):
	name = models.CharField(max_length=10)
	def __str__(self):
		return self.name

# class DepartmentAndDesignationManager(models.Manager):
#     def get_queryset(self):
#         return super(DepartmentAndDesignationManager, self).get_queryset().filter(department='it')

# class DepartmentAndDesignation(models.Model):
# 	department_id  = models.ForeignKey(Department,on_delete=models.CASCADE,default=0,blank=True)
# 	designation_id = models.ForeignKey(Designation,on_delete=models.CASCADE,default=0,blank=True)
	
# 	# dept = DepartmentAndDesignationManager()

# 	def __str__(self):
# 		return self.department_id.name+ ' - ' +self.designation_id.name


# class DepartmentAndSection(models.Model):
# 	department_id  = models.ForeignKey(Department,on_delete=models.CASCADE,default=0,blank=True)
# 	section_id     = models.ForeignKey(Section,on_delete=models.CASCADE,default=0,blank=True)
# 	def __str__(self):
# 		return self.department_id.name+ ' - ' +self.section_id.name

# class SectionAndTeam(models.Model):
# 	section_id     = models.ForeignKey(Section,on_delete=models.CASCADE,default=0,blank=True)
# 	team_id        = models.ForeignKey(Team,on_delete=models.CASCADE,default=0,blank=True)
# 	def __str__(self):
# 		return self.section_id.name+ ' - ' +self.team_id.name

class Employee(models.Model):
	name 				     = models.CharField(max_length=50)
	father_name 		     = models.CharField(max_length=50)
	mother_name 		     = models.CharField(max_length=50)
	nid 				     = models.IntegerField()
	present_address 	     = models.TextField(max_length=150)
	permanent_address 	     = models.TextField(max_length=150)
	phone 				     = models.IntegerField()
	image         		     = models.ImageField(upload_to='employee/%Y/%m/%d', blank=True)
	department 			     = models.ForeignKey(Department, on_delete=models.CASCADE,default=0,blank=True)
	section 			     = models.ForeignKey(Section, on_delete=models.CASCADE,default=0,blank=True)
	designation 		     = models.ForeignKey(Designation, on_delete=models.CASCADE,default=0,blank=True)
	# departmentanddesignation = models.ForeignKey(DepartmentAndDesignation, on_delete=models.CASCADE,default=0,blank=True)
	# departmentandsection     = models.ForeignKey(DepartmentAndSection, on_delete=models.CASCADE,default=0,blank=True)
	# sectionandteam 		     = models.ForeignKey(SectionAndTeam, on_delete=models.CASCADE,default=0,blank=True)
	# department 			     = models.ForeignKey(Department, on_delete=models.CASCADE,default=0,blank=True)
	# designation              = models.ForeignKey(DepartmentAndDesignation, on_delete=models.CASCADE,default=0,blank=True)
	# section     			 = models.ForeignKey(DepartmentAndSection, on_delete=models.CASCADE,default=0,blank=True)
	team 		             = models.ForeignKey(Team, on_delete=models.CASCADE,default=0,blank=True)
	#team 		             = models.ForeignKey(SectionAndTeam, on_delete=models.CASCADE,default=0,blank=True)
	grade					 = models.ForeignKey(Grade,on_delete=models.CASCADE,default=0)


	class Meta:
		ordering = ('name',)
		#verbose_name = 'category'
		#verbose_name_plural = 'categories'

	def __str__(self):
		return self.name
