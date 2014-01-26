from django.db import models
from django import forms



class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"نام دسته")
    parent = models.ForeignKey('self', null=True, blank=True, verbose_name=u"دسته‌ی بالایی")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "دسته"
        verbose_name_plural = "دسته ها"

class SlideShow(models.Model):
    imageURL = models.URLField(verbose_name=u"آدرس عکس بزرگ")

    def __str__(self):
        return self.imageURL

    class Meta:
        verbose_name = "عکس اسلاید"
        verbose_name_plural = "عکس های اسلاید"


class Image(models.Model):
    picUrl=models.URLField(verbose_name=u"آدرس عکس")
    #pic=models.ImageField(upload_to="images/")

    class Meta:
        verbose_name = "عکس "
        verbose_name_plural = "  عکس ها"


class Good(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"نام کالا")
    category = models.ForeignKey(Category)
    slidShow = models.OneToOneField(SlideShow, null=True, blank=True)
    price = models.IntegerField(verbose_name=u"قیمت")
    pic= models.ForeignKey(Image)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالاها"


class Comment(models.Model):

    subject = models.CharField(max_length=100, verbose_name=u"نام نویسنده", null=True, blank=True)
    message = models.CharField(max_length=300, verbose_name=u"پیغام")
    sender = models.EmailField(verbose_name=u"میل")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "نظر"
        verbose_name_plural = "نظرات"



