from django.urls import path,include
from Shinchan.schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('snapp',GraphQLView.as_view(graphiql=True,schema=schema))
]
