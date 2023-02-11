from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def user_register(request):
    # if this is a POST request we need to process the form data
    template = 'register.html'
    if request.method == 'POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password']
                )
                user.save()
                login(request, user)               
                return render(request,'register.html') 
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})  

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check username and password combination if correct
        user = authenticate(username=username, password=password)
        if user is not None:
            # Save session as cookie to login the user
            login(request, user)
            # Success, now let's login the user.
            return render(request, 'home.html')
        else:
            # Incorrect credentials, let's throw an error to the screen.
            return render(request, 'register.html', {'error_message': 'Incorrect username and / or password.'})
    else:
        # No post data availabe, let's just show the page to the user.
        return render(request, 'register.html') 

def homepage(request):
    return render(request, 'home.html')         

def monthly(request):
    return render(request,'monthy.html')



def investment(request):
    return render(request,'ivestment_guide.html')

def Strategy(request):
    return render(request,'strategy.html')

