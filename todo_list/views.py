
from django.shortcuts import render, redirect
from .forms import ListForm
from django.contrib import messages
from .models import List



def todo(request):
    if request.method == 'POST':
        form = ListForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = List.objects.all
            messages.success(request,('Item has been added'))
            return render(request, 'todo_list/home1.html', {'all_items':all_items})
    else:
        all_items = List.objects.all
        return render(request, 'todo_list/home1.html', {'all_items':all_items})


def delete(request, list_id):
    item = List.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item has been deleted!'))
    return redirect('todo')

def cross_off(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = True
    item.save()
    return redirect('todo')

def uncross(request, list_id):
    item = List.objects.get(pk=list_id)
    item.completed = False
    item.save()
    return redirect('todo')
