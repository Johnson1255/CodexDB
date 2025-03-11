import requests
import json

# Configuración base
BASE_URL = "http://localhost:8000/api"

def print_response(response):
    """Imprime la respuesta formateada"""
    print(f"Status Code: {response.status_code}")
    try:
        print(json.dumps(response.json(), indent=2, ensure_ascii=False))
    except:
        print(response.text)
    print("-" * 50)

# 1. Obtener codificaciones disponibles
print("Obteniendo codificaciones disponibles...")
response = requests.get(f"{BASE_URL}/texts/available_encodings/")
print_response(response)

# 2. Crear un texto con caracteres especiales
print("Creando texto con caracteres especiales...")
text_data = {
    "content": "Texto con caracteres especiales: áéíóúñÑ¿¡€",
    "encoding": "UTF-8"
}
response = requests.post(f"{BASE_URL}/texts/", json=text_data)
print_response(response)

# Guardamos el ID del texto creado
if response.status_code == 201:
    text_id = response.json()["id"]
else:
    # Si ya existe un texto, obtenemos el primero
    response = requests.get(f"{BASE_URL}/texts/")
    if response.status_code == 200 and len(response.json()) > 0:
        text_id = response.json()[0]["id"]
    else:
        print("No se pudo crear o encontrar un texto para pruebas")
        exit(1)

print(f"ID del texto para pruebas: {text_id}")

# 3. Obtener el texto creado
print("Obteniendo el texto creado...")
response = requests.get(f"{BASE_URL}/texts/{text_id}/")
print_response(response)

# 4. Convertir a ISO-8859-1
print("Convirtiendo a ISO-8859-1...")
conversion_data = {"target_encoding": "ISO-8859-1"}
response = requests.post(f"{BASE_URL}/texts/{text_id}/convert/", json=conversion_data)
print_response(response)

# 5. Verificar la conversión
print("Verificando la conversión...")
response = requests.get(f"{BASE_URL}/texts/{text_id}/")
print_response(response)

# 6. Convertir de vuelta a UTF-8
print("Convirtiendo de vuelta a UTF-8...")
conversion_data = {"target_encoding": "UTF-8"}
response = requests.post(f"{BASE_URL}/texts/{text_id}/convert/", json=conversion_data)
print_response(response)

# 7. Verificar la conversión de vuelta
print("Verificando la conversión de vuelta...")
response = requests.get(f"{BASE_URL}/texts/{text_id}/")
print_response(response)

# 8. Probar con una codificación inválida
print("Probando con una codificación inválida...")
invalid_encoding = {"target_encoding": "INVALID-ENCODING"}
response = requests.post(f"{BASE_URL}/texts/{text_id}/convert/", json=invalid_encoding)
print_response(response)

# 9. Validar codificaciones
print("Validando codificación UTF-8...")
validation_data = {"encoding": "UTF-8"}
response = requests.post(f"{BASE_URL}/texts/validate_encoding/", json=validation_data)
print_response(response)

print("Validando codificación inválida...")
invalid_validation = {"encoding": "INVALID-ENCODING"}
response = requests.post(f"{BASE_URL}/texts/validate_encoding/", json=invalid_validation)
print_response(response)

print("¡Pruebas completadas!")