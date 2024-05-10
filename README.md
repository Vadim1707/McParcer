# McParcer application
## Description
This is a small project containing several features:

* Parcing web-site to gather data about McDonald's goods
* API to display product details using Django

## Available endpoints
### /api/all\_products/
List containing all McDonald's products
### /api/products/{product\_name}/
List containing all McDonald's products that match search criteria. API uses inexact search, thats why some funny searches are possible.
> This is made this way so that you can find "Біг Мак®" with just typing "біг мак"
### /api/products/{product\_name}/{product\_field}/
Retrieve method that shows one field of one product, as described in url parameters.
## How to start server
In terminal (not PowerShell):

0. cd to root folder (McParcer)
1. pip install -r requirements.txt 
2. python manage.py runserver

To see all data in other format:

1. Abort server by pressing Ctrl+C
2. python manage.py createsuperuser (create profile for admin access)
3. start server and go to _/admin/_ page.
4. Insert your creditentials here and look at data in more convenient way

## Preview of endpoints


![all_products](https://github.com/Vadim1707/McParcer/blob/master/media/all_products.png)

![all_products](https://github.com/Vadim1707/McParcer/blob/master/media/products_cheese.png)

![all_products](https://github.com/Vadim1707/McParcer/blob/master/media/cheeseburger_salt.png)