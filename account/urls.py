from django.conf.urls import url
from account import views
from adminlogin import views as v

app_name='supervisorlogin'
urlpatterns = [
    url( r'^$' , views.LoginPageView.login_view, name='index' ),
   	url(r'^login/$', views.LoginPageView.login_view, name='loginpage'),
    url(r'^logout/$', views.LoginPageView.logout_view, name='logout'),
    url(r'^adminlogin/$',v.AdminLoginView.as_view(), name='adminlogin'),
    url(r'^supervisorlogin/$', v.AdminLoginView.as_view(), name='supervisorlogin'),
    url(r'^stafflogin/$', v.AdminLoginView.as_view(), name='stafflogin'),
    url(r'^dashboard/$', views.dashboard.as_view(),name='dashboardview'),
    url(r'^notification/$', views.NotificationView.notify,name='notification'),
    url(r'^notification/outofstock/$', views.NotificationView.notifyOTS,name='notificationOTS'),
    url(r'^notification/expiry/$', views.NotificationView.notifyExp,name='notificationexp'),
]