from django.db import models
from django.core.validators import MinLengthValidator

DRAFT = 'draft'
PUBLISHED = 'published'

STATUS_CHOICES = (
    (DRAFT, 'Draft'),
    (PUBLISHED, 'Published'),
)

class Content(models.Model):
    title           = models.CharField(blank=False, max_length=200, 
                                       validators=[MinLengthValidator(1)], verbose_name='Title')
    published_date  = models.DateTimeField(null=True, blank=True, verbose_name='Published Date')
    author          = models.CharField(blank=True, max_length=200, verbose_name='Author')
    summary         = models.TextField(blank=True, verbose_name='Summary')
    content         = models.TextField(blank=True, verbose_name='Content')
    status          = models.CharField(blank=False, max_length=30, verbose_name='Status', 
                                       choices=STATUS_CHOICES, default=DRAFT)

    def __str__(self):
        return self.title