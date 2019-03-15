from django.urls import path

from guides import views


app_name = "guides"
urlpatterns = [
    path("", views.main_view, name="tags"),
    path("<str:tag_value>/", views.tag_view, name="guides"),
    path("<str:tag_value>/<int:guide_id>/", views.guide_view, name="guide"),
]

