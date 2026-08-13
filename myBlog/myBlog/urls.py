"""
URL configuration for myBlog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

handler404='common.error_views.error_404'
handler500='common.error_views.error_500'
handler403='common.error_views.error_403'
handler400='common.error_views.error_400'





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('user/', include('login.urls')),
    path('my-profile/', include('myProfile.urls')),
    path('my-settings/', include('mySettings.urls')),
    path('myPosts/', include('myPosts.urls')),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
