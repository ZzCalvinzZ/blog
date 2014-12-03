from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
import calendar, datetime
# from django.http import HttpResponse

def index(request) :
  """The blog index"""

  # return HttpResponse('django 1.7 on Openshift') 
  return render(request, 'blog/base.html')
