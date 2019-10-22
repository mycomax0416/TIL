from django.shortcuts import render
from .models import Article
from .forms import ArticleForm

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


def create(request):
    if request.method == 'POST':
        pass
    else:
        form = ArticleForm()
    context = {'form': form,}
    return render(request, 'articles/create.html', context)