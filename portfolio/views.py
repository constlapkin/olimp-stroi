from django.shortcuts import render
from .models import Project, Image
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# def project_list(request):
class ProjectsList(ListView):
    '''
    Отображает страницу портфолио в котором передается все проекты и первое изображение для каждого проекта
    :param request:
    :return request, template, list of projects and list of images (element - first for project):
    '''

    model = Project
    template_name = 'portfolio/project_list.html'
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        projects = Project.objects.filter(moderation=True)
        images = Image.objects.all()
        list_images = []
        i = 0
        for element_projects in projects:
            for element_images in images:
                if element_images.project.id == element_projects.pk and i == 0:
                    i = i + 1
                    list_images.append(element_images)
            i = 0
        kwargs['images'] = list_images
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        projects = Project.objects.filter(moderation=True)
        paginator = Paginator(projects, 16)
        page = self.request.GET.get('page')
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)
        return projects

    # return render(request, 'portfolio/project_list.html', {'projects': projects, 'images': list_images})


def project_view(request, id):
    project = Project.objects.get(pk=id)
    images = Image.objects.filter(project=id)
    len_images = images.count()
    return render(request, 'portfolio/project_view.html', {'project': project, 'images': images, 'id': id,
                                                           'len_images': len_images})
