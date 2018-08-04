from django.db import models

# Create your models here.


class HomePage:
    first_text = models.TextField(verbose_name="Первый текст")
    second_text = models.TextField(verbose_name="Второй текст")

    def __str__(self):
        return "Данные на главной странице"

    class Meta:
        verbose_name = 'Главная страница'
        verbose_name_plural = 'Главная страница'


class AboutPage:
    text = models.TextField(verbose_name="Текст о компании")

    def __str__(self):
        return "Данные для страницы о компании"

    class Meta:
        verbose_name = 'Страница о компании'
        verbose_name_plural = 'Страница о компании'


class ContactsPage:
    '''
    Сделать проверку имения адрессов и шорт адресов и телефонов
    '''
    number = models.CharField(max_length=30, verbose_name="Номер телефона")
    short_number = models.CharField(max_length=30, verbose_name="Номер на страницах",
                                    help_text="Короткая запись номера, "
                                              "которая будет отображена вверху и снизу каждой страницы")
    email = models.EmailField(verbose_name="Почта")
    real_address = models.CharField(max_length=255, verbose_name="Фактический адрес")
    short_address = models.CharField(max_length=255, verbose_name="Адрес на страницах",
                                     help_text="Короткая запись адреса, "
                                               "которая будет отображена вверху и снизу каждой страницы")
    fake_address = models.CharField(max_length=255, verbose_name="Юридический адрес")

    def __str__(self):
        return "Данные для страницы контактов"

    class Meta:
        verbose_name = 'Страница контактов'
        verbose_name_plural = 'Страница контактов'


class ServicesPage:
    '''
    Здесь должны быть поля определяющие цены на услуги
    '''
    pass



