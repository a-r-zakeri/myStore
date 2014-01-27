from django.http import *
from webStore import models
import json
from webStore.form import *
from django.shortcuts import render
from django.http import HttpResponseRedirect



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


def goodsList(request):
    print("method: " + request.method)
    allGood = models.Good.objects.all()
    JSONallGoods = []
    for good in allGood:
        JSONallGoods.append({"picUrl": good.name, "category" : good.id, "id" : good.id, "name" : good.name, "price" : good.price})#should be complete
    print(JSONallGoods)
    data = {}
    data ['result'] = "1"
    data ['page'] = request.POST["page"]
    data ['pageSize'] = request.POST["pageSize"]
    data ['productList'] = JSONallGoods
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



