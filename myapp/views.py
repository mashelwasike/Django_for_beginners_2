from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    return render(request,'home.html')

# requiring login to open the template
@login_required(login_url='login')
def create(request):
    return render(request,'create.html')

# signing up the user
def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            user = form.save()
            # Loging in the user after sign up
            login(request,user)
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request,'signup.html',{'form':form})

# Loging in the user
def log_in(request):
    if request.method == "POST":
        form_1 = AuthenticationForm(data = request.POST)
        if form_1.is_valid():
            user = form_1.get_user()
            login(request,user)
            # redirecting after login
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('home')
    else:
        form_1 = AuthenticationForm()
    return render(request,'login.html',{'form':form_1})

# Loging out user
def log_out(request):
    logout(request)
    return redirect('home')