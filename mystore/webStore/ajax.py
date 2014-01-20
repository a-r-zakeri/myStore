from django.http import *
from webStore import models
import json


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