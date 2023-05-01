from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView
from .models import *
# Create your views here.
def homePage(request):
    pass
class PersonalInfoList(ListView):
    model = PersonalInfo
    template_name = 'portfol/personal.html'
    context_object_name = 'personal_list'

class ContctInfoList(ListView):
    model = Contact
    template_name = 'portfol/personal.html'
    context_object_name = 'contact_list'

class ExperienceList(ListView):
    model = Experience
    template_name = 'portfol/personal.html'
    context_object_name = 'experience_list'

class CompetenceList(ListView):
    model = competence
    template_name = 'portfol/personal.html'
    context_object_name = 'competence_list'

class EducationList(ListView):
    model = Education
    template_name = 'portfol/personal.html'
    context_object_name = 'education_list'

def Competences(request):
    ed=Education.objects.all().order_by('year')
    co=competence.objects.all()
    ex=Experience.objects.all().order_by('year')
    return render(request,'portfol/personal.html', {'education_list': ed,'experience_list':ex,'competence_list':co})

def projectHighLight(request):
    projects=Project.objects.all().order_by('-date')
    return render(request,'portfol/personal.html',{'projecthighlight':projects})

def projectDetail(request,slug):
    project=get_object_or_404(Project,slug=slug)
    return render(request,'portfol/personal.html',{'projectdetail':project})