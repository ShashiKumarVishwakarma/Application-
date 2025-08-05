from django.contrib import admin
from django.urls import path
from myapp import views  # replace 'myapp' with your app name

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('dashboard/<int:user_id>/', views.dashboard, name='dashboard'),
]
