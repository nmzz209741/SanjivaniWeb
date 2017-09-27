from django.shortcuts import render,redirect,HttpResponse
from django.views.generic import ListView,TemplateView
from account.models import medicine,batchdata,bill,amount,purchase,user
from account.forms import bill_form
from django.views.generic.edit import CreateView
import  datetime
import operator
from django.db.models import Q


class StaffLoginView(TemplateView):

    def get(self, request, **kwargs):
        return render(request,'stafflogin/staff_home.html', context=None)

class store(TemplateView):
    def get(self, request, **kwargs):
        amt = amount.objects.all()
        query=request.GET.get("q")
        if query:
           amt=amt.filter(itemscode__in=medicine.objects.filter( itemsname__icontains=query)).distinct()|amt.filter(itemscode__in=medicine.objects.filter( itemscode__icontains=query)).distinct()
           query=""
        return render(request,'stafflogin/table.html', {'amt':amt})

class BillCreateView(CreateView):
    def create_new(request):
        if request.method == "POST":
            form = bill_form(request.POST)
            if form.is_valid():
                billformcontext=form
                form.save()
                amt = amount.objects.all()
                query = request.GET.get("q")
                if query:
                    amt = amt.filter(itemscode__in=medicine.objects.filter(itemsname__icontains=query)).distinct() | amt.filter(itemscode__in=medicine.objects.filter(itemscode__icontains=query)).distinct()
                    query=""
                return render(request,'stafflogin/billtable.html',{'form':billformcontext,'amt':amt})
        else:
            form = bill_form()

        return render(request, 'account/bill_form.html', {'form': form})

    def addToBill(request):
        query = request.GET.getlist("selectedmed")
        print(query)
        amt=amount.objects.all()
        # staffs=user.objects.all()
        error=amount.objects.all()
        amt=amt.filter(itemscode__in=medicine.objects.filter( itemscode__in=query)).distinct()
        print (amt)
        errorexp=error.filter(batchno__in=amt.filter(batchno__in=batchdata.objects.filter(expdate__lt=datetime.date.today())))
        errorquantity = error.filter(batchno__in=amt.filter(batchno__in=batchdata.objects.filter(stock__lt=1)))
        if (errorexp|errorquantity):
            return HttpResponse("Sorry the medicine is unavailable in the stock ... Please review the medicine list")
        return render(request,'stafflogin/prebill.html', {'amt':amt})

    def addToBill2(request):
        query=request.GET.getlist("query")
        purchaselist=[]
        header=['BILL NO','DATE',"PATIENT'S NAME","DISCOUNT SCHEME"]
        detail=[]
        print("query is::",query)
        s=bill.objects.last()
        print(s.billno)
        detail.append(s.billno+1)
        detail.append(datetime.date.today())
        detail.append(query[0])
        detail.append(query[1])
        p = bill(billno=s.billno+1,date=datetime.date.today(),patientsname=query[0],discount=query[1])
        print("billdata::",p)
        p.save()
        j=0
        for i in range(2,len(query),2):
            med=medicine.objects.filter(itemscode__icontains=query[i])
            updatebatch = batchdata.objects.filter(itemscode_id__in=med.filter(itemscode__icontains=query[i]))
            for update in updatebatch:
                x = update.stock
                print("here i am:::::::::::::::", x)
                update.stock = x - int(query[i + 1])
                update.save()
            # purchaselist=[]
            for items in med:
                purchaseslist=[]
                q=purchase(id=j+1,billno=p, medid=items,quantity=query[i+1])


                purchaseslist.append(query[i])
                purchaseslist.append(query[i+1])
                a=query[i+1]
                print ("the value of a ",a)
                r=amount.objects.filter(itemscode__in=med.filter(itemscode__icontains=query[i]))
                print("r isssss:::::::",r)
                for each in med:
                    b = each.itemsname
                    purchaseslist.append(b)
                for x in r:

                    y=x.sellprice
                    z= y * int(a)
                    print("Selling amount",z)
                    print ("Selling Price ",y)

                    # purchaselist.append(b)
                    purchaseslist.append(y)
                    purchaseslist.append(z)



                j=j+1
                q.save()
            purchaselist += [purchaseslist]
            print ("q is",q)
            # billobj=bill.objects.filter(billno__icontains=p)
            looptimes=range(0,len(purchaselist))
        retList=[]
        a=0

        for i in range(0,1000,5) :
            retlist=i



        return render(request, 'stafflogin/billlayout.html',
                      {'sup': detail, 'header': header, 'purchaselist': purchaselist,
                       'looptimes': looptimes})

    def submit(request):
        return HttpResponse("done")









