from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import Http404

from guides.models import Tag
from guides.models import Guide


def main_view(request):
    """
    The main view, displaying all tags.
    """

    # Get all top level tags.
    tags = Tag.objects.all().filter(parent_tag=None)

    return render(
        request,
        "guides/main_view.html",
        {
            "tags": tags, })


def tag_view(request, tag_id):
    """
    The tag detail view, displaying all guides related to the tag.
    """

    tag = get_object_or_404(Tag, id=tag_id)

    guide_list = tag.guides.all()

    return render(
        request,
        "guides/tag_view.html",
        {
            "tag": tag,
            "guides": guide_list, })

def guide_view(request, tag_id, guide_id):
    """
    The guide view, displaying the actual guide.
    """

    guides = get_object_or_404(Tag, id=tag_id).guides.all()

    try:
        guide = guides.get(id=guide_id)
    except Guide.DoesNotExist:
        raise Http404

    lightmode = None
    if request.method == "GET":
        if "light" in request.GET:
            lightmode = True

    return render(
        request,
        "guides/guide_view.html",
        {
            "lightmode": lightmode,
            "guide": guide, })
