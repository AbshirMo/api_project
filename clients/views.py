from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Branch, Client, Manager


def index(request):
    """View function for home page of site."""
    branch_list = Branch.objects.order_by('-no_of_emps')
    num_branches = Branch.objects.all().count()
    # template = loader.get_template('phonecatalog/index.html')
    context = {
        'branch_list': branch_list,
        'num_branches': num_branches,
    }
    return HttpResponse(render(request, 'clients/index.html', context))
