from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required

# Create your views here


def base(request):
    return render(request, 'ghost/base.html')


def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'ghost/customer_list.html', {'customers': customers})


def customer_detail(request, pk):
    customer = Customer.objects.get(id=pk)
    return render(request, 'ghost/customer_detail.html', {'customer': customer})


def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customer_list')
    form = CustomerForm()
    return render(request, 'ghost/customer_create.html', {'form': form})


def customer_edit(request, pk):
    customer = Customer.objects.get(pk=pk)
    if request.method == "POST":
        form = CustomerForm(request.POST, instance=customer)
        if form.is_valid():
            customer = form.save()
            return redirect('customer_detail', pk=customer.pk)
    else:
        form = CustomerForm(instance=customer)
    return render(request, 'ghost/customer_create.html', {'form': form})


def customer_delete(request, pk):
    Customer.objects.get(id=pk).delete()
    return redirect('customer_list')
