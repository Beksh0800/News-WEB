from datetime import datetime

from django.db import models

class News(models.Model):
    title = models.CharField('Заголовок', max_length=250)
    pub_date = models.DateTimeField('Дата публикации', default=datetime.now)
    image = models.CharField('Ссылка на фото', max_length=500)
    description = models.TextField('Описание')

    def __str__(self):
        return self.title
