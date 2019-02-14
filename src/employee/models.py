 # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


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

class DepartmentAndDesignation(models.Model):
	department_id  = models.ForeignKey(Department,on_delete=models.CASCADE,default=0,blank=True)
	designation_id = models.ForeignKey(Designation,on_delete=models.CASCADE,default=0,blank=True)
	def __str__(self):
		return self.id

class DepartmentAndSection(models.Model):
	department_id  = models.ForeignKey(Department,on_delete=models.CASCADE,default=0,blank=True)
	section_id     = models.ForeignKey(Section,on_delete=models.CASCADE,default=0,blank=True)
	def __str__(self):
		return self.id

class SectionAndTeam(models.Model):
	section_id     = models.ForeignKey(Section,on_delete=models.CASCADE,default=0,blank=True)
	team_id        = models.ForeignKey(Team,on_delete=models.CASCADE,default=0,blank=True)
	def __str__(self):
		return self.id

class Employee(models.Model):
	name 				= models.CharField(max_length=50)
	father_name 		= models.CharField(max_length=50)
	mother_name 		= models.CharField(max_length=50)
	nid 				= models.IntegerField()
	present_address 	= models.TextField(max_length=150)
	permanent_address 	= models.TextField(max_length=150)
	phone 				= models.IntegerField()
	image         		= models.ImageField(upload_to='employee/%Y/%m/%d', blank=True)
	department 			= models.ForeignKey(Department, on_delete=models.CASCADE,default=0,blank=True)
	section 			= models.ForeignKey(Section, on_delete=models.CASCADE,default=0,blank=True)
	designation 		= models.ForeignKey(Designation, on_delete=models.CASCADE,default=0,blank=True)

	class Meta:
		ordering = ('name',)
		#verbose_name = 'category'
		#verbose_name_plural = 'categories'

	def __str__(self):
		return self.name

