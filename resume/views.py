from django.shortcuts import render
from django.views import View

from resume.models import ComputerSkill
from resume.models import EducationExperience
from resume.models import Skill
from resume.models import VolunteerExperience
from resume.models import WorkExperience
from resume.models import CoverLetter


class Main(View):
    """
    The main resume view, displaying all information.
    """

    @staticmethod
    def get(request, **kwargs):
        """
        GET method handler.
        """

        skills = Skill.objects.all()
        computer = ComputerSkill.objects.filter(parent_skill=None)
        education = EducationExperience.objects.all()
        work = WorkExperience.objects.all()
        volunteer = VolunteerExperience.objects.all()
        cover_letter = CoverLetter.objects.first()

        params = {
            "skills": skills,
            "computer_skills": computer,
            "education_experience": education,
            "work_experience": work,
            "volunteer_experience": volunteer,
            "cover_letter": cover_letter, }

        return render(
            request,
            "resume/main.html",
            params)
