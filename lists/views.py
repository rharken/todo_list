from django.shortcuts import redirect, render
from django.http import HttpResponse
from lists.models import Item, List

# Create your views here.
def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    list_ = List.lists.get(id=list_id)
    return render(request, 'list.html', {'list' : list_})

def new_list(request):
    list_ = List.lists.create()
    Item.items.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def add_item(request, list_id):
    list_ = List.lists.get(id=list_id)
    Item.items.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')