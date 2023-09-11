from django.db import models

# Create your models here.
class Articles(models.Model):
    TITLE = [
        (1, 'Продам'),
        (2, 'Куплю'),
        (3, 'Меняю'),
        (4, 'Разное')
    ]
    # title = models.IntegerField('Категория', choices=TITLE)
    title = models.TextField('Тема объявления, например, "ПРОДАМ"')
    ANONS = [
        (1, 'Недвижимость'),
        (2, 'Авто'),
        (3, 'Инструмент'),
        (4, 'Разное'),
    ]
    anons = models.IntegerField('Тема', choices=ANONS)
    full_text = models.TextField('Объявление')
    date = models.DateTimeField('Дата размещения')

    def __str__(self) -> str:
        return self.title
    
    def get_absolute_url(self):
        return f'/news/{self.id}'
    
    class Meta:
        verbose_name = 'Объявление'
        verbose_name_plural = 'Объявления'
        
