from django.contrib.auth.models import User
from rest_framework import serializers
from ..models import Usuario, Rol

METODOS = [
    ('Transfermovil','Transfermovil'),
    ('Enzona', 'Enzona')
]

class RegisterSerializer(serializers.Serializer):
    username        = serializers.CharField(max_length=150)
    email           = serializers.EmailField()
    password        = serializers.CharField(write_only=True)
    confirmPassword = serializers.CharField(write_only=True)
    metodos         = serializers.ChoiceField(choices=METODOS)
    rol             = serializers.PrimaryKeyRelatedField(queryset=Rol.objects.all())

    def validate(self, data):
        if data['password'] != data['confirmPassword']:
            raise serializers.ValidationError({
                'confirmPassword': 'Las contraseñas no coinciden.'
            })
        if User.objects.filter(username=data['username']).exists():
            raise serializers.ValidationError({'username': 'Ya existe ese username.'})
        if User.objects.filter(email=data['email']).exists():
            raise serializers.ValidationError({'email': 'Ese email ya está en uso.'})
        return data

    def create(self, validated_data):
        pwd = validated_data.pop('password')
        validated_data.pop('confirmPassword')
        metodos = validated_data.pop('metodos')
        rol = validated_data.pop('rol')

        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=pwd
        )

        perfil = Usuario.objects.create(
            user=user,
            metodos=metodos,
            rol=rol
        )
        return perfil

    def to_representation(self, instance: Usuario):
        from ..serializers import UsuarioSerializer
        return UsuarioSerializer(instance).data
