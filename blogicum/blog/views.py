from django.shortcuts import render, get_object_or_404

from .models import Category
from .utils import get_published_posts_with_relations
from .constants import INDEX_POSTS_LIMIT


def index(request):
    post_list = get_published_posts_with_relations()[:INDEX_POSTS_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        get_published_posts_with_relations(),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    post_list = get_published_posts_with_relations().filter(
        category=category
    )

    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
