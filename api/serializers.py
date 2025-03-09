from rest_framework import serializers
from .models import EncodedText, EncodingSchema
from .utils.encoding import convert_encoding, is_valid_encoding

class EncodingSchemaSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncodingSchema
        fields = '__all__'

class EncodedTextSerializer(serializers.ModelSerializer):
    class Meta:
        model = EncodedText
        fields = ['id', 'content', 'encoding', 'original_encoding', 'created_at', 'updated_at']
        read_only_fields = ['original_encoding', 'created_at', 'updated_at']

    def create(self, validated_data):
        # Por defecto, asumimos que el texto ingresado está en UTF-8
        validated_data['original_encoding'] = 'UTF-8'
        return super().create(validated_data)

class EncodedTextConversionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    target_encoding = serializers.CharField(max_length=20)
    
    def validate_target_encoding(self, value):
        if not is_valid_encoding(value):
            raise serializers.ValidationError(f"La codificación '{value}' no es válida")
        return value
    
    def validate_id(self, value):
        try:
            EncodedText.objects.get(pk=value)
        except EncodedText.DoesNotExist:
            raise serializers.ValidationError("El texto con este ID no existe")
        return value