from django import forms
import re
from django.forms import ModelForm
from webStore.models import User, Good


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,required=False)#name
    message = forms.CharField(widget=forms.Textarea, required=False)
    sender = forms.EmailField(required=False)

    def clean_confirmpass(self):
        copass = self.cleaned_data['confirmpass']
        password = self.cleaned_data['password']
        if copass != password:
            raise forms.ValidationError(u"رمز ورود با رمز تایید برابر نیست")
        return copass

    def clean_subject(self):
        sender = self.cleaned_data['subject']
        if sender=='':
            raise forms.ValidationError('لطفا نام خود را وارد کنید')
        return sender

    def clean_message(self):
        sender = self.cleaned_data['message']
        if sender=='':
            raise forms.ValidationError('لطفا نظر خود را وارد کنید')
        return sender

    def clean_sender(self):
        sender = self.cleaned_data['sender']
        if sender=='':
            raise forms.ValidationError('لطفا میل خود را وارد کنید')
        return sender

    def clean(self):
        cleaned_data = super(ContactForm, self).clean()



        # Always return the full collection of cleaned data.
        return cleaned_data

class GoodForm(ModelForm):
    class Meta:
        model = Good
        fields = ['name', 'category', 'price', 'count']

class FileForm(forms.Form):
    file = forms.FileField(label="enter file")

# class GoodForm(forms.Form):
#     imageFile = forms.FileField(label=u"یک عکس برای محصول انتخاب کنید")
    # count = forms.IntegerField(required=True)
    # name = forms.CharField(max_length=100, required=True)
    # about = forms.CharField(widget=forms.Textarea, required=False)
    # price = forms.IntegerField(required=False)
    #
    # def clean_count(self):
    #     count = self.cleaned_data['count']
    #     if count <= 0:
    #         raise forms.ValidationError(u"باید حد اقل یک موجودی از این محصول باشد")
    #     return count
    #
    # def clean_price(self):
    #     print(self)
    #     print(self.cleaned_data)
    #     count = self.cleaned_data['price']
    #     if count == None or count <= 0:
    #         raise forms.ValidationError(u"لطفا قیمت صحیح وارد کنید")
    #     return count
    #
    # def clean_name(self):
    #     name = self.cleaned_data['name']
    #     if name=='':
    #         raise forms.ValidationError('لطفا نام محصول را وارد کنید')
    #     return name
    #
    # def clean(self):
    #     cleaned_data = super(GoodForm, self).clean()

        # return cleaned_data
#
#

class Register(forms.Form):
    username = forms.CharField(required=False)
    password = forms.CharField(widget = forms.PasswordInput(), required=False)
    cpassword = forms.CharField(widget = forms.PasswordInput(),required=False)
    email= forms.CharField(required=False)

    def clean_username(self):
        username = self.cleaned_data['username']
        if not username:
            raise forms.ValidationError(u"نام کاربری الزامی است")
        elif not re.match("[\d\w_\.]{6,}", username):
            raise forms.ValidationError(u"نام کاربری باید حداقل شش حرفی شامل حروف یا اعداد باشد")
        elif User.objects.filter(username=username).count() > 0:
            raise forms.ValidationError(u"این نام در دسترس نیست")
        return username

    def clean_email(self):
        email=self.cleaned_data['email']
        if not email:
            raise forms.ValidationError(u" آدرس ایمیل الزامی است")
        elif User.objects.filter(email=email).count() > 0:
            raise forms.ValidationError(u" قبلا با این آدرس ثبت نام شده است")
        return email

    def clean_cpassword(self):
        password1 = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('cpassword')

        if not password2:
            raise forms.ValidationError("رمز عبور را تایید کنید")
        if password1 != password2:
            raise forms.ValidationError("با رمز عبور مطابقت نمی کند")
        return password2

    def clean_password(self):
        password1 = self.cleaned_data.get('password')
        if not password1:
            raise forms.ValidationError("رمز عبور الزامی است")
        return password1


    def clean(self):
        cleaned_data = super(Register, self).clean()

        return cleaned_data



class LoginForm(forms.Form):
    uname = forms.CharField(required=False)
    pword = forms.CharField(widget = forms.PasswordInput(), required=False)

    def clean_uname(self):
        username = self.cleaned_data.get('uname')
        if not username:
            raise forms.ValidationError(u"نام کاربری را وارد کنید")
        return username

    def clean_pword(self):
        password = self.cleaned_data.get('pword')
        if not password:
            raise forms.ValidationError("رمز عبور را وارد کنید")
        return password

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

        return cleaned_data