import logging
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post

logger = logging.getLogger('blog')

def blog_list(request):
    posts = Post.objects.filter(is_published=True)

    paginator = Paginator(posts, 6)  # Show 6 posts per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    logger.info(f"Blog list viewed - page {page_number or 1}")
    return render(request, 'blog/blog_list.html', {'page_obj': page_obj})

def blog_detail(request, slug):
    post = get_object_or_404(Post, slug=slug, is_published=True)
    related = Post.objects.filter(
        is_published=True,
        category=post.category
    ).exclude(id=post.id)[:3]

    logger.info(f"Blog post viewed: {post.title}")
    context = {
        'post': post,
        'related': related,
    }
    return render(request, 'blog/blog_detail.html', context)