from django.urls import  path
from . import views# . means your current package

urlpatterns=[
    path ('',views.index(),name='index')
]