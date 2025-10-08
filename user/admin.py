from django.contrib import admin

# Register your models here.
from . models import *
class contactAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','message')
admin.site.register(contact,contactAdmin)
class RegisteredAdmin(admin.ModelAdmin):
    list_display = ('name','email','mobile','paddre','whereto','arrival','howmany','leaving','ppic','msj')
admin.site.register(Registered,RegisteredAdmin)
class categoryAdmin(admin.ModelAdmin):
    list_display = ('id','cname','cpic','cdate')
admin.site.register(category,categoryAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display = ('name','mobile','email','passwd','ppic','address')
admin.site.register(profile,profileAdmin)

class addplaceAdmin(admin.ModelAdmin):
    list_display = ('id','sseen','ptitle','city','baplace','pdes','placepic','pdate')
admin.site.register(addplace,addplaceAdmin)

class galleryAdmin(admin.ModelAdmin):
    list_display = ('id','pdes','picture','gdate')
admin.site.register(gallery,galleryAdmin)

class guiderAdmin(admin.ModelAdmin):
    list_display = ('id','name','city','guiderpic','qualification','gid','gidp','address','gdate','mobile')
admin.site.register(guider,guiderAdmin)

class notificationAdmin(admin.ModelAdmin):
    list_display = ('id','ndes','ndate')
admin.site.register(notification,notificationAdmin)

class videoAdmin(admin.ModelAdmin):
    list_display = ('id','vtitle','vdes','thumb','vlink','vdate')
admin.site.register(video,videoAdmin)

class sliderAdmin(admin.ModelAdmin):
    list_display = ('id','stitle','sdes','spic','sdate')
admin.site.register(slider,sliderAdmin)