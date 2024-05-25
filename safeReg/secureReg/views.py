from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Module, Registration


def home(request):
    
    return render(request, 'index.html')


def register(request):
    form = UserForm()
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('two_factor:login')
        
    context = {'RegistrationForm': form}
    
    return render(request, 'register.html', context)


@login_required(login_url='two_factor:login')
def dashboard(request):
    enrolled_modules = Registration.objects.filter(user=request.user).select_related('module')
    
    context = {
        'enrolled_modules': enrolled_modules,
    }
    
    return render(request, 'dashboard.html', context)

'''
@login_required(login_url='two_factor:login')
def modules(request):

    return render(request, 'modules.html')'''
  
@login_required(login_url='two_factor:login')
def modules(request):
    modules = Module.objects.all()
    user = request.user
    
    enrollment_status = {module.id: module.registration_set.filter(user=user).exists() for module in modules}
    
    return render(request, 'modules.html', {'modules': modules, 'enrollment_status': enrollment_status})
 

#Displays available Modules
@login_required(login_url='two_factor:login')
def enroll(request, module_id):
    module = get_object_or_404(Module, id=module_id)
    registration, created = Registration.objects.get_or_create(user=request.user, module=module)
    registration.status = 'pending'
    registration.save()
    return redirect('modules')


def user_logout(request):
    
    auth.logout(request)
    messages.success(request, "Successfully Logged Out!")
    
    return redirect("")


def account_locked(request):
    
    return render(request, 'account-locked.html')