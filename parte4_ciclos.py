# ============================================================
#  HDT1 — Parte 4: Ciclos
#  DataFest 2026 — Sistema de Operaciones
# ============================================================

# ============================================================
#  Ejercicio 4.1 — Reporte Visual de Afluencia por Hora  (8 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
afluencia_por_hora = [
    0,  0,  0,  0,  0,  0,  0,  0,   # 00 – 07
   45, 120, 230, 310, 280,             # 08 – 12
   190, 260, 310, 420, 390,            # 13 – 17
   280, 150,  80,  30,  10,  0        # 18 – 23
]

print("=== AFLUENCIA POR HORA ===")

total_dia = 0
hora_pico = 0
afluencia_pico = 0

for hora, afluencia in enumerate(afluencia_por_hora):
    if afluencia <= 0:
        continue

    total_dia += afluencia

    if afluencia > afluencia_pico:
        afluencia_pico = afluencia
        hora_pico = hora

    bloques = afluencia // 30
    barra = "█" * bloques

    pico_tag = " [PICO]" if afluencia >= 300 else ""

    if bloques > 0:
        print(f"Hora {hora:02d} | {barra} {afluencia} asistentes{pico_tag}")
    else:
        print(f"Hora {hora:02d} | {afluencia} asistentes{pico_tag}")

print()
print(f"Total del día : {total_dia:,} asistentes")
print(f"Hora pico     : Hora {hora_pico:02d} con {afluencia_pico} asistentes")


# ============================================================
#  Ejercicio 4.2 — Simulador de Plan de Pagos  (8 pts)
# ============================================================

precio_vip = 1200

print("\n=== SIMULADOR DE PAGOS — ENTRADA VIP ===")

# Validación de cuota
while True:
    try:
        cuota = int(input("Ingresa tu cuota mensual (Q): "))
    except ValueError:
        print("Ingresa un número válido.")
        continue

    if cuota < 100:
        print("La cuota mínima es Q100")
        continue
    if cuota > 600:
        print("La cuota máxima es Q600")
        continue
    if cuota % 50 != 0:
        print("La cuota debe ser múltiplo de 50")
        continue

    break

print(f"Cuota ingresada válida: Q{cuota:.2f}\n")

print("=== PLAN DE PAGOS ===")
saldo = float(precio_vip)
num_cuota = 0
total_pagado = 0.0

while saldo > 0:
    num_cuota += 1
    pago = float(cuota)
    if pago > saldo:
        pago = saldo

    saldo -= pago
    total_pagado += pago

    print(f"Cuota #{num_cuota} : Q{pago:.2f} | Saldo restante: Q{saldo:.2f}")

print()
print(f"Total de cuotas : {num_cuota}")
print(f"Total pagado    : Q{total_pagado:.2f}")


# ============================================================
#  Ejercicio 4.3 — Ranking de Géneros Musicales  (9 pts)
# ============================================================

# --- Datos de prueba (NO modificar) ---
artistas = [
    ("Resonancia",   "Rock"),        ("Pixel Dreams",  "Electrónica"),
    ("La Guardia",   "Reggaeton"),   ("Voz del Sur",   "Folk"),
    ("Bass Station", "Electrónica"), ("Los Caminos",   "Rock"),
    ("Noche Caribe", "Reggaeton"),   ("Eco Urbano",    "Hip-Hop"),
    ("Marimba 2.0",  "Folk"),        ("Circuito",      "Electrónica"),
    ("Tierra Roja",  "Rock"),        ("Bit a Bit",     "Hip-Hop"),
    ("Cumbia Tech",  "Cumbia"),      ("Guitarra 404",  "Rock"),
]

generos = []
conteos = []

# 1) Contar con listas paralelas
for nombre, genero in artistas:
    if genero in generos:
        idx = generos.index(genero)
        conteos[idx] += 1
    else:
        generos.append(genero)
        conteos.append(1)

# 2) Ordenar de mayor a menor conteo (sin diccionarios)
n = len(conteos)
for i in range(n):
    for j in range(i + 1, n):
        if conteos[j] > conteos[i]:
            conteos[i], conteos[j] = conteos[j], conteos[i]
            generos[i], generos[j] = generos[j], generos[i]

# 3) Imprimir ranking
print("\n=== RANKING DE GÉNEROS DATAFEST 2026 ===")
for i in range(len(generos)):
    genero = generos[i]
    cnt = conteos[i]
    barra = "█" * cnt
    print(f"#{i+1}  {genero:<12} {barra:<4} {cnt} artistas")
