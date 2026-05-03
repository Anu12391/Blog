from django.shortcuts import render, redirect

from login.forms import RegisterForm


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

