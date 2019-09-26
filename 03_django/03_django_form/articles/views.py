from IPython import embed
from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.views.decorators.http import require_POST
from .models import Article, Comment
from .forms import ArticleForm, CommentForm

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
    comments = article.comment_set.all() # article 의 모든 댓글
    comment_form = CommentForm() # 댓글 폼
    context = {'article': article, 'comment_form': comment_form, 'comments': comments,}
    return render(request, 'articles/detail.html', context)


@require_POST
def delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    article.delete()
    return redirect('articles:index')


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


@require_POST
def comments_create(request, article_pk):
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        # 객체를 Create 하지만, db 에 레코드는 작성하지 않는다.
        comment =  comment_form.save(commit=False)
        comment.article_id = article_pk
        comment.save()
    return redirect('articles:detail', article_pk)


@require_POST
def comments_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    comment.delete()
    return redirect('articles:detail', article_pk)