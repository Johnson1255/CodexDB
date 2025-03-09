def convert_encoding(text, source_encoding, target_encoding):
    """
    Convierte un texto de una codificación a otra
    
    Args:
        text (str): Texto a convertir
        source_encoding (str): Codificación de origen
        target_encoding (str): Codificación de destino
        
    Returns:
        str: Texto convertido
    """
    try:
        # Si el texto ya es un string en Python, primero lo codificamos
        # en bytes usando la codificación de origen
        if isinstance(text, str):
            binary_data = text.encode(source_encoding, errors='replace')
        else:
            binary_data = text
            
        # Luego decodificamos los bytes a string usando la codificación de destino
        converted_text = binary_data.decode(target_encoding, errors='replace')
        return converted_text
    except Exception as e:
        raise ValueError(f"Error al convertir codificación: {str(e)}")

def get_available_encodings():
    """
    Devuelve una lista de codificaciones comunes disponibles
    
    Returns:
        list: Lista de codificaciones disponibles
    """
    return [
        'UTF-8',
        'UTF-16',
        'ASCII',
        'ISO-8859-1',
        'Windows-1252',
        'CP437',
        'GBK',
        'Big5',
        'EUC-JP',
        'EUC-KR',
        'ANSI'
    ]

def is_valid_encoding(encoding):
    """
    Verifica si una codificación es válida
    
    Args:
        encoding (str): Nombre de la codificación
        
    Returns:
        bool: True si la codificación es válida, False en caso contrario
    """
    try:
        "test".encode(encoding)
        return True
    except LookupError:
        return False