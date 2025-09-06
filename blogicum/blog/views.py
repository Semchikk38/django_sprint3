from django.shortcuts import render, get_object_or_404

from .models import Category
from .services import filter_posts_by_publication
from .constants import INDEX_POSTS_LIMIT


def index(request):
    post_list = filter_posts_by_publication()[:INDEX_POSTS_LIMIT]
    return render(request, 'blog/index.html', {'post_list': post_list})


def post_detail(request, post_id):
    post = get_object_or_404(
        filter_posts_by_publication(),
        id=post_id
    )
    return render(request, 'blog/detail.html', {'post': post})


def category_posts(request, category_slug):
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True
    )

    category_posts = category.posts.all()
    post_list = filter_posts_by_publication(category_posts)

    return render(
        request,
        'blog/category.html',
        {'category': category, 'post_list': post_list}
    )
