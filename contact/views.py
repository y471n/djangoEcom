from django.shortcuts import render
from .forms import ContactForm


def contact(request):
    form = ContactForm(request.POST or None)
    title = 'Contact'
    confirm_message = None
    if form.is_valid():
        print(request.POST)
        title = "Thanks"
        confirm_message = "Thanks for the message. We will get back to you."

    context = {'title': title, 'confirm_message': confirm_message, 'form': form}
    template = 'contact.html'
    return render(request=request, template_name=template, context=context)
