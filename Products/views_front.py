from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView,DeleteView,DetailView,ListView,UpdateView
from django.urls import reverse_lazy
from .models import Product


class  ProductListView(LoginRequiredMixin,ListView):
    template_name = "Products/Product_list.html"
    model = Product
    context_object_name = "Products"


class  ProductDetailView(LoginRequiredMixin,DetailView):
    template_name = "Products/Product_detail.html"
    model = Product
    def get_success_url(self):
        return reverse_lazy("Product_list", args=[self.object.pk])


class  ProductUpdateView(LoginRequiredMixin, UpdateView):
    template_name = "Products/Product_update.html"
    model = Product
    fields = "__all__"

    def get_success_url(self):
        return reverse_lazy("Product_detail", args=[self.object.pk])





class  ProductCreateView(LoginRequiredMixin,CreateView):
    template_name = "Products/Product_create.html"
    model = Product
    fields = "__all__" # "__all__" for all of them
    def get_success_url(self):
        return reverse_lazy("Product_detail", args=[self.object.pk])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "Products/Product_delete.html"
    model = Product
    success_url = reverse_lazy("Product_list")