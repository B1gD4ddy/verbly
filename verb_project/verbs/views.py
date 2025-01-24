from django.shortcuts import render
from .models import Verb
# Create your views here.



def home(request):
    if request.method == "POST":
        searched = request.POST['searched']
        verbs = Verb.objects.filter(name__contains=searched)
        return render(request, 'verbs_app/search_verbs.html', {'searched': searched, 'verbs': verbs})
    
    else:
        return render(request, 'verbs_app/home.html')


def search_verb(request):
    if request.method == "POST":
        searched = request.POST['searched']
        verbs = Verb.objects.filter(name__contains=searched)
        return render(request, 'verbs_app/search_verbs.html', {'searched': searched, 'verbs': verbs})
    
