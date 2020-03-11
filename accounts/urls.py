from django.contrib import admin
from django.urls import path
from accountsapp import views as app

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', app.home, name="home"),
]
