from django.contrib.auth.models import User
from django.db import models
from django_extensions.db.fields import CreationDateTimeField, ModificationDateTimeField
from django.utils.translation import gettext as _, gettext_lazy as _l

class Company(models.Model):
    class Meta:
        verbose_name_plural = 'Companies'

    name = models.CharField(max_length=200, verbose_name=_l('Name'))
    address = models.CharField(max_length=255, verbose_name=_l('Address'))
    phone = models.CharField(max_length=15, verbose_name=_l('Phone'))
    city = models.CharField(max_length=200, verbose_name=_l('City'))
    state = models.CharField(max_length=200, verbose_name=_l('State'))
    country = models.CharField(max_length=200, verbose_name=_l('Country'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Name') , self.name, _('Address'), self.address)


class School(models.Model):
    name = models.CharField(max_length=200, verbose_name=_l('Name'))
    address = models.CharField(max_length=255, verbose_name=_l('Address'))
    phone = models.CharField(max_length=15, verbose_name=_l('Phone'))
    city = models.CharField(max_length=200, verbose_name=_l('City'))
    state = models.CharField(max_length=200, verbose_name=_l('State'))
    country = models.CharField(max_length=200, verbose_name=_l('Country'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Name') , self.name, _('Address'), self.address)

class UserResume(models.Model):
    user = models.ForeignKey(User, related_name='resumes', verbose_name=_l('User'))
    city = models.CharField(max_length=200, null=True, blank=True, verbose_name=_l('City'))
    state = models.CharField(max_length=200, null=True, blank=True, verbose_name=_l('State'))
    country = models.CharField(max_length=200, null=True, blank=True, verbose_name=_l('Country'))
    address = models.CharField(max_length=255, verbose_name=_l('Address'))
    website = models.URLField(max_length=255, null=True, blank=True, verbose_name=_l('Web Site'))
    mobile_phone = models.CharField(max_length=15, verbose_name=_l('Mobile Phone'))
    local_phone = models.CharField(max_length=15, null=True, blank=True, verbose_name=_l('Local Phone'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s %s' % (_('Resume for') , self.user)


class UserResumeLanguage(models.Model):
    user_resume = models.ForeignKey(UserResume, related_name='languages', verbose_name=_l('User Resume'))
    name = models.CharField(max_length=50, verbose_name=_l('Name'))
    domain = models.CharField(max_length=250, verbose_name=_l('Domain'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Language Name') , self.name, _('Domain'), self.domain)


class UserResumeEducation(models.Model):
    user_resume = models.ForeignKey(UserResume, related_name='educations', verbose_name=_l('User Resume'))
    school = models.ForeignKey(School, related_name='graduates', verbose_name=_l('School'))
    title = models.CharField(max_length=255, verbose_name=_l('Title'))
    date_start = models.DateField(verbose_name=_l('Date Start'))
    date_end = models.DateField(null=True, blank=True, verbose_name=_l('Date End'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('School') , self.school, _('Title'), self.title)


    @property
    def period(self):
        if self.date_end:
            return '%s - %s' % (self.date_start, self.date_end)

        return '%s - %s' % (self.date_start, _('Present'))


    @property
    def period_name(self):
        if self.date_end:
            return '%s - %s' % (self.date_start.strftime('%b %Y'), self.date_end.strftime('%b %Y'))

        return '%s - %s' % (self.date_start.strftime('%b %Y'), _('Present'))


class UserResumeInterest(models.Model):
    user_resume = models.ForeignKey(UserResume, related_name='interests', verbose_name=_l('User Resume'))
    name = models.CharField(max_length=200, verbose_name=_l('Name'))
    description = models.TextField(verbose_name=_l('Description'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Name') , self.name, _('Description'), self.description)

class UserResumeQualification(models.Model):
    user_resume = models.ForeignKey(UserResume, related_name='qualifications', verbose_name=_l('User Resume'))
    name = models.CharField(max_length=200, verbose_name=_l('Name'))
    description = models.TextField(verbose_name=_l('Description'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Name') , self.name, _('Description'), self.description)


class UserResumeJob(models.Model):
    user_resume = models.ForeignKey(UserResume, related_name='jobs')
    company = models.ForeignKey(Company, related_name='jobs', verbose_name=_l('Company'))
    title = models.CharField(max_length=255, verbose_name=_l('Title'))
    description = models.TextField(verbose_name=_l('Description'))
    date_start = models.DateField(verbose_name=_l('Date Start'))
    date_end = models.DateField(null=True, blank=True, verbose_name=_l('Date End'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Company') , self.company.name, _('Title'), self.title)


    @property
    def period(self):
        if self.date_end:
            return '%s - %s' % (self.date_start, self.date_end)

        return '%s - %s' % (self.date_start, _('Present'))


    @property
    def period_name(self):
        if self.date_end:
            return '%s - %s' % (self.date_start.strftime('%b %Y'), self.date_end.strftime('%b %Y'))

        return '%s - %s' % (self.date_start.strftime('%b %Y'), _('Present'))


class UserResumeReferences(models.Model):
    class Meta:
        verbose_name_plural = 'User resume references'

    user_resume = models.ForeignKey(UserResume, related_name='references')
    name = models.CharField(max_length=80, verbose_name=_l('Name'))
    title = models.CharField(max_length=100, verbose_name=_l('Title'))
    phone = models.CharField(max_length=15, verbose_name=_l('Phone'))
    address = models.CharField(max_length=255, null=True, blank=True, verbose_name=_l('Address'))
    type = models.SmallIntegerField(choices=((0, _l('Familiar')), (1, _l('Personal'))), verbose_name=_l('Type'))

    created_at = CreationDateTimeField(verbose_name=_l('Created at'))
    modified_at = ModificationDateTimeField(verbose_name=_l('Modified at'))

    def __unicode__(self):
        return '%s: %s, %s: %s' % (_('Name') , self.name, _('Phone'), self.phone)