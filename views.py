from django.shortcuts import render  
import logging  
from django.conf import settings  
from .models import *  
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger ##导入  
  
# Get an instance of a logger  
logger = logging.getLogger(__name__)  
  
def global_setting(request):  
    return {'SITE_NAME': settings.SITE_NAME,  
            'WEIBO_SINA': settings.WEIBO_SINA}  
  
  
def index(request):  
    try:  
        categories = Cateory.objects.all()  
        articles = Article.objects.all()  
        paginator = Paginator(articles, 2) #分页  
        try:  
            page = int(request.GET.get('page', 1))  
            articles = paginator.page(page)  
        except PageNotAnInteger:  
            articles = paginator.page(1)  
        except EmptyPage:  
            articles = paginator.page(paginator.num_pages)  
  
    except Exception as e:  
        logger.error(e)  
    return render(request, 'index.html', locals())  
