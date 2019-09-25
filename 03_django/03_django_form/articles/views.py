from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {'articles': articles,}
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        # -----------------필요없음--------------------
        # title = request.POST.get('title') django form을 이용할 경우 필요없다
        # content = request.POST.get('content')
        # article = Article(title=title, content=content)
        # article.save()
        # -----------------여기까지 필요 없음-----------------

        # Form Instance를 생성하고 요청에 의한 데이터를 인자로 받는다.(binding)
        # 이 처리과정은 binding이라고 불리며 유효성 체크를 할 수 있게 해준다.
        form = ArticleForm(request.POST)
        if form.is_valid(): # 유효성 검사
            article = form.save()
            return redirect(article)
    # 상황에 따라 context에 다른 form을 넘겨주어야 한다.
    # GET : 기본 form
    # POST : 검증에 실패 후의 form(is_valid = False일때)
    # POST로 들어왔을때 검증이 실패할 시, 경로를 잡아주기 위해 context와 return은 if와 else와 같은 선상에 작성.
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/form.html', context)


def detail(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    context = {'article': article,}
    return render(request, 'articles/detail.html', context)


def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        return redirect(article)


def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save()
            return redirect(article)
    else:
        form = ArticleForm(instance=article)
    context = {'form': form, 'article': article,}
    return render(request, 'articles/form.html', context)