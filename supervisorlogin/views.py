from django.shortcuts import render,redirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView,TemplateView,DetailView
from account.forms import employee_form,user_add_form,medicine_form,batchdata_form,amount_form
from account.models import medicine,batchdata,amount,employee,employeeCategory,user
from django.views.generic.edit import CreateView,UpdateView,DeleteView
import operator
from django.db.models import Q

class SupervisorLoginView(TemplateView):

    def get(self, request, **kwargs):
        render(request,'supervisionlogin/super_home.html',{"username":username})
        if (request.GET.get('logout')):
            return render_to_response('account/login.html')

class sales(TemplateView):
    def get(self, request, **kwargs):
        return render(request,'supervisorlogin/sales.html', context=None)
class StaffUpdateView(UpdateView):
    model = employee
    template_name = 'account/employee_form.html'
    fields = '__all__'
    success_url = reverse_lazy('Staffs')

    def get_context_data(self, **kwargs):
        context = super(StaffUpdateView, self).get_context_data(**kwargs)
        return context

    def get(self, request, *args, **kwargs):
        return super(StaffUpdateView, self).get(request, *args, **kwargs)


class StaffListView(ListView):
    model = employee
    template_name = 'supervisorlogin/staffs.html'
    def get_queryset(self):
        query = self.request.GET.get("q")
        print(query)
        stf = employee.objects.filter(role_id__in=employeeCategory.objects.filter(type='staff')).distinct()

        if query:
            return stf.filter(first_name__icontains=query) | stf.filter(last_name__icontains=query)
        return employee.objects.filter(role_id__in=employeeCategory.objects.filter(type='staff')).distinct()
class StaffDetailView(DetailView):
    model = employee

class staffCreateView(CreateView):
    def add_new(request):
        if request.method == "POST":
            form = employee_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('staff-userid-add')
        else:
            form = employee_form()
        return render(request, 'account/employee_form.html', {'form': form})
    def add_userid(request):
        if request.method == "POST":
            form = user_add_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('viewStaff')
        else:
            form = user_add_form()
        return render(request, 'account/employee_form.html', {'form': form})


class MedicineCreateView(CreateView):
    def add_new(request):
        if request.method == "POST":
            form = medicine_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('med-add-batch')
        else:
            form = medicine_form()
        return render(request, 'account/medicine_form.html', {'form': form})
    def add_new_batch(request):
        if request.method == "POST":
            form = batchdata_form(request.POST)
            if form.is_valid():
                form.save()
                return redirect('amount')
        else:
            form = batchdata_form()
        return render(request, 'account/medicine_form.html', {'form': form})
    def add_new_amount(request):
        if request.method == "POST":
            form = amount_form(request.POST)
            if form.is_valid():
                form.save()
                # print("batchdata saved!")
                return redirect('store')
        else:
            form = amount_form()
        return render(request, 'account/medicine_form.html', {'form': form})

class MedicineUpdateViewtable(TemplateView):
    def get(self, request, **kwargs):
        amt = amount.objects.all()
        query=request.GET.get("q")
        if query:
           amt=amt.filter(itemscode__in=medicine.objects.filter( itemsname__icontains=query)).distinct()|amt.filter(itemscode__in=medicine.objects.filter( itemscode__icontains=query)).distinct()
        return render(request,'supervisorlogin/updatetable.html', {'amt':amt})

class MedicineUpdateView(UpdateView):
    model = amount
    template_name = 'account/medicine_form.html'
    fields = '__all__'
    success_url = reverse_lazy('store')

    def get_context_data(self, **kwargs):
        context = super(MedicineUpdateView, self).get_context_data(**kwargs)
        context['medicine_form'] = medicine_form
        # context['batchdata_form']=batchdata_form()
        return context

    def get(self, request, *args, **kwargs):
        return super(MedicineUpdateView, self).get(request, *args, **kwargs)


class store(TemplateView):
    def get(self, request, **kwargs):
        amt = amount.objects.all()
        query=request.GET.get("q")
        if query:
           amt=amt.filter(itemscode__in=medicine.objects.filter( itemsname__icontains=query)).distinct()|amt.filter(itemscode__in=medicine.objects.filter( itemscode__icontains=query)).distinct()
        return render(request,'supervisorlogin/table.html', {'amt':amt})

class notification(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'notifications.html', context=None)
