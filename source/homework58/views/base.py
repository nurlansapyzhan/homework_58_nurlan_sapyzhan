from django.views.generic import TemplateView, RedirectView

from homework58.models.issue import Issue


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issues'] = Issue.objects.all()
        return context


class IndexRedirectView(RedirectView):
    pattern_name = 'index'
