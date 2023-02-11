from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('signup',views.signup,name="signup"),
    path('login',views.login_function,name="login"),
    path('logout',views.logout_function,name="logout"),
    path('waiting',views.waiting,name="waiting"),
    path('videocall',views.videocall,name="videocall"),
    path('video/<str:room>/<str:created>/',views.video,name='video')
]