from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.
def home(request):
    cdata=category.objects.all().order_by('id')[0:6]
    pdata=products.objects.all()
    print(pdata)

    return render(request,'user/index.html',{"data":cdata,"product":pdata})

def about(request):
    return render(request,'user/about.html')

def contactus(request):
    status=False
    if request.method=='POST':
        name = request.POST.get("name","")
        mobile=request.POST.get("mobile","")
        email = request.POST.get("email","")
        message = request.POST.get("msg","")
        contact(name=name,email=email,contact=mobile,message=message).save()
        status=True
        #return HttpResponse("<script>alert('Thanks for enquiry..');window.location.href='/user/contactus'</script>")
    return render(request,'user/contactus.html',{'S':status})

def services(request):
    return render(request,'user/services.html')

def myorders(request):
    return render(request,'user/myorders.html')

def myprofile(request):
    return render(request,'user/myprofile.html')

def product(request):
    return render(request,'user/product.html')

def signup(request):
    status=False
    if request.method=='POST':
        name=request.POST.get("name","")
        dob=request.POST.get("dob","")
        email=request.POST.get("email","")
        passwd=request.POST.get("passwd","")
        mobile=request.POST.get("mobile","")
        address=request.POST.get("address","")
        picname=request.FILES['fu']
        d=profile.objects.filter(email=email)

        if d.count()>0:
            return HttpResponse("<script>alert('You are already registered');window.location.href='/user/signup';</script>")
        else:

            profile(name=name,mobile=mobile,email=email,passwd=passwd,address=address,ppic=picname).save()
            return HttpResponse("<script>alert('You are registered successfully');window.location.href='/user/signup';</script>")

        #return HttpResponse("<script>alert('You are Registerd successfully...');window.location.href='/user/signup';</script>")

    return render(request,'user/signup.html')

def signin(request):
    if request.method=='POST':
        uname=request.POST.get('email', "")
        pwd=request.POST.get('password', "")
        checkuser=profile.objects.filter(email=uname, passwd=pwd)
        if(checkuser):
            request.session["user"]=uname
            return HttpResponse("<script>alert('login successfully..');window.location.href='/user/signin';</script>")
        else:
            return HttpResponse("<script>alert('userid or password is incoreect..');window.location.href='/user/signin';</script>")



    return render(request, 'user/signin.html')



def viewdetails(request):
    a=request.GET.get('msg')
    data=products.objects.filter(id=a)

    return render(request,'user/viewdetails.html',{"d":data})

def process(request):
    userid=request.session.get('userid')
    pid=request.GET.get('pid')
    print(userid,pid)
    if userid is not None:
        return render(request,'user/process.html',{"alreadylogin":True})
    else:
        return render(request,'user/signin.html')

    return render(request,'user/process.html')

def logout(request):
    del request.session['userid']
    return HttpResponse("<script>window.location.href='/user/home/'</script>")

def cart(request):
    if request.session.get('userid'):
        userid=request.session.get('userid')
        cursor=connection.cursor()
        cursor.execute("select c.*,p.* from user_addtocart c, user_products p where p.id=c.pid")
        cartdata=cursor.fetchall()
        pid=request.GET.get('pid')
        if request.GET.get('pid'):
            res=addtocart.objects.filter(id=pid,userid=userid)
            res.delete()
            return HttpResponse("<script>alert('Your product has been removed successfully');window.localhost.href='/user/cart';</script>")
    return render(request,'user')

