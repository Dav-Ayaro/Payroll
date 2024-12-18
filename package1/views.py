from django.shortcuts import render
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.utils import timezone
import random, string
from django.core.exceptions import ObjectDoesNotExist
from urllib.parse import urlencode
# Create your views here.

class UserRoles:
    @staticmethod
    def is_accountant(user):
        return user.groups.filter(name='Accountant').exists()

    @staticmethod
    def is_hr(user):
        return user.groups.filter(name='HR').exists()

    @staticmethod
    def is_manager(user):
        return user.groups.filter(name='Manager').exists()

    @staticmethod
    def is_admin(user):
        return user.is_superuser

# Use the `user_passes_test` decorator to restrict views based on roles
accountant_required = user_passes_test(UserRoles.is_accountant, login_url='login')
hr_required = user_passes_test(UserRoles.is_hr, login_url='login')
manager_required = user_passes_test(UserRoles.is_manager, login_url='login')
admin_required = user_passes_test(UserRoles.is_admin, login_url='login')




class systemRequirements():
    def __init__(self):
        pass

    def date_time(self):
        present_datetime = timezone.localtime(timezone.now)
        return present_datetime
    
    def random_generator(self, lenght):
        characters = (string.ascii_letters + string.digits + string.punctuation) 
        return ''.join([random.choice(characters)for i in range(lenght)])
    
    def render_view(self, request, view_file, **kwargs):
        return render(request, view_file, kwargs)

    def redirection_func(self, redirect_path=None, **kwargs):
        if kwargs:
            redirect_path += '?' + urlencode(kwargs)
        return HttpResponseRedirect(reverse(redirect_path))

    def get_employees_details(self, request):
        get_user = request.user
        if get_user:
            try:
                return get_user.employee_name
            except ObjectDoesNotExist:
                return False
        return False

    def manager_member(self, request):
        user = request.user.manager_information
        if user:
            return user
        else:
            return False
        
    def account_member(self, request):
        user = request.user.account_info
        if user: return user
        else: return False

    def hr_member(self, request):
        user = request.user.human_recources
        if user: return user
        else:
            return False

    def get_all_Employee_details():
        employee = Employee_details.objects.all()
        return employee

    
class RenderUrls(systemRequirements):
    
    def unkown_user(self, request):
        return None

object = RenderUrls()


def is_accountant(user):
    return user.groups.filter(name='Accountant').exists()
    
def is_manager(user):
    return user.groups.filter(name='Manager').exists()
def is_hr(user):
    return user.group.filter(name='HR').exists()

def index(request):
    wrong_credentials = False
    if request.method == 'POST':
        next = request.POST.get('next_url')
        capture_form_data = LoginForm(request.POST)
        if capture_form_data.is_valid():
            user = authenticate(username=capture_form_data.cleaned_data['username'],
            password=capture_form_data.cleaned_data['password'])
            if user is not None:
                if user.is_staff:
                    login(request, user)
                    if next:
                        return HttpResponseRedirect(next)
                    elif request.user.is_superuser:
                        return HttpResponseRedirect('/admin/')
                    elif is_accountant:
                        return HttpResponseRedirect(reverse('Accountant_view'))
                    elif is_manager:
                        return HttpResponseRedirect(reverse('manager_view'))
                    elif is_hr:
                        return HttpResponseRedirect(reverse('hr_view'))
                    else:
                        return HttpResponseRedirect(reverse('logout_page'))
                else:
                    wrong_credentials = True
            else:
                wrong_credentials = True
        else:
            capture_form_data=capture_form_data
    return render(request, 'package1/index.html',{
        'LoginForm':LoginForm(), 'wrong_credentials':wrong_credentials
    })

def registration_view(request):
    if request.method == "POST":
        capture_form_data = AddUserForm(request.POST)
        if capture_form_dat.is_valid():
            adduser = 
    return render(request, 'package1/register.html',{
    })

@login_required
@user_passes_test(is_accountant)
def accountant_view(request):
    return render(request, 'accountant_template.html')

@login_required
@user_passes_test(is_manager)
def manager_view(request):
    return render(request, 'manager_template.html')

#accountant pages will be processed here
@accountant_required
def accountant_view(request):
    return render(request, 'accountant_template.html')

#all hr pages will be processed here
@hr_required
def hr_view(request):
    return render(request, 'hr_template.html')

#all managers pages will be processed here
@manager_required
def manager_view(request):
    return render(request, 'manager_template.html')

#an alternative admin will be processed here
@admin_required
def admin_view(request):
    return render(request, 'admin_view.html')


def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))