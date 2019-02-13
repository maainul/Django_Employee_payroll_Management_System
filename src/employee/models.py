# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Department(models.Model):
	name = models.CharField(max_length=130)
	def __str__(self):
		return self.name

class Section(models.Model):
	name = models.CharField(max_length=130)
	def __str__(self):
		return self.name

class Designation(models.Model):
	name = models.CharField(max_length=130)
	def __str__(self):
		return self.name


class Employee(models.Model):
	name 				= models.CharField(max_length=130)
	father_name 		= models.CharField(max_length=130)
	mother_name 		= models.CharField(max_length=130)
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

