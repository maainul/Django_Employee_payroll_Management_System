"""payroll URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from employee.views import EmployeeUpdateView
#from employee.views import EmployeeDeleteView
from django.contrib import admin
from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.employee_list, name='employee_list'),
   # path('', EmployeeListView.as_view(), name='employee_list'),
    path('create/', views.employee_create_view, name='employee_create_view'),
    path('<int:id>/', views.employee_detail, name='employee_detail'),
    #re_path(r'^employee_list/(?P<id>\d+)/$', views.employee_detail, name='employee_detail'),
    #path('new/', views.get_name, name='get_name'),
    
    #path('<int:id>/edit/', EmployeeUpdateView.as_view(), name='employee_update'),
    #path('<int:id>/delete/', EmployeeDeleteView.as_view(), name='employee_delete'),
    path('<int:id>/delete/', views.employee_delete, name='employee_delete'),
   # path('<int:id>/edit/', views.employee_update, name='employee_update'),

   path('department/',views.department_list, name='department_list'),
   path('department/create',views.department_create, name='department_create'),
   path('department/<int:id>/delete/', views.department_delete, name='department_delete'),


   path('section/',views.section_list, name='section_list'),
   path('section/create',views.section_create, name='section_create'),
   path('section/<int:id>/delete/', views.employee_delete, name='employee_delete'),


   path('designation/',views.designation_list, name='designation_list'),
   path('designation/create',views.designation_create, name='designation_create'),
   path('designation/<int:id>/delete/', views.employee_delete, name='employee_delete'),

]
