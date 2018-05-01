from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView
from django.http import Http404
from .models import Product
from carts.models import Cart
# Create your views here.

class ProductFeaturedListView(ListView):
    template_name = 'products/list.html'

    def get_queryset(self,*args,**kwargs):
        request = self.request
        return Product.objects.all().featured()

class ProductFetauredDetailView(DetailView):
    queryset =Product.objects.all().featured()
    template_name = 'products/featured-details.html'

    # def get_queryset(self,*args,**kwargs):
    #     request = self.request
    #     return Product.objects.featured()

class ProductDetailSlugView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/featured-details.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailSlugView,self).get_context_data(*args,**kwargs)
        cart_obj,new_obj = Cart.objects.new_or_get(self.request)
        context['cart'] = cart_obj
        return context

class ProductListView(ListView):
    queryset =Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self,*args,**kwargs):
    #     context = super(ProductListView,self).get_context_data(*args,**kwargs )
    #     print(context)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context ={'object_list':queryset}

    return render(request,"products/list.html",context)



class ProductDetailSlugView(DetailView):
     queryset =Product.objects.all()
     template_name = 'products/details.html'

     def get_object(self,*args,**kwargs):
         request = self.request
         slug = self.kwargs.get('slug')
         # instance = get_object_or_404(Product,slug = slug,active = True)
         # print(instance)
         try:
             instance = Product.objects.get(slug =slug ,active = True)
         except Product.DoesNotExit:
            raise Http404("Not Found.")
         except Product.MultipleObjectsReturned:
            qs = Product.objects.filter(slug = slug ,active = True)
            instance = qs.first()
         except:
            raise Http404("Ummmmh")
         return instance


class ProductDetailView(DetailView):
    # queryset =Product.objects.all()
    template_name = 'products/details.html'

    def get_context_data(self,*args,**kwargs):
        context = super(ProductDetailView,self).get_context_data(*args,**kwargs )
        # print(context)
        return context

    def get_object(self,*args,**kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.objects.get_by_id(pk)
        # print(instance)
        if instance is None:
            raise Http404("Product Does Not Exist")
        return instance


def product_detail_view(request,pk = None,*args,**kwargs):
    instance= Product.objects.get(id =pk,featured= True)
    #object =Product.objects.get(pk =pk)
    #instance = get_object_or_404(Product,pk =pk)
   # try:
   #     instance= Product.objects.get(id =pk)
   # except Product.DoesNotExit:
   #     print("No Product Here")
   #     raise Http404("Product Does not exist")
   # except:
   #     print("huh ")


    instance = Product.objects.get_by_id(pk)
    print(instance)
    if instance is None:
        raise Http404("Product Does Not Exist")
    # qs = Product.objects.filter(id = pk)
    # if qs.exists and qs.count ==1:
    #     instance = qs.first()
    # else:
    #     raise Http404("Product Does not exist")

    context ={'object': instance }

    return render(request,"products/details.html",context)
