from django.urls import path
from learapp import views
#Template tagging
app_name='learapp'
urlpatterns=[
    path('relative/', views.relative, name='relative'),
    path('other/', views.other, name='other'),
]
