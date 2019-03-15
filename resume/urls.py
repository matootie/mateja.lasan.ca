from django.urls import path

from resume import views

app_name = "resume"
urlpatterns = [
    path("", views.Main.as_view(), name="home"), ]
