from django.db import models

class Post(models.Model):
    title        = models.CharField(max_length=200)
    slug         = models.SlugField(unique=True)
    excerpt      = models.TextField(
                       blank=True,
                       help_text="Short summary shown in blog list. If empty, auto-generated from body."
                   )
    body         = models.TextField()
    cover_image  = models.ImageField(upload_to='blog/', blank=True, null=True)
    category     = models.CharField(max_length=100, blank=True)
    created_at   = models.DateTimeField(auto_now_add=True)
    updated_at   = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title
    
    def get_excerpt(self):
        """Return excerpt if set, otherwise auto-generate from body."""
        if self.excerpt:
            return self.excerpt
        words = self.body.split()
        return ' '.join(words[:30]) + ('...' if len(words) > 30 else '')