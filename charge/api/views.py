from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from charge.models import Plan, PlanSubscription
from charge.api import serilaizers as charge_serializer
from django.contrib.auth import get_user_model
from core.utils.mock_charge import mock_charge


class PlanListView(ListAPIView):
    """
    returning all plans available for subscribe
    """
    permission_classes = [IsAuthenticated, ]
    serializer_class = charge_serializer.PlanSerializer
    model = serializer_class.Meta.model
    queryset = Plan.objects.all()


class SubscriptionView(APIView):
    """
        subscribe the user according to the plan id given
        expected params: "plan_id"
        """
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        if not self.subscription_exists():
            try:
                plan = Plan.objects.get(pk=request.data['plan_id'])
                response = mock_charge()
                if response['status'] == 'succeeded' and response['paid']:
                    user = get_user_model().objects.get(email=request.user.email)
                    subscription = PlanSubscription.objects.create(user=user,
                                                                   plan=plan, status=True)
                    subscription = charge_serializer.PlanSubscriptionSerializer(subscription)
                    return Response(
                        {'data': subscription.data,
                         'message': 'You have been subscribed successfully'},
                        status=status.HTTP_201_CREATED
                    )
            except Exception as e:
                return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Subscription already exist'}, status.HTTP_400_BAD_REQUEST)

    def subscription_exists(self):
        try:
            _ = PlanSubscription.objects.get(user=self.request.user, status=True)
            return True
        except PlanSubscription.DoesNotExist:
            return False


class UnsubscribeView(APIView):
    """
    Unsubscribe the subscription
    """
    permission_classes = [IsAuthenticated, ]

    def post(self, request):
        try:
            subscription = PlanSubscription.objects.filter(status=True, user=request.user).update(re_subscribe=False)
            subscription = charge_serializer.PlanSubscriptionSerializer(subscription)
            return Response(
                {'message': 'You have been successfully unsubscribed the subscription'},
                status=status.HTTP_201_CREATED
            )
        except Exception as e:
            return Response({'error': e.args[0]}, status=status.HTTP_400_BAD_REQUEST)

