from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from .models import Entry
from django.urls import reverse

class HomeView(View):
    def get(self, request):
        return render(request, 'home.html')

    def post(self, request):
        data1 = request.POST.get('data1')
        data2 = request.POST.get('data2')
        Entry.objects.create(data1=data1, data2=data2)
        msg = "Data Stored Successfully"
        return render(request, 'home.html', {'msg': msg})

class ShowView(View):
    def get(self, request):
        data = Entry.objects.all()
        return render(request, 'show.html', {'data': data})

    def post(self, request):
        # Handle the POST request here
        # For example, you can process form data and update the database
        return redirect(reverse('show'))


class DeleteView(View):
    def get(self,request,id):
        Entry.objects.filter(id=id).delete()
        return HttpResponseRedirect("/show")

class EditView(View):
    def get(self, request,id):
        data = Entry.objects.get(id=id)
        return render(request, 'edit.html', {'data': data})
    def post(self, request,id):
            data1 = request.POST.get('data1')
            data2 = request.POST.get('data2')
            Entry.objects.filter(id=id).update(data1=data1, data2=data2)
            return HttpResponseRedirect("/show")

