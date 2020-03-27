from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib.auth.decorators import login_required

# Create your views here.

# this function is first getting the data then it's going to render it in this HTML file
# creating a variable for Artists.objects.all() will make our process cleaner
#

@login_required
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'ghost/customer_list.html', {'customers': customers})


# def post_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     # comments = Comment.object.all(id=fk)
#     return render(request, 'scribble/post_detail.html', {'post': post})


# def post_detail(request, pk):
#     post = Post.objects.get(id=pk)
#     return render(request, 'scribble/post_detail.html', {'post': post})

def customer_detail(request, pk):
    customers = Customer.objects.filter(customer=pk)
    customer = Customer.objects.get(id=pk)
    return render(request, 'ghost/customer_detail.html', {'customer': customer})



def customer_create(request):
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('customer_list')
    form = PostForm()
    return render(request, 'ghost/customer_create.html', {'form': form})
