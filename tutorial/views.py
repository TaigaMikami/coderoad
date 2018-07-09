from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from django.views import generic
from .models import Tutorial, Category

class IndexView(generic.ListView):
  template_name = 'tutorial/tutorial_list.html'
  model = Tutorial

  def get_queryset(self):
    queryset = Tutorial.objects.order_by('-created_at') # 新しい順
    keyword = self.request.GET.get('keyword')
    if keyword:
      queryset = queryset.filter(
        Q(name__icontains=keyword) | Q(description__icontains=keyword)
      )
    return queryset

class CategoryView(generic.ListView):
  model = Tutorial

  def get_queryset(self):
    """ カテゴリ絞り込み
    category = get_object_or_404(Category, pk=self.kwargs['pk'])
    queryset = Tutorial.objects.order_by('-created_at').filter(category=category)
    """
    category_pk = self.kwargs['pk']
    queryset = Tutorial.objects.order_by('-created_at').filter(category__pk=category_pk)
    return queryset


class DetailView(generic.DetailView):
  model = Tutorial
