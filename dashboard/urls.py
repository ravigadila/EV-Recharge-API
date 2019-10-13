from django.conf.urls import url, include
from . import views


urlpatterns = [
    url(r'^$', views.Home.as_view(), name="home_page"),
    url(r'^register/$', views.RegisterView.as_view(), name="register"),
    url(r'^thank-you/$', views.RegistrationSuccess.as_view(), name="thank_you"),
    url(r'^login/$', views.LogInView.as_view(), name="login"),
    url(r'^dashboard/$', views.DashboardView.as_view(), name="dashboard"),
    url(r'^logout/$', views.LogOutView.as_view(), name="logout"),
    url(r'^profile-edit/$', views.ProfileEdit.as_view(), name="profile_edit"),
    url(r'^password-reset/$', views.ForgotPassword.as_view(), name="password_reset"),
    url(r'^password-reset-complete/$', views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
    url(r'^password-reset/done/$', views.PasswordResetSuccessView.as_view(), name="password_reset_done"),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$', views.PasswordResetConfirmationEmail.as_view(), name="password_reset_confirm"),
]