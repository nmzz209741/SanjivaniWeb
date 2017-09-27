from django.conf.urls import url,include
from django.contrib import admin
from account import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('account.urls')),
    url(r'^account/',include('account.urls')),
    url(r'^notification/',include('account.urls')),
    url(r'^adminlogin/', include('adminlogin.urls')),
    url(r'^stafflogin/', include('stafflogin.urls')),
    url(r'^supervisorlogin/', include('supervisorlogin.urls')),

]
