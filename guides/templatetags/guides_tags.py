import markdown2
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.filter('parse_markdown')
def parse_markdown(markdown_text):
    """
    Filter to convert markdown text to HTML text.

    return: str: HTML text content.
    """

    html_text = markdown2.markdown(
        markdown_text,
        extras=['fenced-code-blocks'])

    return mark_safe(html_text)


@register.filter('parse_html')
def parse_html(html_text):
    """
    Filter to safely parse and render HTML text.

    return: str: Safe HTML text content.
    """

    return mark_safe(html_text)

