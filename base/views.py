from django.shortcuts import render, redirect
from django.views.generic import TemplateView, CreateView

from base.forms import ContactCreateForm
from base.models import ContactForm


# Create your views here.
class Dashboard(CreateView):
    model = ContactForm
    template_name = "base.html"
    form_class = ContactCreateForm

    def form_valid(self, form):
        contact_form = form.save(commit=False)
        contact_form.save()
        return redirect("main:main_page")


main_page = Dashboard.as_view()
