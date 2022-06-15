from django.shortcuts import render
from django.views.generic.list import ListView
from receipts.models import Receipt
# Create your views here.


class ReceiptListView(ListView):
    model = Receipt
    template_name = "receipts/list.html"
    context_object_name = "receiptlist"
    fields = ["vendor", "total", "tax", "date", "category", "account"]
