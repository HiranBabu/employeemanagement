from django.urls import path
from employee import views
urlpatterns=[

   # path('index',views.index),
   #  path('signup',views.registration),
   #  path('log',views.login)
    path("index",views.Loginview.as_view()),
    path("register",views.registrationview.as_view())
]