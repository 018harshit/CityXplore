from django.db import models

# Create your models here.
class contact(models.Model):                        # class name is table name
    name=models.CharField(max_length=100)
    email=models.CharField(max_length=120)
    mobile=models.CharField(max_length=20)
    message=models.CharField(max_length=600)

    def __str__(self):
        return self.email
class Registered(models.Model):                        # class name is table name
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=120)
    mobile=models.CharField(max_length=20)
    paddre=models.CharField(max_length=50)
    whereto=models.CharField(max_length=50)
    arrival=models.CharField(max_length=20)
    howmany=models.CharField(max_length=20)
    leaving=models.CharField(max_length=20)
    ppic=models.ImageField(upload_to='static/category/',default="")
    msj=models.CharField(max_length=600)

    def __str__(self):
        return self.email
class category(models.Model):
    cname=models.CharField(max_length=30)
    cpic=models.ImageField(upload_to='static/category/',default="")
    cdate=models.DateField()
    def __str__(self):
        return self.cname
class profile(models.Model):
    name=models.CharField(max_length=120)
    mobile=models.CharField(max_length=80)
    email=models.EmailField(max_length=80,primary_key=True)
    passwd=models.CharField(max_length=100)
    ppic=models.ImageField(upload_to='static/profile/',default="")
    address=models.TextField(max_length=2000)

class addplace(models.Model):
    sseen = models.CharField(max_length=50)
    ptitle=models.CharField(max_length=2000)
    city=models.ForeignKey(category,on_delete=models.CASCADE) #set foreignkey
    baplace=models.CharField(max_length=400)
    pdes=models.TextField(max_length=5000)
    placepic=models.ImageField(upload_to='static/place/',default="")
    pdate=models.DateField()

    def __str__(self):
        return self.baplace

class guider(models.Model):
    name=models.CharField(max_length=100)
    city=models.ForeignKey(category,on_delete=models.CASCADE)
    guiderpic=models.ImageField(upload_to='static/guider/',default="")
    qualification=models.CharField(max_length=100)
    gid=models.CharField(max_length=30)
    gidp=models.CharField(max_length=30)
    mobile=models.CharField(max_length=20)
    address=models.TextField(max_length=1000)
    gdate=models.DateField()

class gallery(models.Model):
    pdes=models.CharField(max_length=500)
    picture=models.ImageField(upload_to='static/gallery',default="")
    gdate=models.DateField()

class notification(models.Model):
    ndes=models.TextField(max_length=5000)
    ndate=models.DateField()

class video(models.Model):
    vtitle=models.CharField(max_length=200)
    vdes=models.TextField(max_length=600)
    thumb=models.ImageField(upload_to='static/thumbnail/',default="")
    vlink=models.CharField(max_length=500)
    vdate=models.DateField()

class slider(models.Model):
    stitle=models.CharField(max_length=200)
    sdes=models.CharField(max_length=500)
    spic=models.ImageField(upload_to='static/slider/',default="")
    sdate=models.DateField()