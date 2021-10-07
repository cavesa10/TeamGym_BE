from rest_framework import serializers
from appTeamGym.models.user import User
from appTeamGym.models.imc import Imc
from appTeamGym.serializers.imc_serializer import imc_serializer

class UserSerializer(serializers.ModelSerializer):
  imc = imc_serializer()
  class Meta:
    model = User
    fields = ['id', 'username', 'password', 'email', 'name', 'last_name','fecha_nacimiento', 'frecuencia_fisica','objetivo_usuario','estatura','estatura','peso','genero','imc']

  def create(self, validated_data):
    imcData = validated_data.pop('imc') #sobrescritura, crear cuenta y usuarios
    userInstance = User.objects.create(**validated_data) # toma y elimina todas las
    Imc.objects.create(user=userInstance, **imcData)
    return userInstance
  def to_representation(self, obj):
    user = User.objects.get(id=obj.id)
    imc = Imc.objects.get(user=obj.id)
    return {
      'id': user.id,
      'username': user.username,
      'password': user.password,
      'name': user.email,
      'last_name': user.last_name,
      'fecha_nacimiento': user.fecha_nacimiento,
      'frecuencia_fisica': user.frecuencia_fisica,
      'objetivo_usuario': user.objetivo_usuario,
      'peso': user.peso,
      'genero': user.genero,
      'estatura': user.estatura,
      'imc': {
        'imc_id': imc.imc_id,
        'imc_value': imc.imc_value,
      }
    }
