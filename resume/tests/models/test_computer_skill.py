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
            proficiency=50,
            colour="rgb(220,200,0)")

        cls.instance_two = ComputerSkill.objects.create(
            name="Django",
            proficiency=62,
            parent_skill=cls.instance_one)

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
            "Django")

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

    def test_subskill_lookup(self):
        """
        Test to ensure lookup of sub skills works correctly.
        """

        self.assertEqual(
            self.instance_one,
            self.instance_two.parent_skill)

    def test_subskill_reverse_lookup(self):
        """
        Test to ensure reverse lookup of sub skills works correctly.
        """

        self.assertIn(
            self.instance_two,
            self.instance_one.subskills.all())

    def test_colours(self):
        """
        Test to ensure the colours are going to display correctly.
        """

        self.assertEqual(
            self.instance_one.get_colour,
            "rgb(220,200,0)")

        self.assertEqual(
            self.instance_two.get_colour,
            "rgba(230,62,123,0.75)")
