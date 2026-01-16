"""lipetsk URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include, re_path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"),
    path('attractions/page1', views.attractions_view1, name='attractions1'),
    path("attractions/page2", views.attractions_view2, name='attractions2'),
    path("news", views.news, name="news"),
    path("page2_1", views.page2_1, name="page2_1"),
    path("page2_2", views.page2_2, name="page2_2"),
    path("page3_1", views.page3_1, name="page3_1"),
    path("page3_2", views.page3_2, name="page3_2"),
    path("other/map", views.map, name="map"),
    path("other/weather", views.weather, name="weather"),

]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
