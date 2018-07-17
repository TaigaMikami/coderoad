from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
  """カテゴリ"""
  name = models.CharField('カテゴリ名', max_length=255)
  created_at = models.DateTimeField('作成日', default=timezone.now)
  
  def __str__(self):
    return self.name
  
class Tutorial(models.Model):
  """チュートリアル"""
  title = models.CharField('タイトル', max_length=255)
  url = models.URLField('URL')
  description = models.TextField('内容', blank=True)
  star = models.IntegerField('スター', blank=True)
  created_at = models.DateTimeField('作成日', default=timezone.now)
  category = models.ManyToManyField(
    Category, verbose_name='カテゴリ',
  )
  user = models.ManyToManyField(
    User, verbose_name='カテゴリ',
  )

  def __str__(self):
    return self.title

class Comment(models.Model):
  '''チュートリアルに対するコメント'''
  text = models.TextField('本文')
  user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post_user', blank=True, null=True)
  tutorial = models.ForeignKey(Tutorial, verbose_name='紐づく記事', on_delete=models.PROTECT)
  created_at = models.DateField('作成日', default=timezone.now)
  
  def __str__(self):
    return self.text[:10]
  
