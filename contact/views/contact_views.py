from django.shortcuts import render
from contact.models import Contact

# Create your views here.
def index(request):
    # Pega todos os contatos que o parâmetro shoe é True do model Contact
    contacts = Contact.objects.filter(show=True).order_by('-id')
    context = {
        'contacts': contacts,
    }
    return render(request,
                  "contact/index.html",
                  context
)