from django.shortcuts import render,HttpResponseRedirect,reverse
from .models import *
from random import *

# Create your views here.
def IndexPage(request):
    return render(request,"eplastic/index.html")
def Index2Page(request):
    return render(request,"eplastic/index-2.html")
def CustomerSignUp(request):
    return render(request,"eplastic/customer_signup.html")
def CustomerSignIn(request):
    return render(request,"eplastic/customer_signin.html")
def CustomerProfile(request):
    return render(request,"eplastic/customer_profile.html")

def AdminSignUp(request):
    return render(request,"eplastic/admin_signup.html")
def AdminSignin(request):
    return render(request,"eplastic/admin_signin.html")
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
            return render(request,"eplastic/index.html",{'msg':message})
        else:
            if password==cpassword:
                otp = randint(10000,99999)
                newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                newCust=Customer.objects.create(master_id=newMaster,fname=fname,lname=lname,contact=contact,address=address)
                request.session['Email'] = newMaster.email
                request.session['id'] = newMaster.id
                request.session['Role']=newMaster.role
                request.session['Firstname'] = newCust.fname
                request.session['Lastname'] = newCust.lname
                request.session['Add'] = newCust.address
                request.session['Password'] = newMaster.password
                request.session['Contact'] = newCust.contact
                return render(request,"eplastic/index-2.html")

            else:
                message= "Password doesn't match!"
                return render(request,"eplastic/customer_signup.html",{'msg':message})
    else:
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
                return render(request,"eplastic/index.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newComp=Company.objects.create(master_id=newMaster,comp_name=name,comp_address=address,comp_contact=contact)
                    
                    return render(request,"eplastic/admin_index.html")
                else:
                    message= "Password doesn't match!"
                    return render(request,"eplastic/admin_signup.html",{'msg':message})
        # else:
        #     message= "Select Role!"
        #     return render(request,"eplastic/admin_signup.html",{'msg':message})
    
        if request.POST['role']=="Plastic3Collector":
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
                return render(request,"eplastic/index.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newCust=PlasticC.objects.create(master_id=newMaster,pc_fname=name,pc_address=address,pc_contact=contact)
                    return render(request,"eplastic/admin_index.html")
                else:
                    message= "Password doesn't match!"
                    return render(request,"eplastic/admin_signup.html",{'msg':message})
        # else:
        #     message= "Select Role!"
        #     return render(request,"eplastic/admin_signup.html",{'msg':message})


def Login(request):
    if request.POST['role'] == "customer":
        email = request.POST['email']
        password = request.POST['password']
        user = Master.objects.get(email=email , password=password)
        if user.password==password and user.role=="customer":
            cust = Customer.objects.get(master_id=user)
            request.session['Email'] = user.email
            request.session['id'] = user.id
            request.session['Role']=user.role
            request.session['Firstname'] = cust.fname
            request.session['Lastname'] = cust.lname
            request.session['Add'] = cust.address
            request.session['Password'] = user.password
            request.session['Contact'] = cust.contact
            return render(request,"eplastic/index-2.html")
        else:
            return render(request,"eplastic/customer_signin.html")
    if request.POST['role'] == "PlasticCollector":
        email = request.POST['email']
        password = request.POST['password']
        user = Master.objects.get(email=email , password=password)
        if user.password==password and user.role=="PlasticCollector":
            pcoll = PlasticC.objects.get(master_id=user)
            request.session['pfname'] = pcoll.pc_fname
            request.session['pcontact'] = pcoll.pc_contact
            request.session['paddress'] = pcoll.pc_address
            request.session['pemail'] = user.email
            request.session['prole'] = user.role
            request.session['pid'] = user.id
            return render(request,"eplastic/admin_index.html")
    


def ProfileData(request,pk):
    print("==================PK===================",pk)
    udata = Master.objects.get(id=pk)
    if udata.role=="customer":
        cust = Customer.objects.get(master_id=udata)
        return render(request,"eplastic/customer_profile.html",{'key3':cust})
     #if request.POST['role']=="Re-cycling Company"

def UpdateData(request,pk):
    edata = Master.objects.get(id=pk)
    if edata.role == "customer":
        cust = Customer.objects.get(master_id=edata)
        edata.email = request.POST['email']
        edata.password = request.POST['password']
        edata.cpassword = request.POST['cpassword']
        cust.fname = request.POST['fname']
        cust.lname = request.POST['lname']
        cust.contact = request.POST['contact']
        cust.address = request.POST['address']
        edata.save()
        cust.save()
        request.session['Email'] = edata.email
        request.session['id'] = edata.id
        request.session['Role']=edata.role
        request.session['Firstname'] = cust.fname
        request.session['Lastname'] = cust.lname
        request.session['Add'] = cust.address
        request.session['Password'] = edata.password
        request.session['Contact'] = cust.contact
        return render(request,"eplastic/customer_profile.html",{'key3':cust})
    
def CustomerProfileUpdate(request,pk):
    data = Master.objects.get(id=pk)
    if data.role=="customer":
        cust = Customer.objects.get(master_id=data)   
        return render(request,"eplastic/customer_update.html",{'key4':cust})
      
def CustomerProfileDelete(request,pk):
    ddata = Master.objects.get(id=pk)
    if ddata.role == "customer":
        dcust = Customer.objects.get(master_id=ddata)
        dcust.delete()
        ddata.delete() 
        return render(request,"eplastic/customer_signup.html")
def AdminProfile(request,pk):
    adata = Master.objects.get(id=pk)
    if adata.role=="PlasticCollector":
        plast = PlasticC.objects.get(master_id=adata)
        return render(request,"eplastic/admin_profile.html",{'key5':plast})


    
