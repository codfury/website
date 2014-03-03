from django.utils import timezone
from django.db import models


class PublishedPressReleaseManager(models.Manager):
    def get_queryset(self):
        return super(PublishedPressReleaseManager, self).get_queryset().filter(
            release_date__lt=timezone.now())


class PressRelease(models.Model):
    objects = models.Manager()
    published_objects = PublishedPressReleaseManager()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)
    body = models.TextField()
    release_date = models.DateTimeField()

    class Meta:
        ordering = ('-release_date',)


class PressMention(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    publisher = models.CharField(max_length=60)
    publication_date = models.DateField()
    url = models.URLField()
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, null=True)
    author = models.CharField(max_length=100)
    notes = models.TextField()

    # TODO: add a projects FK.

    class Meta:
        ordering = ('-publication_date',)