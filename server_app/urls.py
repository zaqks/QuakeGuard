from django.urls import path
from .views import server_app, check

urlpatterns = [path('', server_app), path("api", check)]
