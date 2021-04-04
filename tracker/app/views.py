from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from . scrap import scrapWeb




def dashboard(request):
       
    print(request.GET)   
    context = {
        'scrappedContent' : scrapWeb(),
        'formData' : request.GET
    }
    # return HttpResponse("Welcome tom Shenovate")
    return render(request, 'index.html', context)




