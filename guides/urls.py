from django.urls import path

from guides import views


app_name = "guides"
urlpatterns = [
    path("", views.main_view, name="tags"),
    path("<int:tag_id>/", views.tag_view, name="guides"),
    path("<int:tag_id>/<int:guide_id>/", views.guide_view, name="guide"),
]
