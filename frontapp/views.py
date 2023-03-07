from django.shortcuts import render, redirect
from backent.models import addcategorydb, producpagedb
from frontapp.models import CustomerDetails, checkkoutdb
from django.contrib import messages

# Create your views here.
def homeepgess(request):
    data = addcategorydb.objects.all()
    return render(request, "homepage.html", {'data':data})

def aboutpage(request):
    return render(request, "about.html")

def contactpage(request):
    return render(request, "contact.html")

def OrderPAGE(request):
    data = addcategorydb.objects.all()
    return render(request, "order_page.html", {'data':data})

def TestimoniaPage(request):
    return render(request, 'testimonia_page.html')

def displayprdctPage(req, itemCatg):
    print("===itemCatg===", itemCatg)
    catg = itemCatg.upper()
    products = producpagedb.objects.filter(Category=itemCatg)
    context = {
        'products': products,
        'catg': catg
    }
    return render(req, "display_products.html", context)

def ProductSinglee(request, dataid):
    dat = producpagedb.objects.get(id=dataid)
    return render(request, "product_single.html", {'dat':dat})

def loginregister(request):
    return render(request, "login_or_register.html")

def savecostemerdetails(request):
    if request.method == "POST":
        usr = request.POST.get('uname')
        em = request.POST.get('email')
        ps = request.POST.get('password')
        cnp = request.POST.get('cpassword')
        obj = CustomerDetails(username=usr, email=em, password=ps, confirmpassword=cnp)
        obj.save()
        messages.success(request, "Register Successfully")
        return redirect(loginregister)


def customerlogin(request):
    if request.method=="POST":
        username_r=request.POST.get("uname")
        password_r=request.POST.get("password")
        if CustomerDetails.objects.filter(username=username_r, password=password_r).exists():
            request.session['uname']=username_r
            request.session['password']=password_r
            messages.success(request, "Login Successfully")
            return redirect(homeepgess)
        else:
            messages.error(request, "Invalid User")
            return render(request, 'login_or_register.html')



def userlogout(request):
    del request.session['uname']
    del request.session['password']

def chckoutpage(request):
    return render(request, "CheckoutPage.html")

def savecheckout(request):
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        addrs = request.POST.get('address')
        landmrk = request.POST.get('landmark')
        state = request.POST.get('state')
        city = request.POST.get('city')
        pincd = request.POST.get('pincd')
        obj = checkkoutdb(Fname=fname, Lname=lname, Email=email, Address=addrs, Landmark=landmrk, state=state, city=city, Pin=pincd)
        obj.save()
        messages.success(request, "Order Successfully")
        return redirect(homeepgess)




