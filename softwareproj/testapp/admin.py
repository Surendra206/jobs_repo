from django.contrib import admin
from testapp.models import Hydjobs, Bangjobs, Chennaijobs, Kolkatajobs

# Register your models here.
class HydjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(Hydjobs,HydjobsAdmin)
class BangjobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(Bangjobs,BangjobsAdmin)
class ChennaijobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(Chennaijobs,ChennaijobsAdmin)
class KolkatajobsAdmin(admin.ModelAdmin):
    list_display = ['date','company','title','address','email','phonenumber']
admin.site.register(Kolkatajobs,KolkatajobsAdmin)
