from django.shortcuts import render, get_object_or_404
from .models import Articles

def index(request):
    articles = Articles.objects.all().order_by('-created_at')
    return render(request, 'articles/index.html', {'articles': articles})

def article(request, id):
    article = get_object_or_404(Articles, id=id)
    return render(request, 'articles/article.html', {'article': article})