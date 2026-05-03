from django.db import models

class Service(models.Model):
    title       = models.CharField(max_length=200)
    description = models.TextField()
    icon        = models.CharField(max_length=100, help_text="Font Awesome class e.g. fas fa-laptop-code")
    price_from  = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)
    order       = models.IntegerField(default=0)
    is_active   = models.BooleanField(default=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title