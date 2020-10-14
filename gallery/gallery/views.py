from django.shortcuts import render
from gallery.models import gallery


def gallerydisplay(request):
    resultsdisplay=gallery.objects.all()
    return render(request,'index.html',{'gallery':resultsdisplay})