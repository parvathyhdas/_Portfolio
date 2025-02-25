from django.shortcuts import render,redirect
from PortApp.models import ContactDB
from django.contrib import messages

# Create your views here.
def indexPage(request):
    return render(request,"_Portfolio.html")

def saveContact(request):
    if request.method == "POST":
        na = request.POST.get("name")
        em = request.POST.get("email")
        su = request.POST.get("subject")
        me = request.POST.get("message")
        obj = ContactDB(Name=na, Email=em, Subject=su, Message=me)
        obj.save()
        messages.success(request,"Message sent successfully..")
        return redirect(indexPage)