from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import article, topic, Comment
from django.http import Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import RegistrationForm, CommentForm, Search
# Create your views here.
def index(request):
    Data = { 'Book' : article.objects.filter(topic = 'book').order_by('-date')[:6],
    'Code': article.objects.filter(topic = 'code').order_by('-date')[:6],
    'Travel': article.objects.filter(topic = 'travel').order_by('-date')[:6],
    'Others': article.objects.filter(topic = 'others').order_by('-date')[:6],
    'newest' : article.objects.all().order_by('-date')[:5],
    'most': article.objects.all().order_by('-view')[:5],
    'new4' : article.objects.all().order_by('-date')[:4],
    }
    return render(request, 'index.html', Data)

def search(request, *args):
    if request.GET:
        keyword = request.GET['keyword']
        liststr = keyword.split(" ")
        result = article.objects.all()
        for i in liststr:
            result = result.filter(body__icontains=i).order_by('-date')
        form = Search
        newest = article.objects.all().order_by('-date')[:5]
        most = article.objects.all().order_by('-view')[:5]
        return render(request, 'search.html', {'form':form, 'result': result, 'newest': newest, 'most': most })
    form = Search
    newest = article.objects.all().order_by('-date')[:5]
    most = article.objects.all().order_by('-view')[:5]
    return render(request, 'search.html', {'form':form,'newest': newest, 'most': most })

def post(request, topic, slug):
    try:
        post = article.objects.get(slug = slug)
    except article.DoesNotExist:
        raise Http404("Bài viết không tồn tại")
    blog_post_slug = slug
    if not blog_post_slug in request.session:
        post.view += 1
        post.save()
        # Insert the slug into the session as the user has seen it
        request.session[blog_post_slug] = blog_post_slug
    articleList = article.objects.filter(topic = topic).order_by('-date')[:5]
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.path)
    newest = article.objects.all().order_by('-date')[:5]
    most = article.objects.all().order_by('-view')[:5]
    return render(request, 'article.html', {'article': post, 'form' : form, 'articleList': articleList,'newest': newest, 'most': most })

def topicview(request, topicname):
    try:
        topic1 = topic.objects.get(name = topicname)
    except topic.DoesNotExist:
        raise Http404("Chủ đề không tồn tại")
    Article = article.objects.filter(topic = topicname).order_by('-date')
    paginator = Paginator(Article, 3)
    pageNumber = request.GET.get('page')
    
    try:
        Article = paginator.page(pageNumber)
    except PageNotAnInteger:
        Article = paginator.page(1)
    except EmptyPage:
        Article = paginator.page(paginator.num_pages)
    newest = article.objects.all().order_by('-date')[:5]
    most = article.objects.all().order_by('-view')[:5]
    return render(request, 'topic.html', {'Article': Article, 'topic': topic1, 'newest': newest, 'most': most} )

def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
    return render(request, 'register.html', {'form': form})




