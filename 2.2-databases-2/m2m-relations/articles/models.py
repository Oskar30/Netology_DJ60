from django.db import models


class Tag(models.Model):
    #tag = models.CharField(max_length=30)
    name = models.CharField(max_length=30, verbose_name='Тэг')

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тэги'
    
    def __str__(self):
        return self.name


class Article(models.Model):
    
    title = models.CharField(max_length=256, verbose_name='Название')
    text = models.TextField(verbose_name='Текст')
    published_at = models.DateTimeField(verbose_name='Дата публикации')
    image = models.ImageField(null=True, blank=True, verbose_name='Изображение',)
    #tags = models.ManyToManyField(Tag, verbose_name='Тэг',)
    #scopes
    

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['-published_at']

    def __str__(self):
        return self.title


class Scope(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='scopes')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, default=None, verbose_name='Раздел')
    is_main = models.BooleanField(default=False, verbose_name='Основной')


    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Тематика'
        ordering = ['-is_main', 'tag']
