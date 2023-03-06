from django.urls import path

from homework58.views.base import IndexView, IndexRedirectView

from homework58.views.issues import IssueDetail, IssueUpdateView, IssueCreateView, IssueDeleteView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('issue/', IndexRedirectView.as_view(), name='issue_index_redirect'),
    path('issue/<int:pk>', IssueDetail.as_view(), name='issue_detail'),
    path('issue/<int:pk>/update', IssueUpdateView.as_view(), name='issue_update'),
    path('issue/create', IssueCreateView.as_view(), name='issue_create'),
    path('issue/<int:pk>/delete', IssueDeleteView.as_view(), name='issue_delete')
]
