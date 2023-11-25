from django.urls import path

from . import views

urlpatterns = [
    path("", views.employees, name="index"),
    path('employee/<int:employee_id>/', views.employee_details, name='employee_details'),
    path('create_employee', views.create_employee, name="create_employee"),
    path('update_employee/<int:employee_id>/', views.update_employee, name="update_employee"),
    path('delete_employee/<int:employee_id>/', views.delete_employee, name='delete_employee'),
    path('success', views.success_action, name='success_action'),
 
]