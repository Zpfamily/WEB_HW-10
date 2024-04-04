from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import DetailView
from .models import Author, Tag, Quote
from django.views import View


from .utils import get_mongodb
PER_PAGE = 4

def main(request, page=1):
    db = get_mongodb()
    quotes = db.quotes.find()
    per_page = 10
    paginator = Paginator(list(quotes), per_page)
    quotes_on_page = paginator.page(page)
    return render(request, "quotes/index.html", context={'quotes': quotes_on_page})


def author(request, author: str):
    try:
        author = Author.objects.get(fullname=author)
    except:
        author = None
    context = {"author": author}
    return render(request, "quotes/author.html", context)


def tag(request, tag: str, page: int = 1):
    quotes = []
    tag_id = None
    try:
        tag_id = Tag.objects.get(name=tag).id
    except Tag.DoesNotExist:
        pass

    if tag_id:
        quotes = Quote.objects.filter(tags=tag_id).order_by('id')  # Assuming 'id' is the field you want to order by

    paginator = Paginator(quotes, per_page=PER_PAGE)
    context = {"quotes": paginator.page(page), "tag_query": tag}
    return render(request, "quotes/tag.html", context)
