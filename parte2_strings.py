# ============================================================
#  HDT1 — Parte 2: Strings
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 2.1 — Generador de Credenciales  (8 pts)
# ============================================================
# Formato: FD26-[ZONA3]-[INICIALES][NUMERO]

# Casos de prueba (NO modificar):
registros = [
    ("Carlos Mendoza",        "vip",         47),
    ("Ana García",            "campo",         5),
    ("José Luis Rodríguez",   "gradería",   1823),
    ("María López",           "preferencia", 312),
]

for nombre, zona, numero in registros:
    zona3 = zona.strip().upper()[:3]

    partes = nombre.strip().split()
    inicial_nombre = partes[0][0].upper()
    inicial_apellido = partes[-1][0].upper()

    numero4 = str(numero).zfill(4)

    credencial = f"FD26-{zona3}-{inicial_nombre}{inicial_apellido}{numero4}"
    print(credencial)


# ============================================================
#  Ejercicio 2.2 — Limpieza de Datos de Asistentes  (6 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
registros_crudos = [
    "  ana GARCIA    ,   ana.garcia@gmail.com  ,   22  ",
    "  JOSE LUIS perez  ,  jl_perez@outlook  ,  17  ",
    "  María Fernanda SOLIS  ,  mfernanda@ufm.edu  ,  150  ",
]

def email_valido(email: str) -> bool:
    email = email.strip().lower()
    if "@" not in email:
        return False
    at = email.find("@")
    # Debe haber un punto DESPUÉS del "@"
    return "." in email[at+1:]

for i, registro in enumerate(registros_crudos, start=1):
    print(f"--- Registro {i} ---")

    campos = registro.split(",")
    nombre_raw = campos[0].strip()
    email_raw = campos[1].strip()
    edad_raw = campos[2].strip()

    nombre = nombre_raw.title()
    email = email_raw.lower()

    valido_email = email_valido(email)
    try:
        edad = int(edad_raw)
    except ValueError:
        edad = -1

    en_rango = (5 <= edad <= 100)

    print(f"Nombre : {nombre}")
    print(f"Email  : {email} | Válido: {'Sí' if valido_email else 'No'}")

    if en_rango:
        print(f"Edad   : {edad} | En rango: Sí")
    else:
        print(f"Edad   : {edad} | En rango: No — fuera del rango [5, 100]")

    print()


# ============================================================
#  Ejercicio 2.3 — Análisis de Reseñas  (6 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
resenas = [
    "El festival fue espectacular los artistas son increíble el sonido la energía todo genial",
    "Lamentablemente el sonido fue terrible aunque los artistas estuvieron genial pero el acceso horrible",
]

vocales = "aeiouáéíóúAEIOUÁÉÍÓÚ"
palabras_positivas = ["increíble", "excelente", "genial", "espectacular", "maravilloso", "fantástico"]
palabras_negativas = ["malo", "pésimo", "terrible", "aburrido", "decepcionante", "horrible"]

for i, resena in enumerate(resenas, start=1):
    print(f"--- Reseña {i} ---")

    palabras = resena.split()
    total_palabras = len(palabras)

    total_vocales = 0
    for ch in resena:
        if ch in vocales:
            total_vocales += 1

    palabra_larga = ""
    max_len = 0
    for p in palabras:
        if len(p) > max_len:
            max_len = len(p)
            palabra_larga = p

    tiene_pos = False
    tiene_neg = False
    for p in palabras:
        pl = p.lower()
        if pl in palabras_positivas:
            tiene_pos = True
        if pl in palabras_negativas:
            tiene_neg = True

    if tiene_pos and not tiene_neg:
        sentimiento = "positiva"
    elif tiene_neg and not tiene_pos:
        sentimiento = "negativa"
    elif tiene_pos and tiene_neg:
        sentimiento = "mixta"
    else:
        sentimiento = "neutral"

    print(f"Palabras      : {total_palabras}")
    print(f"Vocales       : {total_vocales}")
    print(f'Palabra larga : "{palabra_larga}"')
    print(f"Sentimiento   : {sentimiento}")
    print()
