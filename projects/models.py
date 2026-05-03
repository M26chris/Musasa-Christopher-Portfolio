from django.db import models

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('mobile', 'Mobile Development'),
        ('data', 'Data Analytics'),
        ('health', 'Health Tech'),
        ('cyber', 'Cybersecurity'),
        ('learning', 'Learning Projects'),
        ('other', 'Other'),
    ]

    title        = models.CharField(max_length=200)
    slug         = models.SlugField(unique=True)
    description  = models.TextField()
    problem      = models.TextField(
                       blank=True,
                       help_text="What problem does this project solve?"
                   )
    solution     = models.TextField(
                       blank=True,
                       help_text="How does your project solve it?"
                   )
    impact       = models.TextField(
                       blank=True,
                       help_text="What was the result or outcome?"
                   )
    tech_stack   = models.CharField(max_length=300, help_text="e.g. Python, Django, Tailwind")
    thumbnail    = models.ImageField(upload_to='projects/', blank=True, null=True)
    live_url     = models.URLField(blank=True)
    github_url   = models.URLField(blank=True)
    category     = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    is_featured  = models.BooleanField(default=False)
    date         = models.DateField()
    created_at   = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title