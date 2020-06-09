from django.shortcuts import render

# Create your views here.

def main(request):
   """ A view to return to the main home page. """
   return render(request,"pages/index.html")