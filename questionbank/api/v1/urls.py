from django.urls import path
from questionbank.api.v1.views import QuestionBankView


urlpatterns = [
    path('createquiz/', QuestionBankView.as_view(), name="question-bank")
]