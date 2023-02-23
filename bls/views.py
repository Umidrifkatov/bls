from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
def main(request):
    return render(request, 'index.html')

def register(request):
    return render(request, 'bls.html')
