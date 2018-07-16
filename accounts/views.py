from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .forms import UserCreateForm

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import (
  LoginView, LogoutView
)
from django.views import generic
from .forms import LoginForm

class IndexView(generic.TemplateView):
  template_name = 'accounts/index.html'


def signup(request):
  """ユーザ作成ページへ"""

  user_form = UserCreateForm(request.POST or None)

  if request.method == "POST" and user_form.is_valid():
    user = user_form.save(commit=False)
    user.save()
    return redirect('accounts:login')

  context = {
    "user_form": user_form,
  }
  return render(request, 'accounts/signup.html', context)

class LoginView(LoginView):
  """ログインページ"""
  form_class = LoginForm
  template_name = 'accounts/login.html'


class LogoutView(LoginRequiredMixin, LogoutView):
  """ログアウトページ"""
  template_name = 'tutorial/tutorial_list.html'
