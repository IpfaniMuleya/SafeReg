from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import modules, enroll

urlpatterns = [
    path('', views.home, name=""),
    path('register', views.register, name="register"),
    path('dashboard', views.dashboard, name="dashboard"),
    #path('modules', views.modules, name="modules"),
    path('modules', views.modules, name='modules'),
    path('enroll/<int:module_id>/', enroll, name='enroll'),
    path('user-logout', views.user_logout, name="user-logout"),
    path('account-locked', views.account_locked, name="account-locked"),
    
    # Pass management
    path('reset_password', auth_views.PasswordResetView.as_view(template_name="passManage/passwordReset.html"), name="reset_password"), #email pass reset
    path('reset_password_sent', auth_views.PasswordResetDoneView.as_view(template_name="passManage/passwordResetSent.html"), name="password_reset_done"), # Sucess eamil message
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="passManage/passwordResetForm.html"), name="password_reset_confirm"),# reset link
    path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(template_name="passManage/passwordResetComplete.html"), name="password_reset_complete"), # Success message
    
]
