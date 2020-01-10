from django.shortcuts import render
from listings.models import Listing
from realtors.models import Realtor

# Create your views here.
def about(request):
    realtors = Realtos.objects.order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)
    context = {
        'realtors': realtors,
        'mvp_realtors': mvp_realtors
    }
    return render(request, 'pages/about.html', context)