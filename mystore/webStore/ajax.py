from django.http import *
from webStore import models
import json
from webStore.form import ContactForm
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django import forms
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def goods(request):
    print("method: " + request.method)
    allCats = models.Category.objects.all()
    JSONallCats = []
    for category in allCats:
        if (category.parent):
            JSONallCats.append({"name": category.name, "id" : category.id, "parent": category.parent.id})
        else:
            JSONallCats.append({"name": category.name, "id" : category.id})
    print(JSONallCats)
    data = {}
    data ['result'] = "1"
    data ['categoryList'] = JSONallCats
    return HttpResponse(json.dumps(data), content_type="application/json")

def comments(request):
    print("method: " + request.method)
    allComments = models.Comment.objects.all()
    JSONallComments = []
    for category in allComments:
        JSONallComments.append({"message": category.message, "name" : category.subject})

    print(JSONallComments)
    data = {}
    data ['result'] = "1"
    data ['commentList'] = JSONallComments
    return HttpResponse(json.dumps(data), content_type="application/json")


def uploadimage(request):

    object = models.Image(request['image'])
    object.save()
    data ={}
    data ['picId']=object.id

    data ['picUrl']=request['image']
    return HttpResponse(json.dumps(data), content_type="application/json")


def register(request):
    if request.method == "POST":
        username = request.POST.get('username', None)
        if not username:
            username_error = u"نام کاربری الزامی است"
        elif not re.match("[\d\w_\.]{6,}", username):
            username_error = u"نام کاربری باید حداقل شش حرفی شامل حروف یا اعداد باشد"
        elif User.objects.filter(username=username).count() > 0:
            username_error = u"این نام در دسترس نیست"
        email = request.POST.get('email', None)
        if not email:
            email_error = u" آدرس ایمیل الزامی است"
        elif not email_re.search(email):
            email_error = u" ایمیل وارد شده معتبر نیست"
        elif User.objects.filter(email=email).count() > 0:
            email_error = u" قبلا با این آدرس ثبت نام شده است"


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']
            recipients = ['info@example.com']
            if cc_myself:
                recipients.append(sender)
            from django.core.mail import send_mail
            send_mail(subject, message, sender, recipients)
            return HttpResponseRedirect('/thanks/')
    else:
        form = ContactForm()

    return render(request, 'specification.html', {'form': form,})



