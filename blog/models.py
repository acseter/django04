from django.contrib.auth.models import User
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.



class BlogType(models.Model):
    type_name = models.CharField(max_length=15)

    def __str__(self):
        return self.type_name

class Blog(models.Model):
    title = models.CharField(max_length=50)
    blog_type = models.ForeignKey(BlogType,on_delete=True)
    # content = models.TextField()
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    readed_num = models.IntegerField(default=0)
    create_time = models.DateTimeField(auto_now_add=True)
    last_update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "<Blog:%s>"%self.title


    class Meta:
        ordering = ['-create_time']     #ordering标签排序设置，按照创建时间排序

class MediaTest(models.Model):
    picture_url = models.ImageField(
        null=True,
        blank=True,
        upload_to='image',
        max_length=200)

    class Meta:
        db_table = 'media_test'