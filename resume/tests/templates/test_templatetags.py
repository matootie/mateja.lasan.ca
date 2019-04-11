from django.test import TestCase

from resume.templatetags.resume_tags import site_title


class ResumeTagsTest(TestCase):
    """
    A collection of tests for the Resume app template tags.
    """

    def test_site_title(self):
        """
        Test that the site title is formatted correctly.
        """

        self.assertEqual(
            site_title(),
            "Mateja Lasan")

        self.assertEqual(
            site_title("Resume"),
            "Mateja Lasan | Resume")
