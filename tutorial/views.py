from django.shortcuts import render
from django.views import generic
from .models import Tutorial

class IndexView(generic.ListView):
  template_name = 'tutorial/tutorial_list.html'
  model = Tutorial

  def get_queryset(self):
    return Tutorial.objects.order_by('-created_at')


