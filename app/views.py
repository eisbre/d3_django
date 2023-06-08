from django.shortcuts import render

def index (request): #request为前端返回的参数
    return render(request, "web.html")


def BarChart (request):
    return render(request, "BarChart.html")


def PieChart(request):
    return render(request, "PieChart.html")
