from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^sales/$', views.sales.as_view(), name='viewSales'),
    url(r'^staff/$', views.StaffListView.as_view(), name='Staffs'),
    url(r'^staff/(?P<pk>\d+)$', views.StaffDetailView.as_view(), name='Staff-detail'),
    url(r'^staff/add/$', views.staffCreateView.add_new, name='staff-add'),

    url(r'^staff/add_userid/$', views.staffCreateView.add_userid, name='staff-userid-add'),
    url(r'^medicine/add/$', views.MedicineCreateView.add_new, name='med-add'),
    url(r'^medicine/add_batch/$', views.MedicineCreateView.add_new_batch, name='med-add-batch'),
    url(r'^medicine/add_amount/$', views.MedicineCreateView.add_new_amount, name='amount'),
    url(r'^staff/update/(?P<pk>\d+)$', views.StaffUpdateView.as_view(), name='update'),
    # url(r'^staff/update_userid/$', views.staffCreateView.add_userid, name='staff-userid-add'),
    url(r'^store/$', views.store.as_view(), name='store'),
    url(r'^medicine/update/$', views.MedicineUpdateViewtable.as_view(), name='med-update'),
    url(r'^medicine/update/(?P<pk>\d+)$', views.MedicineUpdateView.as_view(), name='med-update'),
    url(r'^notification/$', views.notification.as_view(), name='notification'),
    # url(r'^medsearchlist/$',views.medsearchlistview.as_view(),name='search')
]
