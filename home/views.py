from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
import requests
# Create your views here.
def index(request):
    return render(request,"home/index.html")

def calculate(request):
    if request.method=='GET':
        return HttpResponseRedirect(reverse("index"))
    base=request.POST.get("fromCurrency")
    other=request.POST.get("toCurrency")
    amount=float(request.POST.get("amount"))
    res = requests.get("https://api.exchangeratesapi.io/latest",
                    params={"base":base, "symbols":other})
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = res.json()
    rate = float(data["rates"][other])
    final=amount*rate
    return render(request,"home/result.html",{'base':base,'other':other,'amount':amount,'final':final})
    

def dateconvert(request):
    if request.method=='POST':
        base=request.POST.get("fromCurrency")
        other=request.POST.get("toCurrency")
        amount=float(request.POST.get("amount"))
        date=request.POST.get('date')
        base_url="https://api.exchangeratesapi.io/"+ date
        res= requests.get(base_url,
                        params={"base":base, "symbols":other})
        if res.status_code != 200:
            raise Exception("ERROR: API request unsuccessful.")
        data = res.json()
        rate = float(data["rates"][other])
        final=amount*rate
        return render(request,"home/result.html",{'base':base,'other':other,'amount':amount,'final':final,'date':date})
    return render(request,'home/date.html')
