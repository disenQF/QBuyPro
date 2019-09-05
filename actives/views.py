from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView

from .models import ActiveModel

class ActiveGoodsView(TemplateView):
    template_name = 'goods_list.html'

    def get_context_data(self, **kwargs):
        context = super(ActiveGoodsView, self).get_context_data(**kwargs)

        active = ActiveModel.objects.get(pk=1)
        context['active'] = active

        return context