from django.http import HttpResponse
from django.template import loader
from members.models import Member



def members(request):
  template = loader.get_template('myfirst.html')
  return HttpResponse(template.render())

def mymemb(request):
  mymembers = Member.objects.all().values()
  template = loader.get_template('all_members.html')

  context = {
    'mymembers': mymembers
  }

  return HttpResponse(template.render(context,request))

def details(request,id):
  mymember = Member.objects.get(id=id)
  template = loader.get_template('details.html')
  context = {
    'mymember': mymember
  }

  return HttpResponse(template.render(context,request))


def main(request):
  template = loader.get_template('main.html')
  return HttpResponse(template.render())



def testing(request):
  # template = loader.get_template('template.html')
  # context = {
  #   'fruits': ['Apple', 'Banana', 'Cherry'],
  # }
  # return HttpResponse(template.render(context, request))

  # mydata = Member.objects.all().values()
  # mydata = Member.objects.all()
  # mydata = Member.objects.values_list('firstname', flat=True)
  #mydata = Member.objects.filter(firstname='aman',id=2).values() | Member.objects.filter(firstname='pratvi').values()
  #mydata = Member.objects.filter(firstname__startswith='p').values()
  mydata = Member.objects.all().order_by('firstname','-id').values()
  template = loader.get_template('template.html')
  context = {
    'mymembers' : mydata,
  }
  return HttpResponse(template.render(context,request))


