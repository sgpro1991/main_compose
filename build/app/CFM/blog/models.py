from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils.safestring import mark_safe
# Create your models here.



class Rubric(models.Model):
    title = models.CharField('Название рубрики', max_length=255)
    def __str__(self):              # __unicode__ on Python 2
        return self.title
    class Meta:
         verbose_name_plural = "Рубрики"



class Blog(models.Model):
    meta_title = models.CharField('Title', max_length=255,blank=True)
    meta_keywords = models.CharField('Keywords', max_length=255,blank=True)
    meta_description = models.CharField('Description', max_length=255,blank=True)
    title = models.CharField('Заголовок', max_length=255)
    description = models.CharField('Краткое описание', max_length=255)
    rubric = models.ForeignKey(Rubric, verbose_name='Рубрика')
    text  = RichTextUploadingField('Текст материала')
    date = models.DateTimeField('Дата и время публикации')

    image = models.ImageField(upload_to='media/static/upload/blog/', blank=True, verbose_name='Главная картинка')
    def image_tag(self):
        return mark_safe('<img src="/media/%s" style="max-width:300px;"/>' % (self.image))

    image_tag.short_description = 'Предпросмотр'

    class Meta:
         verbose_name_plural = "Материалы"
