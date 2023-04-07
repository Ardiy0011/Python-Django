# Ardiy0011

## Introduction

Chowshack is a food service app that allows users to navigate through an array of meals and beverages, make payment and have the meals delivered to them or a self pick up option is also available.

The project makes use of the python Framework Django, html, CSS, python and vanila javascript.

*pages and templates*

**python backend setup pages**

## URLS.PY

In the urls .py I made use of the `Class-based` views thus no extra `urls .py` file was created for creating the routes to the html templates.

## VIEWS.PY

The views.py functions working in conjunction with the class-based `urls .py` page is also reference based on the view class.

Both Menulist, OrderModel Models were imported to be utilized by all the views created.

## MODELS.PY

I created 3 models for this project; Menulist, Category and Ordermodel.Each model giving admin access to create new menu categories for meals to be advertised on the site.

* the  __Category model__ designates the category an assigned order or item to be assgned.The Category model is also linked to the menu item as well as the category model hence each category can contain many or serveal menu items and each menu item can be attributed to several categories.

* the __menulistmodels__ contains the name, description and price to be rendered by the html for withing the order menu templates.It hold the menu item fields of the site essentially.

* the __Ordermodel__ contains the orderdetails of a particular order  under a partiicular category to be rendered by the html template e.g the `is_paid` model to determine if payment of the product has been made.Each menu item can have multiple orders and each order can be associated with several menu items.

## Frontend setup files and folders

## STATIC FOLDER

This folder contains:

* the media (images) folder linked to the urls.py and settings file named ("menu_pages")
* the CSS styling file named ("style.css") and
* the Javascript functions file for frontend effects named("script.js")

## TEMPLATES/HTML PAGES

This file contains all the templates renderd by the python class functions in the view.py page.
* Layoutpage:

This page serves as a nexus and commmon feature page among majority of the templates, the features of this page run accross most of the rendered pages.In more specific terms it makes use of a block  and block end to include both a common navbar and a footer to all pages to applicable pages or templates.

* Navbar and footer:
.
these extend to the  layout page and which is in turn extended to most of the pages if needed

* Indexpage:

This is the page that greets the user and ushers them through the food ordering process.

* Storepage:

This page provides users with options on what type of meal journey they want to partake in ,ie whether local cuisine of Ghana or international meals not native of Ghana.

* Orderpages:

After selecting the genre of meal jorney this page provides users with an array of options of meals from various undisclosed vendors. the main Vendors are however published on the index page but have no association to each meal.The user selects each meal and keys in delivery details

* Order confirmation page:

This page shows the summary of an order placed by the user as well as the payment button.

* payment confirmation page:

After payment has been made an email for confirmation is sent and payment success page appears with delivery and preparation message.

* menupage:

contains current menu of Chowshack.

* Contactpage:

Users can send emails to shop with review etc(this is not the focus of this project though,merely peripheral)


*Distinctiveness and Complexity*

**Responsive design**

This app satisfies the distinctiveness and complexity requirements because the above pages are fully responsive for either desktop, tablet and dedicated mobile devices.
 
**Api implementation**
This app satisfies the distinctiveness and complexity requirements because  the app makes use of a retrofited payment system api for users to make payments in Chowshack

**Data retieval**

This app satisfies the distinctiveness and complexity requirements because it makes use of loops to retrieve data from models contextualised in the views,py page within the admin panel.

**Ordering Sytem**

This app satisfies the distinctiveness and complexity requirements because after meal items are selected and delivery details are keyed in the app gathers each model item within the form along with its associated price model, calculates the total price to be displayed to user on the order summary page

**Aesthetics**

This app satisfies the distinctiveness and complexity requirements because the aesthetic features such as the implementation of overlay image cards, swipers, scroll reveal effects and carousels enhance the user experience and flow.


*How it works/running application:*

**Order button on index page**:

The user runs the command `python manage.py runserver(optional server no.)`.According to the arrangemnt and order the url in the `urls .py` file the index page runs the python function in the views .py file named `indexpage` which in turn renders the index.html template or the index page on the homepage in the windows.

The user then clicks the `order` button either  in the navigation bar or the button clearly displayed  at the center of the home section of the homepage which passes a command from the link in the `order` button to the `stores url` in the urls.py file  which in turn causes the `storepage` class function in the views.py file to render the storespage. 

* choose a store:

The user is met with a page with two image cards with overlays.hovering over each card causes the css effect of an opaque overlay to appear along with text of information about a store to choose from.

Clicking any of the said image cards passes a command from the link in the "image-card" named `local` or `international` in the storepage to either the `order 1` or `order 2` url in the urls.py file  which in turn causes the `orderpage1` or `orderpage2` class function in the views.py file to render the order menu page.
 
* Order Menu page:

After the local and international image cards are clicked in the storespage next is the order menu page which contains a form with a "for loop" which generates several instances of a particular order depending on the amount of orders created in a category on the /admin server.Each form references the category model image, description and price which is rendered and displayed in the order1.html or order2.html templates depending on what the user chooses.

* Select meal:

On the order menu page the user is provided with several meal choices(generated for loop orders).To select a meal in the order1 or 2.html page respectively by clicking a checkbox which grabs the particular model items found within a meal category listed in the dictionary of the `Orderpage` class function in the views py file. The user then scrolls down and is introduced to an order details form which allows user to input delivery details and then confirm the meals chosen.This is done by clicking the `confrim order` button at the bottom of the page after which the orderpage model function gathers each model item found within the order form along with its associated price model and calculates the total price to be displayed to the user on the order summary page

* Confirm:

After clicking the `order` button which passes a command from the link embedding in the `confirm order` button to the "orderconfirm url" in the urls.py file which in turn causes the "Orderconfirmationpage" class function in the views.py file to render the order_confirmation html tmeplate which displays a summary of the order, its price and the total price of all the orders selected, the user then clicks the payment system button(in this case pay pal).

* Pay pal Api:

Clicking the Pay pal generated button triggers an api fetch using already written script from the pay pal documentation site found in the script.js file in the static folder. The user is then taken through the payment process on the pay pal platform.finishing the payment proceess triggers the views.py function found in the orderconfirmation class function which determines if indeed payment has been made then renders the payemnt confirmation template.An email of confrimation is then sent to the email provided in the order menu page by the user.

(for the purposes of this project I only made use of Paypals API)

*additional python packages*
crispy forms

*Dependencies:*
django pip,
crispy forms,
pillow,
paypalAPI,
scrollreveal,
ajax,
bootstrap,
msql.

## Link demonstrating functionality

https://youtu.be/ml6p82OuvNs

Hope you enjoy my project! :)
