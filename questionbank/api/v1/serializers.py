from rest_framework import serializers
from questionbank.models import QuestionBank

class QuestionBankSerializer(serializers.ModelSerializer):
    correct_answer = serializers.CharField()

    class Meta:
        model = QuestionBank
        fields = '__all__'

    def validate_answer(self, value):
        value =value.upper()
        if len(value) > 1 or value not in ['A', 'B', 'C', 'D']:
            raise serializers.ValidationError('Answer length can only contain single alphabets from A to D')
        
        return value
