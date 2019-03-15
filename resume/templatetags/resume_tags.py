from django import template

register = template.Library()


@register.simple_tag()
def site_title(text=None):
    if text:
        return f"Mateja Lasan | {text}"
    return "Mateja Lasan"
