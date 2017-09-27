from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^supervisor/$', views.supervisorProfile.as_view(), name='supevisorProfile'),
    url(r'^Gotostore/$', views.goToStore.as_view(), name='Gotostore'),
    url(r'^staff/$', views.staff.as_view(), name='viewStaff'),
    url(r'^sales/$', views.sales.as_view(), name='viewSales'),
    url(r'^notification/$', views.notification.as_view(), name='notification'),
]