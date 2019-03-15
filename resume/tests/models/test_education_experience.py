from django.test import TestCase
from django.utils import timezone

from resume.models import EducationExperience
from resume.models import Location


class EducationExperienceTest(TestCase):
    """
    A collection of tests for the EducationExperience model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the testing data for the EducationExperience model.
        """

        # A location for one of the object instances.
        location = Location.objects.create(
            city="Guelph",
            province="Ontario",
            country="Canada")

        # Two dates to use in both instances.
        long_time_ago = timezone.datetime.today() - timezone.timedelta(days=130)
        short_while_ago = timezone.datetime.today() - timezone.timedelta(days=29)

        # Instance one has all information provided.
        cls.instance_one = EducationExperience.objects.create(
            location=location,
            start_date=long_time_ago,
            end_date=short_while_ago,
            institution="University of Guelph",
            accreditation="Bachelor of Computing")

        # Instance two is missing a location, and a start date.
        cls.instance_two = EducationExperience.objects.create(
            start_date=short_while_ago,
            institution="Ryerson University",
            accreditation="Certificate in Computer Applications Programming")

    def test_created_correctly(self):
        """
        Test to ensure the EducationExperience models have been created correctly.
        """

        self.assertIn(
            self.instance_one,
            EducationExperience.objects.all())

        self.assertIn(
            self.instance_two,
            EducationExperience.objects.all())

    def test_string_format(self):
        """
        Test to ensure the EducationExperience model is properly casted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Bachelor of Computing, University of Guelph")

        self.assertEqual(
            str(self.instance_two),
            "Certificate in Computer Applications Programming, Ryerson University")

    def test_verbose_name(self):
        """
        Test to ensure the EducationExperience model has a consistent verbose name.
        """

        self.assertEqual(
            str(EducationExperience._meta.verbose_name),
            "Educational Credibility")

    def test_verbose_plural_name(self):
        """
        Test to ensure the EducationExperience model has a consistent verbose plural name.
        """

        self.assertEqual(
            str(EducationExperience._meta.verbose_name_plural),
            "Educational Credibility's")

    def test_location_deletion(self):
        """
        Test to ensure the model is still functional when it's Location is deleted.
        """

        Location.objects.get(pk=self.instance_one.location.pk).delete()

        # We need to get an updated copy of instance one,
        # because changes were made (deletion of related location).
        instance_one = EducationExperience.objects.get(pk=self.instance_one.pk)

        self.assertEqual(
            instance_one.location,
            None)

        self.assertEqual(
            self.instance_two.location,
            None)
