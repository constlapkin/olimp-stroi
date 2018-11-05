from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class Project(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок",
                             help_text="Название проекта, отображаемое при открытии")
    description = RichTextField(verbose_name="Описание", help_text="Подробное описание проекта")
    date = models.DateField(blank=True, null=True, verbose_name="Дата", help_text="Дата сдачи проекта")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Стоимость",
                                        help_text="Конечная стоимость проекта")
    common_sq_m = models.FloatField(blank=True, null=True, verbose_name="Общая площадь, кв.м.",
                                    help_text="Общая площадь готового проекта")
    residential_sq_m = models.FloatField(blank=True, null=True, verbose_name="Жилая площадь, кв.м.",
                                         help_text="Жилая площадь проекта")
    moderation = models.BooleanField(default=True, verbose_name="Публикация", help_text="Публикация проекта на сайте")
    months = models.PositiveIntegerField(blank=True, null=True, verbose_name="Выполнение проекта в месяцах")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'


class Image(models.Model):
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название",
                           help_text="Описание/название фотографии, в случае если она не загрузилась")
    image = models.ImageField(upload_to="projects/", verbose_name="Фотография *",
                              help_text="Фотография готового проекта")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name="Проект *",
                                help_text="Проект к которому фотография относится")


class HomePage(models.Model):
    first_title = models.CharField(max_length=255, verbose_name="Заголовок первого текста")
    first_text = RichTextUploadingField(verbose_name="Первый текст")
    second_title = models.CharField(max_length=255, blank=False, null=True, verbose_name="Заголовок второго текста")
    second_text = RichTextUploadingField(verbose_name="Второй текст", blank=False, null=True)
    moderation = models.BooleanField(default=True, verbose_name="Публикация", help_text="Одобрение главной страницы")

    def __str__(self):
        return "Данные на главной странице"

    class Meta:
        verbose_name = 'Главная'
        verbose_name_plural = 'Главная'


class AboutPage(models.Model):
    text = RichTextUploadingField(verbose_name="Текст о компании")
    moderation = models.BooleanField(default=True, verbose_name="Публикация", help_text="Одобрение страницы о компании")

    def __str__(self):
        return "Данные для страницы о компании"

    class Meta:
        verbose_name = 'О компании'
        verbose_name_plural = 'О компании'


class ContactsPage(models.Model):
    number = models.CharField(max_length=30, verbose_name="Номер телефона")
    short_number = models.CharField(max_length=30, verbose_name="Номер на страницах",
                                    help_text="Короткая запись номера, "
                                              "которая будет отображена сверху и снизу каждой страницы")
    email = models.EmailField(verbose_name="Почта")
    real_address = models.CharField(max_length=255, verbose_name="Фактический адрес")
    short_address = models.CharField(max_length=255, verbose_name="Адрес на страницах",
                                     help_text="Короткая запись адреса, "
                                               "которая будет отображена вверху и снизу каждой страницы")
    fake_address = models.CharField(max_length=255, verbose_name="Юридический адрес")
    moderation = models.BooleanField(default=True, verbose_name="Публикация", help_text="Одобрение набора контактов")

    def __str__(self):
        return "Данные для страницы контактов"

    class Meta:
        verbose_name = 'Контакты'
        verbose_name_plural = 'Контакты'


class ServicesPage(models.Model):
    '''
    Здесь должны быть поля определяющие цены на услуги
    '''
    def __str__(self):
        return "Услуги"

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'


class Solution(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок",
                             help_text="Название проекта, отображаемое при открытии")
    description = RichTextField(verbose_name="Описание", help_text="Подробное описание проекта")
    price = models.PositiveIntegerField(blank=True, null=True, verbose_name="Стоимость",
                                        help_text="Конечная стоимость проекта")
    common_sq_m = models.FloatField(blank=True, null=True, verbose_name="Общая площадь, кв.м.",
                                    help_text="Общая площадь готового проекта")
    residential_sq_m = models.FloatField(blank=True, null=True, verbose_name="Жилая площадь, кв.м.",
                                         help_text="Жилая площадь проекта")
    moderation = models.BooleanField(default=True, verbose_name="Публикация", help_text="Публикация проекта на сайте")
    months = models.PositiveIntegerField(blank=True, null=True, verbose_name="Выполнение проекта в месяцах")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Решение'
        verbose_name_plural = 'Решения'


class ImageSolution(models.Model):
    alt = models.CharField(max_length=255, blank=True, null=True, verbose_name="Название",
                           help_text="Описание/название фотографии, в случае если она не загрузилась")
    image = models.ImageField(upload_to="solutions/", verbose_name="Фотография *",
                              help_text="Фотография готового решения")
    project = models.ForeignKey('Project', on_delete=models.CASCADE, verbose_name="Решение *",
                                help_text="Рещение к которой фотография относится")
