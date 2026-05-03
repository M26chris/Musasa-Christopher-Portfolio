import logging
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Project

logger = logging.getLogger('projects')

VALID_CATEGORIES = ['all', 'web', 'mobile', 'data', 'health', 'cyber', 'learning', 'other']

def projects_list(request):
    category = request.GET.get('category', 'all')
    
    # Validate category parameter
    if category not in VALID_CATEGORIES:
        logger.warning(f"Invalid category param received: '{category}' - falling back to 'all'")
        category = 'all'

    if category == 'all':
        projects = Project.objects.all()
    else:
        projects = Project.objects.filter(category=category)


    paginator = Paginator(projects, 6)  # Show 6 projects per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'active_category': category,
    }
    return render(request, 'projects/projects_list.html', context)


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    related = Project.objects.filter(
        category=project.category
    ).exclude(id=project.id)[:3]
    context = {
        'project': project,
        'related': related,
    }
    logger.info(f"Project detail viewed: {project.title}")
    return render(request, 'projects/project_detail.html', context)