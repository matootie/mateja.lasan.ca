from django.test import TestCase

from resume.models import Location


class LocationTest(TestCase):
    """
    A collection of tests for the Location model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the testing data for the Location model.
        """

        cls.instance_one = Location.objects.create(
            city="Toronto",
            province="Ontario",
            country="Canada")

        cls.instance_two = Location.objects.create(
            city="Montreal",
            province="Quebec",
            country="Canada")

    def test_created_correctly(self):
        """
        Test to ensure the Location models have been created correctly.
        """

        self.assertIn(
            self.instance_one,
            Location.objects.all())

        self.assertIn(
            self.instance_two,
            Location.objects.all())

    def test_string_format(self):
        """
        Test to ensure the Location model is properly casted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Toronto, Ontario, Canada")

        self.assertEqual(
            str(self.instance_two),
            "Montreal, Quebec, Canada")

    def test_verbose_name(self):
        """
        Test to ensure the Location model has a consistent verbose name.
        """

        self.assertEqual(
            str(Location._meta.verbose_name),
            "Location")

    def test_verbose_plural_name(self):
        """
        Test to ensure the Location model has a consistent verbose plural name.
        """

        self.assertEqual(
            str(Location._meta.verbose_name_plural),
            "Locations")

    def test_object_ordering(self):
        """
        Test to ensure the Location models are ordered accordingly.
        """

        self.assertLess(
            list(Location.objects.all()).index(self.instance_one),
            list(Location.objects.all()).index(self.instance_two))
