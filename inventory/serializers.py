from django.utils import timezone
from rest_framework import serializers
from . import models


class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Store
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'


class UnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Unit
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    store = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    units = serializers.SerializerMethodField()

    class Meta:
        model = models.Product
        fields = '__all__'

    def get_store(self, obj):
        return StoreSerializer(instance=obj.store_id).data

    def get_category(self, obj):
        return CategorySerializer(instance=obj.category_id).data

    def get_units(self, obj):
        return UnitSerializer(instance=obj.unit_id).data

    def create(self, validated_data):
        validated_data['inventoryOnHand'] = validated_data['startingInventory']
        return models.Product.objects.create(**validated_data)


class RequisitionSerializer(serializers.ModelSerializer):
    store = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = models.Requisition
        fields = '__all__'

    def get_store(self, obj):
        return StoreSerializer(instance=obj.store_id).data

    def get_product(self, obj):
        return ProductSerializer(instance=obj.product_id).data

    def update(self, instance, validated_data):
        product = instance.product_id
        if product.inventoryOnHand < int(validated_data['quantity_released']):
            raise serializers.ValidationError("You can't dispatch more than quantity on hand")

        product.inventoryOnHand -= int(validated_data['quantity_released'])
        product.inventoryShipped += int(validated_data['quantity_released'])
        product.save()
        instance.quantity_released = validated_data['quantity_released']
        instance.is_dispatched = True
        instance.updated = timezone.now()
        instance.save()
        return instance


class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Supplier
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    supplier = serializers.SerializerMethodField()
    product = serializers.SerializerMethodField()

    class Meta:
        model = models.Order
        fields = '__all__'

    def get_supplier(self, obj):
        return StoreSerializer(instance=obj.supplier_id).data

    def get_product(self, obj):
        return ProductSerializer(instance=obj.product_id).data

    def update(self, instance, validated_data):
        product = instance.product_id
        product.inventoryOnHand += int(validated_data['number_received'])
        product.inventoryReceived += int(validated_data['number_received'])
        product.save()

        instance.number_received = validated_data['number_received']
        instance.batch_number = validated_data['batch_number']
        instance.is_supplied = True
        instance.updated = timezone.now()
        instance.cost = validated_data['cost']
        instance.save()
        return instance
