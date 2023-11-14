from django.shortcuts import render, get_object_or_404
from .models import Article, Comment

def article_detail(request, article_id):
    article = get_object_or_404(Article, pk=article_id)
    comments = Comment.objects.filter(article=article)
    return render(request, 'bbs/article_detail.html', {'article': article, 'comments': comments})