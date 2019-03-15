from django.test import TestCase

from guides.models import Tag
from guides.models import Guide


class TagTest(TestCase):
    """
    A collection of tests for the Tag model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the test data for the Tag model.
        """

        cls.instance_one = Tag.objects.create(
            value="Server Administration")
        cls.instance_two = Tag.objects.create(
            value="Web Development",
            parent_tag=cls.instance_one)

    def test_string_format(self):
        """
        Test to ensure the model is properly formatted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Server Administration")

        self.assertEqual(
            str(self.instance_two),
            "Server Administration/Web Development")


class GuideTest(TestCase):
    """
    A collection of tests for the Guide model.
    """

    @classmethod
    def setUpTestData(cls):
        """
        Initialize the test data for the Guide model.
        """

        tag_one = Tag.objects.create(
            value="Server Administration")
        tag_two = Tag.objects.create(
            value="Web Development",
            parent_tag=tag_one)
        cls.instance_one = Guide.objects.create(
            title="Using MongoDB with Django on Ubuntu 18.04 LTS",
            content_md="This is some example content.")
        cls.instance_two = Guide.objects.create(
            title="Initial Server Configuration on Ubuntu 18.04 LTS",
            content_md="Some other example content. Blah blah? Yes.")

        cls.instance_one.tags.add(tag_one)
        cls.instance_two.tags.add(tag_two)

    def test_string_format(self):
        """
        Test to ensure the model is properly formatted to a string.
        """

        self.assertEqual(
            str(self.instance_one),
            "Using MongoDB with Django on Ubuntu 18.04 LTS")

        self.assertEqual(
            str(self.instance_two),
            "Initial Server Configuration on Ubuntu 18.04 LTS")

