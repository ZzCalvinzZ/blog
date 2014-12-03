from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from blog.models import Category, Article
import calendar, datetime
from django.http import HttpResponse

def index(request) :
  """The news index"""

  return HttpResponse('django 1.7 on Openshift') 
   #  archive_dates = Article.objects.dates('date_publish','month', order='DESC')
   #  categories = Category.objects.all()

   #  page = request.GET.get('page')
   #  article_queryset = Article.objects.all()
   #  paginator = Paginator(article_queryset, 5)

   # try:
   #      articles = paginator.page(page)
   #  except PageNotAnInteger:
   #      # If page is not an integer, deliver first page.
   #      articles = paginator.page(1)
   #  except EmptyPage:
   #      # If page is out of range (e.g. 9999), deliver last page of results.
   #      articles = paginator.page(paginator.num_pages)

    # return render(
    #     request,
    #     "blog/article/index.html",
    #     {
    #         "articles" : articles,
    #         "archive_dates" : archive_dates,
    #         "categories" : categories
    #     }
    # )
