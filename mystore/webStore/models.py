from django.db import models

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

class Good(models.Model):
    name = models.CharField(max_length=200, verbose_name=u"نام کالا")
    category = models.ForeignKey(Category)
    slidShow = models.OneToOneField(SlideShow, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "کالا"
        verbose_name_plural = "کالاها"