from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
# from django.db.models.base import ModelStateFieldsCacheDescriptor


class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)

    user_webpage = models.URLField(blank=True)
    user_facebook_link = models.URLField(blank=True)
    user_instagram_link = models.URLField(blank=True)

    user_presentation = models.TextField()
    user_birthdate = models.DateField(blank=True)
    user_unmarried_lname = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return self.user.username



class GroupProfile(models.Model):

    group = models.OneToOneField(Group, on_delete=models.PROTECT)

    group_description = models.CharField(max_length=250, blank=True)
    group_presentation = models.TextField()

    group_ext_url = models.URLField(blank=True)

    def __str__(self):
        return self.group.name



class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name



class Post(models.Model):
    class Meta:
        ordering = ['-publish_date']

    title = models.CharField(max_length=240, unique=True)
    subtitle = models.CharField(max_length=240, blank=True)
    slug = models.SlugField(max_length=240, unique=True)
    body = models.TextField()
    meta_description = models.CharField(max_length=200, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    publish_date = models.DateTimeField(blank=True, null=True)
    published = models.BooleanField(default=False)

    author = models.ForeignKey(UserProfile, on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title

