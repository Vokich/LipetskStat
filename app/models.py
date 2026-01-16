from django.db import models
from django.utils import timezone

class Attractions(models.Model):
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    picture = models.ImageField(upload_to='images', verbose_name="Фото", null=True, blank=True)
    description = models.TextField(max_length=1000, verbose_name="Описание", null=True, blank=True)
    source = models.CharField(max_length=100, default="unknown", help_text="Укажите город", verbose_name="Город")

    def __str__(self):
        return self.title


class News(models.Model):
  title = models.CharField(max_length=200, verbose_name="Заголовок новости")
  content = models.TextField(verbose_name="Содержание новости")
  image = models.ImageField(upload_to='news_images/', verbose_name="Изображение", null=True, blank=True)
  created_at = models.DateTimeField(default=timezone.now, verbose_name="Дата публикации")
  is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

  def __str__(self):
    return self.title

  class Meta:
    db_table = 'app_news'
    verbose_name = "Новость"
    verbose_name_plural = "Новости"
    ordering = ['-created_at']


class WeatherCache(models.Model):
    temperature = models.FloatField()
    description = models.CharField(max_length=100)
    humidity = models.IntegerField()
    wind_speed = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.temperature}°C, {self.description}"
