from django.db import models

class EncodedText(models.Model):
    """
    Modelo para almacenar texto con información de codificación
    """
    content = models.TextField()
    encoding = models.CharField(max_length=20, default='UTF-8')
    original_encoding = models.CharField(max_length=20, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Text {self.id} ({self.encoding})"

class EncodingSchema(models.Model):
    """
    Modelo para almacenar los esquemas de codificación disponibles
    """
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
