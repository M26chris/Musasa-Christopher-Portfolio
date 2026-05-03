from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from projects.models import Project
from blog.models import Post


class StaticViewSitemap(Sitemap):
    priority = 0.9
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'services', 'contact', 'resume', 'testimonials', 'blog', 'projects']

    def location(self, item):
        return reverse(item)


class ProjectSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return Project.objects.all()

    def location(self, obj):
        return f'/projects/{obj.slug}/'

    def lastmod(self, obj):
        return obj.created_at


class BlogSitemap(Sitemap):
    priority = 0.7
    changefreq = 'weekly'

    def items(self):
        return Post.objects.filter(is_published=True)

    def location(self, obj):
        return f'/blog/{obj.slug}/'

    def lastmod(self, obj):
        return obj.updated_at