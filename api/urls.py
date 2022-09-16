from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from api import views


urlpatterns = [
    path('login', views.login),
    path('search_by_name',views.search_by_name),
    # path('contact_list',views.ContactList.as_view()),
    path('search_by_number',views.search_by_number),
    path('view_contact',views.view_contact),
    # path('register',views.register),
    path('register',views.Register.as_view())

]