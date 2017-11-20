from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *



# render index for blog
def Main(request):
    state = Blog.objects.all().order_by('-date')
    return render(request,'blog.html',{'state':state})




def StateF(request,sid):
    state = Blog.objects.get(id=sid)
    return render(request,'blog-state.html',{'state':state,'keywords_seo':state.meta_keywords,'title_seo':state.meta_title,'description_seo':state.meta_description})
