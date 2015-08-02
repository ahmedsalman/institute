from django.db import models
from django.utils.translation import ugettext as _

from base.models import TimeStampAwareModel

from django_countries import CountryField

class TimeStampAwareModel( models.Model ):
    """
    A model class that can be used as super class
    for any model that is considered timestamp aware 
    model.
    """
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(blank=True, null=True)

    def is_deleted(self):
        if self.date_deleted:
            return True
        return False
    is_deleted.boolean = True
    
    class Meta:
        abstract = True

class Institute( TimeStampAwareModel ):
    """
    Institute model
    """
    title = models.CharField(_('title'), max_length = 100)
    description = models.TextField(_('description'), null = True, blank = True)
    country = CountryField(_('country'), )

    def __unicode__(self):
        return _("%s") % (self.title)


    class Meta:
        app_label = "institute"
        verbose_name = "institute"
        verbose_name_plural = "institutes"


class Discipline( TimeStampAwareModel ):
    """
    Discipline model
    """
    institute = models.ManyToManyField(Institute)

    title = models.CharField(_('title'), max_length = 30)

    def __unicode__(self):
        return _("%s") % (self.title)


    class Meta:
        verbose_name = "discipline"
        verbose_name_plural = "disciplines"


class SubDiscipline( TimeStampAwareModel ):
    """
    SubDiscipline model
    """
    institute = models.ForeignKey(Institute)
    discipline = models.ForeignKey(Discipline)

    title = models.CharField(_('title'), max_length = 30)
    description = models.TextField(_('description'), null = True, blank = True)
    code = models.CharField(_('subdiscipline code'), max_length = 30)

    def __unicode__(self):
        return _("%s") % (self.title)


    class Meta:
        verbose_name = "subdiscipline"
        verbose_name_plural = "subdisciplines"
        unique_together = (("institute", "discipline", "title"),)
