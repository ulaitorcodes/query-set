from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . scrap import scrapWeb




def dashboard(request):
    context = {
        'scrappedContent' : scrapWeb()
    }
    # return HttpResponse("Welcome tom Shenovate")
    return render(request, 'index.html', context)




