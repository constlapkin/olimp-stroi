from django.db import models


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок", help_text="Название проекта, отображаемое при открытии")
    description = models.TextField(verbose_name="Описание", help_text="Подробное описание проекта")
    date = models.DateField(blank=True, null=True, verbose_name="Дата", help_text="Дата сдачи проекта")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Стоимость", help_text="Конечная стоимость проекта")
    common_sq_m = models.FloatField(blank=True, null=True, verbose_name="Общая площадь, кв.м.", help_text="Общая площадь готового проекта")
    residential_sq_m = models.FloatField(blank=True, null=True, verbose_name="Жилая площадь, кв.м.", help_text="Жилая площадь проекта")
    moderation = models.BooleanField(default=True, verbose_name="Публикация", help_text="Публикация проекта на сайте")
    # сроки проекта в месяцах мб

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Image(models.Model):
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название", help_text="Описание/название фотографии, в случае если она не загрузилась")
    image = models.ImageField(upload_to="projects/", verbose_name="Фотография *", help_text="Фотография готового проекта")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name="Проект *", help_text="Проект к которому фотография относится")
