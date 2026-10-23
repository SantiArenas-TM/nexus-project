# Reglas del sistema: el rol y el estilo que debe seguir la IA
SYSTEM_RULES = """
Eres un experto en copywriting y conversión para e-commerce y dropshipping.
Escribes en español, con un tono persuasivo, cercano y claro.
Te enfocas en los beneficios para el cliente y no solo en las características.
No inventes datos que no te den (garantías, certificaciones, cifras ni reseñas).
Responde únicamente con el contenido de la landing, sin introducciones ni comentarios.
""".strip()


# Función que construye el prompt con los datos del producto
def build_landing_prompt(product_name, main_benefit, price):
    return f"""
Crea el texto de una landing page para el siguiente producto:

- Nombre del producto: {product_name}
- Beneficio principal: {main_benefit}
- Precio: {price}

Organiza la respuesta exactamente en estas secciones:

1. Titular: una frase corta y llamativa.
2. Sub-cabecera: una frase que complemente el titular.
3. Beneficios Clave: una lista de 3 a 5 beneficios.
4. Llamado a la Acción: una frase final que invite a comprar.
""".strip()