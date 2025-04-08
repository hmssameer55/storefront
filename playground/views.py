from django.shortcuts import render
from django.core.mail import send_mail  
from django.http import HttpResponse


def say_hello(request):
    send_mail(
        'Subject here', # subject
        'Here is the message.', # message
        'admin@example.com', # from email
        ['other@example.com'], # to email
        fail_silently=False, # if the email fails, it will not raise an exception
    )
    return HttpResponse('Email sent successfully')
