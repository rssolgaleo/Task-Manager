from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _

class HomePageView(TemplateView):
    template_name = 'home.html'
