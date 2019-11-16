from django.shortcuts import render ,redirect

from.models import Email_Newsletter
from django.shortcuts import render
from django.http import HttpResponse

def email_subscription(request):
    if request.method == "POST":
        email =request.POST.get("email_subscription")
        subscription = Email_Newsletter(Email=email)
        subscription.save()
    else:
        return redirect('/')
    