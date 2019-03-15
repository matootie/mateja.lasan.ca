from django.test import TestCase

from resume.models import Experience


class ExperienceTest(TestCase):
    """
    A collection of tests for the Experience model.
    """

    def test_is_abstract(self):
        """
        Test to ensure the Experience model is abstract.
        """

        self.assertTrue(Experience._meta.abstract)
