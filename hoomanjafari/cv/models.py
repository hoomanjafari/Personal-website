from django.db import models


class MyCv(models.Model):
    img = models.ImageField(upload_to='img/%y')
    body = models.CharField(max_length=300)

    def __str__(self):
        return f'{self.body[:20]}'
