from django.test import TestCase, TransactionTestCase, Client
from django.utils import timezone
from django.http import Http404

from guides import views
from guides import models


class GuidesMainViewTests(TransactionTestCase):
    """
    A collection of test cases for the Resume app main view.
    """

    @classmethod
    def setUp(cls):
        """
        Initialize some testing data for the main view.
        """

        cls.client = Client()

        cls.tag_one = models.Tag.objects.create(
            value="Python",
            description="A collection of tags regarding the Python programming language.")

        cls.tag_two = models.Tag.objects.create(
            value="Django",
            description="A collection of tags regarding the Django Web Framework in Python.",
            parent_tag=cls.tag_one)

        cls.guide_one = models.Guide.objects.create(
            title="Unit testing in Python 3",
            content_md="Foo bar lorem ipsum.")

        cls.guide_one.tags.set([cls.tag_one])

        cls.guide_two = models.Guide.objects.create(
            title="Serving Django Staticfiles on Amazon S3",
            content_md="Foo foo bar bar lorem.")

        cls.guide_two.tags.set([cls.tag_two])

    def test_main_url(self):
        """
        Test the main view url.
        """

        response = self.client.get("/guides/")

        self.assertEqual(
            response.status_code,
            200)

    def test_tag_url(self):
        """
        Test the tag view url.
        """

        response_one = self.client.get("/guides/{}/".format(self.tag_one.id))
        response_two = self.client.get("/guides/{}/".format(self.tag_two.id))

        self.assertEqual(
            response_one.status_code,
            200)

        self.assertEqual(
            response_two.status_code,
            200)

    def test_guide_url(self):
        """
        Test the guide view url.
        """

        response_one = self.client.get("/guides/{}/{}/".format(
            self.tag_one.id,
            self.guide_one.id))

        response_two = self.client.get("/guides/{}/{}/".format(
            self.tag_two.id,
            self.guide_two.id))

        response_three = self.client.get("/guides/{}/{}/".format(
            self.tag_two.id,
            23))

        self.assertEqual(
            response_one.status_code,
            200)

        self.assertEqual(
            response_two.status_code,
            200)

        self.assertEqual(
            response_three.status_code,
            404)

    def test_main_context(self):
        """
        Test that the main view contains the correct context.
        """

        response = self.client.get("/guides/")

        self.assertQuerysetEqual(
            response.context["tags"],
            models.Tag.objects.filter(parent_tag=None),
            transform=lambda x: x)

    def test_tag_context(self):
        """
        Test that the tag view contains the correct context.
        """

        response_one = self.client.get("/guides/{}/".format(self.tag_one.id))
        response_two = self.client.get("/guides/{}/".format(self.tag_two.id))

        self.assertEqual(
            response_one.context["tag"],
            self.tag_one)

        self.assertQuerysetEqual(
            response_one.context["guides"],
            models.Guide.objects.filter(tags=self.tag_one),
            transform=lambda x: x)

        self.assertEqual(
            response_two.context["tag"],
            self.tag_two)

        self.assertQuerysetEqual(
            response_two.context["guides"],
            models.Guide.objects.filter(tags=self.tag_two),
            transform=lambda x: x)

    def test_guide_context(self):
        """
        Test that the guide view contains the correct context.
        """

        response_one = self.client.get("/guides/{}/{}/".format(
            self.tag_one.id,
            self.guide_one.id))

        response_two = self.client.get("/guides/{}/{}/?light".format(
            self.tag_two.id,
            self.guide_two.id))

        self.assertEqual(
            response_one.context["lightmode"],
            None)

        self.assertEqual(
            response_one.context["guide"],
            self.guide_one)

        self.assertEqual(
            response_two.context["lightmode"],
            True)

        self.assertEqual(
            response_two.context["guide"],
            self.guide_two)
