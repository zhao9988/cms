from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import datetime
from django import template
from   django1 import settings
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def index (request):
    tep=loader.get_template("polls/mo.html")
    context={
    }
    return  HttpResponse(tep.render(context,request))

def index1(request):
    tep=loader.get_template("polls/son.html")
    context={
    }
    return  HttpResponse(tep.render(context,request))


# def index (request):
#     tep=loader.get_template("polls/current_datetime.html")
#     context={
#         "word":"这是views层",
#         "item_list":[1,2,3,4,5],
#         # "ordered_warranty":True
#     }
#     return  HttpResponse(tep.render(context,request))

# def current_datetime(request):
#     now = datetime.datetime.now()
#     html = "<html><body>It is now %s.</body></html>" % now
#     return HttpResponse(html)

# t = template.Template('My name is {{ name }}.')
# c = template.Context({'name': 'Adrian'})
# print(t.render(c))
# def index1(request):
#     now = datetime.datetime.now()
#     fp = open(settings.BASE_DIR + '/templates/polls/index.html')
#     t = template.Template(fp.read())
#     fp.close()
#     html = t.render(template.Context({'current_date': now}))
#     return HttpResponse(html)



# def current_datetime(request):
#     now = datetime.datetime.now()
#     t = loader.get_template('polls/current_datetime.html')
#     html = t.render({'current_date': now})
#     return HttpResponse(html)
