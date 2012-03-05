from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template.context import RequestContext
from resumes.models import UserResume

def list_resume(request):
    return HttpResponse()


def view_resume(request, resume_id=None, user_id=None):
    resume = None

    if resume_id:
        resume = get_object_or_404(UserResume, id=resume_id)
    elif user_id:
        resume = get_object_or_404(UserResume, user__id=user_id)

    return render_to_response('resumes/resume.html', {'resume': resume, }, context_instance=RequestContext(request))


def export_resume(request, resume_id=None, user_id=None):
    resume = None

    if resume_id:
        resume = get_object_or_404(UserResume, id=resume_id)
    elif user_id:
        resume = get_object_or_404(UserResume, user__id=user_id)

    return render_to_response('resumes/resume.html', {'resume': resume, }, context_instance=RequestContext(request))