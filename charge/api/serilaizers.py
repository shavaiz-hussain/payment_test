from rest_framework import serializers
from charge.models import PlanSubscription, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class PlanSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanSubscription
        fields = '__all__'
