from django.db import models
from django.shortcuts import render
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.core.urlresolvers import reverse
import re
class employeeCategory(models.Model):
    HEIRARCHY=(
        (0,'ADMIN'),
        (1,'SUPER'),
        (2,'STAFF'),
    )
    type=models.CharField(max_length=30)
    number_of_employee = models.IntegerField()
    heirarchy = models.IntegerField(choices=HEIRARCHY)
    def __str__(self):
        return self.type

class employee(models.Model):
    GEND_CHOICES=(
	("Male", ("Male")),
	("Female", ("Female"))
	)
    first_name=models.CharField(max_length=30)
    last_name=models.CharField(max_length=30)
    address_city=models.CharField(max_length=30)
    address_district=models.CharField(max_length=30)
    # contact=PhoneNumberField()
    salary=models.IntegerField()
    role_id=models.ForeignKey(employeeCategory,on_delete=models.CASCADE)
    Gender=models.CharField(max_length=10,choices=GEND_CHOICES)
    joined_date=models.DateField()

    def __str__(self):
        return self.first_name +" "+self.last_name+self.address_city+self.address_district+str(self.salary)+str(self.role_id)+self.Gender+str(self.joined_date)
    # def get_absolute_url(self):
    #     return reverse('supervisorlogin:Staffs',kwargs={'pk':self.pk})
class user(models.Model):
    user_id=models.OneToOneField(employee,on_delete=models.CASCADE,primary_key=True)
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=30)
    created_date=models.DateField()


    def __str__(self):
        return str(self.username)

    def authenticate(password, username):
        try:
             print(" authentication............")
             print(username,password)
             o=user.objects.get(username=username, password=password)
             print(o.user_id.role_id.type)
             return {'status':True, 'employeeCategory':o.user_id.role_id.type}
        except:
             return False

    def logout(request,form):
        print("preceeding to logout")
        if request.session.has_key('employeeCategory'):
            del request.session['employeeCategory']
            request.session.modified = True
            print("logged out",request)
        return render(request, 'account/login.html')
class medicine(models.Model):
    itemscode=models.CharField(max_length=10,primary_key=True)
    itemsname=models.CharField(max_length=50)
    categoryname=models.CharField(max_length=40)
    locationname=models.CharField(max_length=20)
    reorderlimit=models.IntegerField()
    maxlimit=models.IntegerField()
    def __str__(self):
        return self.itemscode+" "+self.itemsname+" "+self.categoryname+" "+self.locationname+" "+str(self.reorderlimit)+" "+str(self.maxlimit)

class batchdata(models.Model):
    batchno=models.IntegerField(primary_key=True)
    itemscode_id=models.ForeignKey(medicine,on_delete=models.CASCADE)
    expdate= models.CharField(
        max_length=8,default='2017/09',
        # if you want that field to be mandatory
        validators=[
            RegexValidator(
                regex='((20)(1([2-9])|([2-9])([0-9])))/((0[1-9])|(1[0-2]))',
                message='Date doesnt comply',
            ),
        ]
    )
    stock=models.CharField(max_length=10)
    def __str__(self):
        return str(self.batchno)+" "+str(self.itemscode_id)+" "+str(self.expdate) +" " +str(self.stock)

class amount(models.Model):
    batchno=models.ForeignKey(batchdata,on_delete=models.CASCADE,primary_key=True)
    itemscode=models.ForeignKey(medicine,on_delete=models.CASCADE)
    costprice=models.FloatField()
    sellprice=models.FloatField()
    def __str__(self):
        return str(self.batchno)+", "+str(self.itemscode)+", "+str(self.costprice)+", "+str(self.sellprice)


class bill(models.Model):
    billno = models.IntegerField(primary_key=True)
    date = models.DateTimeField()
    patientsname = models.CharField(max_length=30)
    discount = models.FloatField()
    staffid = models.ForeignKey(user, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.billno) + str(self.date)

class purchase(models.Model):
    id=models.IntegerField(primary_key=True)
    billno = models.ForeignKey(bill,on_delete=models.CASCADE)
    medid = models.ForeignKey(medicine, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    def __str__(self):
        return str(id)


