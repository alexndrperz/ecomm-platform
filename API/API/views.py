import os
from django.conf import settings
from .models import Product, Transact, Seller
from .serializers import ProductAdmSerializer, ProductViewSerializer, SellerSerializer, TransactSerializer
from rest_framework import viewsets
from django.http.response import JsonResponse

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all()

    def get_all_products(self, request):
        products = Product.objects.all()
        serializer =  ProductAdmSerializer(products, many=True)
        return JsonResponse({'data':serializer.data})
    
    def get_one_product(self, request, id):
        try: 
            product= Product.objects.get(id=id)
        except Exception as e:
            return JsonResponse({'success':False, 'mes':'Producto inexistente'}, status=404)
        
        serializer = ProductViewSerializer(product)
        return JsonResponse({'data':serializer.data})

    def get_url_product(self, request, sell_id, prod_id):
        try:
            seller = Seller.objects.get(id=sell_id)
            product = Product.objects.get(id=prod_id)
        except Exception as e:
            return JsonResponse({'msg':'Alguno de los id suministrados no existen'}, status=404)
        url = f'http://localhost:4200/{seller.token}/{product.token}'
        return JsonResponse({'url':url})
    
    def get_url_based_product(self, request, sell_tokn, prod_tokn):
        try:
            seller = Seller.objects.get(token=sell_tokn)
            product = Product.objects.get(token=prod_tokn)
        except Exception as e:
            return JsonResponse({'msg':'Alguno de los id suministrados no existen'}, status=404)
        
        serializer = ProductViewSerializer(product)
        return JsonResponse({'product':serializer.data, 'seller_id':seller.id})

    def post_product(self, request):
        serializer = ProductViewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse(serializer.data, status=201)

    def delete_product(self, request, id):
        try:
            product = Product.objects.get(id=id)
        except Exception:
            return JsonResponse({'message':'No existe'}, status=404)
        
        
        if product.image:
            image_path = os.path.join(settings.MEDIA_ROOT, str(product.image))
            if os.path.exists(image_path):
                os.remove(image_path)
        product.delete()
        return JsonResponse({'msg':'Producto borrado con exito'})
    
class SellerView(viewsets.ModelViewSet):
    def get_seller_profile(self, request, tokn):
        seller = Seller.objects.get(access_tokn=tokn)
        serializer = SellerSerializer(seller)
        product=Product.objects.all()
        Pdserializer = ProductViewSerializer(product, many=True)
        return JsonResponse({'data':serializer.data, 'products':Pdserializer.data})
    
    def create_seller(self, request):
        serializer = SellerSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({'data':serializer.data})

    def get_sellers(self, request):
        queryset= Seller.objects.all()
        serializer= SellerSerializer(queryset, many=True)
        return JsonResponse({'data':serializer.data})
    
class TransactsView(viewsets.ModelViewSet):
    queryset = Transact.objects.all()

    def get_all_transacts(self, request):
        queryset= Transact.objects.all()
        serializer = TransactSerializer(queryset, many=True)
        return JsonResponse({'data':serializer.data})
    
    def create_transact(self, request):
        seller_id = request.data.get('seller_id')
        product_id = request.data.get('product_id')

        try:
            seller = Seller.objects.get(id=seller_id)
            product = Product.objects.get(id=product_id)
        except (Seller.DoesNotExist, Product.DoesNotExist):
            return JsonResponse({'message': 'Vendedor o producto no encontrado'}, status=404)
        
        serializer = TransactSerializer(data=request.data, context={'seller':seller, 'product':product})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return JsonResponse({'data':serializer.data}, status=201)