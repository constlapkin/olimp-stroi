from django.contrib import admin
from portfolio.models import Project, Image


class ProjectImageInline(admin.TabularInline):
    model = Image
    extra = 3


class ProjectAdmin(admin.ModelAdmin):
    inlines = [ProjectImageInline, ]


admin.site.register(Project, ProjectAdmin)
