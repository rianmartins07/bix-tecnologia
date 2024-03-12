# serializers.py
from rest_framework import serializers
from reserva.models import Reserva

class ReservaSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Validação personalizada para garantir que a data de check-in seja menor que a data de check-out.
        """
        checkin = data.get('check_in')
        checkout = data.get('check_out')

        if checkin and checkout and checkin >= checkout:
            raise serializers.ValidationError("A data de check-in deve ser anterior à data de check-out.")

        return data
    class Meta:
        model = Reserva
        fields = '__all__'
