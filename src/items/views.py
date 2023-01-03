
import logging
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Q

from .models import Item
from .forms import ItemForm

# Create logger object
logger = logging.getLogger('django')


# Create your views here.

def create_item(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = ItemForm(request.POST, request.FILES or None)
            if form.is_valid():
                item = form.save(commit=False)
                item.user = request.user
                item.save()
                form = ItemForm()
                logger.info(f'User {request.user} created item "{item.activity}" ')
                messages.success(request, ("Success. You have a new to do on the list"))
                return redirect('create-item')
            else:
                messages.error(request, ("Item was not created "))
                return render(request, 'create-item.html', {})
        else:
            form = ItemForm
            return render(request, 'create_item.html', {'form': form})
    else:
        messages.success(request, ("You must log in to create a task on Todo Un"))
        return redirect('%s?next=%s' % ('users/login', request.path))

    
def view_items(request):
    context = {}
    if request.user.is_authenticated:
        items = Item.objects.filter(user=request.user.id).order_by('-time_created')
        context = {
            'items': items
        }
    
    return render(request, 'items.html', context)


@login_required()
def update_item(request, item_id):
    item = Item.objects.get(pk=item_id, user=request.user.id)
    form = ItemForm(request.POST or None, request.FILES or None, instance=item)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, ("To do item updated"))
            return redirect('list-items')
        
    return render(request, 'update_item.html', {'item': item, 'form': form})


@login_required()
def delete_item(request, item_id):
    item = Item.objects.get(pk=item_id)
    item.is_done = True
    item.time_done = timezone.now()
    item.save(update_fields=['is_done', 'time_done'])
    return redirect('list-items')


@login_required()
def search_items(request):
    q = request.GET.get('q')
    if q:
        search = Item.objects.filter(
            Q(activity__icontains=q) |
            Q(description__icontains=q),
            
            user = request.user.id
        )
        return render(request, 'search.html', {'q': q, 'search': search})
    else:
        return render(request, 'search.html', {})


def view_home(request):
    return render(request, 'home.html', {})

