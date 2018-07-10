from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from django.views import generic
from .forms import CommentCreateForm
from django import forms
from .models import Tutorial, Category, Comment

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


class DetailAndCreate(generic.edit.ModelFormMixin, generic.DetailView):
  model = Tutorial
  form_class = CommentCreateForm
  template_name = 'tutorial/tutorial_detail_and_comment_create.html'

  def form_valid(self, form):
    tutorial_pk = self.kwargs['pk']
    comment = form.save(commit=False)
    comment.post = get_object_or_404(Tutorial, pk=tutorial_pk)
    comment.tutorial_id = tutorial_pk
    comment.save()
    return redirect('tutorial:detail_and_create', pk=tutorial_pk)

  def post(self, request, *args, **kwargs):
    form = self.get_form()
    if form.is_valid():
      return self.form_valid(form)
    else:
      self.object = self.get_object()
      return self.form_invalid(form)
