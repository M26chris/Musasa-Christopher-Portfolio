from django.shortcuts import render
from .models import Testimonial

def testimonials(request):
    all_testimonials = Testimonial.objects.all()
    context = {'testimonials': all_testimonials}
    return render(request, 'testimonials/testimonials.html', context)