from django.shortcuts import render


def home(request):
    context = locals()
    template = 'home.html'
    return render(request, template, context=context)


def about(request):
    context = locals()
    template = 'about.html'
    return render(request=request, template_name=template, context=context)
