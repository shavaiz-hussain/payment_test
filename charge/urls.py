from django.urls import path
from charge.api import views as charge_api_views

urlpatterns = [
    path('plans/', charge_api_views.PlanListView.as_view()),
    path('subscribe/', charge_api_views.SubscriptionView.as_view()),
    path('unsubscribe/', charge_api_views.UnsubscribeView.as_view()),
]