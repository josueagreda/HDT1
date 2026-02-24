# ============================================================
#  HDT1 — Parte 1: Condicionales
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 1.1 — Precios Dinámicos de Entradas  (10 pts)
# ============================================================
# Precios base: campo=Q200, gradería=Q350, preferencia=Q600, vip=Q1200
#
# Descuento mayor aplica (NO acumulables entre sí):
#   - Estudiante UFM con carnet válido    → 25%
#   - Compra en los primeros 30 días  → 15%
#   - Menor de 12 O mayor de 64 años      → 50%
#
# Regla adicional (sí aplica SOBRE el precio ya descontado):
#   - Más de 4 entradas de la misma zona  → 10% extra



# --- Datos de prueba (NO modificar) ---
zona          = "vip"
edad          = 30
es_ufm        = True
carnet_valido = True
dias_anticipacion = 35
cantidad      = 5

# --- Tu código aquí ---

precio_final = 0  # reemplaza con tu lógica

# TODO 1: Determina el precio base según zona
#         (campo, gradería, preferencia, vip o zona inválida)
if zona == "vip" :
     precio = 1200
elif zona == "preferencia" :
    precio = 600
elif zona == "gradería" :
    precio = 350
elif zona == "campo" :
    precio = 200    
else :
    precio = 0

# TODO 2: Calcula el porcentaje de descuento más alto que aplica
descuento = 0.0
motivo = "sin descuento"

# Estudiante UFM con carnet válido → 25%
if es_ufm and carnet_valido:
    descuento = 0.25
    motivo = "estudiante UFM"

# Compra en los primeros 30 días → 15%
if dias_anticipacion <= 30 and 0.15 > descuento:
    descuento = 0.15
    motivo = "compra anticipada"

# Menor de 12 O mayor de 64 años → 50%
if (edad < 12 or edad > 64) and 0.50 > descuento:
    descuento = 0.50
    motivo = "edad"

# TODO 3: Aplica el descuento al precio base
precio_desc = precio * (1 - descuento)

# TODO 4: Si cantidad > 4, aplica 10% adicional sobre el precio ya descontado
descuento_volumen = 0.0
if cantidad > 4 and precio > 0:
    descuento_volumen = precio_desc * 0.10 * cantidad  # 10% por entrada * cantidad

total = (precio_desc * cantidad) - descuento_volumen

# TODO 5: Imprime el resumen con el formato esperado
print("=== ENTRADA DATAFEST 2026 ===")
print(f"Zona       : {zona}")
print(f"Precio base: Q{precio:.2f}")
print(f"Descuento  : {descuento*100:.1f}% ({motivo})")
print(f"Precio/entrada: Q{precio_desc:.2f}")

if cantidad > 4 and precio > 0:
    print(f"Descuento volumen ({cantidad} entradas): -Q{descuento_volumen:.2f}")
else:
    print(f"Descuento volumen ({cantidad} entradas): -Q0.00")

print(f"TOTAL A PAGAR: Q{total:.2f}")


# ============================================================
#  Ejercicio 1.2 — Control de Acceso al Festival  (10 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
casos_acceso = [
    # (zona,         edad, tiene_entrada, pulsera_especial, con_acompanante, prohibicion)
    ("vip",          25,   False,         True,             True,            False),  # sin entrada
    ("vip",          22,   True,          False,            True,            False),  # sin pulsera
    ("campo",        16,   True,          False,            False,           False),  # menor sin acomp.
    ("preferencia",  30,   True,          False,            True,            False),  # todos ok
]

for i, caso in enumerate(casos_acceso, start=1):
    zona_c, edad_c, entrada, pulsera, acompanante, prohibicion = caso
    zona_c_norm = zona_c.strip().lower()

    # 1. Sin entrada válida → denegado
    if not entrada:
        print(f"Caso {i}: [DENEGADO] Sin entrada válida")
        continue

    # 2. Zona vip/backstage sin pulsera → denegado
    if (zona_c_norm == "vip" or zona_c_norm == "backstage") and not pulsera:
        print(f"Caso {i}: [DENEGADO] Zona VIP requiere pulsera especial")
        continue

    # 3. Menor de 18 sin acompañante → denegado
    if edad_c < 18 and not acompanante:
        print(f"Caso {i}: [DENEGADO] Menor de edad requiere acompañante")
        continue

    # 4. prohibicion = True → denegado (siempre)
    if prohibicion:
        print(f"Caso {i}: [DENEGADO] Acceso denegado por prohibición")
        continue

    # 5. Si pasa todo lo anterior → permitido
    print(f"Caso {i}: [PERMITIDO] Bienvenido/a a zona: {zona_c_norm}")