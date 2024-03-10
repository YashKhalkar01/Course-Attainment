
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from home import views
urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('user_logout', views.user_logout, name='user_logout'),
    path('user_login', views.user_login, name='user_login'),
    path('user_signup', views.user_signup, name='user_signup'),
    path('change_password', views.change_password, name='change_password'),
    path('forgot_password', views.forgot_password ,name="forgot_password"),
    path('email_sent', views.email_sent ,name="email_sent"),
    
    path('home', views.home, name='home'),
    path('excel', views.excel, name='excel'),   
    path('remove', views.remove, name='remove'),
    path('setCourceOutcome', views.setCourceOutcome, name='setCourceOutcome'),
    path('setPaper', views.setPaper, name='setPaper'),
    path('displayPaper', views.displayPaper, name='displayPaper'),
    path('insertMarks', views.insertMarks, name='insertMarks'),
    path('updateMarks', views.updateMarks, name='updateMarks'),
    path('student', views.student, name='student'),


    # path('forgot_password', auth_views.PasswordResetView.as_view() ,name="reset_password"),
    # path('forgot_password-sent', auth_views.PasswordResetDoneView.as_view() ,name="password_reset_done"),
    # path('forgot/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view() ,name="password_reset_confirm"),
    # path('forgot_password_complete', auth_views.PasswordResetCompleteView.as_view() ,name="password_reset_complete"),
        

    


]
