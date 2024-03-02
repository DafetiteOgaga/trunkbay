from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'trunkbay_app/index.html')

def home_proj(request):
    return render(request, 'index_proj_level.html')
