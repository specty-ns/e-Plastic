from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import *
import datetime

# Create your views here.
def IndexPage(request):
    return render(request,"ep/index.html")
def CompanyIndexPage(request):
    return render(request,"ep/company_index.html")
def CollectorIndexPage(request):
    return render(request,"ep/plasticCollector_index.html")
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
def PlasticCollectorProfile(request):
    return render(request,"ep/plasticCollector_profile.html")
def PProduct(request):
    return render(request,"ep/addpproduct.html")
def RProduct(request):
    return render(request,"ep/addrproduct.html")
def AdminLogin(request):
    return render(request,"ep/admin/login.html")
def Dashboard(request):
    return render(request,"ep/admin/aindex.html")


def Register(request):
    try:
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
                    newPlastic=PlasticC.objects.create(master_id=newMaster,pc_name=name,pc_address=address,pc_contact=contact)
                    return render(request,"ep/admin_signin.html")
                else:
                    message= "Password doesn't match!"
                    return render(request,"ep/admin_signup.html",{'msg':message})
    except Exception as e1:
        print("RegistrationException---------------------->",e1)

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
                    message = "User Email or Password Doesnot match"
                    return render(request,"ep/customer_signin.html",{'msg':message})
            else:
                message = "User Email or Password Doesnot match"
                return render(request,"ep/customer_signin.html",{'msg':message})

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
                    request.session['Cfb']=comp.comp_fb
                    request.session['Cins']=comp.comp_insta
                    request.session['Clin']=comp.comp_linkedin
                    request.session['Ctwit']=comp.comp_twitter
                    request.session['Cweb']=comp.comp_website
                    request.session['Ofname']=comp.owner_fname
                    request.session['Olname']=comp.owner_lname
                    request.session['Ogen']=comp.owner_gender
                    request.session['Ocon']=comp.owner_contact
                    request.session['Oemail']=comp.owner_email
                    return render(request,"ep/company_index.html")
                else:
                    message= "Role or Email or Password doesn't match!"
                    return render(request,"ep/admin_signin.html",{'msg':message})

        elif request.POST['role']=="PlasticCollector":
            email = request.POST['email']
            password= request.POST['password']
            user = Master.objects.get(email=email)
            if user:
                if user.password==password and user.role=="PlasticCollector":
                    pc = PlasticC.objects.get(master_id=user)
                    request.session['email']=user.email
                    request.session['id']=user.id
                    request.session['Role']=user.role
                    request.session['Pcname']=pc.pc_name
                    request.session['Pcadd']=pc.pc_address
                    request.session['Pccon']=pc.pc_contact
                    request.session['Pcfb']=pc.pc_fb
                    request.session['Pcins']=pc.pc_insta
                    request.session['Pclin']=pc.pc_linkedin
                    request.session['Pctwit']=pc.pc_twitter
                    request.session['Pcweb']=pc.pc_website
                    request.session['Ofname']=pc.owner_fname
                    request.session['Olname']=pc.owner_lname
                    request.session['Ogen']=pc.owner_gender
                    request.session['Ocon']=pc.owner_contact
                    request.session['Oemail']=pc.owner_email
                    return render(request,"ep/plasticCollector_index.html")
                else:
                    message= "Role or Email or Password doesn't match!"
                    return render(request,"ep/admin_signin.html",{'msg':message})
    except Exception as e2:
        print("LoginException---------------------->",e2)
                
def CustomerProfileData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="customer":
        cust = Customer.objects.get(master_id=udata)
        return render(request,"ep/customer_profile.html",{'key3':cust})

def UpdateButtonClick(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="customer":
        cust = Customer.objects.get(master_id=udata)
        return render(request,"ep/customer_update.html",{"key4":cust})

def CompanyProfileData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="RecyclingCompany":
        comp = Company.objects.get(master_id=udata)
        return render(request,"ep/company_profile.html",{'key5':comp})

def CompanyUpdateClick(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="RecyclingCompany":
        comp = Company.objects.get(master_id=udata)
        return render(request,"ep/company_update.html",{"key6":comp})

def PlasticCollectorProfileData(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="PlasticCollector":
        pc = PlasticC.objects.get(master_id=udata)
        return render(request,"ep/plasticCollector_profile.html",{'key8':pc})
def PlasticCollectorUpdateButtonClick(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="PlasticCollector":
        pc = PlasticC.objects.get(master_id=udata)
        return render(request,"ep/plasticCollector_update.html",{"key7":pc})

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
        udata.email = request.POST['email']
        comp.comp_name= request.POST['cname']
        comp.comp_contact = request.POST['ccontact']
        comp.comp_address = request.POST['caddress']
        comp.comp_website = request.POST['cwebsite']
        comp.comp_image = request.FILES['cimage']
        comp.comp_insta = request.POST['cinsta']
        comp.comp_linkedin = request.POST['clinkedin']
        comp.comp_twitter = request.POST['ctwitter']
        comp.comp_fb = request.POST['cfb']
        comp.owner_fname = request.POST['cofname']
        comp.owner_lname = request.POST['colname']
        comp.owner_gender = request.POST['cogender']
        comp.owner_email = request.POST['coemail']
        comp.owner_contact = request.POST['cocontact']
        udata.save()
        comp.save()
        url = f'/companydata/{pk}'
        return redirect(url)

def PlasticCollectorUpdateData(request,pk):
    udata = Master.objects.get(id=pk)
    
    if udata.role=="PlasticCollector":
        pc = PlasticC.objects.get(master_id=udata)
        udata.email = request.POST['email']
        pc.pc_name = request.POST['pcname']
        pc.pc_address = request.POST['pcaddress']
        pc.pc_contact = request.POST['pccontact']
        pc.pc_image = request.FILES['pcimage']
        pc.pc_fb = request.POST['pcfb']
        pc.pc_insta = request.POST['pcinsta']
        pc.pc_linkedin = request.POST['pclinkedin']
        pc.pc_twitter = request.POST['pctwitter']
        pc.pc_website = request.POST['pcwebsite']
        pc.owner_fname = request.POST['pcofname']
        pc.owner_lname = request.POST['pcolname']
        pc.owner_gender = request.POST['pcogender']
        pc.owner_email = request.POST['pcoemail']
        pc.owner_contact = request.POST['pcocontact']
        udata.save()
        pc.save()   
        url = f'/plasticCollectordata/{pk}'
        return redirect(url)

def AddPProduct(request,pk):
    try:
        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            pro_name = request.POST['pname']
            pro_date = request.POST['pdate']
            pro_price = request.POST['pprice']
            pro_image = request.FILES['pimage']
            pro_quantity = request.POST['pqty']

            newProduct=PlasticProduct.objects.create(plasticc_id=pc,pproduct_name=pro_name,pproduct_date=pro_date,pproduct_price=pro_price,pproduct_image=pro_image,pproduct_quantity=pro_quantity)
            message= "Product Added Successfully"
            return render(request,"ep/addpproduct.html",{'msg':message})
    except Exception as ae:
        print("Add P Product--------->",ae)

def GetAllPProduct(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="PlasticCollector":
        pc = PlasticC.objects.get(master_id=udata)
        allpproduct= PlasticProduct.objects.all().filter(plasticc_id=pc)
        return render(request,"ep/allpproducts.html",{'key9':allpproduct})


def PPUpdateButton(request,pk):
    try:
        pp = PlasticProduct.objects.get(id=pk)
        print("IDt--------->",id)
        return render(request,"ep/pproduct_update.html",{"key10":pp})
    except Exception as r:
        print("Button Product--------->",r)


def UpdateProduct(request,pk):
    try:
        pro = PlasticProduct.objects.get(pk=pk)
        pro.pproduct_name = request.POST['pname']
        pro.pproduct_date = request.POST['pdate']
        pro.pproduct_price = request.POST['pprice']
        pro.pproduct_image = request.FILES['pimage']
        pro.pproduct_quantity = request.POST['pqty']
        pro.save()
        pp = request.session['id']
        url = f"/allpproducts/{pp}"
        return redirect(url)
    except Exception as i:
        print("Image Product--------->",i)

def DeleteProduct(request,pk):
    try:
        ddata = PlasticProduct.objects.get(pk=pk)
        ddata.delete()
        pp = request.session['id']
        url = f"/allpproducts/{pp}"
        return redirect(url)
    except Exception as ok:
        print("------------>delete error",ok)

def RPAllProduct(request):
    all_pro = PlasticProduct.objects.all() 
    return render(request,"ep/rp_allproducts.html",{'key11':all_pro})

def RPButtonClick(request,pk):
    try:
        pc = PlasticProduct.objects.get(pk=pk)
        return render(request,"ep/requestpproduct.html",{'key12':pc})
    except Exception as k:
        print("------------>Click error",k)


def RPButton(request,pk):
    try:
        udata = Master.objects.get(id=pk)
        if udata.role == "RecyclingCompany":
            rcdata = Company.objects.get(master_id=udata)
            pc_id = request.POST['pc_id']
            pla_id = PlasticC.objects.get(id=pc_id)
            print("Plastic ID>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",pla_id)
            pc_date = request.POST['rdate']
            pc_qty = request.POST['rqty']
            pid = request.POST['pid']
            pro_id = PlasticProduct.objects.get(id=pid)
            newRequest=RequestButton.objects.create(comp_id=rcdata,plasticc_id=pla_id,pproduct_id=pro_id,request_date=pc_date,request_quantity=pc_qty)
            message= "Request Sent Successfully"
            return HttpResponseRedirect(reverse('rpallpro'),{'msg':message})
    except Exception as e11:
        print("Req Button ----------------------------->",e11)

def ShowPReq(request):
    try:
        all_preq = RequestButton.objects.all() 
        return render(request,"ep/showplasticreq.html",{'key13':all_preq})
    except Exception as s:
        print("Show ----------------------------->",s)

def RejectProduct(request,pk):
    try:
        rdata = RequestButton.objects.get(pk=pk)
        rdata.delete()
        return HttpResponseRedirect(reverse('showpreq'))
    except Exception as rr:
        print("------------>delete error",rr)

def AddRProduct(request,pk):
    try:
        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            rc = Company.objects.get(master_id=udata)
            rpro_name = request.POST['rpname']  
            rpro_date = request.POST['rpdate']
            rpro_price = request.POST['rpprice']
            rpro_image = request.FILES['rpimage']
            rpro_quantity = request.POST['rpqty']
            newRProduct=RecycleProduct.objects.create(company_id=rc,rproduct_name=rpro_name,rproduct_date=rpro_date,rproduct_price=rpro_price,rproduct_image=rpro_image,rproduct_quantity=rpro_quantity)
            message= "Product Added Successfully"
            return render(request,"ep/addrproduct.html",{'msg':message})   
    except Exception as asp:
        print("------------>Add R Product",asp)

def GetAllRProduct(request,pk):
    udata = Master.objects.get(id=pk)
    if udata.role=="RecyclingCompany":
        pc = Company.objects.get(master_id=udata)
        allpproduct= RecycleProduct.objects.all().filter(company_id=pc)
        return render(request,"ep/allrproducts.html",{'key14':allpproduct})

def ShopProduct(request):
    try:
        all_preq = RecycleProduct.objects.all() 
        return render(request,"ep/shop-right.html",{'key15':all_preq})
    except Exception as saa:
        print("Show ----------------------------->",saa)

def DeleteRProduct(request,pk):
    try:
        rdata = RecycleProduct.objects.get(pk=pk)
        rdata.delete()
        rp = request.session['id']
        url = f"/allrproducts/{rp}"
        return redirect(url)
    except Exception as okes:
        print("------------>delete error",okes)

def RPUpdateButton(request,pk):
    try:
        rp = RecycleProduct.objects.get(id=pk)
        print("IDt--------->",id)
        return render(request,"ep/rproduct_update.html",{"key16":rp})
    except Exception as rsa:
        print("Button Product--------->",rsa)

def UpdateRProduct(request,pk):
    try:
        pro = RecycleProduct.objects.get(pk=pk)
        pro.rproduct_name = request.POST['pname']
        pro.rproduct_date = request.POST['pdate']
        pro.rproduct_price = request.POST['pprice']
        pro.rproduct_image = request.FILES['pimage']
        pro.rproduct_quantity = request.POST['pqty']
        pro.save()
        pp = request.session['id']
        url = f"/allrproducts/{pp}"
        return redirect(url)
    except Exception as i:
        print("Image Product--------->",i)
    
def ShowPro(request,pk):
    pro_id = RecycleProduct.objects.get(pk=pk)
    return render(request,"ep/shop-product-right.html",{'key17':pro_id})
def ALogin(request):
    try:
        username = request.POST['username']
        password= request.POST['password']
        if username == "admin" and password == "admin":
            request.session['Username']=username
            request.session['Password']=password
             
            return render(request,"ep/admin/aindex.html")
        else:
            message = "Invalid Username or Password"
            return render(request,"ep/admin/login.html",{'msg':message})
    except Exception as ll:
        print("Admin Login-------------------------------.",ll)
def SAdmin(request):
    all_preq = Master.objects.all() 
    return render(request,"ep/admin/tables.html",{'key18':all_preq})
           
def AButton(request,pk):
    try:
        ab = Master.objects.get(id=pk)
        print("IDt--------->",id)
        return render(request,"ep/admin/aupdate.html",{"key19":ab})
    except Exception as rsa:
        print("Button Product--------->",rsa)
def AUpdate(request,pk):
    try:
        udata = Master.objects.get(id=pk)
        udata.is_verified = request.POST['verification'] 
        udata.is_updated = datetime.datetime.now()  
        udata.save()
        url = f"/showadmin/"
        return redirect(url)
    except Exception as au:
        print("Verify nai tha tu------------------->",au)

def AddCart(request,pk):
    try:
        atcdata = Master.objects.get(id=pk)
        if atcdata.role=="customer":
            atc = Customer.objects.get(master_id=atcdata)
            print("Cust--------------->",atc)
            pro_id = request.POST['pid']
            rp = RecycleProduct.objects.get(id=pro_id)
            print("Recycle--------------->",rp)
            atc_price = request.POST['atcprice']
            atc_date = datetime.date.today()
            newAddCart=AddToCart.objects.create(rp_id=rp,cust_id=atc,cart_price=atc_price,cart_date=atc_date)
            ppp = request.session['id']
            url = f"/showthecart/{ppp}"
            return redirect(url)
            
    except Exception as aaaa:
        print("Add to cart nai thatu--------------->",aaaa)

def ShowCart(request,pk):
    try:
        cdata = Master.objects.get(id=pk)
        if cdata.role=="customer":
            cust = Customer.objects.get(master_id=cdata)
            show = AddToCart.objects.all().filter(cust_id=cust)
            return render(request,"ep/customercart.html",{"key20":show})
    except Exception as skc:
        print("nai avtu---------------",skc)

def DelCart(request,pk):
    ddata = AddToCart.objects.get(pk=pk)
    ddata.delete()
    p = request.session['id']
    url = f"/showthecart/{p}"
    return redirect(url)
