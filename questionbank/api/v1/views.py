from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status

from questionbank.models import QuestionBank
from questionbank.api.v1.serializers import QuestionBankSerializer


class QuestionBankView(APIView):
    serializer_class = QuestionBankSerializer

    def post(self, request:Request) -> Response:
        """Create questions and answer."""

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get(self, request: Request) -> Response:
        all_quiz: dict[str, any] = {}
        try:
            all_quiz = QuestionBank.objects.all()
        except QuestionBank.DoesNotExist:
             return Response({'non_field_errors': ['No question found']}, status=status.HTTP_400_BAD_REQUEST)
        serializer = QuestionBankSerializer(all_quiz, many=True)
        return Response({'data': serializer.data}, status=status.HTTP_200_OK)
    


        