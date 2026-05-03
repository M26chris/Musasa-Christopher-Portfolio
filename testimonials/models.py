from django.db import models

class Testimonial(models.Model):
    name        = models.CharField(max_length=100)
    role        = models.CharField(max_length=150, help_text="e.g. CEO at Acme Ltd")
    message     = models.TextField()
    photo       = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    rating      = models.IntegerField(default=5)
    is_featured = models.BooleanField(default=False)
    created_at  = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} — {self.role}"