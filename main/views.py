from django.shortcuts import render
from portfolio.models import Project, Image
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    projects = Project.objects.filter(moderation=True)[:8]
    images = Image.objects.all()
    list_images = []
    i = 0
    for element_projects in projects:
        for element_images in images:
            if element_images.project.id == element_projects.pk and i == 0:
                i = i + 1
                list_images.append(element_images)
        i = 0
    list_images = list_images[:8]
    return render(request, 'main/index.html', {'projects': projects, 'images': list_images})


def contacts(request):
    return render(request, 'main/contacts.html', {})


def about(request):
    return render(request, 'main/about.html', {})


#def services(request, id):
class ServicesList(ListView):
    model = Project
    template_name = 'main/services.html'
    context_object_name = 'projects'

    # projects = Project.objects.filter(moderation=True)
    # count = projects.count()
    # pages = count / 8

    # if id > pages:
    #     id = pages
    # elif id < pages:
    #     id = 1

    # if pages == 1:
    #     id = 1

    # start_id_projects = (id - 1) * 8
    # finish_id_projects = (id - 1) * 8 + 8

    # if pages > 1:
    #     projects = projects[start_id_projects:finish_id_projects]

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
        paginator = Paginator(projects, 8)
        page = self.request.GET.get('page')
        try:
            projects = paginator.page(page)
        except PageNotAnInteger:
            projects = paginator.page(1)
        except EmptyPage:
            projects = paginator.page(paginator.num_pages)
        return projects

   # return render(request, 'main/services.html', {'projects': projects, 'images': list_images, 'id': id, 'pages': pages})


def sitemap(request):
    return render(request, 'main/sitemap.html', {})
