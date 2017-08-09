from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)

    if form.is_valid():
        print(request.POST)
    context = locals()
    template = 'contact.html'
    return render(request=request, template_name=template, context=context)