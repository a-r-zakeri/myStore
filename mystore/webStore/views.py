from django.core.serializers import json
from django.http import *
from django.shortcuts import render_to_response, render
from django.template import RequestContext
from django.utils import simplejson
import socket
 
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
    return HttpResponse("cat list")

def catList():
    pass


def ajax(request):
    print(request.method)
    if(request.method=="POST"):
        tmp=searchFunc(request.REQUEST["keyword"],request.REQUEST['catId'],int(request.REQUEST['year']),int(request.REQUEST['month']),int(request.REQUEST['day']))
        page=int(request.REQUEST["page"])
        head = page*9
        tail = head + 9
        if page == ((tmp[0]-1)//9):
            data=[[((tmp[0]-1)//9)+1,tmp[0]%9],tmp[1][head:tail]]
        else:
            data=[[((tmp[0]-1)//9)+1,9],tmp[1][head:tail]]
        json_data = json.dumps(data)
        return HttpResponse(json_data, mimetype="application/json")
    else:
        context = "10"
        return render(request, 'test.html' , context)

def goods(request):
    print("views. gooods: " + request.method)
    return render_to_response("goods.html", RequestContext(request, {}))

def mainPage(request):
    print("views.mainPage: " + request.method)
    return render_to_response("mainPage.html", RequestContext(request, {}))