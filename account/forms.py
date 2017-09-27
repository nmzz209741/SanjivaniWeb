from django import forms
from . import models
from .models import employee,medicine,user,amount,batchdata,bill,purchase

from account.models import user
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=30,label='Username')
    password = forms.CharField(widget=forms.PasswordInput())
    def clean(self, *args, **kwargs):
        username= self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        if username and password:
            user=models.user.authenticate(username=username, password=password)
            print('###########333')
            print(username, password)
            if not user:
                raise forms.ValidationError("Invalid Login Attempt")

        return super(UserLoginForm,self).clean(*args,**kwargs)


class employee_form(forms.ModelForm):

    class Meta:
        model = employee
        fields = ['first_name', 'last_name', 'Gender', 'role_id', 'address_city','address_district','salary', 'joined_date']

class user_add_form(forms.ModelForm):
    class Meta:
        model = user
        fields = ['username','password','user_id','created_date']

class medicine_form(forms.ModelForm):
    class Meta:
        model = medicine
        fields = '__all__'

class amount_form(forms.ModelForm):
    class Meta:
        model = amount
        fields = '__all__'

class batchdata_form(forms.ModelForm):
    class Meta:
        model = batchdata
        fields = '__all__'

class bill_form(forms.ModelForm):
    class Meta:
        model = bill
        fields = '__all__'


class purchase_form(forms.ModelForm):
    class Meta:
        model = purchase
        fields = '__all__'
