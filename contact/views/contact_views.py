from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from contact.models import Contact
from django.db.models import Q


# Create your views here.
def index(request):
    # Pega todos os contatos que o parâmetro shoe é True do model Contact
    contacts = Contact.objects.filter(show=True).order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        "site_title": "Contatos -"
    }
    return render(request,
                  "contact/index.html",
                  context
                  )


def search(request):
    search_value = request.GET.get("q", '').strip()

    if search_value == '':
        return redirect("contact:index")
    # Procura todos os contatos que tem o "search" em algum parametro o "Q" junto com o "|" funciona como: If o first_name E o last_name contem o mesmo "search" e retorna
    contacts = Contact.objects.filter(
        show=True)\
        .filter(
            Q(firts_name__icontains=search_value) |
            Q(last_name__icontains=search_value) |
            Q(email__icontains=search_value) |
            Q(phone__icontains=search_value)
    )\
        .order_by('-id')

    paginator = Paginator(contacts, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        "site_title": "Search -"
    }
    return render(request,
                  "contact/index.html",
                  context
                  )


def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # Verifica se o retorno da consulta é None, se sim, retorna o erro 404
    single_contact = get_object_or_404(
        Contact.objects.filter(pk=contact_id, show=True))
    site_title = f'{single_contact.first_name} {single_contact.last_name} -'
    context = {
        "contact": single_contact,
        "site_title": site_title,
    }
    return render(request, "contact/contact.html", context)
