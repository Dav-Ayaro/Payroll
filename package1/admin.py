from django.contrib import admin
from . models import *
# Register your models here.


class SpecialUsersView(admin.ModelAdmin):
    list_display = ['username', 'email', 'is_superuser']

class EmployeeView(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'position']

class PayrollView(admin.ModelAdmin):
    list_display  = ['employee', 'pay_date', 'hours_worked', 'net_pay']


admin.site.register(SpecialUsers, SpecialUsersView)
admin.site.register(Employee,  EmployeeView)
admin.site.register(Payroll, PayrollView)