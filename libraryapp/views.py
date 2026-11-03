from django.shortcuts import render
from django.views.generic import View
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
class Book_View(View):
    def get(self,request):
        data = [
        {
            "ID" : 201,
            "Book_Name" : "Python Programming",
            "Author" : "Mark Lutz",
            "Category":"Programming",
            "Price":500,
            "published_year":2022,
            "Availability":True
        },
        {
                "ID": 202,
                "Book_Name": "Django for Beginners",
                "Author": "William S. Vincent",
                "Category": "Web Development",
                "Price": 650,
                "Published_year": 2023,
                "Availability": True
            },
        {
                "ID": 203,
                "Book_Name": "Clean Code",
                "Author": "Robert C. Martin",
                "Category": "Software Engineering",
                "Price": 700,
                "Published_Year": 2008,
                "Availability": False
            }
        ]
        return JsonResponse(data,safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class Add_Book_View(View):
    def post(self, request):
        data = request.body
        form_data = loads(data)

        Book_Name = form_data.get('Book_Name')
        Author = form_data.get('Author')
        category = form_data.get('Category')
        Price = form_data.get('Price')
        Published_Year = form_data.get('Published_Year')
        Availability = form_data.get('Availability')

        Book = {
            "Book_Name": Book_Name,
            "Author": Author,
            "category": category,
            "Price": Price,
            "Published_Year": Published_Year,
            "Availability": Availability
        }

        return JsonResponse(Book)

@method_decorator(csrf_exempt, name='dispatch')
class Update_Book_View(View):
    def put(self, request):
        data = request.body
        form_data = loads(data)

        Book_id = form_data.get('id')
        Book_name = form_data.get('Book_Name')
        Author = form_data.get('Author')
        Category = form_data.get('Category')
        Price = form_data.get('Price')
        Published_Year = form_data.get('Published_Year')
        Availability = form_data.get('Availability')

        Book = {
            "ID": Book_id,
            "Book_Name": Book_name,
            "Author": Author,
            "Category": Category,
            "Price": Price,
            "Published_Year": Published_Year,
            "Availability": Availability
        }

        return JsonResponse(Book)