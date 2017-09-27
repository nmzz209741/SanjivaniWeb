from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from .models import amount,medicine,batchdata
import operator
from django.db.models import Q
from . import models
from . import forms
import datetime
from dateutil.relativedelta import relativedelta
from django.db.models import F
def check_session(request):
    print("in check_session")
    if request.session['employeeCategory'] == "admin":
        print('in admin')
        return render(request, 'adminlogin/admin_home.html', context=None)
    elif request.session['employeeCategory'] == "supervisor":
        print("in supervisor")
        return render(request, 'super_home.html', context=None)
    elif request.session['employeeCategory'] == "staff":
        return render(request, 'staff_home.html', context=None)
    else:
        print('Error in user profile')

    pass


from django.contrib.auth.models import User


class index(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'account/login.html', context=None)


class dashboard(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'dashboard.html', context=None)


class LoginPageView(TemplateView):
    def login_view(request):
        next = request.GET.get('next')
        render(request, 'account/login.html', context=None)
        if 'employeeCategory' in request.session:
            print(request.session['employeeCategory'])
            obj = check_session(request)
            return obj
        # print(request.user.is_authenticated())

        title = "Login"
        form = forms.UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get('password')
            user = models.user.authenticate(username=username, password=password)
            print("authenticated..........")
            print(user)
            if (user):
                request.session['employeeCategory'] = user['employeeCategory']
                request.session.modified = True
                obj = check_session(request)
                return obj
            if next:
                return redirect(next)
            return redirect("/")
            # redirect
        else:
            models.user.logout(request, forms.UserLoginForm)
        return render(request, 'account/login.html', {"form": form, "title": title})

    def logout_view(request):
        models.user.logout(request, forms.UserLoginForm)
        form = forms.UserLoginForm(request.POST or None)
        return redirect("/")


class NotificationView(TemplateView):
    def notify(request):
        return render(request, 'notifications.html')
    def notifyOTS(request):
        message="Medicines whose quantity is less than 10 in stock"

        amt = amount.objects.filter(batchno_id__in=batchdata.objects.filter(stock__lt=10)).distinct()
        return render(request, 'outofstock.html',{'amt':amt,'message':message})
    def notifyExp(request):
        message = "Medicines whose Expiry Date is less than 2 month from today in stock"
        d = datetime.date.today() + relativedelta(months=2)
        d=str(d.year)+"/"+str(d.month)
        amt =amount.objects.filter(batchno_id__in=batchdata.objects.filter(expdate__lt=d)).distinct()
        return render(request, 'outofstock.html',{'amt':amt,'message':message})