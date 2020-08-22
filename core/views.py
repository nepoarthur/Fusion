from django.views.generic import FormView
from .models import Service, Employee, Feature, OtherImage
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContactForm


class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['all_services'] = Service.objects.order_by('?').all()
        context['all_employees'] = Employee.objects.all()
        context['left_side_features'] = Feature.objects.all()[:3]
        context['right_side_features'] = Feature.objects.all()[3:]
        context['mobile_image'] = OtherImage.objects.all()[0]
        return context

    # quando a gente trabalha com Class Based View e trabalha com FormView,
    # a gente ganha automaticamente dois métodos

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'Email sent successfully.')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Error trying to send email.')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)
