from django.db import models
from django.utils.translation import gettext as _

class Review(models.Model):
    name = models.CharField(_("name"), max_length=50, null=False, blank=False)
    email = models.CharField(_("email"), max_length=50, null=False, blank=False)
    topic = models.CharField(_("topic"), max_length=50, null=False, blank=False)
    message = models.CharField(_("message"), max_length=500, null=False, blank=False)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date_updated"), auto_now=True)

class Vote(models.Model):
    review = models.OneToOneField(Review, verbose_name=_(""), on_delete=models.CASCADE)
    email = models.CharField(_("email"), max_length=50, null=True, blank=True)
    up_votes = models.IntegerField(_("up"), default=0)
    down_votes = models.IntegerField(_("down"), default=0)
    date_created = models.DateTimeField(_("date_created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date_updated"), auto_now=True)
