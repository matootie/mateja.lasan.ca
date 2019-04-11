from django.test import TransactionTestCase, Client
from django.utils import timezone

from resume import views
from resume import models


class ResumeMainViewTests(TransactionTestCase):
    """
    A collection of test cases for the Resume app main view.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize some testing data for the main view.
        """

        cls.client = Client()

        models.Skill.objects.create(
            description="Dependable in a team setting")

        models.Skill.objects.create(
            description="Able to quickly analyze a problem and develop an effective response")

        python = models.ComputerSkill.objects.create(
            name="Python",
            proficiency=50,
            colour="rgb(220,200,0)")

        models.ComputerSkill.objects.create(
            name="Django",
            proficiency=62,
            parent_skill=python)

        guelph = models.Location.objects.create(
            city="Guelph",
            province="Ontario",
            country="Canada")

        toronto = models.Location.objects.create(
            city="Toronto",
            province="Ontario",
            country="Canada")

        montreal = models.Location.objects.create(
            city="Montreal",
            province="Quebec",
            country="Canada")

        long_time_ago = timezone.datetime.today() - timezone.timedelta(days=130)
        short_while_ago = timezone.datetime.today() - timezone.timedelta(days=29)

        models.EducationExperience.objects.create(
            location=guelph,
            start_date=long_time_ago,
            end_date=short_while_ago,
            institution="University of Guelph",
            accreditation="Bachelor of Computing")

        models.EducationExperience.objects.create(
            start_date=short_while_ago,
            institution="Ryerson University",
            accreditation="Certificate in Computer Applications Programming")

        models.WorkExperience.objects.create(
            location=toronto,
            start_date=long_time_ago,
            end_date=short_while_ago,
            position="Ticket Seller",
            employer="Ticketmaster")

        models.WorkExperience.objects.create(
            start_date=short_while_ago,
            position="Web Developer",
            employer="Freelance")

        models.VolunteerExperience.objects.create(
            location=montreal,
            start_date=long_time_ago,
            end_date=short_while_ago,
            recipient="Keele St. Public School")

        models.VolunteerExperience.objects.create(
            start_date=short_while_ago,
            recipient="Habitat for Humanity")

        models.CoverLetter.objects.create(
            text="This is an example cover letter!")

    def test_url(self):
        """
        Test the main view url.
        """

        response = self.client.get("/resume/")

        self.assertEqual(
            response.status_code,
            200)

    def test_skill_context(self):
        """
        Test that the main view contains the correct context for Skill objects.
        """

        response = self.client.get("/resume/")

        self.assertQuerysetEqual(
            response.context["skills"],
            models.Skill.objects.all())

    def test_computer_skill_context(self):
        """
        Test that the main view contains the correct context for ComputerSkill objects.
        """

        response = self.client.get("/resume/")

        self.assertQuerysetEqual(
            response.context["computer_skills"],
            models.ComputerSkill.objects.filter(parent_skill=None))

    def test_education_experience_context(self):
        """

        Test that the main view contains the correct context for EducationExperience objects.
        """

        response = self.client.get("/resume/")

        self.assertQuerysetEqual(
            response.context["education_experience"],
            models.EducationExperience.objects.all())

    def test_work_experience_context(self):
        """

        Test that the main view contains the correct context for WorkExperience objects.
        """

        response = self.client.get("/resume/")

        self.assertQuerysetEqual(
            response.context["work_experience"],
            models.WorkExperience.objects.all())

    def test_volunteer_experience_context(self):
        """

        Test that the main view contains the correct context for VolunteerExperience objects.
        """

        response = self.client.get("/resume/")

        self.assertQuerysetEqual(
            response.context["volunteer_experience"],
            models.VolunteerExperience.objects.all())

    def test_coverletter_context(self):
        """
        Test that the main view contains the correct context for CoverLetter objects.
        """

        response = self.client.get("/resume/")

        self.assertEqual(
            response.context["cover_letter"],
            models.CoverLetter.objects.first())
