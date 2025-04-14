from django.shortcuts import render
from django.core.mail import send_mail  
from django.http import HttpResponse
# from .tasks import notify_customers
import requests
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from rest_framework.views import APIView
from rest_framework.response import Response
from django.utils.decorators import method_decorator

@cache_page(timeout=300) 
def say_hello(request):
    # send_mail(
    #     'Subject here', # subject
    #     'Here is the message.', # message
    #     'admin@example.com', # from email
    #     ['other@example.com'], # to email
    #     fail_silently=False, # if the email fails, it will not raise an exception
    # )
    # notify_customers.delay("Hello, world!")
   

   #we will call delay api here and use cache to store the result
   response = requests.get('https://httpbin.org/delay/2')
   data = response.json()
   return HttpResponse(data)


#class based say_hello view with cache  
class SayHelloView(APIView):
   @method_decorator(cache_page(timeout=300))
   def get(self, request):
      response = requests.get('https://httpbin.org/delay/2')
      data = response.json()
      return Response(data)
   
    