from django.shortcuts import render, HttpResponse
from home.models import Contact
from home.models import Product
from django.contrib import messages
from django.core.serializers import serialize
import json
def index(request):
   
    product =  Product.objects.all()
    para = {
        'product' : product,
    }
    
    return render(request, 'index.html',para)
def about(request):
    return render(request, 'about.html')
def services(request):
    product =  Product.objects.all()
    serialized_data = serialize('json',product)

    # para = {
    #     'product' : product,
    # }
    # params= {
    #     'product' : Product.objects.all(),
        
    # }
    return render(request, 'services.html',{'product' : serialized_data})




    # all_users = Product.objects.all()
    # list_colmns = ['product_name', 'price', 'product_quantity','image']
    # list_rows = []
    # for user in all_users:
    #       list_rows.append(
    #          [user.product_name, user.price, user.product_quantity,user.image ])
    # total_price = 0
    # for x in list_rows:
    #     total_price += int(x[2])*int(x[1])
    # return render(request, 'services.html', {"list_rows": list_rows, "list_colmns": list_colmns, "total_price" : total_price})


    # products = Product.objects.all(),
    # params = {
    #      "product" : products,
         
    #      "range" : 3
    # }
 
    # return render(request, 'services.html',params)
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        number = request.POST.get('number')
        email = request.POST.get('email')
        password = request.POST.get('password')
        contact = Contact(name = name,number = number, email = email,password = password )
        contact.save()
        messages.success(request, "Your details has been added sucessfully!")

    return render(request, 'contact.html')

def productview(request,myid):
    product = Product.objects.all().filter(id = myid);
    print(product)
    return render(request, 'productview.html')