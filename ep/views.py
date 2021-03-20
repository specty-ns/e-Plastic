from django.shortcuts import render,HttpResponseRedirect,reverse,redirect
from .models import *
from random import *
import datetime
from django.conf import settings
from .paytm import generate_checksum, verify_checksum
from .utils import *
from django.views.decorators.csrf import csrf_exempt

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
def CustData(request):
    return render(request,"ep/customer_data.html",{"cust":Customer.objects.all()})


def OTP(request):
    return render(request,"ep/otpverify.html")

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
                return render(request,"ep/customer_signup.html",{'msg':message})
            else:
                if password==cpassword:
                    otp = randint(10000,99999)
                    newMaster=Master.objects.create(email=email,password=password,otp=otp,role=role)
                    newCust=Customer.objects.create(master_id=newMaster,fname=fname,lname=lname,contact=contact,address=address)
                    email_subject = "Customer Verification"
                    sendmail(email_subject,'mail_template',email,{'name':fname,'otp':otp})
                    mail = email
                    return render(request,"ep/otpverify.html",{'email':mail})
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
                    email_subject = "Recycling Company Verification"
                    sendmail(email_subject,'mail_template',email,{'name':name,'otp':otp})
                    mail = email
                    return render(request,"ep/otpverify.html",{'email':mail})
                    
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
                    email_subject = "Plastic Collector Verification"
                    sendmail(email_subject,'mail_template',email,{'name':name,'otp':otp})
                    mail = email
                    return render(request,"ep/otpverify.html",{'email':mail})    
                else:
                    message= "Password doesn't match!"
                    return render(request,"ep/admin_signup.html",{'msg':message})
    except Exception as e1:
        print("RegistrationException---------------------->",e1)

def VerifyOtp(request):
    print("------------1--------------")
    try:
        email=request.POST['email']
        eotp=int(request.POST['eotp'])
        print("Eotp--------------->",eotp)
        user = Master.objects.get(email=email)
        if user.otp==eotp and user.role =="customer":
            message = "otp verified successfully"
            return render(request,"ep/customer_signin.html",{'msg2':message})
        elif user.otp==eotp and user.role=="RecyclingCompany":
            message = "otp verified successfully"
            return render(request,"ep/admin_signin.html",{'msg2':message})
        elif user.otp==eotp and user.role=="PlasticCollector":
            message = "otp verified successfully"
            return render(request,"ep/admin_signin.html",{'msg2':message})
        else:
            message = "Enter Correct OTP "
            return render(request,"ep/otpverify.html",{'email':email, 'msg3':message})
    except Exception as e:
        print("OTP Verify Exception-------------->",e)
        
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
                    request.session['password'] = user.password
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
                    request.session['password'] = user.password
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
                    request.session['password'] = user.password
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
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="customer":
            cust = Customer.objects.get(master_id=udata)
            return render(request,"ep/customer_profile.html",{'key3':cust})
    else:
        return redirect('signin')

def UpdateButtonClick(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="customer":
            cust = Customer.objects.get(master_id=udata)
            return render(request,"ep/customer_update.html",{"key4":cust})
    else:
        return redirect('signin')

def CompanyProfileData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            comp = Company.objects.get(master_id=udata)
            return render(request,"ep/company_profile.html",{'key5':comp})
    else:
        return redirect('adminin')
def CompanyUpdateClick(request,pk):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            comp = Company.objects.get(master_id=udata)
            return render(request,"ep/company_update.html",{"key6":comp})
    else:
        return redirect('adminin')

def ReqPlastic(request):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        comp = Company.objects.get(id=udata)
        request = PlasticRequest.objects.all().filter(comp_id=comp)
        return render(request,"ep/company_reqplastic",{'requested_plastic':request})
    else:
        return redirect('adminin')
def PlasticCollectorProfileData(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            return render(request,"ep/plasticCollector_profile.html",{'key8':pc})
    else:
        return redirect('adminin')
def PlasticCollectorUpdateButtonClick(request,pk):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            return render(request,"ep/plasticCollector_update.html",{"key7":pc})
    else:
        return redirect('adminin')

def UpdateData(request,pk):
    if "email" in request.session and "password" in request.session:

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
            cust.city = request.POST['city']
            cust.postalcode = request.POST['postcode']
            udata.save()
            cust.save()
            url = f'/profiledata/{pk}'
            return redirect(url)    
    else:
        return redirect('signin')

def CompanyUpdateData(request,pk):
    if "email" in request.session and "password" in request.session:

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
    else:
        return redirect('adminin')

def PlasticCollectorUpdateData(request,pk):
    if "email" in request.session and "password" in request.session:

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
    else:
        return redirect('adminin')    

def AddPProduct(request,pk):
    if "email" in request.session and "password" in request.session:

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
    else:
        return redirect('adminin')
def GetAllPProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="PlasticCollector":
            pc = PlasticC.objects.get(master_id=udata)
            allpproduct= PlasticProduct.objects.all().filter(plasticc_id=pc)
            return render(request,"ep/allpproducts.html",{'key9':allpproduct})
    else:
        return redirect('adminin')

def PPUpdateButton(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            pp = PlasticProduct.objects.get(id=pk)
            print("IDt--------->",id)
            return render(request,"ep/pproduct_update.html",{"key10":pp})
        except Exception as r:
            print("Button Product--------->",r)
    else:
        return redirect('adminin')


def UpdateProduct(request,pk):
    if "email" in request.session and "password" in request.session:
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
    else:
        return redirect('adminin')
def DeleteProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            ddata = PlasticProduct.objects.get(pk=pk)
            ddata.delete()
            pp = request.session['id']
            url = f"/allpproducts/{pp}"
            return redirect(url)
        except Exception as ok:
            print("------------>delete error",ok)
    else:
        return redirect('adminin')

def RPAllProduct(request):
    if "email" in request.session and "password" in request.session:

        all_pro = PlasticProduct.objects.all() 
        return render(request,"ep/rp_allproducts.html",{'key11':all_pro})
    else:
        return redirect('adminin')
def RPButtonClick(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pc = PlasticProduct.objects.get(pk=pk)
            return render(request,"ep/requestpproduct.html",{'key12':pc})
        except Exception as k:
            print("------------>Click error",k)
    else:
        return redirect('adminin')

def CompanyCheckOut(request):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        total = 0
        if udata.role == "RecyclingCompany":
            cdata = Company.objects.get(master_id=udata)
            cartdata = PlasticRequest.objects.all().filter(comp_id=cdata,pproduct_id=request.POST['pro_id'])
            for t in cartdata:
                total = t.request_quantity*t.pproduct_id.pproduct_price
            return render(request,"ep/company_checkout.html",{"key26":cartdata,"total":total,"key27":cdata})
    else:
        return redirect('signin')

def RPButton(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            udata = Master.objects.get(id=pk)
            if udata.role == "RecyclingCompany":
                rcdata = Company.objects.get(master_id=udata)
                email = rcdata.master_id.email
                rcname = rcdata.comp_name
                pc_id = request.POST['pc_id']
                pla_id = PlasticC.objects.get(id=pc_id)
                pc_email = pla_id.master_id.email
                pcname= pla_id.pc_name
                pc_date = request.POST['rdate']
                pc_qty = request.POST['rqty']
                pid = request.POST['pid']
                pro_id = PlasticProduct.objects.get(id=pid)
                plasticname= pro_id.pproduct_name
                newRequest=PlasticRequest.objects.create(comp_id=rcdata,plasticc_id=pla_id,pproduct_id=pro_id,request_date=pc_date,request_quantity=pc_qty)
                email_subject = "Plastic Request"
                sendreq(email_subject,'mail_template',email,{'pcname':pcname,'requestqty':pc_qty,'productname':plasticname,'requestdate':pc_date})
                showreq(email_subject,'mail_template',pc_email,{'rcname':rcname,'requestqty':pc_qty,'productname':plasticname,'requestdate':pc_date})
                message= "Request Sent Successfully"
                return HttpResponseRedirect(reverse('rpallpro'),{'msg':message})
        except Exception as e11:
            print("Req Button ----------------------------->",e11)
    else:
        return redirect('adminin')
def ShowPReq(request):
    if "email" in request.session and "password" in request.session:
        try:
            udata = Master.objects.get(id=request.session['id'])
            if udata.role=="PlasticCollector":
                pc = PlasticC.objects.get(master_id=udata)
                allpproduct = PlasticRequest.objects.all().filter(plasticc_id=pc)
                for i in allpproduct:
                    print("Status ------------>",i.status, len(allpproduct))
            return render(request,"ep/showplasticreq.html",{'key13':allpproduct})
        except Exception as s:
            print("Show ----------------------------->",s)
            return render(request,"ep/showplasticreq.html")
    else:
        return redirect('adminin')

def reqaccept(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pc_id = request.session['id'] 
            print("iddddd>>>>>>>>>>>>>>>.",pc_id)  
            plastic_id =PlasticC.objects.get(master_id=pc_id)
            pcname = plastic_id.pc_name
            all_preq = PlasticRequest.objects.get(pk=pk,plasticc_id=plastic_id)
            reqqty = all_preq.request_quantity
            pproductname = all_preq.pproduct_id.pproduct_name
            reqdate = all_preq.request_date
            email = request.POST['email']
            print("emaillll",email)
            email_subject = "Plastic Request Accepted"
            acceptreq(email_subject,'mail_template',email,{'pcname':pcname,'requestqty':reqqty,'productname':pproductname,'requestdate':reqdate})
            all_preq.status = request.POST['acceptreq']
            all_preq.save()
            message="Request Accepted"
            return HttpResponseRedirect(reverse('showpreq'))
        except Exception as reee:
            print("Acc ----------------------------->",reee)
    else:
        return redirect('adminin')    
def RejectProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            pc_id = request.session['id'] 
            print("iddddd>>>>>>>>>>>>>>>.",pc_id)  
            plastic_id =PlasticC.objects.get(master_id=pc_id)
            pcname = plastic_id.pc_name
            all_preq = PlasticRequest.objects.get(pk=pk,plasticc_id=plastic_id)
            reqqty = all_preq.request_quantity
            pproductname = all_preq.pproduct_id.pproduct_name
            reqdate = all_preq.request_date
            email = request.POST['email']
            print("emaillll",email)
            email_subject = "Plastic Request Rejected"
            rejectreq(email_subject,'mail_template',email,{'pcname':pcname,'requestqty':reqqty,'productname':pproductname,'requestdate':reqdate})
            all_preq.status = request.POST['rejectreq']
            all_preq.save()
            return HttpResponseRedirect(reverse('showpreq'))
        except Exception as rr:
            print("------------>delete error",rr)
    else:
        return redirect('adminin')
def SortPlasticRequest(request):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        if udata.role == "PlasticCollector":
            if request.POST['status'] == "All":
                pc = PlasticC.objects.get(master_id=udata)
                filtered_data = PlasticRequest.objects.all().filter(plasticc_id=pc)
                return render(request, "ep/showplasticreq.html", {"key24": filtered_data,"filter":request.POST['status']})
            else:
                pc = PlasticC.objects.get(master_id=udata)
                filtered_data = PlasticRequest.objects.filter(plasticc_id=pc,status=request.POST['status'])
                return render(request, "ep/showplasticreq.html", {"key24": filtered_data,"filter":request.POST['status']})
        if udata.role == "RecyclingCompany":
            if request.POST['status'] == "SendRequest":
                all_pro = PlasticProduct.objects.all() 
                return render(request,"ep/rp_allproducts.html",{'key11':all_pro,"filter":request.POST['status']})
            if request.POST['status'] == "All":
                comp = Company.objects.get(master_id=udata)
                data = PlasticRequest.objects.all().filter(comp_id=comp)
                return render(request, "ep/rp_allproducts.html", {"key25": data,"filter":request.POST['status']})
            else:
                comp = Company.objects.get(master_id=udata)
                data = PlasticRequest.objects.filter(comp_id=comp,status=request.POST['status'])
                return render(request, "ep/rp_allproducts.html", {"key25":data,"filter":request.POST['status']})
    else:
        return redirect('adminin')
def AddRProduct(request,pk):
    if "email" in request.session and "password" in request.session:
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
    else:
        return redirect('adminin')

def GetAllRProduct(request,pk):
    if "email" in request.session and "password" in request.session:

        udata = Master.objects.get(id=pk)
        if udata.role=="RecyclingCompany":
            pc = Company.objects.get(master_id=udata)
            allpproduct= RecycleProduct.objects.all().filter(company_id=pc)
            return render(request,"ep/allrproducts.html",{'key14':allpproduct})
    else:
        return redirect('adminin')

def ShopProduct(request):
    if "email" in request.session and "password" in request.session:
        try:
            all_preq = RecycleProduct.objects.all() 
            return render(request,"ep/shop-right.html",{'key15':all_preq})
        except Exception as saa:
            print("Show ----------------------------->",saa)
    else:
        return redirect('signin')
def DeleteRProduct(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            rdata = RecycleProduct.objects.get(pk=pk)
            rdata.delete()
            rp = request.session['id']
            url = f"/allrproducts/{rp}"
            return redirect(url)
        except Exception as okes:
            print("------------>delete error",okes)
    else:
        return redirect('adminin')

def RPUpdateButton(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            rp = RecycleProduct.objects.get(id=pk)
            print("IDt--------->",id)
            return render(request,"ep/rproduct_update.html",{"key16":rp})
        except Exception as rsa:
            print("Button Product--------->",rsa)
    else:
        return redirect('adminin')

def UpdateRProduct(request,pk):
    if "email" in request.session and "password" in request.session:

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
    else:
        return redirect('adminin')
def ShowPro(request):
    if "email" in request.session and "password" in request.session:

        pro_id = RecycleProduct.objects.all()
        return render(request,"ep/shop-product-right.html",{'key17':pro_id})
    else:
        return redirect('adminin')
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
    if "Username" in request.session and "Password" in request.session:
        all_preq = Master.objects.all()     
        return render(request,"ep/admin/tables.html",{'key18':all_preq})
    else:
        return redirect('alogin')       
def AButton(request,pk):
    if "Username" in request.session and "Password" in request.session:
        try:
            ab = Master.objects.get(id=pk)
            print("IDt--------->",id)
            return render(request,"ep/admin/aupdate.html",{"key19":ab})
        except Exception as rsa:
            print("Button Product--------->",rsa)
    else:
        return redirect('alogin')
def AUpdate(request,pk):
    if "Username" in request.session and "Password" in request.session:
        try:
            udata = Master.objects.get(id=pk)
            udata.is_verified = request.POST['verification'] 
            udata.is_updated = datetime.datetime.now()  
            udata.save()
            url = f"/showadmin/"
            return redirect(url)
        except Exception as au:
            print("Verify nai tha tu------------------->",au)
    else:
        return redirect('alogin')

def AddCart(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            atcdata = Master.objects.get(id=pk)
            if atcdata.role=="customer":
                atc = Customer.objects.get(master_id=atcdata)
                print("Cust--------------->",atc)
                pro_id = request.POST['pid']
                rp = RecycleProduct.objects.get(id=pro_id)
                print("Recycle--------------->",rp)
                atc_price = int(request.POST['atcprice'])
                atc_qty = int(request.POST['product_quantity'])
                atc_subtotal = int(atc_price * atc_qty)
                atc_date = datetime.date.today()
                newAddCart=AddToCart.objects.create(rp_id=rp,cust_id=atc,cart_price=atc_price,cart_date=atc_date,cart_quantity=atc_qty,cart_subtotal=atc_subtotal)
                rp.rproduct_quantity-=atc_qty
                rp.save()
                ppp = request.session['id']
                url = f"/showthecart/{ppp}"
                return redirect(url)
                
        except Exception as aaaa:
            print("Add to cart nai thatu--------------->",aaaa)
    else:
        return redirect('signin')

def ShowCart(request,pk):
    if "email" in request.session and "password" in request.session:
        try:
            cdata = Master.objects.get(id=pk)
            total = 0
            if cdata.role=="customer":
                cust = Customer.objects.get(master_id=cdata)
                show = AddToCart.objects.all().filter(cust_id=cust)
                for t in show:
                    total += t.cart_subtotal
                print("Totallll",total)
                return render(request,"ep/customercart.html",{"key20":show, "total": total})
        except Exception as skc:
            print("nai avtu---------------",skc)
    else:
        return redirect('signin')

def loadCart(request,pk):
    if "email" in request.session and "password" in request.session:

        try:
            cdata = Master.objects.get(id=pk)
            total = 0
            cust = Customer.objects.get(master_id=cdata)
            show = AddToCart.objects.all().filter(cust_id=cust)
            for t in show:
                total += t.cart_subtotal
            print(total)
            return {"key20": show, "total": total}
        except Exception as err:
            print(err)
    else:
        return redirect('signin')

def DelCart(request,pk):
    if "email" in request.session and "password" in request.session:
        r =  RecycleProduct.objects.get(id=request.POST['rcp'])
        qty = int(request.POST['product_quantity'])
        print("dellll",qty)
        ddata = AddToCart.objects.get(pk=pk)
        r.rproduct_quantity+=qty
        r.save()
        ddata.delete()
        p = request.session['id']
        url = f"/showthecart/{p}"
        return redirect(url)
    else:
        return redirect('signin')

def UpdateCart(request,pk):
    if "email" in request.session and "password" in request.session:
        rcp =  RecycleProduct.objects.get(id=request.POST['rcp'])
        print("RCPPPPPPP",rcp)
        adata = AddToCart.objects.get(pk=pk)
        quant = int(request.POST['product_quantity'])
        if quant > adata.cart_quantity:
            update = quant-adata.cart_quantity
            rcp.rproduct_quantity-=update 
            rcp.save()
            adata.cart_quantity = quant
            adata.cart_subtotal = quant*adata.cart_price
            adata.save()
            ppp = request.session['id']
            url = f"/showthecart/{ppp}"
            return redirect(url)
        elif quant < adata.cart_quantity:
            update =  adata.cart_quantity-quant
            rcp.rproduct_quantity+=update
            rcp.save()
            adata.cart_quantity = quant
            adata.cart_subtotal = quant*adata.cart_price
            adata.save()
            inc = request.session['id']
            url = f"/showthecart/{inc}"
            return redirect(url)
        else:
            adata.cart_quantity = quant
            adata.cart_subtotal = quant*adata.cart_price
            adata.save()
            sam = request.session['id']
            url = f"/showthecart/{sam}"
            return redirect(url)
    else:
        return redirect('signin')

def CartCheckout(request,pk):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        total = 0
        if udata.role == "customer":
            cdata = Customer.objects.get(master_id=udata)
            cartdata = AddToCart.objects.all().filter(cust_id=cdata)
            for t in cartdata:
                    total += t.cart_subtotal
            return render(request,"ep/customer_cartcheckout.html",{"key22":cartdata,"total":total,"key23":cdata})
    else:
        return redirect('signin')

def Schedule(request):
    if "email" in request.session and "password" in request.session:
        udata = Master.objects.get(id=request.session['id'])
        if udata.role == "customer":
            cdata = Customer.objects.get(master_id=udata)
            cname = request.POST['pickup_name']
            email = cdata.master_id.email
            cnumber = request.POST['pickup_number']
            stime = request.POST['pickup_date_time']
            scomment = request.POST['pickup_comment']
            pickupschedule = ScheduleOrder.objects.create(cust_id=cdata,cust_name=cname,cust_number=cnumber,sc_date_time=stime,sc_comment=scomment)

            email_subject = "Plastic Pickup Request Sent"
            PickupSent(email_subject,'mail_template',email,{'fullname':cname,'contact':cnumber,'pickup_datetime':pickupschedule.sc_date_time,'pickup_details':scomment})
            message = "Pickup Done"
            return render(request,"ep/index-2.html",{'msg':message})
            
    else:
        return redirect('signin')
def ShowPickUp(request):     
    if "email" in request.session and "password" in request.session:
        pick = ScheduleOrder.objects.all()
        return render(request,"ep/showpickupreq.html",{'pickup':pick})
    else:   
        return redirect('adminin')
def PickUpStatus(request,pk):
    if "email" in request.session and "password" in request.session:
        master = Master.objects.get(id=request.session['id'])
        pick = ScheduleOrder.objects.get(id=pk)
        plastic_id = PlasticC.objects.get(master_id=master)
        if request.POST['status'] == "Accepted":
            pick.pickup_status = request.POST['status']
            pick.save()
            email_subject = "Plastic Pickup Request Accepted"
            PickupAccept(email_subject,'mail_template',pick.cust_id.master_id.email,{'pcname':plastic_id.pc_name,'pccontact':plastic_id.pc_contact,'pickup_datetime':pick.sc_date_time,'pickup_details':pick.sc_comment})
            return HttpResponseRedirect(reverse('pickuprequests'))
        if request.POST['status'] == "Rejected":
            pick.pickup_status = "pending"
            pick.save()
            # PickupReject(email_subject,'mail_template',pick.cust_id.master_id.email,{'pcname':plastic_id.pc_name,'pccontact':plastic_id.pc_contact,'pickup_datetime':pick.sc_date_time,'pickup_details':pick.sc_comment})
            return HttpResponseRedirect(reverse('pickuprequests')) 
    else:   
        return redirect('adminin')

def AddData(request):
    if "email" in request.session and "password" in request.session:
        user = Master.objects.get(id=request.session['id'])
        if user.role == "PlasticCollector":
            customer_id = Customer.objects.get(id=request.POST['c_id'])
            plastic_id = PlasticC.objects.get(master_id=user)
            total_collect = request.POST['totalcollect']
            use = request.POST['usage']
            waste = request.POST['wastage']
            date = request.POST['date_coll']
            newData = CustomerData.objects.create(cust_id=customer_id,plastic_id=plastic_id,total_collection=total_collect,usage=use,wastage=waste,collection_date=date)
            message = "Data Added!"
            return render(request,"ep/customer_data.html",{"cust":Customer.objects.all(),"msg":message})
    else:   
        return redirect('adminin')

def CustReport(request,pk):
    if "email" in request.session and "password" in request.session:
        user= Master.objects.get(id=pk)
        cust = Customer.objects.get(master_id=user)
        report=CustomerData.objects.all().filter(cust_id=cust)
        totalcollection = 0
        totalusage = 0
        totalwastage = 0
        count =0
        for c in enumerate(report): 
            count=count+1
            print(count)
        for i in report:
            totalcollection += i.total_collection
        for u in report:
            totalusage+=u.usage
        for w in report:
            totalwastage+=w.wastage
        return render(request,"ep/customer_report.html",{"report":report,"totalcollection":totalcollection,"count":count,"t_usage":totalusage,"t_waste":totalwastage})
    else:   
        return redirect('signin')
@csrf_exempt
def callback(request):
    if "email" in request.session and "password" in request.session:
        if request.method == 'POST':
            received_data = dict(request.POST)
            paytm_params = {}
            paytm_checksum = received_data['CHECKSUMHASH'][0]
            checkout = Order.objects.get(id=10)
            
            for key, value in received_data.items():
                if key == 'CHECKSUMHASH':
                    paytm_checksum = value[0]
                else:
                    paytm_params[key] = str(value[0])
            # Verify checksum
            is_valid_checksum = verify_checksum(paytm_params, settings.PAYTM_SECRET_KEY, str(paytm_checksum))
            if is_valid_checksum:
                received_data['message'] = "Checksum Matched"
                checkout.payment_status = 'ok'
                checkout.save()
            else:
                received_data['message'] = "Checksum Mismatched"
                checkout.payment_status = 'not ok'
                checkout.save()
                return render(request, 'ep/callback.html', context=received_data)
            return render(request, 'ep/callback.html', context=received_data)
    else:
        return redirect('signin')

def initiate_payment(request):
    udata = Master.objects.get(id=request.session['id'])
    if udata.role == "customer":
        if "email" in request.session and "password" in request.session:

            try:
                cdata = Master.objects.get(email=request.session['email'])
                amount = int(request.POST['total'])
                print("-------------------------------------------",amount)
                # user = authenticate(request, username=username, password=password)
            except:
                return render(request, 'ep/customer_cartcheckout.html')
            
            transaction = Transaction.objects.create(made_by=cdata, amount=amount)
            
            transaction.save()
            cid = request.POST['cid']
            cust_id  =Customer.objects.get(id=cid)
            print("CCCCCCCCCCID",cid)
            # pstatus = request.POST['paystatus']

            merchant_key = settings.PAYTM_SECRET_KEY

            params = (
                ('MID', settings.PAYTM_MERCHANT_ID),
                ('ORDER_ID', str(transaction.order_id)),
                ('CUST_ID', str(transaction.made_by.email)),
                ('TXN_AMOUNT', str(transaction.amount)),
                ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                ('WEBSITE', settings.PAYTM_WEBSITE),
                # ('EMAIL', request.user.email),
                # ('MOBILE_N0', '9911223388'),
                ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
                ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
                # ('PAYMENT_MODE_ONLY', 'NO'),
            )

            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)

            transaction.checksum = checksum
            transaction.save()

            paytm_params['CHECKSUMHASH'] = checksum
            #print('SENT: ', paytm_params['RESPCODE'])
            return render(request, 'ep/redirect.html', context=paytm_params)
        else:
            return redirect('signin')
    elif udata.role == "RecyclingCompany":
        if "email" in request.session and "password" in request.session:

            try:
                cdata = Master.objects.get(email=request.session['email'])
                amount = int(request.POST['total'])
                print("-------------------------------------------",amount)
                # user = authenticate(request, username=username, password=password)
            except:
                return render(request, 'ep/customer_cartcheckout.html')
            
            transaction = Transaction.objects.create(made_by=cdata, amount=amount)
            
            transaction.save()
            comp = request.POST['comp']
            comp_id  =Company.objects.get(id=comp)
            # pstatus = request.POST['paystatus']
            
            merchant_key = settings.PAYTM_SECRET_KEY

            params = (
                ('MID', settings.PAYTM_MERCHANT_ID),
                ('ORDER_ID', str(transaction.order_id)),
                ('CUST_ID', str(transaction.made_by.email)),
                ('TXN_AMOUNT', str(transaction.amount)),
                ('CHANNEL_ID', settings.PAYTM_CHANNEL_ID),
                ('WEBSITE', settings.PAYTM_WEBSITE),
                # ('EMAIL', request.user.email),
                # ('MOBILE_N0', '9911223388'),
                ('INDUSTRY_TYPE_ID', settings.PAYTM_INDUSTRY_TYPE_ID),
                ('CALLBACK_URL', 'http://127.0.0.1:8000/callback/'),
                # ('PAYMENT_MODE_ONLY', 'NO'),
            )
            paytm_params = dict(params)
            checksum = generate_checksum(paytm_params, merchant_key)

            transaction.checksum = checksum
            transaction.save()
       
            paytm_params['CHECKSUMHASH'] = checksum
            #print('SENT: ', paytm_params['RESPCODE'])
            return render(request, 'ep/redirect.html', context=paytm_params)
        else:
            return redirect('signin')


def Logout(request):
    if request.session['Role'] == "customer":
        del request.session['email'] 
        del request.session['password']   
        del request.session['id']  
        del request.session['Role']   
        del request.session['Firstname']  
        del request.session['Lastname']  
        del request.session['Gender']  
        del request.session['State']   
        return render(request,"ep/customer_signin.html")
    
    if request.session['Role'] == "RecyclingCompany":
        del request.session['email']  
        del request.session['password']  
        del request.session['id']  
        del request.session['Role']   
        del request.session['Cname']  
        del request.session['Cadd']  
        del request.session['Ccon']  
        del request.session['Cfb']   
        del request.session['Cins']   
        del request.session['Clin']   
        del request.session['Ctwit']  
        del request.session['Cweb']  
        del request.session['Ofname'] 
        del request.session['Olname']    
        del request.session['Ogen'] 
        del request.session['Ocon']  
        del request.session['Oemail']
        return render(request,"ep/admin_signin.html")

    if request.session['Role'] == "PlasticCollector":
        del request.session['email'] 
        del request.session['password']   
        del request.session['id']  
        del request.session['Role']   
        del request.session['Pcname']  
        del request.session['Pcadd']  
        del request.session['Pccon']  
        del request.session['Pcfb']   
        del request.session['Pcins']   
        del request.session['Pclin']   
        del request.session['Pctwit']  
        del request.session['Pcweb']  
        del request.session['Ofname'] 
        del request.session['Olname']    
        del request.session['Ogen'] 
        del request.session['Ocon']  
        del request.session['Oemail'] 
        return render(request,"ep/admin_signin.html")
