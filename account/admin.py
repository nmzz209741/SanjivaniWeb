from django.contrib import admin
from .models import employee, user, amount,employeeCategory,medicine,batchdata,bill,purchase

admin.site.register(employeeCategory)
admin.site.register(employee)
admin.site.register(user)
admin.site.register(medicine)
admin.site.register(batchdata)
admin.site.register(amount)
admin.site.register(bill)
admin.site.register(purchase)