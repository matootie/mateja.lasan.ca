"""
Admin registrations for models.
"""

from django.contrib import admin
from django.contrib.contenttypes.admin import GenericTabularInline

from resume.models import ComputerSkill
from resume.models import EducationExperience
from resume.models import Location
from resume.models import Skill
from resume.models import VolunteerExperience
from resume.models import WorkExperience
from resume.models import CoverLetter


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    fields = (
        "description",)
    list_display = (
        "id",
        "description",)


@admin.register(ComputerSkill)
class ComputerSkillAdmin(admin.ModelAdmin):
    fields = (
        "name",
        "proficiency",
        "parent_skill",
        "colour", )
    list_display = (
        "proficiency",
        "parent_skill",
        "name", )


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    fields = (
        "country",
        "province",
        "city",)
    list_display = (
        "country",
        "province",
        "city",)


@admin.register(EducationExperience)
class EducationExperienceAdmin(admin.ModelAdmin):
    fields = (
        "location",
        "start_date",
        "end_date",
        "institution",
        "accreditation",)
    list_display = (
        "institution",
        "accreditation",)


@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    fields = (
        "location",
        "start_date",
        "end_date",
        "employer",
        "position",)
    list_display = (
        "employer",
        "position",)


@admin.register(VolunteerExperience)
class VolunteerExperienceAdmin(admin.ModelAdmin):
    fields = (
        "location",
        "start_date",
        "end_date",
        "recipient",)
    list_display = (
        "recipient",)


@admin.register(CoverLetter)
class CoverLetterAdmin(admin.ModelAdmin):
    fields = (
        "text", )
    list_display = (
        "created", )
