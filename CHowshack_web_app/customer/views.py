import json
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import JsonResponse
from django.shortcuts import HttpResponse, HttpResponseRedirect, render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render ,redirect
from django.views import View
from django.core.mail import send_mail
from .models import Menulist, OrderModel


class Indexpage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/index.html')
    
class Storespage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/stores.html')

class Contactpage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/contact.html')

class Menupage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/menu.html')
    
class Orderpage1(View):
    def get(self, request, *args, **kwargs):
        #used to get all items from each category created
        
        Rice_Dishes = Menulist.objects.filter(category__name__contains='Rice')
        local_Cuisine = Menulist.objects.filter(category__name__contains='local')
        Desserts = Menulist.objects.filter(category__name__contains='Dessert')
        Sides = Menulist.objects.filter(category__name__contains='Side')
        Beverages = Menulist.objects.filter(category__name__contains='Beverage')
        asankadelight = Menulist.objects.filter(category__name__contains='Fufu')
        chris = Menulist.objects.filter(category__name__contains='Fufu')
        kfc = Menulist.objects.filter(category__name__contains='Streetwise2')
        rigabs = Menulist.objects.filter(category__name__contains='Assorted Jollof rice and chicken')
        SugarDoughnuts = Menulist.objects.filter(category__name__contains='bakeshop')
        internationals = Menulist.objects.filter(category__name__contains='International')
        breakfasts = Menulist.objects.filter(category__name__contains='Breakfast')
        lunchs = Menulist.objects.filter(category__name__contains='Lunch')
        drinks = Menulist.objects.filter(category__name__contains='Drinks')
        locals = Menulist.objects.filter(category__name__contains='Local')

        
        #we have to pass the above function to through the context 
        context ={
            'Rice_Dishes' : Rice_Dishes,
            'local_Cuisine' : local_Cuisine,
            'Desserts' : Desserts,
            'Sides' : Sides,
            'Beverages' : Beverages,
            'asankadelight' : asankadelight,
            'chris' : chris,
            'kfc' : kfc,
            'rigabs' : rigabs,
            'SugarDoughnuts' : SugarDoughnuts,
            'internationals' : internationals,
            'breakfasts' : breakfasts,
            'lunchs' : lunchs,
            'drinks' : drinks,
            'locals' : locals,

        }
        
        return render(request, 'customer/order1.html', context)


class Orderpage2(View):
    def get(self, request, *args, **kwargs):
        #used to get all items from each category created
        
        Rice_Dishes = Menulist.objects.filter(category__name__contains='Rice')
        local_Cuisine = Menulist.objects.filter(category__name__contains='local')
        Desserts = Menulist.objects.filter(category__name__contains='Dessert')
        Sides = Menulist.objects.filter(category__name__contains='Side')
        Beverages = Menulist.objects.filter(category__name__contains='Beverage')
        asankadelight = Menulist.objects.filter(category__name__contains='Fufu')
        chris = Menulist.objects.filter(category__name__contains='Fufu')
        kfc = Menulist.objects.filter(category__name__contains='Streetwise2')
        rigabs = Menulist.objects.filter(category__name__contains='Assorted Jollof rice and chicken')
        SugarDoughnuts = Menulist.objects.filter(category__name__contains='bakeshop')
        internationals = Menulist.objects.filter(category__name__contains='International')
        breakfasts = Menulist.objects.filter(category__name__contains='Breakfast')
        lunchs = Menulist.objects.filter(category__name__contains='Lunch')
        drinks = Menulist.objects.filter(category__name__contains='Drinks')
        locals = Menulist.objects.filter(category__name__contains='Local')

        
        #we have to pass the above function to through the context 
        context ={
            'Rice_Dishes' : Rice_Dishes,
            'local_Cuisine' : local_Cuisine,
            'Desserts' : Desserts,
            'Sides' : Sides,
            'Beverages' : Beverages,
            'asankadelight' : asankadelight,
            'chris' : chris,
            'kfc' : kfc,
            'rigabs' : rigabs,
            'SugarDoughnuts' : SugarDoughnuts,
            'internationals' : internationals,
            'breakfasts' : breakfasts,
            'lunchs' : lunchs,
            'drinks' : drinks,
            'locals' : locals,

        }
        
        return render(request, 'customer/order2.html', context)


class breakfastpage(View):
    def get(self, request, *args, **kwargs):


        Rice_Dishes = Menulist.objects.filter(category__name__contains='Rice')
        local_Cuisine = Menulist.objects.filter(category__name__contains='local')
        Desserts = Menulist.objects.filter(category__name__contains='Dessert')
        Sides = Menulist.objects.filter(category__name__contains='Side')
        Beverages = Menulist.objects.filter(category__name__contains='Beverage')
        asankadelight = Menulist.objects.filter(category__name__contains='Fufu')
        chris = Menulist.objects.filter(category__name__contains='Fufu')
        kfc = Menulist.objects.filter(category__name__contains='Streetwise2')
        rigabs = Menulist.objects.filter(category__name__contains='Assorted Jollof rice and chicken')
        SugarDoughnuts = Menulist.objects.filter(category__name__contains='bakeshop')
        internationals = Menulist.objects.filter(category__name__contains='International')
        breakfasts = Menulist.objects.filter(category__name__contains='Breakfast')
        lunchs = Menulist.objects.filter(category__name__contains='Lunch')
        drinks = Menulist.objects.filter(category__name__contains='Drinks')
        locals = Menulist.objects.filter(category__name__contains='Local')

        
        #we have to pass the above function to through the context 
        context ={
            'Rice_Dishes' : Rice_Dishes,
            'local_Cuisine' : local_Cuisine,
            'Desserts' : Desserts,
            'Sides' : Sides,
            'Beverages' : Beverages,
            'asankadelight' : asankadelight,
            'chris' : chris,
            'kfc' : kfc,
            'rigabs' : rigabs,
            'SugarDoughnuts' : SugarDoughnuts,
            'internationals' : internationals,
            'breakfasts' : breakfasts,
            'lunchs' : lunchs,
            'drinks' : drinks,
            'locals' : locals,

        }

        return render(request, 'customer/breakfast.html')


class lunchpage(View):
    def get(self, request, *args, **kwargs):

        Rice_Dishes = Menulist.objects.filter(category__name__contains='Rice')
        local_Cuisine = Menulist.objects.filter(category__name__contains='local')
        Desserts = Menulist.objects.filter(category__name__contains='Dessert')
        Sides = Menulist.objects.filter(category__name__contains='Side')
        Beverages = Menulist.objects.filter(category__name__contains='Beverage')
        asankadelight = Menulist.objects.filter(category__name__contains='Fufu')
        chris = Menulist.objects.filter(category__name__contains='Fufu')
        kfc = Menulist.objects.filter(category__name__contains='Streetwise2')
        rigabs = Menulist.objects.filter(category__name__contains='Assorted Jollof rice and chicken')
        SugarDoughnuts = Menulist.objects.filter(category__name__contains='bakeshop')
        internationals = Menulist.objects.filter(category__name__contains='International')
        breakfasts = Menulist.objects.filter(category__name__contains='Breakfast')
        lunchs = Menulist.objects.filter(category__name__contains='Lunch')
        drinks = Menulist.objects.filter(category__name__contains='Drinks')
        locals = Menulist.objects.filter(category__name__contains='local')

        
        #we have to pass the above function to through the context 
        context ={
            'Rice_Dishes' : Rice_Dishes,
            'local_Cuisine' : local_Cuisine,
            'Desserts' : Desserts,
            'Sides' : Sides,
            'Beverages' : Beverages,
            'asankadelight' : asankadelight,
            'chris' : chris,
            'kfc' : kfc,
            'rigabs' : rigabs,
            'SugarDoughnuts' : SugarDoughnuts,
            'internationals' : internationals,
            'breakfasts' : breakfasts,
            'lunchs' : lunchs,
            'drinks' : drinks,
            'locals' : locals,

        }
        return render(request, 'customer/lunch.html')


class drinkpage(View):
    def get(self, request, *args, **kwargs):

        Rice_Dishes = Menulist.objects.filter(category__name__contains='Rice')
        local_Cuisine = Menulist.objects.filter(category__name__contains='local')
        Desserts = Menulist.objects.filter(category__name__contains='Dessert')
        Sides = Menulist.objects.filter(category__name__contains='Side')
        Beverages = Menulist.objects.filter(category__name__contains='Beverage')
        asankadelight = Menulist.objects.filter(category__name__contains='Fufu')
        chris = Menulist.objects.filter(category__name__contains='Fufu')
        kfc = Menulist.objects.filter(category__name__contains='Streetwise2')
        rigabs = Menulist.objects.filter(category__name__contains='Assorted Jollof rice and chicken')
        SugarDoughnuts = Menulist.objects.filter(category__name__contains='bakeshop')
        internationals = Menulist.objects.filter(category__name__contains='International')
        breakfasts = Menulist.objects.filter(category__name__contains='Breakfast')
        lunchs = Menulist.objects.filter(category__name__contains='lunch')
        drinks = Menulist.objects.filter(category__name__contains='drinks')
        locals = Menulist.objects.filter(category__name__contains='Local')

        
        #we have to pass the above function to through the context 
        context ={
            'Rice_Dishes' : Rice_Dishes,
            'local_Cuisine' : local_Cuisine,
            'Desserts' : Desserts,
            'Sides' : Sides,
            'Beverages' : Beverages,
            'asankadelight' : asankadelight,
            'chris' : chris,
            'kfc' : kfc,
            'rigabs' : rigabs,
            'SugarDoughnuts' : SugarDoughnuts,
            'internationals' : internationals,
            'breakfasts' : breakfasts,
            'lunchs' : lunchs,
            'drinks' : drinks,
            'locals' : locals,

        }
        return render(request, 'customer/drinks.html')

    #now to post the menu price category etc page 
    def post(self, request, *args, **kwargs): 
        name = request.POST.get('name')#these are for the form in the order.html  
        email = request.POST.get('email')#these are for the form in the order.html 
        street = request.POST.get('street')#these are for the form in the order.html 
        region = request.POST.get('region')
        city = request.POST.get('city')
        zip_code = request.POST.get('zip')
        
        #grab all the selected items and return
        #so we first create a dictionary to store all of our items selected
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')#getting the items and making lis of items selected
        
        for item in items:
            menu_item = Menulist.objects.get(pk__contains=int(item))
            item_data = {
                'id': menu_item.pk,
                'name': menu_item.name,
                'price': menu_item.price
            }

            order_items['items'].append(item_data) #append into the above list
            
            # now we calculate the total price to be displayed to user
            price = 0
            item_ids = []

        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            price=price,
            name=name,
            email=email,
            street=street,
            region=region,
            city=city,
            zip_code=zip_code
        )
        order.items.add(*item_ids)
        
        # After everything is done, send confirmation email to the user
        
        body = ('Thank you for your order! Meal Prep Ongoing and will be delivered shortly!\n'  #lets define ou email mesage body shall we,note always define body untop of function
                f'Your bill: Ghs {price}\n'
                'Have a yummy day!')
        
        send_mail(
            'Thank You For Your Order!',#subject
            body,
            '............@.com',#from
            [email],#to
            fail_silently=False
        )
        
        context = {
            'items': order_items['items'],
            'price': price
        }

        return redirect('orderconfirmation', pk=order.pk)


class Orderconfirmationpage(View):
    def get(self, request, pk, *args, **kwargs):
        order = OrderModel.objects.get(pk=pk)

        context = {
            'pk': order.pk,
            'items': order.items,
            'price': order.price,
        }
        return render(request, 'customer/order_confirmation.html', context)

    def post(self, request, pk, *args, **kwargs):
        data = json.loads(request.body)
        if data['isPaid']:
            order =OrderModel.objects.get(pk=pk)
            order.is_paid =True
            order.save()
        return redirect('payment')

class Paymentconfirmationpage(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'customer/paymentconfirmation.html')
