from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Item
from django.template import loader
from .forms import ItemForm
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

# Create your views here.
def index(request):
    item_list = Item.objects.all()
    #template = loader.get_template('food/index.html')
    context = {
        'item_list': item_list,
    }
    return render(request, 'food/index.html', context)
    #return HttpResponse(template.render(context, request))

#Another Way Class based view
class IndexClassView(ListView):
   model = Item
   templateName = 'food/index.html'
   context_object_name = 'item_name'


def item(request):
    return HttpResponse('this is an item view')

def details(request, item_id):
    item = Item.objects.get(pk=item_id)
    context ={
        'item' : item
    }
    return render(request, 'food/detail.html', context)

    #return HttpResponse('this is item id: %s' %item_id)
#class Based
class FoodDetail(DetailView):
    model = Item
    template_name = 'food/detail.html'



class foodDetail(DetailView):
    model = item
    template_name = 'food/detail.html'

def create_item(request):
    # print(request)
    # breakpoint()
    form = ItemForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-from.html', {'form' : form})

#Classbased View
# this is a class based view for create item
 
class CreateItem(CreateView):
    model = Item;
    fields = ['item_name','item_description','item_price','item_image']
    template_name='food/item-from.html'
 
    def form_valid(self,form):
        form.instance.user_name = self.request.user
 
        return super().form_valid(form)





def update_item(request, id):
    item = Item.objects.get(id =id)
    form = ItemForm(request.POST or None, instance=item)

    if form.is_valid():
        form.save()
        return redirect('food:index')
    
    return render(request, 'food/item-from.html', {'form':form, 'item':item})


def delete_item(request, id):
    item = Item.objects.get(id = id)
    if request.method == 'POST':
        item.delete()
        return redirect('food:index')
    
    return render(request, 'food/item-delete.html', {'item':item})




    
