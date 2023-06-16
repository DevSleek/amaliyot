from django.urls import path
from .views import CreateDataView, DataListView

app_name = 'users'
urlpatterns = [
    path('', CreateDataView.as_view(), name='index'),
    path('xabarlar/', DataListView.as_view(), name='user-data-list'),
]