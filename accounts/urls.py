from django.contrib.auth.views import (
  LoginView, LogoutView,
  # PasswordChangeView, PasswordChangeDoneView,
  # PasswordResetView, PasswordResetDoneView,
  # PasswordResetConfirmView, PasswordResetCompleteView
)

from django.urls import path

from accounts import views

app_name = 'accounts'

urlpatterns = [
  path('signup/', views.signup, name='signup'),
  path('login/', views.LoginView.as_view(), name='login'),
  path('logout/', views.LogoutView.as_view(), name='logout'),
  path('', views.IndexView.as_view(), name='index'),

  # path('password_change/', PasswordChangeView.as_view(), name='password_change'),
  # path('password_change/done/', PasswordChangeDoneView.as_view(), name='password_change_done'),
  #
  # path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
  # path('password_reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
  #
  # path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
  # path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
  # path("login/<provider>", views.auth, name="begin"),
  # path("complete/<provider>", views.complete, name="complete"),
  # path("disconnect/<provider>", views.disconnect, name="disconnect"),
  # path("disconnect/<provider>/<int:association_id>", views.disconnect,
  #      name="disconnect_individual"),
]