from django.shortcuts import render,redirect
from Rojgaar.models import SRecruiter,LRecruiter,SJobseeker,LJobseeker,JobProfile,PosJob,MLRecruiter,MSRecruiter,MSJobseeker,MLJobseeker,MPosJob,MJobProfile
import mysql.connector
from operator import itemgetter
from django.contrib import messages
from django.db import connections
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
import mysql.connector


def index(request):
    return render(request,'Rojgaar/index.html')

def mindex(request):
    return render(request,'Rojgaar/mindex.html')

def recruiter(request):
    return render(request,'Rojgaar/recruiter.html')

def lrecruiter(request):
    con = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor = con.cursor(buffered=True)
    con2 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor2 = con.cursor(buffered=True)
    sqlcommand = "select rmobno from rojgaar_srecruiter"
    sqlcommand2 = "select passs from rojgaar_srecruiter"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e = []
    p = []
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    con3 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor3 = con2.cursor(buffered=True)
    if request.method == "POST":
        rmobno = request.POST.get('rmobno')
        passs = request.POST.get('passs')
        k = len(res)
        i = 1
        sqlcommand3 = "select fname from rojgaar_srecruiter where rmobno=rmobno"
        cursor3.execute(sqlcommand3)
        lst = []
        for name in cursor3:
            name = name
            name2 = ''.join(name)
        print(name2)
        user = LRecruiter()
        user.rmobno = request.POST.get('rmobno')
        user.passs = request.POST.get('passs')
        while i < k:
            if res[i] == rmobno and res2[i] == passs:
                user.save()
                request.session['rmobno'] = rmobno
                return redirect('recoption')
                break
            i += 1
        else:
            messages.info(request, "Check username or password")
            return render(request, 'Rojgaar/lrecruiter.html')
    else:
        return render(request,'Rojgaar/lrecruiter.html')


def srecruiter(request):
    if request.method=="POST":
        user=SRecruiter()
        user.fname=request.POST.get('fname')
        user.add=request.POST.get('add')
        user.rmobno=request.POST.get('rmobno')
        user.adhrno=request.POST.get('adhrno')
        user.passs=request.POST.get('passs')
        user.rpass=request.POST.get('rpass')
        error_message=None
        if user.passs!=user.rpass:
            error_message="Password dose not match"
        elif user.fname=="" or user.add=="" or user.rmobno=="" or user.adhrno=="" or user.passs=="" or user.rpass=="":
            error_message="Some fields are empty"
        elif len(user.rmobno)<10 or len(user.rmobno)>10:
            error_message="Mobile number must be 10 character long"
        elif len(user.adhrno)<12 or len(user.adhrno)>12:
            error_message="Adhar number must be 12 character long"

        if not error_message:
            messages.info(request,"Registration done")
            user.save()
            return redirect('lrecruiter')
    else:
        return render(request,'Rojgaar/srecruiter.html')

def jobseeker(request):
    return render(request,'Rojgaar/jobseeker.html')

def sjobseeker(request):
    if request.method=="POST":
        user=SJobseeker()
        user.jname=request.POST.get('jname')
        user.add=request.POST.get('add')
        user.rmobno=request.POST.get('rmobno')
        user.adhrno=request.POST.get('adhrno')
        user.passs=request.POST.get('passs')
        user.rpass=request.POST.get('rpass')
        error_message=None
        if user.passs!=user.rpass:
            error_message="Password dose not match"
        elif user.jname=="" or user.add=="" or user.rmobno=="" or user.adhrno=="" or user.passs=="" or user.rpass=="":
            error_message="Some fields are empty"
        elif len(user.rmobno)<10 or len(user.rmobno)>10:
            error_message="Mobile number must be 10 character long"
        elif len(user.adhrno)<12 or len(user.adhrno)>12:
            error_message="Adhar number must be 12 character long"

        if not error_message:
            messages.info(request,"Registration done")
            user.save()
            return redirect('ljobseeker')
        else:
            return render(request, 'Rojgaar/sjobseeker.html', {'error': error_message})
    else:
        return render(request,'Rojgaar/sjobseeker.html')

def ljobseeker(request):
    con = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor = con.cursor(buffered=True)
    con2 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor2 = con.cursor(buffered=True)
    sqlcommand = "select rmobno from rojgaar_sjobseeker"
    sqlcommand2 = "select passs from rojgaar_sjobseeker"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e = []
    p = []
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    con3 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor3 = con2.cursor(buffered=True)
    if request.method == "POST":
        rmobno = request.POST.get('rmobno')
        passs = request.POST.get('passs')
        k = len(res)
        i = 1
        sqlcommand3 = "select jname from rojgaar_sjobseeker where rmobno=rmobno"
        cursor3.execute(sqlcommand3)
        lst = []
        for name in cursor3:
            name = name
            name2 = ''.join(name)
        print(name2)
        user = LJobseeker()
        user.rmobno = request.POST.get('rmobno')
        user.passs = request.POST.get('passs')
        while i < k:
            if res[i] == rmobno and res2[i] == passs:
                user.save()
                request.session['rmobno'] = rmobno
                return redirect('joboption')
                break
            i += 1
        else:
            messages.info(request, "Check username or password")
            return render(request, 'Rojgaar/ljobseeker.html')
    else:
        return render(request,'Rojgaar/ljobseeker.html')

def mrecruiter(request):
    return render(request,'Rojgaar/mrecruiter.html')

def mjobseeker(request):
    return render(request,'Rojgaar/mjobseeker.html')

def msrecruiter(request):
    if request.method=="POST":
        user=SRecruiter()
        user.fname=request.POST.get('fname')
        user.add=request.POST.get('add')
        user.rmobno=request.POST.get('rmobno')
        user.adhrno=request.POST.get('adhrno')
        user.passs=request.POST.get('passs')
        user.rpass=request.POST.get('rpass')
        error_message=None
        if user.passs!=user.rpass:
            error_message="Password dose not match"
        elif user.fname=="" or user.add=="" or user.rmobno=="" or user.adhrno=="" or user.passs=="" or user.rpass=="":
            error_message="Some fields are empty"
        elif len(user.rmobno)<10 or len(user.rmobno)>10:
            error_message="Mobile number must be 10 character long"
        elif len(user.adhrno)<12 or len(user.adhrno)>12:
            error_message="Adhar number must be 12 character long"

        if not error_message:
            messages.info(request,"Registration done")
            user.save()
            return redirect('mlrecruiter')
    else:
        return render(request,'Rojgaar/msrecruiter.html')

def mlrecruiter(request):
    con = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor = con.cursor(buffered=True)
    con2 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor2 = con.cursor(buffered=True)
    sqlcommand = "select rmobno from rojgaar_srecruiter"
    sqlcommand2 = "select passs from rojgaar_srecruiter"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e = []
    p = []
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    con3 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor3 = con2.cursor(buffered=True)
    if request.method == "POST":
        rmobno = request.POST.get('rmobno')
        passs = request.POST.get('passs')
        k = len(res)
        i = 1
        sqlcommand3 = "select fname from rojgaar_srecruiter where rmobno=rmobno"
        cursor3.execute(sqlcommand3)
        lst = []
        for name in cursor3:
            name = name
            name2 = ''.join(name)
        print(name2)
        user = LRecruiter()
        user.rmobno = request.POST.get('rmobno')
        user.passs = request.POST.get('passs')
        while i < k:
            if res[i] == rmobno and res2[i] == passs:
                user.save()
                request.session['rmobno'] = rmobno
                return redirect('mrecoption')
                break
            i += 1
        else:
            messages.info(request, "Check username or password")
            return render(request, 'Rojgaar/mlrecruiter.html')
    else:
        return render(request,'Rojgaar/mlrecruiter.html')

def msjobseeker(request):
    if request.method=="POST":
        user=SJobseeker()
        user.jname=request.POST.get('jname')
        user.add=request.POST.get('add')
        user.rmobno=request.POST.get('rmobno')
        user.adhrno=request.POST.get('adhrno')
        user.passs=request.POST.get('passs')
        user.rpass=request.POST.get('rpass')
        error_message=None
        if user.passs!=user.rpass:
            error_message="Password dose not match"
        elif user.jname=="" or user.add=="" or user.rmobno=="" or user.adhrno=="" or user.passs=="" or user.rpass=="":
            error_message="Some fields are empty"
        elif len(user.rmobno)<10 or len(user.rmobno)>10:
            error_message="Mobile number must be 10 character long"
        elif len(user.adhrno)<12 or len(user.adhrno)>12:
            error_message="Adhar number must be 12 character long"

        if not error_message:
            messages.info(request,"Registration done")
            user.save()
            return redirect('mljobseeker')
    else:
        return render(request,'Rojgaar/msjobseeker.html')

def mljobseeker(request):
    con = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor = con.cursor(buffered=True)
    con2 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor2 = con.cursor(buffered=True)
    sqlcommand = "select rmobno from rojgaar_sjobseeker"
    sqlcommand2 = "select passs from rojgaar_sjobseeker"
    cursor.execute(sqlcommand)
    cursor2.execute(sqlcommand2)
    e = []
    p = []
    for i in cursor:
        e.append(i)
    for j in cursor2:
        p.append(j)
    res = list(map(itemgetter(0), e))
    res2 = list(map(itemgetter(0), p))
    con3 = mysql.connector.connect(host="localhost", port="8111", user="root", passwd="", database="rojgaardb")
    cursor3 = con2.cursor(buffered=True)
    if request.method == "POST":
        rmobno = request.POST.get('rmobno')
        passs = request.POST.get('passs')
        k = len(res)
        i = 1
        sqlcommand3 = "select fname from rojgaar_srecruiter where rmobno=rmobno"
        cursor3.execute(sqlcommand3)
        lst = []
        for name in cursor3:
            name = name
            name2 = ''.join(name)
        print(name2)
        user = LJobseeker()
        user.rmobno = request.POST.get('rmobno')
        user.passs = request.POST.get('passs')
        while i < k:
            if res[i] == rmobno and res2[i] == passs:
                user.save()
                request.session['rmobno'] = rmobno
                return redirect('mjoboption')
                break
            i += 1
        else:
            messages.info(request, "Check username or password")
            return render(request, 'Rojgaar/mljobseeker.html')
    else:
        return render(request,'Rojgaar/mljobseeker.html')

def postjob(request):
    if request.method=="POST":
        user = PosJob()
        user.rmobno=request.POST['rmobno']
        user.jtitle=request.POST['jtitle']
        user.jobregion=request.POST.get('jobregion')
        user.jadd=request.POST['jadd']
        user.jobtype=request.POST.get('jobtype')
        user.jobcat=request.POST.get('jobcat')
        user.noofopen=request.POST['noofopen']
        user.gender=request.POST.get('gender')
        user.salary1=request.POST.get('salary1')
        user.salary2=request.POST.get('salary2')
        user.jstime=request.POST['jstime']
        user.jetime=request.POST['jetime']
        user.jobdes=request.POST['jobdes']
        user.comname=request.POST['comname']
        user.comtagline=request.POST['comtagline']
        user.comdes=request.POST['comdes']
        #user.comimg=request.POST['comimg']

        #user.agree=request.POST['agree']
        smob=request.session['rmobno']
        if smob == user.rmobno:
            user.save()
            messages.info(request,"Job Posted Successfully")
            return redirect('recoption')
    else:
        return render(request,'Rojgaar/postjob.html')

def mpostjob(request):
    if request.method=="POST":
        user = PosJob()
        user.rmobno=request.POST.get('rmobno')
        user.jtitle=request.POST.get('jtitle')
        user.jobregion=request.POST.get('jobregion')
        user.jadd=request.POST.get('jadd')
        user.jobtype=request.POST.get('jobtype')
        user.jobcat=request.POST.get('jobcat')
        user.noofopen=request.POST.get('noofopen')
        user.gender=request.POST.get('gender')
        user.salary1=request.POST.get('salary1')
        user.salary2=request.POST.get('salary2')
        user.jstime=request.POST.get('jstime')
        user.jetime=request.POST.get('jetime')
        user.jobdes=request.POST.get('jobdes')
        user.comname=request.POST.get('comname')
        user.comtagline=request.POST.get('comtagline')
        user.comdes=request.POST.get('comdes')
        #user.comimg=request.POST['comimg']

        #user.agree=request.POST['agree']
        smob = request.session['rmobno']
        if smob == user.rmobno:
            user.save()
            messages.info(request,"Job Posted Successfully")
            return redirect('mrecoption')
    else:
        return render(request,'Rojgaar/mpostjob.html')


def jobprofile(request):
    if request.method=="POST":
        user=JobProfile()
        user.jname=request.POST['jname']
        user.jsadd=request.POST['jsadd']
        user.jmobno=request.POST['jmobno']
        user.qual=request.POST['qual']
        user.exp=request.POST['exp']
        user.gender=request.POST.get('gender')
        user.jobcat=request.POST.get('jobcat')
        user.jobtype=request.POST.get('jobtype')
        user.jobregion=request.POST.get('jobregion')
        user.myimg=request.POST['myimg']
        smob = request.session['rmobno']
        if smob == user.jmobno:
            user.save()
            messages.info(request,"Successfully Done")
            return redirect('joboption')
    else:
        return render(request,'Rojgaar/jobprofile.html')

def mjobprofile(request):
    if request.method=="POST":
        user=JobProfile()
        user.jname=request.POST['jname']
        user.jsadd=request.POST['jsadd']
        user.jmobno=request.POST['jmobno']
        user.qual=request.POST['qual']
        user.exp=request.POST['exp']
        user.gender = request.POST.get('gender')
        user.jobcat = request.POST.get('jobcat')
        user.jobtype = request.POST.get('jobtype')
        user.jobregion = request.POST.get('jobregion')
        user.myimg=request.POST.get('myimg')
        smob = request.session['rmobno']
        if smob == user.jmobno:
            user.save()
            messages.info(request,"Successfully Done")
            return redirect('mjoboption')
    else:
        return render(request,'Rojgaar/mjobprofile.html')

def recoption(request):
    return render(request,'Rojgaar/recoption.html')

def mrecoption(request):
    return render(request,'Rojgaar/mrecoption.html')

def recprofile(request):
    smob = request.session['rmobno']
    data = PosJob.objects.raw('select * from rojgaar_postjob where rmobno = '+smob)
    return render(request,'Rojgaar/recprofile.html',{'messages':data})

def mrecprofile(request):
    smob = request.session['rmobno']
    data = PosJob.objects.raw('select * from rojgaar_postjob where rmobno = ' + smob)
    return render(request, 'Rojgaar/mrecprofile.html', {'messages': data})

def joboption(request):
    return render(request,'Rojgaar/joboption.html')

def mjoboption(request):
    return render(request,'Rojgaar/mjoboption.html')

def myjobprofile(request):
    smob = request.session['rmobno']
    data = JobProfile.objects.raw('select * from rojgaar_jobprofile where jmobno = ' + smob)
    return render(request, 'Rojgaar/myjobprofile.html', {'messages': data})

def mmyjobprofile(request):
    smob = request.session['rmobno']
    data = JobProfile.objects.raw('select * from rojgaar_jobprofile where jmobno = ' + smob)
    return render(request, 'Rojgaar/mmyjobprofile.html', {'messages': data})

def aboutus(request):
    return render(request,'Rojgaar/aboutus.html')

def contactus(request):
    return render(request,'Rojgaar/contactus.html')

def listjobseeker(request):
    smob = request.session['rmobno']
    data = JobProfile.objects.raw('select * from rojgaar_jobprofile where jobcat = (select jobcat from rojgaar_postjob where rmobno = ' + smob + ') ')
    return render(request,'Rojgaar/listjobseeker.html',{'messages':data})

def mlistjobseeker(request):
    smob = request.session['rmobno']
    data = JobProfile.objects.raw('select * from rojgaar_jobprofile where jobcat = (select jobcat from rojgaar_postjob where rmobno = ' + smob + ') ')
    return render(request,'Rojgaar/mlistjobseeker.html',{'messages':data})

def listrecruiter(request):
    smob = request.session['rmobno']
    data = PosJob.objects.raw('select * from rojgaar_postjob where jobcat = (select jobcat from rojgaar_jobprofile where jmobno = ' + smob + ') ')
    return render(request,'Rojgaar/listrecruiter.html',{'messages':data})

def mlistrecruiter(request):
    smob = request.session['rmobno']
    data = PosJob.objects.raw('select * from rojgaar_postjob where jobcat = (select jobcat from rojgaar_jobprofile where jmobno = ' + smob + ') ')
    return render(request,'Rojgaar/mlistrecruiter.html',{'messages':data})

def maboutus(request):
    return render(request,'Rojgaar/maboutus.html')

def mcontactus(request):
    return render(request,'Rojgaar/mcontactus.html')

def recedit(request):
    return render(request,'Rojgaar/recedit.html')

def jobedit(request):
    return render(request,'Rojgaar/jobedit.html')

def appliedrecruiter(request):
    smob = request.session['rmobno']
    data = PosJob.objects.raw('select * from rojgaar_postjob where jobcat = (select jobcat from rojgaar_jobprofile where jmobno = ' + smob + ') ')
    return render(request,'Rojgaar/appliedrecruiter.html',{'messages':data})


def interestinjobseeker(request):
    smob = request.session['rmobno']
    data = JobProfile.objects.raw(
        'select * from rojgaar_jobprofile where jobcat = (select jobcat from rojgaar_postjob where rmobno = ' + smob + ') ')
    return render(request, 'Rojgaar/interestinjobseeker.html', {'messages': data})
