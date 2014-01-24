from django.db import models
from django import forms
from django.core.exceptions import ValidationError
from django import forms
from django.core.validators import validate_email


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







class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField()
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


class MultiEmailField(forms.Field):
    def to_python(self, value):
        "Normalize data to a list of strings."
        # Return an empty list if no input was given.
        if not value:
            return []
        return value.split(',')

    def validate_even(value):
        if value % 2 != 0:
            raise ValidationError(u'%s is not an even number' % value)

    def validate(self, value):
        "Check if value consists only of valid emails."

        # Use the parent's handling of required fields, etc.
        super(MultiEmailField, self).validate(value)

        for email in value:
            validate_email(email)



class comment(forms.Form):
    c=MultiEmailField;
    subject=forms.CharField(validators=[c.validate_even])

