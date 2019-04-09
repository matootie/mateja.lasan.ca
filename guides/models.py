from django.db import models


class Tag(models.Model):
    """
    Model representing a Guide tag.
    """

    value = models.CharField(max_length=20)
    description = models.TextField(blank=True, null=True)
    parent_tag = models.ForeignKey(
        'Tag', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        """
        String format of the Tag model.
        """

        ancestry = [str(self.value)]

        def get_ancestry(tag):
            if tag.parent_tag:
                ancestry.append(str(tag.parent_tag.value))
                get_ancestry(tag.parent_tag)
            return

        get_ancestry(self)

        return "/".join(ancestry[::-1])

    class Meta:
        """
        Meta properties of the Tag model.
        """

        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Guide(models.Model):
    """
    Model representing a full guide.
    """

    title = models.CharField(max_length=140)
    content_md = models.TextField(null=True, blank=True)
    content_html = models.TextField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, related_name='guides')
    published = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """
        String format of the Guide model.
        """

        return f'{self.title}'

    class Meta:
        """
        Meta properties of the Guide model.
        """

        verbose_name = 'Guide'
        verbose_name_plural = 'Guides'
