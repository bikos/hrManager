from django.conf.urls import include, url
from django.contrib import admin

from hrTransaction import views

urlpatterns = [
    # Examples:
    url(r'^$', views.post_list, name='home'),
    url(r'^admin/', include(admin.site.urls), ),
    url(r'^logout/$', views.post_list, name='home'),

]
