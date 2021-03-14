from django.db import models

class SRecruiter(models.Model):
    id = models.AutoField(primary_key = True)
    fname = models.CharField(max_length = 30)
    add = models.CharField(max_length = 200)
    rmobno = models.CharField(max_length = 10)
    adhrno = models.CharField(max_length = 15)
    passs = models.CharField(max_length = 8)
    rpass = models.CharField(max_length = 8)

    class Meta:
        db_table="rojgaar_srecruiter"


class LRecruiter(models.Model):
    id = models.AutoField(primary_key = True)
    rmobno = models.CharField(max_length = 10)
    passs = models.CharField(max_length=8)

    class Meta:
        db_table = "rojgaar_lrecruiter"


class SJobseeker(models.Model):
    id = models.AutoField(primary_key = True)
    jname = models.CharField(max_length = 30)
    add = models.CharField(max_length = 200)
    rmobno = models.CharField(max_length = 10)
    adhrno = models.CharField(max_length = 15)
    passs = models.CharField(max_length = 8)
    rpass = models.CharField(max_length = 8)

    class Meta:
        db_table = "rojgaar_sjobseeker"


class LJobseeker(models.Model):
    id = models.AutoField(primary_key = True)
    rmobno = models.CharField(max_length=10)
    passs = models.CharField(max_length=8)

    class Meta:
        db_table = "rojgaar_ljobseeker"

'''
PostJob (id(PK), jtitle,jregion,jadd,jtype,jcat,noofopen,gender,salary,jtime,jdes,jcname,jctag,jcdes,jimg)
'''
class PosJob(models.Model):
    Gender = (('m' , 'Male') , ('f' , 'Female'))
    id = models.AutoField(primary_key=True)
    rmobno = models.CharField(max_length = 10)
    jtitle = models.CharField(max_length=30)
    jobregion=models.CharField(max_length=100)
    jadd = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=50, default="", editable=False)
    jobcat = models.CharField(max_length=100, default="", editable=False)
    noofopen = models.CharField(max_length=10)
    gender=models.CharField(max_length=5,choices=Gender)
    salary1 = models.IntegerField(max_length=10)
    salary2 = models.IntegerField(max_length=10)
    jstime = models.CharField(max_length=10)
    jetime = models.CharField(max_length=10)
    jobdes = models.CharField(max_length=500)
    comname = models.CharField(max_length=100)
    comtagline = models.CharField(max_length=200)
    comdes = models.CharField(max_length=500)
    #comimg=models.ImageField()
    #agree=models.CharField(max_length=200)

    class Meta:
        db_table = "rojgaar_postjob"


class JobProfile(models.Model):
    id = models.AutoField(primary_key=True)
    jname = models.CharField(max_length=50)
    jsadd = models.CharField(max_length=100)
    jmobno = models.CharField(max_length=10)
    qual = models.CharField(max_length=20)
    exp = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    jobcat = models.CharField(max_length=100, default="", editable=False)
    jobtype = models.CharField(max_length=50, default="", editable=False)
    jobregion = models.CharField(max_length=100)
    myimg=models.ImageField(null = True, blank = True, upload_to='images/')

    class Meta:
        db_table = "rojgaar_jobprofile"


class MSRecruiter(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    add = models.CharField(max_length=200)
    rmobno = models.CharField(max_length=10)
    adhrno = models.CharField(max_length=15)
    passs = models.CharField(max_length=8)
    rpass = models.CharField(max_length=8)

    class Meta:
        db_table = "rojgaar_msrecruiter"


class MLRecruiter(models.Model):
    id = models.AutoField(primary_key=True)
    rmobno = models.CharField(max_length=10)
    passs = models.CharField(max_length=8)

    class Meta:
        db_table = "rojgaar_mlrecruiter"

class MSJobseeker(models.Model):
    id = models.AutoField(primary_key = True)
    jname = models.CharField(max_length = 30)
    add = models.CharField(max_length = 200)
    rmobno = models.CharField(max_length = 10)
    adhrno = models.CharField(max_length = 15)
    passs = models.CharField(max_length = 8)
    rpass = models.CharField(max_length = 8)

    class Meta:
        db_table = "rojgaar_msjobseeker"

class MLJobseeker(models.Model):
    id = models.AutoField(primary_key = True)
    rmobno = models.CharField(max_length=10)
    passs = models.CharField(max_length=8)

    class Meta:
        db_table = "rojgaar_mljobseeker"

class MPosJob(models.Model):
    Gender = (('m' , 'Male') , ('f' , 'Female'))
    id = models.AutoField(primary_key=True)
    rmobno = models.CharField(max_length = 10)
    jtitle = models.CharField(max_length=30)
    #jobregion=models.CharField(max_length=100)
    jadd = models.CharField(max_length=100)
    jobtype = models.CharField(max_length=50, default="", editable=False)
    jobcat = models.CharField(max_length=100, default="", editable=False)
    noofopen = models.CharField(max_length=10)
    #gender=models.CharField(max_length=5,choices=Gender)
    salary = models.CharField(max_length=10)
    jstime = models.CharField(max_length=10)
    jetime = models.CharField(max_length=10)
    jobdes = models.CharField(max_length=500)
    comname = models.CharField(max_length=100)
    comtagline = models.CharField(max_length=200)
    comdes = models.CharField(max_length=500)
    #comimg=models.ImageField()
    #agree=models.CharField(max_length=200)

    class Meta:
        db_table = "rojgaar_mpostjob"


class MJobProfile(models.Model):
    id = models.AutoField(primary_key=True)
    jname = models.CharField(max_length=50)
    jsadd = models.CharField(max_length=100)
    jmobno = models.CharField(max_length=10)
    qual = models.CharField(max_length=20)
    exp = models.CharField(max_length=100)
    myimg=models.ImageField(null = True, blank = True, upload_to='imges/')

    class Meta:
        db_table = "rojgaar_mjobprofile"
