from django.db import models
from django.utils import timezone
#import re
# Create your models here.


class PersonalInfo(models.Model):
    name=models.CharField(max_length=100,blank=True,null=True)
    my_pic=models.ImageField(upload_to='my_pic/%Y/%m/%d',blank=True,null=True)
    bio=models.TextField(blank=True,null=True)
    intro= models.TextField(blank=True, null=True)
    birthday=models.DateField()
    addr=models.CharField(max_length=100,blank=True,null=True)
    tel=models.CharField(max_length=14,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    cv=models.FileField(upload_to='cv',blank=True,null=True)
    #social media handles

    '''linkedin=models.URLField(blank=True,null=True)
    facebook=models.URLField(blank=True,null=True)
    twitter=models.URLField(blank=True,null=True)
    instargram=models.URLField(blank=True,null=True)'''
    def __str__(self):
        return self.name

class Contact(models.Model):
    person=models.ForeignKey(PersonalInfo,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='link/%Y/%m/%d', blank=True, null=True)
    name=models.CharField(max_length=15)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name

class competence(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=True,null=False)
    description=models.TextField(blank=False,null=False)
    image=models.FileField(upload_to='competence/%Y/%m/%d',blank=False,null=False)

    def __str__(self):
        return self.title

class Education(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title=models.CharField(max_length=50,blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    year=models.CharField(max_length=10,blank=False,null=False)

    def __str__(self):
        return self.title

class Experience(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=False, null=False)
    description = models.TextField(blank=False, null=False)
    year = models.CharField(max_length=10, blank=False, null=False)

    def __str__(self):
        return self.title
class Project(models.Model):
    person = models.ForeignKey(PersonalInfo, on_delete=models.CASCADE)
    title=models.CharField(max_length=200,blank=False,null=False)
    slug=models.SlugField(max_length=200,blank=True,null=True)
    description=models.TextField(blank=False,null=False)
    image=models.ImageField(upload_to='projects/%Y/%m/%d',blank=True,null=True)
    tools=models.CharField(max_length=200,blank=False,null=False)
    demo=models.URLField()
    github=models.URLField()
    date=models.DateField(default=timezone.now)
    show_in_slider=models.CharField(max_length=5,blank=False,null=False)


    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return '/project_detail/{}'.format(self.slug)
