from django.db import models


class Gallery(models.Model):
    name = models.CharField(max_length=35, blank=False, help_text='название картины')
    pictures = models.ImageField(help_text='фото картины')
    genres = models.IntegerField(default=0, help_text="1 - портреты, 2 - живопись, 3 - абстракция,  4 - графика, 5 - светящиеся")
    instock = models.IntegerField(default=0, help_text="0 - в коллекции, 1 - в наличии")
    description = models.TextField(help_text='описание картины')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "картину"
        verbose_name_plural = "Картины"


class Media(models.Model):
    videos = models.TextField(help_text='cсылка на видео ютуб')
    body = models.TextField(help_text='описание видео')
    header = models.TextField(help_text='заголовок видео')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "видео"
        verbose_name_plural = "Видео"


class News(models.Model):
    photo = models.ImageField(help_text='фото новости')
    body = models.TextField(help_text='текст новости')
    header = models.CharField(max_length=35, blank=False, help_text='заголовок новости')
    date = models.DateField(help_text='дата новости')

    def __str__(self):
        return self.header

    class Meta:
        verbose_name = "новость"
        verbose_name_plural = "Новости"


class Orders(models.Model):
    FIO = models.CharField(max_length=35, blank=False, help_text='ФИО')
    emails = models.CharField(max_length=35, blank=False, help_text='почта')
    phone = models.CharField(max_length=35, blank=False, help_text='Телефон')
    comment = models.TextField(max_length=235, blank=False, help_text='Комментарий')
    def __str__(self):
        return self.FIO

    class Meta:
        verbose_name = "заказа"
        verbose_name_plural = "Заказы"
