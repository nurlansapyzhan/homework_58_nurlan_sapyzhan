from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView

from homework58.forms import IssueForm
from homework58.models import Issue


class IssueDetail(TemplateView):
    template_name = 'issue.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context


class IssueUpdateView(TemplateView):
    template_name = 'issue_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        context['form'] = IssueForm(instance=context['issue'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        form = IssueForm(request.POST, instance=issue)
        if form.is_valid():
            form.save()
            return redirect('issue_detail', issue.pk)
        return render(request, 'issue_update.html', context={'form': form, 'issue': issue})


class IssueCreateView(TemplateView):
    template_name = 'issue_create.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = IssueForm()
        return context

    def post(self, request, *args, **kwargs):
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save()
            if request.POST.get('type'):
                for type in request.POST.get('type'):
                    issue.type.add(type)
            else:
                issue.save()
                return redirect('index')
        else:
            return render(request, 'issue_create.html', context={'form': form})


class IssueDeleteView(TemplateView):
    template_name = 'issue_delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['issue'] = get_object_or_404(Issue, pk=kwargs['pk'])
        return context

    def post(self, request, *args, **kwargs):
        issue = get_object_or_404(Issue, pk=kwargs['pk'])
        issue.type.clear()
        issue.delete()
        return redirect('index')
