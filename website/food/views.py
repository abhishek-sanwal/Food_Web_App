from django.forms import BaseModelForm
from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.
from . import models
from .forms import ItemForm

from django.contrib import messages
from django.views.generic import CreateView
'''
Function for Testing Django app
'''


def index(request):

    if request.method == "GET":
        return HttpResponse("<h1>Welcome to My django web page</h>")


'''
View for showing all food items in webpage
'''


def show(request):

    item_lis = models.Item.objects.all()

    return render(request, 'index.html', {
        'lis': item_lis
    })


'''
View for showing particular item based on item_id
'''


def display_item(request, item_id):

    i1 = models.Item.objects.get(pk=item_id)

    return render(request, 'demo.html', {
        'id': i1.id,
        'name': i1.item_name,
        'des': i1.item_description,
        'img': i1.item_image,
        'price': i1.item_price
    })


''''
View for adding item into db and then redirecting to list all items

'''


class CreateItem(CreateView):

    model = models.Item
    fields = ["item_name", "item_description", "item_price", "item_image"]
    template_name = "create.html"

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        form.instance.user = self.request.user
        return super().form_valid(form)


def add_item(request):

    form = ItemForm(request.POST or None)

    if form.is_valid():

        form.save()
        item_name = form.cleaned_data("item_name")
        messages.success(request, f"{item_name} product added successfully.")
        return redirect('show')

    return render(request, 'create.html', {
        'form': form
    })


''''
View for updating item with specific item_id into db and then redirecting to list all items

'''


def update_item(request, item_id):

    item = models.Item.objects.get(pk=item_id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        item_name = form.cleaned_data("item_name")
        messages.success(request, f"{item_name} product updated Successfully.")
        return redirect('show')

    return render(request,
                  'create.html', {
                      'form': form,
                      'item': item
                  })


'''
View for deleting an particular item from db using item_id
'''


def delete_item(request, item_id):

    item = models.Item.objects.get(pk=item_id)

    if request.method == "POST":

        # item_name = item.cleaned_data("item_name")
        item.delete()
        messages.success(
            request, "Product has been deleted successfuly.")
        return redirect('food:show')

    return render(request,
                  'confirm_delete.html', {
                      'item': item
                  })
