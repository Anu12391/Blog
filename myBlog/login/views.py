from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect

from login.forms import RegisterForm,LoginForm




# Create your views here.


def register_new_user(request):
     if request.method == 'POST':
         print(request.POST)
         reg_form=RegisterForm(request.POST)
         if reg_form.is_valid():
             print(reg_form.cleaned_data)
             reg_form.save()

             return redirect("home")

     else:
        reg_form = RegisterForm()
     return render(request, 'login/new_user.html',{'reg_form':reg_form})




def login_user(request):
    if request.method == 'POST':
        print(request.POST)
        login_form=LoginForm(request.POST)
        if login_form.is_valid():
            email = login_form.cleaned_data['email']
            password = login_form.cleaned_data['password']
            user=authenticate(request,username=email,password=password)

            if user is not None:
                print("Inside")
                login(request, user)

                return redirect('home')
            else:
                messages.error(request, "Invalid username or password")



    else:
        login_form=LoginForm()
    return render(request, 'login/login.html',{'login_form':login_form})





def logout_user(request):
    logout(request)
    return redirect('login_user')


