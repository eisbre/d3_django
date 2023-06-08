from django.urls import path
from app.views import index
from app.views import BarChart
from app.views import PieChart

urlpatterns = [
    path("", index, name="index"),
    path("chart1/", BarChart, name="BarChart"),
    path("chart2/", PieChart, name="PieChart"),
]
