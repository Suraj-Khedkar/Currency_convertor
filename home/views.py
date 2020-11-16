from django.shortcuts import render,HttpResponse,HttpResponseRedirect,reverse
import requests
from matplotlib import pyplot as plt
import io
import urllib,base64
import pandas as pd

# Create your views here.
def index(request):
    base_url = "https://api.exchangeratesapi.io/latest"
    res = requests.get(base_url)
    if res.status_code != 200:
        raise Exception("ERROR: API request unsuccessful.")
    data = dict(res.json())
    df = pd.DataFrame(data=data)
    print(df)
    rates=df.to_html()
    text_file = open("home/templates/home/rates.html", "w")
    text_file.write(rates)
    text_file.close()
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

def graph(request):
    if request.method=='POST':
        base=request.POST.get("fromCurrency")
        other=request.POST.get("toCurrency")
        amount=float(request.POST.get("amount"))
        date=request.POST.get('date')
        base_url = "https://api.exchangeratesapi.io/"+ date
        res = requests.get(base_url,
                        params={'base':base})
        if res.status_code != 200:
            raise Exception("ERROR: API request unsuccessful.")
        data = dict(res.json())
        del data['rates']['IDR']
        rate = float(data["rates"][other])
        final=amount*rate
        x = list(data["rates"].keys())
        y = list(data["rates"].values())
        fig = plt.figure(figsize=(27,10))
        plt.title(base)
        plt.xlabel('Currency', fontsize=12)
        plt.ylabel('Exchnage Rate', fontsize=12)
        plt.bar(x,y,color=['red', 'blue', 'purple', 'green', 'cyan','magenta','yellow'])
        buffer=io.BytesIO()
        fig.savefig(buffer,format='png')
        buffer.seek(0)
        string=base64.b64encode(buffer.read())
        graph=urllib.parse.quote(string)
        return render(request,"home/graphresult.html",{'base':base,'other':other,'amount':amount,'final':final,'date':date,'graph':graph})
    return render(request,'home/graph.html')

def rates(request):
    return render(request,'home/rates.html')