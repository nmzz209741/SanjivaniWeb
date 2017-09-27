from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^store/$', views.store.as_view(), name='store'),
    url(r'^createbill/$', views.BillCreateView.create_new, name='newbill'),
    url(r'^createbill/add_to_bill/$',views.BillCreateView.addToBill,name='add-to-bill'),
    url(r'^createbill/add_to_bill2/$',views.BillCreateView.addToBill2,name='add-to-bill2'),
    # url(r'^createbill/add_to_bill2/submit/$', views.BillCreateView.submit, name='submit'),

    # url(r'^notification/$', views.notification.as_view(), name='notification'),

]

# url(r'^notification/$', views.notification.as_view(), name='notification'),