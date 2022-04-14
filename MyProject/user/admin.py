from django.contrib import admin

# Register your models here.
from .models import *
class contactAdmin(admin.ModelAdmin):
    list_display=("name","contact","email","message")
admin.site.register(contact,contactAdmin)

class categoryAdmin(admin.ModelAdmin):
    list_display=("id","cname","cpic","cdate")
admin.site.register(category,categoryAdmin)

class profileAdmin(admin.ModelAdmin):
    list_display=("name","mobile","email","passwd","ppic","address")
admin.site.register(profile,profileAdmin)


class productsAdmin(admin.ModelAdmin):
    list_display=("id","name","ppic","color","tprice","disprice","pdes","pdate","category")
admin.site.register(products,productsAdmin)


class orderAdmin(admin.ModelAdmin):
    list_display=('id',"pid","userid","remarks","status","odate")
admin.site.register(order,orderAdmin)

class addtocartAdmin(admin.ModelAdmin):
    list_display=('id',"pid","userid","status","cdate")
admin.site.register(addtocart,addtocartAdmin)