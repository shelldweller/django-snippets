from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _


class Snippet(models.Model):
    
    name = models.CharField(_("name"), unique=True, max_length=50,
        help_text=_("""Unique name to identify your snippet (e.g., "home-page-announcement"). Do not change this field unless you know what you are doing."""))
    content = models.TextField(_("content"))
    is_html = models.BooleanField(_("is HTML?"), default=True,
        help_text=_("If checked content will be output as is and you must enter a valid HTML code."))
    is_active = models.BooleanField(_("is active"), default=True,
        help_text=_("Inactive snippets will not be rendered on the web site"))
    created_on = models.DateTimeField(_("created on"), auto_now_add=True, editable=False)
    changed_on = models.DateTimeField(_("modified on"), auto_now=True, editable=False)
    last_user = models.ForeignKey(User, verbose_name=_("last modified by"), null=True, editable=False)
    
    def __unicode__(self):
        return self.name
    
    class Meta:
        verbose_name = _("snippet")
        verbose_name_plural = _("snippets")
        ordering = ("name",)
