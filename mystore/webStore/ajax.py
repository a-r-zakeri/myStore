from django.http import *
from webStore import models
import json
from webStore.form import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from webStore.models import *



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
        JSONallGoods.append({"picUrl": good.pic.picUrl, "category" : good.category, "id" : good.id, "name" : good.name, "price" : good.price})#should be complete
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




def addBasket(request):
    good=Good.objects.get(pk=requsest['id'])
    user=User.objects.filter(username=request.user['username'])
    basket=Basket(user=user, good=good, status=False)
    basket.save()
    data={}
    data ['result'] = "1"
    return HttpResponse(json.dumps(data), content_type="application/json")


def removeBasket(request):
    good=Good.objects.get(pk=requsest['id'])
    user=User.objects.filter(username=request.user['username'])
    Basket.objects.filter(user=user, good=good).delete()
    data={}
    data ['result'] = "1"
    return HttpResponse(json.dumps(data), content_type="application/json")

def basketList(request):
    user=User.objects.filter(username=request.user['username'])
    bs=Basket.objects.filter(user=user)
    data={}
    list=[]
    for basket in bs:
        list.append({"name":basket.good['name']})
    data ['result'] = "1"
    data ['basketList'] = list
    return HttpResponse(json.dumps(data), content_type="application/json")




def buy(request):
    user=User.objects.filter(username=request.user['username'])
    basket=Basket.objects.filter(user=user)
    for bs in basket:
        bs.status=True
    basket.save()
    data={}
    data ['result'] = "1"
    return HttpResponse(json.dumps(data), content_type="application/json")