from django.contrib import admin
from models import *

class UserResumeEducationInline(admin.StackedInline):
    model = UserResumeEducation
    extra = 1


class UserResumeLanguageInline(admin.StackedInline):
    model = UserResumeLanguage
    extra = 1


class UserResumeInterestInline(admin.StackedInline):
    model = UserResumeInterest
    extra = 1


class UserResumeQualificationInline(admin.StackedInline):
    model = UserResumeQualification
    extra = 1


class UserResumeJobInline(admin.StackedInline):
    model = UserResumeJob
    extra = 1


class UserResumeReferenceInline(admin.StackedInline):
    model = UserResumeReferences
    extra = 1


class UserResumeAdmin(admin.ModelAdmin):
    inlines = [
        UserResumeEducationInline, UserResumeLanguageInline,
        UserResumeInterestInline, UserResumeQualificationInline,
        UserResumeJobInline, UserResumeReferenceInline
    ]

admin.site.register(Company)
admin.site.register(School)
admin.site.register(UserResume, UserResumeAdmin)
admin.site.register(UserResumeEducation)
admin.site.register(UserResumeLanguage)
admin.site.register(UserResumeInterest)
admin.site.register(UserResumeQualification)
admin.site.register(UserResumeJob)
admin.site.register(UserResumeReferences)