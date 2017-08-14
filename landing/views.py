from django.shortcuts import render


def main(request):
    context = {}
    template = 'main.html'
    return render(request, template, context=context)
