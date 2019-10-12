from django.shortcuts import render
from .models import Page

# Create your views here.
def page_list(request):
    context = {
        "pages": Page.objects.all()
    }
    return render(request, 'list.html', context)


def page_detail(request, page_id):
    context = {
        "page": Page.objects.get(id=page_id)
    }
    return render(request, 'detail.html', context)
