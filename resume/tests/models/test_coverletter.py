from django.test import TestCase

from resume.models import CoverLetter


class CoverLetterTest(TestCase):
    """
    A collection of tests for the CoverLetter model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the testing data for the CoverLetter model.
        """

        cls.instance_one = CoverLetter.objects.create(
            text="This is an example of one of my potential cover letters.")

        cls.instance_two = CoverLetter.objects.create(
            text="This is yet another example of one of my potential cover letters.")

    def test_created_correctly(self):
        """
        Test to ensure the CoverLetter models have been created correctly.
        """

        self.assertIn(
            self.instance_one,
            CoverLetter.objects.all())

        self.assertIn(
            self.instance_two,
            CoverLetter.objects.all())

    def test_string_format(self):
        """
        Test to ensure the CoverLetter model is properly casted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "This is an...")

        self.assertEqual(
            str(self.instance_two),
            "This is ye...")

    def test_verbose_name(self):
        """
        Test to ensure the CoverLetter model has a consistent verbose name.
        """

        self.assertEqual(
            str(CoverLetter._meta.verbose_name),
            "Cover Letter")

    def test_verbose_plural_name(self):
        """
        Test to ensure the CoverLetter model has a consistent verbose plural name.
        """

        self.assertEqual(
            str(CoverLetter._meta.verbose_name_plural),
            "Cover Letters")
