from django.urls import path

from account_api.views import HomeView, LoginView, LogoutView, DashboardView, SignupView, RemoveUserView


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),
    path('account/login/', LoginView.as_view(), name='login'),
    path('account/logout/', LogoutView.as_view(), name='logout'),
    path('account/signup/', SignupView.as_view(), name='signup'),
    path('account/remove/', RemoveUserView.as_view(), name='remove'),
    path('account/dashboard/', DashboardView.as_view(), name='dashboard'),
]
