# ============================================================
#  HDT1 — Parte 5: Integrador
#  DataFest 2026 — Sistema de Taquilla Virtual
# ============================================================

# ============================================================
#  Datos del festival (NO modificar)
# ============================================================

cartel = [
    ("Resonancia",     "Rock",        "Apertura"),
    ("Voz del Sur",    "Folk",        "Apertura"),
    ("La Guardia",     "Reggaeton",   "Soporte"),
    ("Eco Urbano",     "Hip-Hop",     "Soporte"),
    ("Marimba 2.0",    "Folk",        "Soporte"),
    ("Pixel Dreams",   "Electrónica", "Principal"),
    ("Bass Station",   "Electrónica", "Principal"),
    ("Los Caminos",    "Rock",        "Principal"),
    ("Tierra Roja",    "Rock",        "Headliner"),
    ("Circuito",       "Electrónica", "Headliner"),
]

zonas_validas  = ["campo", "gradería", "preferencia", "vip"]
precios_base   = [200,     350,        600,           1200 ]

mis_compras = []

print("=" * 40)
print("     TAQUILLA DATAFEST 2026")
print("=" * 40)

opcion = ""

while opcion != "5":
    print("\n1. Ver cartel de artistas")
    print("2. Comprar entrada")
    print("3. Ver mis compras")
    print("4. Resumen de gastos")
    print("5. Salir")
    opcion = input("\nElige una opción: ").strip()

    # ----------------------------------------------------------
    if opcion == "1":
    # ----------------------------------------------------------
        print("\n=== CARTEL DATAFEST 2026 ===")
        for i, (nombre, genero, turno) in enumerate(cartel, start=1):
            print(f"[{i}] {nombre} ({genero}) — Turno: {turno}")

    # ----------------------------------------------------------
    elif opcion == "2":
    # ----------------------------------------------------------
        zona = input("Ingresa la zona (campo/gradería/preferencia/vip): ").strip().lower()
        while zona not in zonas_validas:
            print("Zona no válida")
            zona = input("Ingresa la zona (campo/gradería/preferencia/vip): ").strip().lower()

        while True:
            try:
                cantidad = int(input("Ingresa la cantidad de entradas: ").strip())
            except ValueError:
                print("Cantidad no válida")
                continue
            if cantidad <= 0:
                print("Cantidad no válida")
                continue
            break

        precio = precios_base[zonas_validas.index(zona)]
        total = float(precio * cantidad)

        mis_compras.append([zona, cantidad, total])

        print("\n✓ Compra realizada:")
        print(f"  Zona      : {zona}")
        print(f"  Cantidad  : {cantidad} entradas")
        print(f"  Total     : Q{total:.2f}")

    # ----------------------------------------------------------
    elif opcion == "3":
    # ----------------------------------------------------------
        if len(mis_compras) == 0:
            print("Aún no has comprado entradas.")
        else:
            print("\n=== MIS COMPRAS ===")
            for i, compra in enumerate(mis_compras, start=1):
                zona, cantidad, total = compra
                print(f"Compra {i} | Zona: {zona} | Cantidad: {cantidad} | Total: Q{total:.2f}")

    # ----------------------------------------------------------
    elif opcion == "4":
    # ----------------------------------------------------------
        if len(mis_compras) == 0:
            print("Aún no has realizado ninguna compra.")
        else:
            print("\n=== RESUMEN DE GASTOS ===")
            total_gastado = 0.0
            total_entradas = 0

            zonas = []
            conteos = []

            for compra in mis_compras:
                zona, cantidad, total = compra
                total_gastado += float(total)
                total_entradas += int(cantidad)

                if zona in zonas:
                    idx = zonas.index(zona)
                    conteos[idx] += 1
                else:
                    zonas.append(zona)
                    conteos.append(1)

            # zona favorita = la que aparece más veces (primer empate gana)
            zona_favorita = zonas[0]
            max_c = conteos[0]
            for i in range(1, len(zonas)):
                if conteos[i] > max_c:
                    max_c = conteos[i]
                    zona_favorita = zonas[i]

            print(f"Total gastado    : Q{total_gastado:.2f}")
            print(f"Total entradas   : {total_entradas}")
            print(f"Zona favorita    : {zona_favorita}")

    # ----------------------------------------------------------
    elif opcion == "5":
    # ----------------------------------------------------------
        print("\n¡Gracias por usar la taquilla de DataFest 2026!")
        print("Nos vemos en el festival. 🎵")

    # ----------------------------------------------------------
    else:
    # ----------------------------------------------------------
        print("Opción no válida. Intenta de nuevo.")
