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


# class Image(models.Model):
#     picUrl=models.URLField(verbose_name=u"آدرس عکس")
#     pic=models.FileField(upload_to="/images/%Y/%m/%d")
#
#     def __str__(self):
#         return self.picUrl
#
#     class Meta:
#         verbose_name = "عکس "
#         verbose_name_plural = "  عکس ها"



class Good(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"نام کالا")
    category = models.ForeignKey(Category, verbose_name=u"دسته‌ی کالا")
    slideShow = models.OneToOneField(SlideShow, null=True, blank=True)
    price = models.IntegerField(verbose_name=u"قیمت")
    count = models.IntegerField(verbose_name=u"تعداد")
    image = models.FileField(upload_to="images/", verbose_name=u"عکس کالا")


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



class User(models.Model):

    username = models.CharField(max_length=100, verbose_name=u"شناسه کاربری")
    password = models.CharField(max_length=100, verbose_name=u"رمز عبور")
    email = models.EmailField()

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"



class Basket(models.Model):

    user = models.ForeignKey(User)
    good = models.ForeignKey(Good)
    status=models.BooleanField()

    def __str__(self):
        return self.user

    class Meta:
        verbose_name = "سبد خرید"
