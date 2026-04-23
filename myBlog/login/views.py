from django.shortcuts import render

# Create your views here.


def register_new_user(request):
    return render(request, 'login/new_user.html',{})
