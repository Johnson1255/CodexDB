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

def test_encoding(language, sample_text, original_encoding="UTF-8", target_encodings=None):
    if target_encodings is None:
        target_encodings = []
    
    print(f"\n{'='*20} PRUEBA CON {language} {'='*20}")
    
    # 1. Crear un texto con caracteres del idioma
    print(f"Creando texto en {language}...")
    text_data = {
        "content": sample_text,
        "encoding": original_encoding
    }
    response = requests.post(f"{BASE_URL}/texts/", json=text_data)
    print_response(response)
    
    if response.status_code == 201:
        text_id = response.json()["id"]
    else:
        print(f"Error al crear texto en {language}")
        return
    
    print(f"ID del texto para pruebas: {text_id}")
    
    # 2. Para cada codificación objetivo, convertir y verificar
    for target_encoding in target_encodings:
        print(f"Convirtiendo de {original_encoding} a {target_encoding}...")
        conversion_data = {"target_encoding": target_encoding}
        response = requests.post(f"{BASE_URL}/texts/{text_id}/convert/", json=conversion_data)
        print_response(response)
        
        print(f"Verificando la conversión a {target_encoding}...")
        response = requests.get(f"{BASE_URL}/texts/{text_id}/")
        print_response(response)
        
        # Convertir de vuelta al original
        print(f"Convirtiendo de vuelta a {original_encoding}...")
        conversion_data = {"target_encoding": original_encoding}
        response = requests.post(f"{BASE_URL}/texts/{text_id}/convert/", json=conversion_data)
        print_response(response)
        
        # Verificar conversión de vuelta
        print(f"Verificando la conversión de vuelta a {original_encoding}...")
        response = requests.get(f"{BASE_URL}/texts/{text_id}/")
        print_response(response)

# Textos de muestra en diferentes idiomas
chinese_text = "你好，世界！这是中文测试。我希望API能够正确处理这些字符。中国有很多不同的方言和文化。"
japanese_text = "こんにちは世界！これは日本語のテストです。APIがこれらの文字を正しく処理できることを願っています。日本には多くの異なる文化があります。"
korean_text = "안녕하세요 세계! 이것은 한국어 테스트입니다. API가 이러한 문자를 올바르게 처리할 수 있기를 바랍니다. 한국에는 다양한 문화가 있습니다."

# Ejecutar pruebas para cada idioma
test_encoding("Chino", chinese_text, "UTF-8", ["GBK", "Big5", "UTF-16"])
test_encoding("Japonés", japanese_text, "UTF-8", ["EUC-JP", "UTF-16", "Shift_JIS"])
test_encoding("Coreano", korean_text, "UTF-8", ["EUC-KR", "UTF-16", "CP949"])

print("\n¡Pruebas con idiomas asiáticos completadas!")