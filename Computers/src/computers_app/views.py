from django.shortcuts import render, redirect
from computers_main.models import MainHrHrMaster
from .models import *
from .forms import computer_inventoryForm
# Create your views here.
def dashboard(request):
    context = {}
    context.update({'title' : 'Dashboard'})

    CompModel = ComputerModel.objects.all()
    clist =[]
    for i in CompModel:
        instock = 0
        instock = computer_inventory.objects.filter(item_model=i.model_description).filter(item_status='IN-STOCK').count()
        inuse = 0
        inuse = computer_inventory.objects.filter(item_model=i.model_description).filter(item_status='IN-USE').count()
        defective = 0
        defective = computer_inventory.objects.filter(item_model=i.model_description).filter(item_status='DEFECTIVE').count()
        tot = instock + inuse +defective
        info = {
            'model' : i.model_description,
            'instock' : instock,
            'inuse' : inuse,
            'def' : defective,
            'total' : tot,
            'type' : i.item_type.item_description
        }
        clist.append(info)

    
    context.update({'clist':clist})


    return render(request, 'computers_app/dashboard.html', context)


def table(request, mdl):
    context = {}
    context.update({'title' : 'Table'})
    cinv = computer_inventory.objects.all()
    

    context.update({'cinv' : cinv})
    if mdl == 'all':
        context.update({'mdl' : '' })
    else:
        context.update({'mdl' : mdl })
    return render(request, 'computers_app/table.html', context)



def item(request, pk):
    context = {}
    context.update({'title' : 'Item'})

    comp = computer_inventory.objects.get(id=pk)
    form = computer_inventoryForm(instance=comp)

    if request.method =='POST':
        form =computer_inventoryForm(request.POST or None, instance=comp)
        if form.is_valid():
            form.save()    
            return redirect('table', 'all')
        else:
            print(form.errors)

    context.update({'form' : form })


    return render(request, 'computers_app/item.html', context)


def sync(request):
    context = {}
    context.update({'title' : 'Sync'})

    hrmaster = MainHrHrMaster.objects.using('main').all()

    for i in hrmaster:
        if len(UserNames.objects.filter(idno=i.idno)) == 0:
            b = UserNames(idno=i.idno, last_name=i.last_name, first_name=i.first_name, nick_name=i.nick_name)
            b.save()


    return render(request, 'computers_app/sync.html', context)