from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import UserCreateForm
from users.models import UserModel


class DataListView(View):
    @staticmethod
    def get(request):
        data = UserModel.objects.all()
        context = {
            'data': data
        }
        return render(request, 'templates/list.html', context)
class CreateDataView(View):
    @staticmethod
    def get(request):
        form = UserCreateForm()
        return render(request, 'index.html', {'form': form})

    @staticmethod
    def post(request):
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:user-data-list')

        else:
            context = {
                'form': form
            }
            return render(request, 'index.html', context)



