from django.shortcuts import render, get_object_or_404
from contact.models import Contact


# Create your views here.
def index(request):
    # Pega todos os contatos que o parâmetro shoe é True do model Contact
    contacts = Contact.objects.filter(show=True).order_by('-id')
    context = {
        'contacts': contacts,
        "site_title": "Contatos -"
    }
    return render(request,
                  "contact/index.html",
                  context
)
 
def contact(request, contact_id):
    # single_contact = Contact.objects.filter(pk=contact_id).first()
    # Verifica se o retorno da consulta é None, se sim, retorna o erro 404
    single_contact = get_object_or_404(Contact.objects.filter(pk=contact_id, show=True))
    site_title = f'{single_contact.firts_name} {single_contact.last_name} -'
    context = {
        "contact": single_contact,
        "site_title": site_title,
    }
    return render(request, "contact/contact.html", context)