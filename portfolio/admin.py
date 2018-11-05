from django.contrib import admin
from portfolio.models import Project, Image, HomePage, AboutPage, ContactsPage, ServicesPage, Solution, ImageSolution


class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ]


class SolutionImageInline(admin.TabularInline):
    model = ImageSolution
    extra = 3


class SolutionAdmin(admin.ModelAdmin):
    inlines = [SolutionImageInline, ]


class HomePageAdmin(admin.ModelAdmin):
    model = HomePage


class AboutPageAdmin(admin.ModelAdmin):
    model = AboutPage


class ContactsPageAdmin(admin.ModelAdmin):
    model = ContactsPage


class ServicesPageAdmin(admin.ModelAdmin):
    model = ServicesPage


admin.site.register(Project, ProjectAdmin)
admin.site.register(Solution, SolutionAdmin)
admin.site.register(HomePage, HomePageAdmin)
admin.site.register(AboutPage, AboutPageAdmin)
admin.site.register(ContactsPage, ContactsPageAdmin)
admin.site.register(ServicesPage, ServicesPageAdmin)
