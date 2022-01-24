from django.shortcuts import render, HttpResponseRedirect
from .Form import FormList
from .models import DataTODO


# Create your views here.
def response(request):
    form = FormList()
    if request.POST:
        text = request.POST['form_task']
        DataTODO(data_todo=text).save()
        return HttpResponseRedirect('/')
    data = DataTODO.objects.all().order_by('id')
    # data = ["dddd" for _ in range(0, 5)]
    return render(request, 'index.html', {'form': form, 'data': data})


def delete(request, id):
    obj = DataTODO.objects.get(id=id)
    obj.delete()
    return HttpResponseRedirect('/')


def update(request, id):
    obj = DataTODO.objects.get(id=id)
    obj.style_todo = "text-decoration: line-through;"
    obj.save()
    return HttpResponseRedirect('/')
