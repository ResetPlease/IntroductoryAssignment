from django.shortcuts import render
from .models import ImgBank
from .forms import ImgBankForm

def main(resp):
    if resp.method == 'POST':
        form = ImgBankForm(resp.POST, resp.FILES)
        if form.is_valid():
            form.save()
            return render(resp, 'bank/mainpage.html', {'form': form})
    else:
        form = ImgBankForm()
    return render(resp,"bank/mainpage.html", {"form":form})

def imagebank(resp):
    images = ImgBank.objects.all()
    return render(resp, "bank/bank.html", {"data":images})