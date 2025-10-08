from django.shortcuts import render
from django.http import HttpResponse
from . models import *
# Create your views here.
def home(request):
    cdata=category.objects.all().order_by('-id')[0:4]      # DYNAMIC CATEGORY
    pdata=addplace.objects.all().order_by('id')[0:8]
    n=notification.objects.all().order_by('-id')[0:4]

    mydict={"data":cdata,"place":pdata,"notification":n}
    return render(request,'user/index.html',mydict)
def about(request):
    return render(request,'user/about.html')
def guiderdetails(request):
    city = category.objects.all().order_by('-id')
    a = request.GET.get('abc')
    gd = ""
    if a is None:
        gd = guider.objects.all().order_by('-id')
    else:
        gd = guider.objects.filter(city=a)
    mydict = {"city": city, "guider": gd}
    return render(request,'user/guiderdetails.html',mydict)
def newplaces(request):
    city=category.objects.all().order_by('-id')
    a=request.GET.get('abc')
    place = ""
    if a is None:
        place = addplace.objects.all().order_by('-id')
    else:
        place=addplace.objects.filter(city=a)
    mydict = {"city": city, "place": place}

    return render(request,'user/newplaces.html',mydict)
def imagegallery(request):
    gdata=gallery.objects.all().order_by('-id')
    return render(request,'user/gallery.html',{"gallery":gdata})
def slider(request):
    return render(request,'user/slider.html')
def videogallery(request):
    vdata=video.objects.all().order_by('-id')
    return render(request,'user/videos.html',{"video":vdata})
def contactus(request):
   status=False
   if request.method=='POST':
       Name=request.POST.get("name","")
       Email=request.POST.get("email","")
       Mobile=request.POST.get("mobile","")
       Message=request.POST.get("msg","")
       res=contact(name=Name,email=Email,mobile=Mobile,message=Message)
       # model table name contact and Name is variable(field)
       res.save()
       status=True
   return render(request,'user/contactus.html',{'S':status})

def signin(request):
    if request.method == 'POST':
        Name = request.POST.get("name", "")
        Email = request.POST.get("email", "")
        Mobile = request.POST.get("mobile", "")
        Paddre = request.POST.get("paddre", "")
        Whereto = request.POST.get("where", "")
        Arrival = request.POST.get("arri", "")
        Hmany = request.POST.get("howmany", "")
        Leave = request.POST.get("leaving", "")
        Message = request.POST.get("msj", "")
        Picname = request.FILES['fu']
        res=Registered(name=Name, mobile=Mobile, email=Email, paddre=Paddre, whereto=Whereto,arrival=Arrival
        ,howmany=Hmany,leaving=Leave,msj=Message, ppic=Picname)
        res.save()
        return HttpResponse("<script> alert('You are Registered successfully.. We will contact you as soon as possible !!');window.location.href='/user/signin';</script>")
    return render(request,'user/signin.html')

def viewdetails(request):
    a=request.GET.get('msg')
    data=addplace.objects.filter(id=a)
    return render(request,'user/viewdetails.html',{"d":data})
