from django.shortcuts import render
from .models import Project, Image, ContactsPage, AboutPage, HomePage, ServicesPage
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


def index(request):
    information = HomePage.objects.filter(moderation=True)[:1]
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
    return render(request, 'portfolio/index.html', {'projects': projects, 'images': list_images,
                                                    'information': information})


def contacts(request):
    contacts = ContactsPage.objects.filter(moderation=True)[:1] # если построково делать то убрать слайс
    return render(request, 'portfolio/contacts.html', {'contacts': contacts})


def about(request):
    about = AboutPage.objects.filter(moderation=True)[:1]
    return render(request, 'portfolio/about.html', {'about': about})


# def services(request, id):
class ServicesList(ListView):
    model = Project
    template_name = 'portfolio/services.html'
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

    # return render(request, 'main/services.html',
    # {'projects': projects, 'images': list_images, 'id': id, 'pages': pages})


def sitemap(request):
    return render(request, 'portfolio/sitemap.html', {})