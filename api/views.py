from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import EncodedText, EncodingSchema
from .serializers import EncodedTextSerializer, EncodingSchemaSerializer, EncodedTextConversionSerializer
from .utils.encoding import convert_encoding, get_available_encodings, is_valid_encoding

class EncodingSchemaViewSet(viewsets.ModelViewSet):
    queryset = EncodingSchema.objects.all()
    serializer_class = EncodingSchemaSerializer
    permission_classes = [AllowAny]  # Para simplificar; ajustar según necesidades de seguridad

class EncodedTextViewSet(viewsets.ModelViewSet):
    queryset = EncodedText.objects.all()
    serializer_class = EncodedTextSerializer
    permission_classes = [AllowAny]  # Para simplificar; ajustar según necesidades de seguridad
    
    @action(detail=True, methods=['post'])
    def convert(self, request, pk=None):
        """
        Convierte el texto a una codificación diferente
        """
        text_obj = self.get_object()
        
        serializer = EncodedTextConversionSerializer(data={
            'id': pk,
            'target_encoding': request.data.get('target_encoding')
        })
        
        if serializer.is_valid():
            target_encoding = serializer.validated_data['target_encoding']
            
            try:
                # Crear una nueva versión del texto con la codificación convertida
                converted_content = convert_encoding(
                    text_obj.content,
                    text_obj.encoding,
                    target_encoding
                )
                
                # Actualizar el texto
                text_obj.content = converted_content
                text_obj.original_encoding = text_obj.encoding
                text_obj.encoding = target_encoding
                text_obj.save()
                
                return Response(
                    EncodedTextSerializer(text_obj).data,
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'error': str(e)},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
    
    @action(detail=False, methods=['get'])
    def available_encodings(self, request):
        """
        Devuelve la lista de codificaciones disponibles
        """
        return Response(get_available_encodings())

    @action(detail=False, methods=['post'])
    def validate_encoding(self, request):
        """
        Valida si una codificación es válida
        """
        encoding = request.data.get('encoding')
        if not encoding:
            return Response(
                {'error': 'Se requiere el parámetro "encoding"'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        valid = is_valid_encoding(encoding)
        return Response({'valid': valid})