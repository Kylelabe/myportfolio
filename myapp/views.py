import json
from django.http import HttpResponse
import requests
from django.shortcuts import render,redirect
from requests.auth import HTTPBasicAuth
from django.conf import settings
from django.contrib import messages
from .forms import ContactForm
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.utils import translation

def index(request):
    return render(request, 'index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data['full_name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Construct the email.Body
            email_body = f"""
            Name: {full_name}
            Email: {email}

            Message:
            {message}
            """

            # Send email
            send_mail(
                subject,
                email_body,
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            messages.success(request, 'Your message has been sent successfully!')
            return redirect('index')
    else:
        form = ContactForm()
        print(f"Form rendered: {form}")
    return render(request, 'contact.html', {'form': form})

def set_language(request):
    user_language = translation.GET.get('language','en')
    translation.activate(user_language)
    response = HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    response.set_cookie(settings.LANGUAGE_COOKIE_NAME, user_language)
    return response