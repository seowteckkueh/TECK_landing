from django.http.response import Http404
from django.shortcuts import render
from django.http import HttpResponse,Http404


from .models import EmailEntry # import EmailEntry
from .forms import EmailEntryForm

# Create your views here.
def email_entry_get_view(request, id, *args, **kwargs): 
    try:
        obj=EmailEntry.objects.get(id=id) 
    except EmailEntry.DoesNotExist: #specific exception
        raise Http404
        
    #return render(request, "get.html",{"email":obj.email})
    return render(request, "get.html",{"object":obj})

def email_entry_create_view(request):
    form = EmailEntryForm()
    return render(request, "form.html", {"form":form})