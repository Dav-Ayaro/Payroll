from django.shortcuts import render
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import HttpResponseRedirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
# Create your views here.


def is_accountant(user):
    return user.groups.filter(name='Accountant').exists()

def is_manager(user):
    return user.groups.filter(name='Manager').exists()

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



@login_required
@user_passes_test(is_accountant)
def accountant_view(request):
    return render(request, 'accountant_template.html')

@login_required
@user_passes_test(is_manager)
def manager_view(request):
    return render(request, 'manager_template.html')

def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))