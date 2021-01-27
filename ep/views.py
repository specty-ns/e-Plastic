from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import *

# Create your views here.
def IndexPage(request):
    return render(request,"ep/index.html")
def Index2Page(request):
    return render(request,"ep/index-2.html")
def CustomerSignUp(request):
    return render(request,"ep/customer_signup.html")
def CustomerSignIn(request):
    return render(request,"ep/customer_signin.html")
def AdminSignUp(request):
    return render(request,"ep/admin_signup.html")
def AdminSignIn(request):
    return render(request,"ep/admin_signin.html")
def CustomerProfile(request):
    return render(request,"ep/customer_profile.html")
def CompanyProfile(request):
    return render(request,"ep/company_profile.html")

def Register(request):
    if request.POST['role']=="customer":
        role = request.POST['role']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        fname = request.POST['fname']
        lname = request.POST['lname']
        contact = request.POST['contact']
        address = request.POST['address']
    
        user=Master.objects.filter(email=email)
        if user:
            message = "User already exist! "
            return render(request,"ep/index.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(10000,99999)
                newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                newCust=Customer.objects.create(master_id=newMaster,fname=fname,lname=lname,contact=contact,address=address)
               
                return render(request,"ep/customer_signin.html")

            else:
                message= "Password doesn't match!"
                return render(request,"ep/customer_signup.html",{'msg':message})
    
    if request.POST['role']=="RecyclingCompany":
        role = request.POST['role']
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['phone']
        address=request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']

        user=Master.objects.filter(email=email)
        if user:
            message = "User already exist! "
            return render(request,"ep/admin_signup.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(10000,99999)
                newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                newComp=Company.objects.create(master_id=newMaster,comp_name=name,comp_address=address,comp_contact=contact)
                
                return render(request,"ep/admin_signin.html")
            else:
                message= "Password doesn't match!"
                return render(request,"ep/admin_signup.html",{'msg':message})
        
    
    if request.POST['role']=="PlasticCollector":
        role = request.POST['role']
        name=request.POST['name']
        email=request.POST['email']
        contact=request.POST['phone']
        address=request.POST['address']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user=Master.objects.filter(email=email)
        if user:
            message = "User already exist! "
            return render(request,"ep/index.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(10000,99999)
                newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                newCust=PlasticC.objects.create(master_id=newMaster,pc_fname=name,pc_address=address,pc_contact=contact)
                return render(request,"ep/admin_index.html")
            else:
                message= "Password doesn't match!"
                return render(request,"ep/admin_signup.html",{'msg':message})



def LoginUser(request):
    try:
        if request.POST['role']=="customer":
            email = request.POST['email']
            password= request.POST['password']
            user = Master.objects.get(email=email)
            print("user------------------------->",user)
            if user:
                if user.password==password and user.role=="customer":
                    cust = Customer.objects.get(master_id=user)
                    print("Customer------------------------->",cust)
                    request.session['email']=user.email
                    request.session['Role']=user.role
                    request.session['Firstname'] = cust.fname
                    request.session['Lastname'] = cust.lname
                    request.session['Gender'] = cust.gender
                    request.session['State'] = cust.state
                    request.session['id'] = user.id
                    return render(request,"ep/index-2.html")
                else:
                    message = "User Password or Role Doesnot match"

                    
        elif request.POST['role']=="RecyclingCompany":

            email = request.POST['email']
            password= request.POST['password']
            user = Master.objects.get(email=email)
            if user:
                if user.password==password and user.role=="RecyclingCompany":
                    comp = Company.objects.get(master_id=user)
                    request.session['email']=user.email
                    request.session['id']=user.id
                    request.session['Role']=user.role
                    request.session['Cname']=comp.comp_name
                    request.session['Cadd']=comp.comp_address
                    request.session['Ccon']=comp.comp_contact
                    request.session['Ofname']=comp.owner_fname
                    request.session['Olname']=comp.owner_lname
                    return render(request,"ep/admin_index.html")
    except Exception as e1:
        print("LoginException---------------------->",e1)
    
                
                
def CustomerProfileData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="customer":
        cust = Customer.objects.get(master_id=udata)
        return render(request,"ep/customer_profile.html",{'key3':cust})

def CompanyProfileData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="RecyclingCompany":
        comp = Company.objects.get(master_id=udata)
        return render(request,"ep/company_profile.html",{'key5':comp})


def UpdateButtonClick(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="customer":
        cust = Customer.objects.get(master_id=udata)
        return render(request,"ep/customer_update.html",{"key4":cust})
def CompanyUpdateClick(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="RecyclingCompany":
        comp = Company.objects.get(master_id=udata)
        return render(request,"ep/company_update.html",{"key6":comp})

def UpdateData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="customer":
        cust = Customer.objects.get(master_id=udata)
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.gender = request.POST['gender']
        udata.email = request.POST['email']
        cust.contact = request.POST['contact']
        cust.address = request.POST['address']
        cust.state = request.POST['state']
        udata.save()
        cust.save()
        url = f'/profiledata/{pk}'
        return redirect(url)

def CompanyUpdateData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="RecyclingCompany":
        comp = Company.objects.get(master_id=udata)
        comp.owner_fname = request.POST['ofname']
        comp.owner_lname = request.POST['olname']
        udata.email = request.POST['email']
        comp.comp_contact = request.POST['ccontact']
        comp.comp_address = request.POST['caddress']
        udata.save()
        comp.save()
        url = f'/companydata/{pk}'
        return redirect(url)
