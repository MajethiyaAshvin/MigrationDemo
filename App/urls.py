from django.conf.urls import url

from App import views

urlpatterns = [
    url("insert",views.insert,name="insert"),
    url("index", views.index, name="index")

]