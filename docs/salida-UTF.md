Obteniendo codificaciones disponibles...
Status Code: 200
[
  "UTF-8",
  "UTF-16",
  "ASCII",
  "ISO-8859-1",
  "Windows-1252",
  "CP437",
  "GBK",
  "Big5",
  "EUC-JP",
  "EUC-KR",
  "ANSI"
]
--------------------------------------------------
Creando texto con caracteres especiales...
Status Code: 201
{
  "id": 2,
  "content": "Texto con caracteres especiales: áéíóúñÑ¿¡€",
  "encoding": "UTF-8",
  "original_encoding": "UTF-8",
  "created_at": "2025-03-11T03:17:04.511546Z",
  "updated_at": "2025-03-11T03:17:04.511586Z"
}
--------------------------------------------------
ID del texto para pruebas: 2
Obteniendo el texto creado...
Status Code: 200
{
  "id": 2,
  "content": "Texto con caracteres especiales: áéíóúñÑ¿¡€",
  "encoding": "UTF-8",
  "original_encoding": "UTF-8",
  "created_at": "2025-03-11T03:17:04.511546Z",
  "updated_at": "2025-03-11T03:17:04.511586Z"
}
--------------------------------------------------
Convirtiendo a ISO-8859-1...
Status Code: 200
{
  "id": 2,
  "content": "Texto con caracteres especiales: Ã¡Ã©Ã­Ã³ÃºÃ±ÃÂ¿Â¡â¬",
  "encoding": "ISO-8859-1",
  "original_encoding": "UTF-8",
  "created_at": "2025-03-11T03:17:04.511546Z",
  "updated_at": "2025-03-11T03:17:04.563591Z"
}
--------------------------------------------------
Verificando la conversión...
Status Code: 200
{
  "id": 2,
  "content": "Texto con caracteres especiales: Ã¡Ã©Ã­Ã³ÃºÃ±ÃÂ¿Â¡â¬",
  "encoding": "ISO-8859-1",
  "original_encoding": "UTF-8",
  "created_at": "2025-03-11T03:17:04.511546Z",
  "updated_at": "2025-03-11T03:17:04.563591Z"
}
--------------------------------------------------
Convirtiendo de vuelta a UTF-8...
Status Code: 200
{
  "id": 2,
  "content": "Texto con caracteres especiales: áéíóúñÑ¿¡€",
  "encoding": "UTF-8",
  "original_encoding": "ISO-8859-1",
  "created_at": "2025-03-11T03:17:04.511546Z",
  "updated_at": "2025-03-11T03:17:04.616337Z"
}
--------------------------------------------------
Verificando la conversión de vuelta...
Status Code: 200
{
  "id": 2,
  "content": "Texto con caracteres especiales: áéíóúñÑ¿¡€",
  "encoding": "UTF-8",
  "original_encoding": "ISO-8859-1",
  "created_at": "2025-03-11T03:17:04.511546Z",
  "updated_at": "2025-03-11T03:17:04.616337Z"
}
--------------------------------------------------
Probando con una codificación inválida...
Status Code: 400
{
  "target_encoding": [
    "La codificación 'INVALID-ENCODING' no es válida"
  ]
}
--------------------------------------------------
Validando codificación UTF-8...
Status Code: 200
{
  "valid": true
}
--------------------------------------------------
Validando codificación inválida...
Status Code: 200
{
  "valid": false
}
--------------------------------------------------
¡Pruebas completadas!