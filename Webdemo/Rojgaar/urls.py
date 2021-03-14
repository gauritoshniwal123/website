from django.urls import path
from Rojgaar import views
from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.contrib import admin

urlpatterns = [
    path('admin/' , admin.site.urls),
    path('', views.index, name='index'),
    path("mindex" , views.mindex, name='mindex'),
    path("recruiter" , views.recruiter, name='recruiter'),
    path("lrecruiter" , views.lrecruiter, name='lrecruiter'),
    path("srecruiter" , views.srecruiter, name='srecruiter'),
    path("jobseeker" , views.jobseeker, name='jobseeker'),
    path("sjobseeker" , views.sjobseeker, name='sjobseeker'),
    path("ljobseeker" , views.ljobseeker, name='ljobseeker'),
    path("mrecruiter" , views.mrecruiter, name='mrecruiter'),
    path("msrecruiter" , views.msrecruiter, name='msrecruiter'),
    path("mlrecruiter" , views.mlrecruiter, name='mlrecruiter'),
    path("mjobseeker" , views.mjobseeker, name='mjobseeker'),
    path("msjobseeker" , views.msjobseeker , name='msjobseeker'),
    path("mljobseeker" , views.mljobseeker , name='mljobseeker'),
    path("postjob" , views.postjob, name='postjob'),
    path("mpostjob" , views.mpostjob, name='mpostjob'),
    path("jobprofile" , views.jobprofile, name='jobprofile'),
    path("mjobprofile" , views.mjobprofile , name='mjobprofile'),
    path("recoption" , views.recoption, name='recoption'),
    path("mrecoption" , views.mrecoption , name='mrecoption'),
    path("recprofile" , views.recprofile, name='recprofile'),
    path("mrecprofile" , views.mrecprofile , name='mrecprofile'),
    path("joboption" , views.joboption, name='joboption'),
    path("mjoboption" , views.mjoboption , name='mjoboption'),
    path("myjobprofile" , views.myjobprofile, name='myjobprofile'),
    path("mmyjobprofile" , views.mmyjobprofile , name='mmyjobprofile'),
    path("aboutus" , views.aboutus , name='aboutus'),
    path("contactus" , views.contactus , name='contactus'),
    path("listjobseeker" , views.listjobseeker , name='listjobseeker'),
    path("mlistjobseeker" , views.mlistjobseeker , name='mlistjobseeker'),
    path("listrecruiter" , views.listrecruiter , name='listrecruiter'),
    path("mlistrecruiter" , views.mlistrecruiter , name='mlistrecruiter'),
    path("maboutus" , views.maboutus ,  name='maboutus'),
    path("mcontactus" , views.mcontactus , name='mcontactus'),
    path("recedit" , views.recedit , name='recedit'),
    path("jobedit" , views.jobedit , name='jobedit'),
    path("appliedrecruiter" , views.appliedrecruiter , name='appliedrecruiter'),
    path("interestinjobseeker" , views.interestinjobseeker , name='interestinjobseeker'),

]

