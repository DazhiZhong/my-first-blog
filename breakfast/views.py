from django.shortcuts import render, get_object_or_404
from django.http import Http404
# Create your views here.
from .models import breakfastho
from django.http import HttpResponse
from .forms import breakfast_form,breakfast_form_new


def breakfast_product_view(request):
    breakfast_object = breakfastho.objects.get(id=1)
    breakfast_object_1 = {
        'breakfast1': breakfast_object
    }
    
    return render(request,'breakfast_page1.html',breakfast_object_1)


'''
def create_breakfast_view(request):
    b_form = breakfast_form()
    if request.method == 'POST':
        b_form = breakfast_form(request.POST )
        if b_form.is_valid():
            print(b_form.cleaned_data)
            breakfastho.objects.create(**b_form.cleaned_data)
    created = {
        'form': b_form
    }
    return render(request,'breakfast_create.html',created)
'''


def create_breakfast_view(request,b_id):# b id used in models and url
    #breakfastobject = breakfastho.objects.get(id=b_id)
    breakfastobject = get_object_or_404(breakfastho,id=b_id)
    objectset = breakfastho.objects.all()
    created = {
        'b': breakfastobject,
        'b_id_up':'b/'+str(b_id+1),
        'b_id_down':'b/'+str(b_id-1),
        'all_objects': objectset
    }
    return render(request, 'bshow.html', created)




def create_new_b_view(request):
    bform = breakfast_form_new(request.POST or None)

    if bform.is_valid:
        #print('ass')
        #print(bform.cleaned_data)
        bform.save()
    bform = breakfast_form_new(request.POST or None)

    created = {
        'form' : bform
    }
    return render(request, 'breakfast_create.html', created)
    