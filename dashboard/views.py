"""
Views for dashboard app
"""
from django.utils import timezone
from django.urls import reverse_lazy, reverse
from django.utils.http import is_safe_url
from django.http import JsonResponse, HttpResponseRedirect
from django.views import View
from django.shortcuts import resolve_url
from django.contrib.sites.shortcuts import get_current_site
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from django.views.decorators.cache import never_cache
from django.views.generic import ListView, DetailView, TemplateView
from django.views.generic.edit import CreateView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout, REDIRECT_FIELD_NAME
from django.contrib.auth.views import (
    PasswordResetView, PasswordResetDoneView, PasswordResetCompleteView,
    PasswordResetConfirmView, LoginView
)

# local imports
from .models import User
from .forms import (
    RegisterForm, LoginForm, ProfileForm,
    PasswordResetEmailForm
)


class Home(TemplateView):
    """To display landing(home) page for website
    """
    template_name = "home.html"


class RegisterView(CreateView):
    """create new account for user
    """
    template_name = "authentication/register.html"
    form_class = RegisterForm

    def get_success_url(self):
        return reverse_lazy("dashboard:thank_you")

    def dispatch(self, request, *args, **kwargs):
        """If your already logged In Redirect To Dashboard
        """
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse("dashboard:home"))
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = User.objects.create_user(
            email=form.cleaned_data.get('email'),
            password=form.cleaned_data.get('password'),
            first_name=form.cleaned_data.get('first_name'),
            last_name=form.cleaned_data.get('last_name'),
            date_of_birth=form.cleaned_data.get('date_of_birth')
        )
        # ToDo: Do not activate user directly. impliment email confirmation by sending emails.
        user.is_active = True
        user.save()
        if self.request.is_ajax():
            data = {'success_url': str(self.get_success_url()), 'error': False}
            return JsonResponse(data)
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        response = super(RegisterView, self).form_invalid(form)
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return response


class RegistrationSuccess(TemplateView):
    """Registration thank you template
    """
    template_name = "authentication/thank_you.html"


class LogInView(LoginView):
    """Login user
    """
    template_name = "authentication/login.html"
    form_class = LoginForm
    success_url = reverse_lazy("dashboard:dashboard")

    def get_success_url(self):
        return reverse_lazy("dashboard:dashboard")

    def form_valid(self, form):
        """Security check complete. Log the user in."""
        login(self.request, form.get_user())
        print('self.get_success_url()', self.get_success_url())
        if self.request.is_ajax():
            return JsonResponse({'error': False, 'success_url': self.get_success_url()})
        return HttpResponseRedirect(self.get_success_url())


    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return super(LogInView, self).form_invalid(form)


class DashboardView(LoginRequiredMixin, TemplateView):
    """Landing page after user logIn are register
    """
    template_name = "user_dashboard/dashboard.html"


class LogOutView(View):
    """Logout User and redirect to site home page
    """
    def get(self, request):
        logout(request)
        return HttpResponseRedirect(reverse("dashboard:home_page"))


class ProfileEdit(LoginRequiredMixin, UpdateView):
    form_class = ProfileForm
    template_name = "user_dashboard/profile_edit.html"

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        return reverse_lazy("dashboard:dashboard")

    def form_invalid(self, form):
        if self.request.is_ajax():
            return JsonResponse({'error': True, 'errors': form.errors})
        return super(ProfileEdit, self).form_invalid(form)

    def form_valid(self, form):
        form.save()
        if self.request.is_ajax():
            data = {'error': False, 'success_url': 3(self.get_success_url())}
            return JsonResponse(data)
        return HttpResponseRedirect(self.get_success_url())

class ForgotPassword(PasswordResetView):
    """form with email field to get reset password link
    """
    template_name = 'authentication/password_reset.html'
    form_class = PasswordResetEmailForm
    success_url = reverse_lazy('dashboard:password_reset_done')
    email_template_name = 'authentication/password_reset_email.html'


class PasswordResetSuccessView(PasswordResetDoneView):
    """confirmation to sent email with reset link
    """
    template_name = 'authentication/password_reset_done.html'
    title = 'Password reset email sent!'
    success_url = reverse_lazy('dashboard:password_reset_done')


class PasswordResetConfirmationEmail(PasswordResetConfirmView):
    """form with new password and confirm password to set new passeord
    """
    template_name = 'authentication/password_reset_confirm.html'
    success_url = reverse_lazy('dashboard:password_reset_complete')


class PasswordResetCompleteView(PasswordResetCompleteView):
    """after succeesfully change of password
    """
    template_name = 'authentication/password_reset_complete.html'
    title = 'Password reset complete'