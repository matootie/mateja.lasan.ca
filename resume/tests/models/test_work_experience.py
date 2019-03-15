from django.test import TestCase
from django.utils import timezone

from resume.models import Location
from resume.models import WorkExperience


class WorkExperienceTest(TestCase):
    """
    A collection of tests for the WorkExperience model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the testing data for the WorkExperience model.
        """

        # A location for one of the object instances.
        location = Location.objects.create(
            city="Toronto",
            province="Ontario",
            country="Canada")

        # Two dates to use in both instances.
        long_time_ago = timezone.datetime.today() - timezone.timedelta(days=129)
        short_while_ago = timezone.datetime.today() - timezone.timedelta(days=42)

        # Instance one has all information provided.
        cls.instance_one = WorkExperience.objects.create(
            location=location,
            start_date=long_time_ago,
            end_date=short_while_ago,
            position="Ticket Seller",
            employer="Ticketmaster")

        # Instance two is missing a location, and a start date.
        cls.instance_two = WorkExperience.objects.create(
            start_date=short_while_ago,
            position="Web Developer",
            employer="Freelance")

    def test_created_correctly(self):
        """
        Test to ensure the WorkExperience models have been created correctly.
        """

        self.assertIn(
            self.instance_one,
            WorkExperience.objects.all())

        self.assertIn(
            self.instance_two,
            WorkExperience.objects.all())

    def test_string_format(self):
        """
        Test to ensure the WorkExperience model is properly casted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Ticket Seller, Ticketmaster")

        self.assertEqual(
            str(self.instance_two),
            "Web Developer, Freelance")

    def test_verbose_name(self):
        """
        Test to ensure the WorkExperience model has a consistent verbose name.
        """

        self.assertEqual(
            str(WorkExperience._meta.verbose_name),
            "Work Experience")

    def test_verbose_plural_name(self):
        """
        Test to ensure the Work Experience model has a consistent verbose plural name.
        """

        self.assertEqual(
            str(WorkExperience._meta.verbose_name_plural),
            "Work Experiences")

    def test_location_deletion(self):
        """
        Test to ensure the model is still functional when it's Location is deleted.
        """

        Location.objects.get(pk=self.instance_one.location.pk).delete()

        # We need to get an updated copy of instance one,
        # because changes were made (deletion of related location).
        instance_one = WorkExperience.objects.get(pk=self.instance_one.pk)

        self.assertEqual(
            instance_one.location,
            None)

        self.assertEqual(
            self.instance_two.location,
            None)
