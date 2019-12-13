import json

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse

import requests
import twstock


# Create your views here.
def hello_view(request):
    return render(request, 'index.html');


def stock(request):
    stock_list = {}
    if request.POST:
        stock_id = request.POST['stock_id']

        # 這是抓取歷史資料
        stock_data = twstock.Stock(stock_id)
        stock_na = twstock.codes[stock_id].name
        open_p = stock_data.open[-10:]  # 近十日之開盤價
        date = stock_data.date[-10:]  # 近十日的日期
        stock_list = {'stock_id': stock_id, 'stock_na': stock_na, 'price': open_p, 'date': date}
    return render(request, "stock.html", stock_list);

def corr(request):
    return render(request, "corr.html");

def health(request):
    return render(request, "health.html");
