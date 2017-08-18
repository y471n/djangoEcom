from allauth.socialaccount.models import SocialAccount, SocialToken
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def home(request):
    social_account = SocialAccount.objects.filter(user=request.user).first()
    print(social_account.uid)
    token = SocialToken.objects.filter(account=social_account).first()

    context = {'token': token.token}
    template = 'home.html'
    return render(request, template, context=context)


def about(request):
    context = {}
    template = 'about.html'
    return render(request=request, template_name=template, context=context)
