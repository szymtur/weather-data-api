from datetime import date

from django.db.models import Q
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.hashers import check_password
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.shortcuts import render, redirect
from django.views import View

from account_api.forms import RegisterForm, LoginForm, RemoveConfirmForm
from account_api.helpers import api_key_generator
from rest_api.models import ApiKeys, Throttling
from weather_api import settings


class HomeView(View):
    def get(self, request):
        logout(self.request)
        return render(self.request, 'home.html')


class LoginView(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return render(request, 'login.html', {'form': LoginForm()})

    def post(self, request):
        form = LoginForm(self.request.POST)
        if form.is_valid():
            login(self.request, form.cleaned_data['user_object'])
            return redirect('dashboard')
        return render(request, 'login.html', {'form': form})


class LogoutView(View):
    def get(self, request):
        context = {'info_message': 'you have been logged out'}
        return render(self.request, 'info.html', context=context)


class DashboardView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = ['auth.view_user', 'rest_api.view_apikeys', 'rest_api.change_apikeys']

    def get(self, request):
        api_key_object = ApiKeys.objects.get(user=self.request.user.id)
        throttling_object = Throttling.objects.filter(Q(api_key=api_key_object) & Q(date=date.today())).first()

        throttling_counter = 0

        if throttling_object:
            throttling_counter = throttling_object.counter

        context = {'users': self.request.user, 'api_key': api_key_object,
                   'remaining_limit': api_key_object.day_limit - throttling_counter}

        return render(self.request, 'dashboard.html', context=context)

    def post(self, request):
        ApiKeys.objects.filter(user_id=self.request.user.id).update(api_key=api_key_generator())
        return redirect('dashboard')


class RemoveUserView(LoginRequiredMixin, PermissionRequiredMixin, View):
    login_url = 'login'
    permission_required = ['auth.delete_user', 'rest_api.delete_apikeys']

    def get(self, request):
        return render(self.request, 'remove.html', {'form': RemoveConfirmForm()})

    def post(self, request):
        form = RemoveConfirmForm(self.request.POST)

        if check_password(request.POST.get('password'), request.user.password):
            form.set_is_correct_flag()

        if form.is_valid():
            User.objects.get(id=self.request.user.id).delete()
            context = {'info_message': 'account have been removed'}
            return render(request, 'info.html', context=context)
        return render(request, 'remove.html', {'form': form})


class SignupView(View):
    def get(self, request):
        if self.request.user.is_authenticated:
            return redirect('dashboard')
        return render(self.request, 'signup.html', {'form': RegisterForm()})

    def post(self, request):
        form = RegisterForm(self.request.POST)

        if form.is_valid():
            # creates new user
            user = User.objects.create_user(username=form.cleaned_data['username'].lower(),
                                            password=form.cleaned_data['pass_first'],
                                            email=form.cleaned_data['email'].lower())

            # generates api key for new user
            ApiKeys.objects.create(api_key=api_key_generator(),
                                   day_limit=settings.DEFAULT_API_KEY_LIMIT,
                                   key_name=settings.DEFAULT_API_KEY_NAME,
                                   user=user)

            # adds user do rest_api_users group
            Group.objects.get(name='rest_api_users').user_set.add(user)

            # authenticate and login new user
            user = authenticate(username=form.cleaned_data['username'].lower(),
                                password=form.cleaned_data['pass_first'])

            if user.is_active:
                login(self.request, user)
                return redirect('dashboard')
        else:
            return render(request, 'signup.html', {'form': form})
