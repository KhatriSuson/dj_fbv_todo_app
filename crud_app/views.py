from django.shortcuts import render, HttpResponseRedirect
from crud_app.models import Crud

# Create your views here.

def crud_create(request):
    if request.method == "GET":
        return render(request, "bootstrap/crud_create.html")

    else:
        dis = request.POST["dis"]
        title = request.POST["title"]
       
        Crud.objects.create(title=title, dis=dis)
        return HttpResponseRedirect("/")

    
def crud_list(request):
    cruds = Crud.objects.all()
    context = {"cruds": cruds}
    return render(request, "bootstrap/crud_list.html", context)


def crud_update(request, id):
    crud = Crud.objects.get(id=id)
    if request.method == "GET":
        return render(request, "bootstrap/crud_update.html", {"crud":crud},)
    else:
        crud.title = request.POST["title"]
        crud.dis = request.POST["dis"]
        crud.save()
        return HttpResponseRedirect("/")    
    
def crud_delete(request, id):
    crud = Crud.objects.get(id=id)
    crud.delete()
    return HttpResponseRedirect("/")
    