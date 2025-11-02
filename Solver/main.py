# ============================================
# PROYECTO: Optimización de Sistema de Redes de Comunicaciones
# Materia: Álgebra Lineal
# ============================================
import numpy as np
import time
import sys

# Colores ANSI para la consola
class Colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def print_slow(text, delay=0.02):
    """Imprime texto con efecto de escritura"""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def print_box(text, color=Colors.CYAN, width=70):
    """Imprime texto en una caja bonita"""
    print(color + "╔" + "═" * (width - 2) + "╗" + Colors.ENDC)
    print(color + "║" + text.center(width - 2) + "║" + Colors.ENDC)
    print(color + "╚" + "═" * (width - 2) + "╝" + Colors.ENDC)

def print_section(title, color=Colors.BLUE):
    """Imprime un título de sección"""
    print("\n" + color + "┌" + "─" * 68 + "┐" + Colors.ENDC)
    print(color + "│" + Colors.BOLD + title.center(68) + Colors.ENDC + color + "│" + Colors.ENDC)
    print(color + "└" + "─" * 68 + "┘" + Colors.ENDC)

def print_matrix(matrix, name="MATRIZ", color=Colors.CYAN):
    """Imprime una matriz de forma bonita"""
    print(color + f"\n{name}:" + Colors.ENDC)
    rows, cols = matrix.shape
    
    # Encontrar el ancho máximo necesario
    max_width = max(len(f"{val:.2f}") for row in matrix for val in row)
    
    for i, row in enumerate(matrix):
        if i == 0:
            print(color + "┌ " + Colors.ENDC, end="")
        elif i == rows - 1:
            print(color + "└ " + Colors.ENDC, end="")
        else:
            print(color + "│ " + Colors.ENDC, end="")
        
        for j, val in enumerate(row):
            print(f"{val:>{max_width}.2f}", end="  ")
        
        if i == 0:
            print(color + "┐" + Colors.ENDC)
        elif i == rows - 1:
            print(color + "┘" + Colors.ENDC)
        else:
            print(color + "│" + Colors.ENDC)

def print_vector(vector, name="VECTOR", color=Colors.GREEN):
    """Imprime un vector de forma bonita"""
    print(color + f"\n{name}:" + Colors.ENDC)
    for i, val in enumerate(vector):
        if i == 0:
            print(color + "┌ " + Colors.ENDC + f"{val:>8.2f} " + color + "┐" + Colors.ENDC)
        elif i == len(vector) - 1:
            print(color + "└ " + Colors.ENDC + f"{val:>8.2f} " + color + "┘" + Colors.ENDC)
        else:
            print(color + "│ " + Colors.ENDC + f"{val:>8.2f} " + color + "│" + Colors.ENDC)

def loading_animation(text="Procesando", duration=1.5):
    """Muestra una animación de carga"""
    animation = ["⠋", "⠙", "⠹", "⠸", "⠼", "⠴", "⠦", "⠧", "⠇", "⠏"]
    end_time = time.time() + duration
    i = 0
    while time.time() < end_time:
        sys.stdout.write(f'\r{Colors.YELLOW}{animation[i % len(animation)]} {text}...{Colors.ENDC}')
        sys.stdout.flush()
        time.sleep(0.1)
        i += 1
    sys.stdout.write('\r' + ' ' * 50 + '\r')
    sys.stdout.flush()

# ============================================
# INICIO DEL PROGRAMA
# ============================================
print("\n" * 2)
print_box("OPTIMIZACIÓN DE SISTEMA DE REDES", Colors.CYAN, 70)
print_box("Proyecto de Álgebra Lineal", Colors.BLUE, 70)
time.sleep(0.5)

# ----------------------------
# FASE 1: Planteamiento del Problema
# ----------------------------
print_section("⚡ FASE 1: PLANTEAMIENTO DEL PROBLEMA", Colors.BLUE)

usar_ejemplo = input(f"\n{Colors.CYAN}❓ ¿Desea usar el ejemplo del documento? (s/n): {Colors.ENDC}").lower()

if usar_ejemplo == 's':
    loading_animation("Cargando datos de ejemplo")
    
    n = 3
    A_original = np.array([[-2., 1., 1.],
                           [1., -2., 1.],
                           [1., 1., -2.]])
    
    A_modificada = np.array([[-3., 1., 1.],
                             [1., -3., 1.],
                             [1., 1., -3.]])
    
    b = np.array([100., 200., 150.])
    
    print(f"\n{Colors.YELLOW}⚠️  NOTA IMPORTANTE:{Colors.ENDC}")
    print("   La matriz original del documento NO es invertible.\n")
    
    print(f"{Colors.GREEN}   [1]{Colors.ENDC} Matriz ORIGINAL (determinante = 0)")
    print(f"       → Se usará pseudo-inversa para solución aproximada")
    
    print(f"\n{Colors.GREEN}   [2]{Colors.ENDC} Matriz MODIFICADA (invertible)")
    print(f"       → Diagonal ajustada: -3 en lugar de -2\n")
    
    opcion = input(f"{Colors.CYAN}🎯 Seleccione opción (1 o 2): {Colors.ENDC}")
    
    if opcion == "2":
        A = A_modificada
        print(f"{Colors.GREEN}✓ Usando matriz MODIFICADA{Colors.ENDC}")
    else:
        A = A_original
        print(f"{Colors.YELLOW}⚠ Usando matriz ORIGINAL{Colors.ENDC}")
        
else:
    n = int(input(f"\n{Colors.CYAN}📊 Ingrese el número de nodos en la red: {Colors.ENDC}"))
    
    print(f"\n{Colors.BLUE}╔{'═' * 60}╗{Colors.ENDC}")
    print(f"{Colors.BLUE}║{'INGRESO DE MATRIZ A (Coeficientes de Conexión)'.center(60)}║{Colors.ENDC}")
    print(f"{Colors.BLUE}╚{'═' * 60}╝{Colors.ENDC}")
    
    A = []
    for i in range(n):
        fila = list(map(float, input(f"{Colors.CYAN}   Fila {i+1}: {Colors.ENDC}").split()))
        A.append(fila)
    A = np.array(A)
    
    print(f"\n{Colors.BLUE}╔{'═' * 60}╗{Colors.ENDC}")
    print(f"{Colors.BLUE}║{'INGRESO DE VECTOR b (Demanda de Tráfico)'.center(60)}║{Colors.ENDC}")
    print(f"{Colors.BLUE}╚{'═' * 60}╝{Colors.ENDC}")
    
    b = []
    for i in range(n):
        valor = float(input(f"{Colors.CYAN}   Demanda del nodo {i+1}: {Colors.ENDC}"))
        b.append(valor)
    b = np.array(b)

time.sleep(0.3)
print_matrix(A, "MATRIZ A (Coeficientes de Conexión)", Colors.CYAN)
print_vector(b, "VECTOR b (Demanda de Tráfico)", Colors.GREEN)

# ----------------------------
# FASE 2: Análisis de la Matriz
# ----------------------------
print_section("🔍 FASE 2: ANÁLISIS DE LA MATRIZ", Colors.BLUE)

loading_animation("Analizando propiedades matemáticas", 1.0)

det_A = np.linalg.det(A)
rank_A = np.linalg.matrix_rank(A)
rank_Aug = np.linalg.matrix_rank(np.column_stack((A, b)))

print(f"\n{Colors.BOLD}{Colors.BLUE}📈 PROPIEDADES MATEMÁTICAS:{Colors.ENDC}\n")
print(f"{Colors.CYAN}   ▪ Determinante de A:{Colors.ENDC}  {det_A:>15.6f}")
print(f"{Colors.CYAN}   ▪ Rango(A):{Colors.ENDC}           {rank_A:>15}")
print(f"{Colors.CYAN}   ▪ Rango(A|b):{Colors.ENDC}         {rank_Aug:>15}")
print(f"{Colors.CYAN}   ▪ Dimensión:{Colors.ENDC}          {n:>15} × {n}")

tolerancia = 1e-10

# ----------------------------
# FASE 3: Resolución del Sistema
# ----------------------------
print_section("⚙️  FASE 3: RESOLUCIÓN DEL SISTEMA Ax = b", Colors.BLUE)

loading_animation("Resolviendo sistema de ecuaciones", 1.5)

if abs(det_A) > tolerancia:
    # Caso 1: Matriz invertible
    print(f"\n{Colors.GREEN}{Colors.BOLD}✓ MATRIZ INVERTIBLE{Colors.ENDC}")
    print(f"{Colors.GREEN}  El sistema tiene solución ÚNICA{Colors.ENDC}\n")
    
    loading_animation("Calculando matriz inversa", 1.0)
    
    A_inv = np.linalg.inv(A)
    x = np.dot(A_inv, b)
    
    print_matrix(A_inv, "MATRIZ INVERSA A⁻¹", Colors.YELLOW)
    
    print(f"\n{Colors.GREEN}{Colors.BOLD}🎯 SOLUCIÓN x (Flujo de datos óptimo):{Colors.ENDC}")
    print(f"{Colors.GREEN}{'─' * 50}{Colors.ENDC}")
    
    for i in range(n):
        if x[i] >= 0:
            signo = "➜"
            color = Colors.GREEN
        else:
            signo = "➜"
            color = Colors.YELLOW
        
        print(f"   {color}Nodo {i+1}: {x[i]:>10.2f} unidades de flujo {signo}{Colors.ENDC}")
    
    # Verificación
    print(f"\n{Colors.BLUE}{Colors.BOLD}✓ VERIFICACIÓN (A × x = b):{Colors.ENDC}")
    Ax = np.dot(A, x)
    print_vector(Ax, "A × x", Colors.CYAN)
    print_vector(b, "b (original)", Colors.GREEN)
    
    error = np.linalg.norm(Ax - b)
    print(f"\n{Colors.GREEN}   ✓ Error: {error:.2e} (prácticamente cero){Colors.ENDC}")
    
else:
    # Caso 2: Matriz no invertible
    print(f"\n{Colors.RED}{Colors.BOLD}✗ MATRIZ NO INVERTIBLE{Colors.ENDC}")
    print(f"{Colors.RED}  (determinante ≈ 0){Colors.ENDC}\n")
    
    if rank_A == rank_Aug:
        print(f"{Colors.YELLOW}   ℹ  El sistema es CONSISTENTE{Colors.ENDC}")
        print(f"{Colors.YELLOW}      → Tiene infinitas soluciones{Colors.ENDC}")
        estado = "consistente"
    else:
        print(f"{Colors.RED}   ✗ El sistema NO es consistente{Colors.ENDC}")
        print(f"{Colors.RED}      → No tiene solución exacta{Colors.ENDC}")
        estado = "inconsistente"
    
    print(f"\n{Colors.CYAN}   📊 Análisis:{Colors.ENDC}")
    print(f"      • Rango(A) = {rank_A} < {n}")
    print(f"      • Existe dependencia lineal entre nodos")
    print(f"      • Los nodos NO son independientes\n")
    
    loading_animation("Calculando pseudo-inversa (mínimos cuadrados)", 1.5)
    
    A_pinv = np.linalg.pinv(A)
    x_pinv = np.dot(A_pinv, b)
    
    print_matrix(A_pinv, "MATRIZ PSEUDO-INVERSA A⁺", Colors.YELLOW)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}🎯 SOLUCIÓN APROXIMADA x:{Colors.ENDC}")
    print(f"{Colors.YELLOW}{'─' * 50}{Colors.ENDC}")
    
    for i in range(n):
        if x_pinv[i] >= 0:
            signo = "➜"
            color = Colors.GREEN
        else:
            signo = "➜"
            color = Colors.RED
        
        print(f"   {color}Nodo {i+1}: {x_pinv[i]:>10.2f} unidades de flujo {signo}{Colors.ENDC}")
    
    # Verificación
    print(f"\n{Colors.BLUE}{Colors.BOLD}🔍 VERIFICACIÓN:{Colors.ENDC}")
    Ax_aprox = np.dot(A, x_pinv)
    print_vector(Ax_aprox, "A × x_aprox", Colors.YELLOW)
    print_vector(b, "b (objetivo)", Colors.GREEN)
    
    error = np.linalg.norm(Ax_aprox - b)
    print(f"\n{Colors.RED}   ⚠ Error (norma euclidiana): {error:.4f}{Colors.ENDC}")
    
    if estado == "inconsistente":
        print(f"\n{Colors.YELLOW}   ℹ  Esta es la MEJOR aproximación posible{Colors.ENDC}")
        print(f"      (minimiza el error cuadrático)")

# ----------------------------
# FASE 4: Interpretación y Conclusiones
# ----------------------------
print_section("📊 FASE 4: INTERPRETACIÓN Y CONCLUSIONES", Colors.BLUE)

time.sleep(0.5)

print(f"\n{Colors.BOLD}{Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}")
print(f"{Colors.BOLD}{Colors.CYAN}📝 INTERPRETACIÓN DE RESULTADOS{Colors.ENDC}")
print(f"{Colors.BOLD}{Colors.CYAN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}\n")

if abs(det_A) > tolerancia:
    print(f"{Colors.GREEN}✓ Sistema con solución única:{Colors.ENDC}\n")
    print(f"   • La red está BIEN configurada")
    print(f"   • Cada nodo tiene un flujo óptimo determinado")
    print(f"   • {Colors.GREEN}Valores positivos{Colors.ENDC}: flujo neto de SALIDA")
    print(f"   • {Colors.YELLOW}Valores negativos{Colors.ENDC}: flujo neto de ENTRADA")
    
else:
    print(f"{Colors.YELLOW}⚠ Sistema singular (matriz no invertible):{Colors.ENDC}\n")
    print(f"   • Existe DEPENDENCIA entre los nodos")
    print(f"   • Algunos nodos pueden estar redundantes")
    print(f"   • La pseudo-inversa da la mejor aproximación")
    print(f"   • Se minimiza el error cuadrático")

print(f"\n{Colors.CYAN}💡 Significado del vector solución x:{Colors.ENDC}\n")
print(f"   • Cada x[i] es el flujo de datos del nodo i")
print(f"   • {Colors.GREEN}Positivo{Colors.ENDC}: el nodo ENVÍA más de lo que recibe")
print(f"   • {Colors.RED}Negativo{Colors.ENDC}: el nodo RECIBE más de lo que envía")

print(f"\n{Colors.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}")
print(f"{Colors.BLUE}🔧 RECOMENDACIONES PARA MEJORAR LA RED{Colors.ENDC}")
print(f"{Colors.BLUE}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Colors.ENDC}\n")

if abs(det_A) > tolerancia:
    print(f"{Colors.GREEN}   ✓ La configuración actual es ÓPTIMA{Colors.ENDC}")
    print(f"   ✓ Mantener el balance de flujos calculado")
    print(f"   ✓ Monitorear el rendimiento regularmente")
else:
    print(f"{Colors.YELLOW}   ⚙  Revisar las conexiones entre nodos{Colors.ENDC}")
    print(f"   ⚙  Considerar agregar o remover enlaces")
    print(f"   ⚙  Ajustar capacidades (diagonal de A)")
    print(f"   ⚙  Verificar redundancia de nodos")
    print(f"   ⚙  Redistribuir la demanda de tráfico")

print("\n")
print_box("FIN DEL PROYECTO", Colors.GREEN, 70)
print_box("Gracias por usar el sistema", Colors.CYAN, 70)

print(f"\n{Colors.CYAN}Presione Enter para salir...{Colors.ENDC}", end="")
input()