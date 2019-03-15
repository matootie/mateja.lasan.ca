from django.test import TestCase

from resume.models import Skill


class SkillTest(TestCase):
    """
    A collection of tests for the Skill model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the testing data for the Skill model.
        """

        cls.instance_one = Skill.objects.create(
            description="Dependable in a team setting")

        cls.instance_two = Skill.objects.create(
            description="Able to quickly analyze a problem and develop an effective response")

    def test_created_correctly(self):
        """
        Test to ensure the Skill models have been created correctly.
        """

        self.assertIn(
            self.instance_one,
            Skill.objects.all())

        self.assertIn(
            self.instance_two,
            Skill.objects.all())

    def test_string_format(self):
        """
        Test to ensure the Skill model is properly casted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Dependable in a...")

        self.assertEqual(
            str(self.instance_two),
            "Able to quickly...")

    def test_verbose_name(self):
        """
        Test to ensure the Skill model has a consistent verbose name.
        """

        self.assertEqual(
            str(Skill._meta.verbose_name),
            "Resume Skill")

    def test_verbose_plural_name(self):
        """
        Test to ensure the Skill model has a consistent verbose plural name.
        """

        self.assertEqual(
            str(Skill._meta.verbose_name_plural),
            "Resume Skills")
