from django.shortcuts import render
from .models import Project, Image, ContactsPage, AboutPage, HomePage, ServicesPage, Solution, ImageSolution
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
        contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
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
        kwargs['contacts_base'] = contacts_base
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
    contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
    return render(request, 'portfolio/project_view.html', {'project': project, 'images': images, 'id': id,
                                                           'len_images': len_images, 'contacts_base': contacts_base})


def index(request):
    information = HomePage.objects.filter(moderation=True)[:1]
    projects = Project.objects.filter(moderation=True)[:8]
    images = Image.objects.all()
    contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
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
                                                    'information': information, 'contacts_base': contacts_base})


def contacts(request):
    contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
    contacts = ContactsPage.objects.filter(moderation=True)[:1] # если построково делать то убрать слайс
    return render(request, 'portfolio/contacts.html', {'contacts': contacts, 'contacts_base': contacts_base})


# def contacts_for_base(request):
#     contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
#     return render(request, 'portfolio/base.html', {'contacts_base': contacts_base})


def about(request):
    contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
    about = AboutPage.objects.filter(moderation=True)[:1]
    return render(request, 'portfolio/about.html', {'about': about, 'contacts_base': contacts_base})


# def services(request, id):
class ServicesList(ListView):
    # TODO: Нужно добавить модель услуг для вывода в таблицу
    model = Solution
    template_name = 'portfolio/services.html'
    context_object_name = 'solutions'

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
        solutions = Solution.objects.filter(moderation=True)
        contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
        images = ImageSolution.objects.all()
        list_images = []
        i = 0
        for element_solutions in solutions:
            for element_images in images:
                if element_images.solution.id == element_solutions.pk and i == 0:
                    i = i + 1
                    list_images.append(element_images)
            i = 0
        kwargs['images'] = list_images
        kwargs['contacts_base'] = contacts_base
        return super().get_context_data(**kwargs)

    def get_queryset(self):
        solutions = Solution.objects.filter(moderation=True)
        paginator = Paginator(solutions, 8)
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

def solution_view(request, id):
    solution = Solution.objects.get(pk=id)
    images = ImageSolution.objects.filter(solution=id)
    len_images = images.count()
    contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
    return render(request, 'portfolio/solution_view.html', {'solution': solution, 'images': images, 'id': id,
                                                           'len_images': len_images, 'contacts_base': contacts_base})


def sitemap(request):
    contacts_base = ContactsPage.objects.filter(moderation=True)[:1]
    return render(request, 'portfolio/sitemap.html', {'contacts_base': contacts_base})
