# ============================================================
#  HDT1 — Parte 3: Listas
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 3.1 — Gestión de Zona VIP  (10 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
lista_espera = ["Valentina", "Diego", "Alejandra", "Kim", "Lu", "Marcelo", "Nati"]
capacidad_vip = 5
zona_vip = []

# Operación 1: Agregar "Óscar" y "Paula" al FINAL de lista_espera
lista_espera.append("Óscar")
lista_espera.append("Paula")

# Operación 2: "Diego" cancela — removerlo de lista_espera
if "Diego" in lista_espera:
    lista_espera.remove("Diego")

# Operación 3: Mover las primeras `capacidad_vip` personas a zona_vip
for _ in range(capacidad_vip):
    zona_vip.append(lista_espera.pop(0))

# Operación 4: En zona_vip, añadir " ★" a todo nombre con MÁS DE 5 caracteres
for i in range(len(zona_vip)):
    if len(zona_vip[i]) > 5:
        zona_vip[i] = zona_vip[i] + " ★"

# Operación 5: Imprime el estado final
print(f"ZONA VIP ({len(zona_vip)}/{capacidad_vip})  : {zona_vip}")
print(f"EN ESPERA ({len(lista_espera)})   : {lista_espera}")


# ============================================================
#  Ejercicio 3.2 — Ajuste de Precios con IVA  (10 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
precios_con_iva = [224.00, 392.00, 672.00, 1344.00, 56.00, 448.00]

# a) Lista con todos los precios sin IVA (round a 2 decimales)
precios_sin_iva = []
for p in precios_con_iva:
    precios_sin_iva.append(round(p / 1.12, 2))

# b) Solo los precios sin IVA menores a Q400
precios_accesibles = []
for p in precios_sin_iva:
    if p < 400:
        precios_accesibles.append(p)

# c) Lista de strings con formato "Q{precio:.2f}" de todos los precios sin IVA
precios_formateados = []
for p in precios_sin_iva:
    precios_formateados.append(f"Q{p:.2f}")

print(f"Sin IVA        : {precios_sin_iva}")
print(f"Accesibles     : {precios_accesibles}")
print(f"Formateados    : {precios_formateados}")
