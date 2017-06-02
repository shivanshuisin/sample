from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.core.files.storage import FileSystemStorage

from .models import *
import hashlib
from django.views import generic


def EditEmp(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    return render(request, 'final/edit_dept.html')





class IndexViewUM(generic.ListView):
    template_name = 'final/edit_deptm.html'
    context_object_name = 'userm'

    def get_queryset(self):
        return User.objects.filter(department='managerial')

class IndexViewUT(generic.ListView):

    template_name = 'final/edit_depttech.html'
    context_object_name = 'userm'

    def get_queryset(self):
        return User.objects.filter(department='technical')

class IndexViewUC(generic.ListView):
    template_name = 'final/edit_deptc.html'
    context_object_name = 'userm'

    def get_queryset(self):
        return User.objects.filter(department='clerical')

class IndexViewPM(generic.ListView):
    template_name = 'final/editpayslipm.html'
    context_object_name = 'userm'

    def get_queryset(self):
        return User.objects.filter(department='managerial')

class IndexViewPC(generic.ListView):
    template_name = 'final/editpayslipc.html'
    context_object_name = 'userm'

    def get_queryset(self):
        return User.objects.filter(department='clerical')

class IndexViewPT(generic.ListView):
    template_name = 'final/editpaysliptech.html'
    context_object_name = 'userm'

    def get_queryset(self):
        return User.objects.filter(department='technical')

class DetailViewPM(generic.DetailView):
    model = User
    template_name = 'final/editpayslipuser.html'

def UserDeleteM(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    if request.method=='POST':
        id=int(request.POST["deleteid"])
        a=get_object_or_404(User,id=id)
        a.delete()
        try:
            b=get_object_or_404(Message,username=a.username)
            b.delete()
        except Exception as e:
            pass
        fs=FileSystemStorage()
        try:
            fs.delete(a.username + '_photo.jpg')
        except Exception as e:
            pass
        try:
            fs.delete(a.username+'_'+'oldest_payslip.pdf')
        except Exception as e:
            pass
        try:
            fs.delete(a.username+'_'+'previous_payslip.pdf')
        except Exception as e:
            pass
        try:
            fs.delete(a.username+'_'+'current_payslip.pdf')
        except Exception as e:
            pass

        return HttpResponseRedirect('/editempm/')

def EditPayslip(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    return render(request,'final/payslipdept.html')

def UpdateUser(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")

        HttpResponseRedirect('/login/')
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST['password']
        accesslevel = request.POST['accesslevel']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        department = request.POST['department']
        designation = request.POST['designation']
        gender = request.POST['gender']
        base_salary = request.POST['base_salary']
        bonus = request.POST['bonus']


        a=get_object_or_404(User,username=username)
        a.username=username
        if a.password!=password:
            a.password=hashlib.md5(password.encode('utf-8')).hexdigest()
        a.accesslevel=accesslevel
        a.f_name=f_name
        a.l_name=l_name
        a.department=department
        a.designation=designation
        a.gender=gender
        a.base_salary=base_salary
        a.bonus=bonus
        try:
            a.save()
            messages.add_message(request,messages.SUCCESS,"User Updated")
        except Exception as e:
            messages.add_message(request,messages.ERROR,"User Not Upadated")

        fs = FileSystemStorage()
        fs.save(username + '_photo.jpg', request.FILES["image"])
        return render(request,'final/updateuser.html',{'user':a})

def UserView(request):
    if request.session["login"] != "user":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    f=request.session["id"]

    u=get_object_or_404(User,username=f).__dict__
    return render(request, 'final/UserView.html', {'u': u})


# Create your views here.
def Authenticate(request):
    if request.method == "POST":
        if "username" in request.POST and "password" in request.POST:
            username = request.POST['username']
            password = request.POST['password']
            try:
                u = get_object_or_404(User, username=username)
            except Exception as e:
                messages.add_message(request,messages.ERROR,'User does not Exist')
                return HttpResponseRedirect("/login/")

            if(u.password == hashlib.md5(password.encode('utf-8')).hexdigest()):
                if u.accesslevel == 'admin':
                    request.session["login"] = "admin"
                    return HttpResponseRedirect('/admn/')
                else:
                    request.session["login"] = "user"
                    request.session["id"]=u.username
                    print(u.username)
                    return HttpResponseRedirect('/userview/')
            else:
                messages.add_message(request,messages.ERROR,'Wrong Password')
                return HttpResponseRedirect('/login/')





def SalaryMain(request):

    return render(request,'final/salary.html')


def Logout(request):
    request.session["login"] = ""
    messages.add_message(request,messages.SUCCESS,"Successfully Logged Out")
    return HttpResponseRedirect('/login/')


def UserStore(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        HttpResponseRedirect('/login/')
    if request.method == "POST":
        username = request.POST['username']
        password = hashlib.md5(request.POST['password'].encode('utf-8')).hexdigest()
        accesslevel = request.POST['accesslevel']
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        department = request.POST['department']
        designation = request.POST['designation']
        gender = request.POST['gender']
        base_salary = request.POST['base_salary']
        bonus = request.POST['bonus']


        reg = User(username=username,
                   password=password,
                   accesslevel=accesslevel,
                   f_name=f_name,
                   l_name=l_name,
                   department=department,
                   designation=designation,
                   base_salary=int(base_salary),
                   gender=gender,
                   bonus=int(bonus),
                   )
        fs=FileSystemStorage()
        fs.save(username+'_photo.jpg',request.FILES['image'])
        try:
            reg.save()
            messages.add_message(request, messages.SUCCESS, 'User Created')
            return render(request,'final/registeruser.html')


        except Exception as e:
            messages.add_message(request, messages.ERROR, 'User not  Created')
            return render(request, 'final/registeruser.html')



class DetailView(generic.DetailView):
    model = User
    template_name = 'final/updateuser.html'


def CreateUser(request):
    return render(request, 'final/registeruser.html')


def AdminView(request):
    if request.session["login"] != "admin":
        messages.add_message(request,messages.ERROR,'Please Login')
        return HttpResponseRedirect('/login/')

    return render(request, 'final/index.html')



def ManageEmp(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    else:
        return render(request, 'final/manage_emp.html')


def ManageSalary(request):
    if request.session["login"] != "admin":
        messages.add_message(request,messages.ERROR,"Please Login")
        return HttpResponseRedirect('/login/')
    return render(request, 'final/salary.html')

def UpdatePayslip(request):
    if request.session["login"] != "admin":
        messages.add_message(request,messages.ERROR,"Please Login")
        return HttpResponseRedirect('/login/')
    try:
        if request.method == "POST":
            username = request.POST['username']
            a=get_object_or_404(User,username=username)
            fs=FileSystemStorage()
            try:
                if request.FILES['oldest_month']!='':
                    if fs.exists(username+'_'+'oldest_payslip.pdf'):
                        fs.delete(username+'_'+'oldest_payslip.pdf')
                fs.save(username+'_'+'oldest_payslip.pdf',request.FILES['oldest_month'])
            except Exception as e:
                pass
            try:
                if request.FILES['previous_month']!='':
                    if fs.exists(username+'_'+'previous_payslip.pdf'):
                        fs.delete(username+'_'+'previous_payslip.pdf')
                fs.save(username+'_'+'previous_payslip.pdf',request.FILES['previous_month'])
            except Exception as e:
                pass
            try:
                if request.FILES['current_month']!='':
                    if fs.exists(username+'_'+'current_payslip.pdf'):
                        fs.delete(username+'_'+'current_payslip.pdf')
                fs.save(username+'_'+'current_payslip.pdf',request.FILES['current_month'])
            except Exception as e:
                pass
            messages.add_message(request, messages.SUCCESS, "Payslip Updated")
            return render(request,'final/editpayslipuser.html',{'user':a})
    except Exception as e:
        messages.add_message(request, messages.ERROR, "Payslip Not Updated")
        return render(request, 'final/editpayslipuser.html', {'user': a})

def MessageUser(request):
    if request.session["login"] != "user":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    if request.method=='POST':
        user=request.POST['username']
        a=get_object_or_404(User,username=user)
        return render(request,'final/messageuser.html',{'a':a})

def SendMessage(request):
    if request.session["login"] != "user":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    if request.method=='POST':
        user=request.POST["username"]
        message=request.POST["message"]
        reg=Message(username=user,message=message)
        reg.save()
        return HttpResponseRedirect('/userview/')

def AdminMessageView(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    user=Message.objects.all()
    return render(request,'final/messageviewadmin.html',{'messages':user})

def DeleteMessage(request):
    if request.session["login"] != "admin":
        messages.add_message(request,messages.ERROR,"Please Login")
        return HttpResponseRedirect('/login/')
    if request.method=='POST':
        msg=request.POST["message"]

        u=Message.objects.filter(message=msg)
        for a in u:
            a.delete()
    return HttpResponseRedirect('/adminmessageview/')

def HomeView(request):
    if request.session["login"] != "admin":
        messages.add_message(request, messages.ERROR, "Please Login")
        return HttpResponseRedirect('/login/')
    if request.session["login"]=="admin":
        return HttpResponseRedirect('/admn/')
    elif request.session["login"]=="user":
        return HttpResponseRedirect('/userview/')






