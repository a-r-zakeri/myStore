from django.core.serializers import json
from django.http import *
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from webStore.form import *
from django.shortcuts import render
from webStore.models import *
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login




def main(request):
   return HttpResponse("main")
 
# def ajax(request):
#    # if request.POST.has_key('client_response'):
#    #      x = request.POST['client_response']
#    #      y = socket.gethostbyname(x)
#    #      response_dict = {}
#    #      response_dict.update({'server_response': y })
#    #      return HttpResponse(simplejson.dumps(response_dict), mimetype='application/javascript')
#    # else:
#    return HttpResponse("ajax")


def test(request):
    return render_to_response("test.html")


def searchFunc(param, param1, param2, param3, param4):
    pass


def categoryList(requset):
    return render(requset, "goods.html", {'title':u"لیست محصولات"})


def catList():
    pass


def ajax(request):
    print(request.method)
    if request.method=="POST":
        tmp = searchFunc(request.REQUEST["keyword"],request.REQUEST['catId'],int(request.REQUEST['year']),int(request.REQUEST['month']),int(request.REQUEST['day']))
        page = int(request.REQUEST["page"])
        head = page*9
        tail = head + 9
        if page == ((tmp[0]-1)//9):
            data = [[((tmp[0]-1)//9)+1,tmp[0]%9],tmp[1][head:tail]]
        else:
            data = [[((tmp[0]-1)//9)+1,9],tmp[1][head:tail]]
        json_data = json.dumps(data)
        return HttpResponse(json_data, mimetype="application/json")
    else:
        context = "10"
        return render(request, 'test.html' , context)


def goods(request):
    print("views. gooods: " + request.method)
    return render_to_response("goods.html", RequestContext(request, {}))



def mainPage(request):

    if request.method != 'POST':
        print("views.mainPage: " + request.method)
        return render_to_response("mainPage.html", RequestContext(request, {'title': u"صفحه‌ی نخست"}))

    if 'uname' in request.POST:
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.clean_uname()
            password = form.clean_pword()
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return ("mainPage.html", RequestContext(request, {}))
        return render(request,"mainPage.html",{
            'form':form,
        })



    form=Register(request.POST)
    if form.is_valid():
        password=form.clean_password()
        cpassword=form.clean_cpassword()
        username=form.clean_username()
        email=form.clean_email()
        user=User.objects.create(username=username, password=password, email=email)
        user.save()


    return render(request,"mainPage.html", {
        'form':form,
    })



def specification(request):
    form=ContactForm()
    if request.method !='POST':
        return render(request,"specification.html",{
            'form':form, 'title':u"مشخصات محصول"
        })


    form=ContactForm(request.POST)
    if form.is_valid():
        sender=form.clean_sender()
        subject=form.clean_subject()
        message=form.clean_message()
        comment = Comment.objects.create(subject=subject, sender=sender, message=message)
        comment.save()

    return render(request,"specification.html",{
            'form':form,
        })


def addGoods(request):
    form=AddGood()
    if request.method !='POST':
        return render(request,"addGood.html",{
            'form':form, 'title':u"افزودن محصول"
        })


    form = AddGood(request.POST, request.FILES)
    if form.is_valid():
        image=form.clean()
        count=form.clean_count()
        name=form.clean_name()
        about=form.clean()
        price=form.clean_price()
        saveImage=Image.objects.create(picUrl=image,pic= request.FILES.get("image"))
        saveImage.save()
        slideShow=SlideShow.objects.create(imageURL=image)
        slideShow.save()
        cat=Category.objects.create(name="majid",parent=None)
        saveGood=Good.objects.create(name=name, category=cat, price= price, count=count, pic= saveImage, slideShow=slideShow)
        saveGood.save()

    return render(request,"addGood.html",{
            'form':form,
        })


