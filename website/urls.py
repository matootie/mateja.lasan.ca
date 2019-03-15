"""
Base project URLs.
"""

from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from resume import urls as resume_urls
from guides import urls as guides_urls


# Production URLs.
urlpatterns = [
    path("resume/", include(resume_urls, namespace="resume")),
    path('admin/', admin.site.urls), ]

# Development only URLs.
if settings.DEBUG:
    urlpatterns += [
        path("guides/", include(guides_urls, namespace="guides")), ]
