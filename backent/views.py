from django.shortcuts import render, redirect
from backent.models import addadmindb, addcategorydb, producpagedb, Contactdb
from django.core.files.storage import FileSystemStorage
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from frontapp.views import contactpage
from django.contrib import messages

# Create your views here.
def indexpage(req):
    return render(req, "index.html")

def adminpage(req):
    return render(req, "addadmin.html")

def saveaddadmin(request):
    if request.method == "POST":
        usr = request.POST.get('uname')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cnp = request.POST.get('cpassword')
        obj = addadmindb(User=usr,Email=em, Password=ps, Conpswd=cnp)
        obj.save()
        return redirect(adminpage)

def displayadmin(request):
    data = addadmindb.objects.all()
    return render(request, "displayaddadmin.html", {'data':data})

def editadmin(request,dataid):
    data = addadmindb.objects.get(id=dataid)
    print(data)
    return render(request, "Editadminpage.html", {'data':data})
def updateadmindata(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        usr = request.POST.get('uname')
        em = request.POST.get('email')
        mb = request.POST.get('mobile')
        ps = request.POST.get('password')
        cnp = request.POST.get('cpassword')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addadmindb.objects.get(id=dataid).Image
        addadmindb.objects.filter(id=dataid).update(Name=na, User=usr,Email=em, Mobile=mb, Password=ps, Conpswd=cnp, Image=file)
        return redirect(displayadmin)

def deleteadmindata(request, dataid):
    data = addadmindb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayadmin)
def addcategory(request):
    return render(request, "category.html")

def savecategorypage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        im = request.FILES['image']
        obj = addcategorydb(Name=na, Description=ds, Image=im)
        obj.save()
        return redirect(addcategory)

def displaycategoryfn(request):
    data = addcategorydb.objects.all()
    return render(request, "Displaycategory.html", {'data':data})

def edtcategory(request, dataid):
    data = addcategorydb.objects.get(id=dataid)
    print(data)
    return render(request, "editcategory.html", {'data':data})

def Updatecategorypage(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        ds = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name, img)
        except MultiValueDictKeyError:
            file = addcategorydb.objects.get(id=dataid).Image
        addcategorydb.objects.filter(id=dataid).update(Name=na, Description=ds, Image=file)
        return redirect(displaycategoryfn)

def Deletecategory(request, dataid):
    data = addcategorydb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycategoryfn)

def productpage(request):
    data = addcategorydb.objects.all()
    return render(request, "product.html", {'data':data})

def productsavepage(request):
    if request.method == "POST":
        na = request.POST.get('name')
        pr = request.POST.get('prize')
        qn = request.POST.get('quantity')
        ca = request.POST.get('category')
        ds = request.POST.get('description')
        im = request.FILES['image']
        obj = producpagedb(Name=na, Prize=pr, Quantity=qn, Category=ca, Description=ds, Image=im)
        obj.save()
        return redirect(productpage)

def displayproductfn(request):
    data = producpagedb.objects.all()
    return render(request, "displayproduct.html", {'data':data})

def editproductpage(request, dataid):
    data = producpagedb.objects.get(id=dataid)
    print(data)
    da = addcategorydb.objects.all()
    return render(request, "Editproductpage.html", {'datas':data, 'da':da})

def updateproductdata(request, dataid):
    if request.method == "POST":
        na = request.POST.get('name')
        pr = request.POST.get('prize')
        qn = request.POST.get('quantity')
        ca = request.POST.get('category')
        ds = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = producpagedb.objects.get(id=dataid).Image
        producpagedb.objects.filter(id=dataid).update(Name=na, Prize=pr, Quantity=qn, Category=ca, Description=ds, Image=file)
        return redirect(displayproductfn)

def Deleteproduct(request, dataid):
    data = producpagedb.objects.filter(id=dataid)
    data.delete()
    return redirect(displayproductfn)

def lognpagee(request):
    return render(request, "loginpage.html")

def adminlogin(request):
    if request.method == "POST":
        username_r = request.POST.get('username')
        password_r = request.POST.get('pass')

        if User.objects.filter(username__contains=username_r).exists():
            user = authenticate(username=username_r, password=password_r)
            if user is not None:
                login(request, user)
                request.session['username']=username_r
                request.session['pass']=password_r
                return redirect(indexpage)
            else:
                return redirect(lognpagee)
        else:
            return redirect(lognpagee)


def logout(request):
    del request.session['username']
    del request.session['pass']
    return redirect(lognpagee)



def savecontact(request):
    if request.method == "POST":
        fname = request.POST.get('Fullname')
        email = request.POST.get('Email')
        phone = request.POST.get('Phone')
        message = request.POST.get('Message')
        obj = Contactdb(FName=fname, Email=email, Phone=phone, Message=message)
        obj.save()
        messages.success(request, "Thank You!")
        return redirect(contactpage)

def displaycontactpage(request):
    cont = Contactdb.objects.all()
    return render(request, "DisplayContactpage.html", {'cont':cont})

def Deletecontactpage(request, dataid):
    data = Contactdb.objects.filter(id=dataid)
    data.delete()
    return redirect(displaycontactpage)




