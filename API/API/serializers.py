from rest_framework import serializers
from .models import Product, Transact, Seller

class ProductAdmSerializer(serializers.ModelSerializer):
    transacts_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Product
        exclude = ['image']

    def get_transacts_count(self, instance):
        return instance.product_transacts_count

    

class ProductNestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductViewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        exclude= ['token']

class SellerSerializer(serializers.ModelSerializer):
    trans_count = serializers.SerializerMethodField()
    total_balance = serializers.SerializerMethodField()
    url = serializers.SerializerMethodField()
    
    class Meta:
        model = Seller
        fields = ('id','name','comissionPercent','trans_count', 'total_balance','url')

    def get_url(self, instance):
        return f'http://localhost:4200/seller/{instance.access_tokn}'

    def get_trans_count(self, instance):
        return instance.total_transacts

    def get_total_balance(self, instance):
        return instance.total_balance
    
class SellerNestSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Seller
        exclude = ['access_tokn']

class TransactSerializer(serializers.ModelSerializer):
    date = serializers.DateTimeField(format="%d/%m/%Y %I:%M:%S %p", required=False)
    seller = SellerNestSerializer(read_only=True)
    product = ProductAdmSerializer(read_only=True)
    product_id = serializers.IntegerField(required=True, write_only=True)
    seller_id = serializers.IntegerField(required=True,write_only=True)
    

    class Meta:
        model = Transact
        fields = '__all__'
    
    def create(self, validated_data):
        seller = self.context['seller']
        product = self.context['product']
        print(product.id)
        transact = Transact.objects.create(product=product, seller=seller, **validated_data)
        return transact


