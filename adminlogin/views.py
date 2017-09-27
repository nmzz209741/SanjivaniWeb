from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,TemplateView
from django.contrib.auth.models import User as authuser
from account.models import medicine,batchdata,amount,employee,employeeCategory,user
# from adminlogin.models import viewstore_admin
import operator
from django.db.models import Q

class AdminLoginView(TemplateView):

    def get(self, request, **kwargs):

        render(request,'adminlogin/admin_home.html', {"username":username})
        if (request.GET.get('logout')):
            return render_to_response('account/login.html')

class supervisorProfile(TemplateView):
    def get(self, request, **kwargs):
        sup = employee.objects.filter(role_id__in=employeeCategory.objects.filter(type='supervisor')).distinct()

        username_sup = user.objects.filter(user_id__in=employee.objects.filter(role_id__in=employeeCategory.objects.filter(type='supervisor'))).distinct()
        password_sup = user.objects.filter(user_id__in=employee.objects.filter(role_id__in=employeeCategory.objects.filter(type='supervisor'))).distinct()
        render(request, 'adminlogin/user.html',{"sup": sup, "username_sup": username_sup, "password_sup": password_sup})

        fname = request.GET.get("fn")
        lname = request.GET.get("ln")
        acity = request.GET.get("ac")
        adist = request.GET.get("ad")
        salary = request.GET.get("sal")
        gend = request.GET.get("gn")
        uname = request.GET.get("un")
        psw = request.GET.get("ps")
        cpsw = request.GET.get("ps1")

        if (fname!=None):
            for items in sup:
                items.first_name = fname
                items.save()

        if (lname!=None):
            for items in sup:
                items.last_name = lname
                items.save()

        if (acity != None):
            for items in sup:
                items.address_city = acity
                items.save()

        if (adist != None):
            for items in sup:
                items.address_district = adist
                items.save()

        if (salary != None):
            for items in sup:
                items.salary = salary
                items.save()

        if (gend != None):
            for items in sup:
                items.Gender = gend
                items.save()

        if (uname != None):
            for items in username_sup:

                u = authuser.objects.get(username=items.username)

                u.username = uname
                u.save()
                items.username = uname
                items.save()

        if (psw != None and cpsw!=None and psw==cpsw):
            for items in password_sup:
                u = authuser.objects.get(username=items.username)
                u.set_password(psw)
                u.save()
                items.password = psw
                items.save()


        return render(request,'adminlogin/user.html',{"sup":sup,"username_sup":username_sup,"password_sup":password_sup})
    # def check(self,request,**kwargs):


class goToStore(TemplateView):
    def get(self, request, **kwargs):
        amt = amount.objects.all()
        query=request.GET.get("q")
        if query:
           amt=amt.filter(itemscode__in=medicine.objects.filter( itemsname__icontains=query)).distinct()|amt.filter(itemscode__in=medicine.objects.filter( itemscode__icontains=query)).distinct()
        return render(request,'adminlogin/table.html', {'amt':amt})

class staff(TemplateView):
    def get(self, request, **kwargs):
        stf = employee.objects.filter(role_id__in=employeeCategory.objects.filter(type='staff')).distinct()
        query = request.GET.get("q")
        if query:
            stf=stf.filter(first_name__icontains=query)|stf.filter(last_name__icontains=query)
        return render(request,'adminlogin/staffs.html', {'stf':stf})

class sales(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'adminlogin/sales.html', context=None)

class notification(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'notifications.html', context=None)

