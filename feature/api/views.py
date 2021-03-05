from rest_framework import status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import FeatureSerializer
from charge.models import PlanSubscription


class FeatureList(ListAPIView):
    """
    Get features according to the subscription
    """
    serializer_class = FeatureSerializer
    model = serializer_class.Meta.model
    queryset = model.objects.all()

    def get_queryset(self):
        try:
            subscription = PlanSubscription.objects.get(status=True, user=self.request.user)
            if subscription:
                return self.model.objects.filter(plan=subscription.plan)
        except PlanSubscription.DoesNotExist:
            return None

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if queryset:
            serializer = self.get_serializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'No subscription found'}, status=status.HTTP_400_BAD_REQUEST)
