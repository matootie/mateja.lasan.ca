from django.test import TestCase

from guides.templatetags.guides_tags import parse_markdown, parse_html


class GuidesTemplateTagsTests(TestCase):
    """
    A collection of tests for the Guides app template tags.
    """

    def test_parse_markdown(self):
        """
        Test parsing Markdown into safe HTML.
        """

        # markdown2 appends a newline to formatted markdown text.
        self.assertEqual(
            parse_markdown("# Hello, world!"),
            "<h1>Hello, world!</h1>\n")

    def test_parse_html(self):
        """
        Test parsing HTML into safe HTML.
        """

        self.assertEqual(
            parse_html("<h1>Hello, Earth!</h1>"),
            "<h1>Hello, Earth!</h1>")
