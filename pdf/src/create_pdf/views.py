from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from datetime import datetime


from pdf.utils import render_to_pdf #created in step 4

class GeneratePdf(View):
    def get(self, request, *args, **kwargs):
        data = {
            'today': datetime.date.today(), 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
        pdf = render_to_pdf('create_pdf/invoice.html', data)
        return HttpResponse(pdf, content_type='application/pdf')



def topdf(request):
    data = {
            'today': '6/15/2021', 
            'amount': 39.99,
            'customer_name': 'Cooper Mann',
            'order_id': 1233434,
        }
    pdf = render_to_pdf('create_pdf/invoice.html', data)
    return HttpResponse(pdf, content_type='application/pdf')