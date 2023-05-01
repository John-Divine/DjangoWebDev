from django.urls import path
from .views import *
app_name='portfol'
urlpatterns=[
    path('',PersonalInfoList.as_view(),name='details'),
    path('competence_info',Competences,name='competence'),
    path('all_projects',projectHighLight,name='projecthighlight'),
    path('project_detail/<str:slug>',projectDetail,name='projectdetails'),
]