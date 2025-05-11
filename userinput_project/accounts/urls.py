from django.urls import path
from . import views

urlpatterns = [
    path("",views.home, name = 'home'),
    path("form-view",views.form_view, name = 'form_view'),
    path("function-view",views.function_view, name = 'function_view'),
    path("class-view",views.ClassBasedView.as_view(), name = 'class_view'),
    path("generic-view",views.GenericCreateVies.as_view(), name = 'generic_view'),
    path('users/',views.user_list,name='user_list'),
    
    
]