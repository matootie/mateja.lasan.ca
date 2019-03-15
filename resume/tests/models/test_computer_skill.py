from django.test import TestCase

from resume.models import ComputerSkill


class ComputerSkillTest(TestCase):
    """
    A collection of tests for the ComputerSkill model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the testing data for the ComputerSkill model.
        """

        cls.instance_one = ComputerSkill.objects.create(
            name="Python",
            proficiency=50)

        cls.instance_two = ComputerSkill.objects.create(
            name="HTML5",
            proficiency=62)

    def test_created_correctly(self):
        """
        Test to ensure the ComputerSkill models have been created correctly.
        """

        self.assertIn(
            self.instance_one,
            ComputerSkill.objects.all())

        self.assertIn(
            self.instance_two,
            ComputerSkill.objects.all())

    def test_string_format(self):
        """
        Test to ensure the ComputerSkill model is properly casted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Python")

        self.assertEqual(
            str(self.instance_two),
            "HTML5")

    def test_verbose_name(self):
        """
        Test to ensure the ComputerSkill model has a consistent verbose name.
        """

        self.assertEqual(
            str(ComputerSkill._meta.verbose_name),
            "Computer Skill")

    def test_verbose_plural_name(self):
        """
        Test to ensure the ComputerSkill model has a consistent verbose plural name.
        """

        self.assertEqual(
            str(ComputerSkill._meta.verbose_name_plural),
            "Computer Skills")
