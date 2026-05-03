import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm
from .models import ContactMessage

logger = logging.getLogger('core')

def home(request):
    # Import here to avoid circular imports
    from projects.models import Project
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    return render(request, 'core/home.html', {'featured_projects': featured_projects})

def about(request):
    return render(request, 'core/about.html')

def services(request):
    return render(request, 'core/services.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            ContactMessage.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                subject=form.cleaned_data['subject'],
                message=form.cleaned_data['message'],
            )

            logger.info(
                f"New contact message from {form.cleaned_data['name']} "
                f"<{form.cleaned_data['email']}> - Subject: {form.cleaned_data['subject']}"
            )

            # Send email notification to yourself
            try:
                send_mail(
                    subject=f"Portfolio Contact: {form.cleaned_data['subject']}",
                    message=f"""
New message from your portfolio website!

Name:    {form.cleaned_data['name']}
Email:   {form.cleaned_data['email']}
Phone:   {form.cleaned_data.get('phone', 'Not provided')}
Service: {form.cleaned_data['service']}

Message:
{form.cleaned_data['message']}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
                logger.info(f"Contact email sent successfully for {form.cleaned_data['email']}")
            except Exception as e:
                logger.error(f"Failed to send contact email: {e}")

            messages.success(
                request, 
                'Thank you! Your message has been sent. I will get back to you shortly.'
            )
            
            return redirect('contact')
        else:
            logger.warning(f"Invalid contact form submission: {form.errors}")
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()

    return render(request, 'core/contact.html', {'form': form})

def resume(request):
    return render(request, 'core/resume.html')