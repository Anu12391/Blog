from django.shortcuts import render
from django.views import View


class MyProfileView(View):
    def get(self, request):
        return render(request, "myProfile/myProfile.html")