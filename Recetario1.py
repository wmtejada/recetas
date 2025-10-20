# sistema_recetas_interactivo.py
from collections import defaultdict

class GestorRecetas:
    def __init__(self):
        # Base de datos simplificada - solo nombres de recetas
        self.recetas = [
            "Paella",
            "Lasagna", 
            "Brownies",
            "Ensalada César",
            "Sopa de Tomate",
            "Tacos",
            "Pizza Margherita"
        ]
        
        self.ingredientes = [
            # Paella
            {"receta": "Paella", "ingrediente": "Arroz", "cantidad": 400, "unidad": "g"},
            {"receta": "Paella", "ingrediente": "Gambas", "cantidad": 200, "unidad": "g"},
            {"receta": "Paella", "ingrediente": "Guisantes", "cantidad": 100, "unidad": "g"},
            {"receta": "Paella", "ingrediente": "Pimiento", "cantidad": 2, "unidad": "unidad"},
            {"receta": "Paella", "ingrediente": "Azafrán", "cantidad": 1, "unidad": "sobre"},
            
            # Lasagna
            {"receta": "Lasagna", "ingrediente": "Arroz", "cantidad": 500, "unidad": "g"},
            {"receta": "Lasagna", "ingrediente": "Carne molida", "cantidad": 600, "unidad": "g"},
            {"receta": "Lasagna", "ingrediente": "Salsa tomate", "cantidad": 400, "unidad": "ml"},
            {"receta": "Lasagna", "ingrediente": "Queso ricotta", "cantidad": 250, "unidad": "g"},
            {"receta": "Lasagna", "ingrediente": "Queso mozzarella", "cantidad": 200, "unidad": "g"},
            
            # Brownies
            {"receta": "Brownies", "ingrediente": "Chocolate", "cantidad": 300, "unidad": "g"},
            {"receta": "Brownies", "ingrediente": "Harina", "cantidad": 200, "unidad": "g"},
            {"receta": "Brownies", "ingrediente": "Azúcar", "cantidad": 250, "unidad": "g"},
            {"receta": "Brownies", "ingrediente": "Mantequilla", "cantidad": 150, "unidad": "g"},
            {"receta": "Brownies", "ingrediente": "Huevos", "cantidad": 3, "unidad": "unidad"},
            
            # Ensalada César
            {"receta": "Ensalada César", "ingrediente": "Lechuga", "cantidad": 1, "unidad": "unidad"},
            {"receta": "Ensalada César", "ingrediente": "Pollo", "cantidad": 300, "unidad": "g"},
            {"receta": "Ensalada César", "ingrediente": "Crutones", "cantidad": 100, "unidad": "g"},
            {"receta": "Ensalada César", "ingrediente": "Queso parmesano", "cantidad": 80, "unidad": "g"},
            {"receta": "Ensalada César", "ingrediente": "Salsa César", "cantidad": 120, "unidad": "ml"},
            
            # Sopa de Tomate
            {"receta": "Sopa de Tomate", "ingrediente": "Tomates", "cantidad": 8, "unidad": "unidad"},
            {"receta": "Sopa de Tomate", "ingrediente": "Cebolla", "cantidad": 1, "unidad": "unidad"},
            {"receta": "Sopa de Tomate", "ingrediente": "Ajo", "cantidad": 2, "unidad": "diente"},
            {"receta": "Sopa de Tomate", "ingrediente": "Caldo de pollo", "cantidad": 500, "unidad": "ml"},
            {"receta": "Sopa de Tomate", "ingrediente": "Crema", "cantidad": 100, "unidad": "ml"},
            
            # Tacos
            {"receta": "Tacos", "ingrediente": "Tortillas de maíz", "cantidad": 12, "unidad": "unidad"},
            {"receta": "Tacos", "ingrediente": "Carne de res", "cantidad": 500, "unidad": "g"},
            {"receta": "Tacos", "ingrediente": "Cebolla", "cantidad": 1, "unidad": "unidad"},
            {"receta": "Tacos", "ingrediente": "Cilantro", "cantidad": 1, "unidad": "manojo"},
            {"receta": "Tacos", "ingrediente": "Limón", "cantidad": 3, "unidad": "unidad"},
            
            # Pizza Margherita
            {"receta": "Pizza Margherita", "ingrediente": "Masa de pizza", "cantidad": 1, "unidad": "unidad"},
            {"receta": "Pizza Margherita", "ingrediente": "Salsa de tomate", "cantidad": 200, "unidad": "ml"},
            {"receta": "Pizza Margherita", "ingrediente": "Mozzarella", "cantidad": 250, "unidad": "g"},
            {"receta": "Pizza Margherita", "ingrediente": "Albahaca", "cantidad": 1, "unidad": "manojo"},
            {"receta": "Pizza Margherita", "ingrediente": "Aceite de oliva", "cantidad": 30, "unidad": "ml"}
        ]
    
    def calcular_compras(self, pedido):
        """Calcula los ingredientes necesarios para un pedido"""
        compras = defaultdict(lambda: {'cantidad': 0, 'unidad': ''})
        
        for receta_nombre, cantidad_recetas in pedido.items():
            # Verificar si la receta existe
            if receta_nombre not in self.recetas:
                print(f"⚠️ Receta '{receta_nombre}' no encontrada")
                continue
            
            # Obtener ingredientes de esta receta
            ingredientes_receta = [i for i in self.ingredientes if i["receta"] == receta_nombre]
            
            for ingrediente in ingredientes_receta:
                nombre_ing = ingrediente["ingrediente"]
                cantidad_ing = ingrediente["cantidad"] * cantidad_recetas
                unidad_ing = ingrediente["unidad"]
                
                compras[nombre_ing]['cantidad'] += cantidad_ing
                compras[nombre_ing]['unidad'] = unidad_ing
        
        return compras
    
    def mostrar_lista_compras(self, compras, pedido):
        """Muestra la lista de compras en formato legible"""
        if not compras:
            print("📝 No hay ingredientes que comprar")
            return
        
        print("\n" + "="*60)
        print("🛒 LISTA DE COMPRAS FINAL")
        print("="*60)
        
        # Mostrar resumen del pedido
        print("\n📋 RESUMEN DEL PEDIDO:")
        for receta, cantidad in pedido.items():
            print(f"   - {receta}: {cantidad} veces")
        
        print("\n📦 INGREDIENTES NECESARIOS:")
        print("-" * 50)
        
        # Ordenar ingredientes alfabéticamente
        for ingrediente, datos in sorted(compras.items()):
            cantidad = datos['cantidad']
            unidad = datos['unidad']
            
            # Formatear cantidades
            if cantidad == int(cantidad):
                cantidad_str = str(int(cantidad))
            else:
                cantidad_str = f"{cantidad:.1f}"
            
            print(f"🍅 {ingrediente:<20} {cantidad_str:>6} {unidad}")
        
        print("="*60)
        print(f"📊 Total de ingredientes diferentes: {len(compras)}")

class InterfazUsuario:
    def __init__(self):
        self.gestor = GestorRecetas()
        self.pedido_actual = {}
    
    def mostrar_menu_principal(self):
        """Muestra el menú principal"""
        while True:
            print("\n" + "="*50)
            print("🍳 SISTEMA DE GESTIÓN DE RECETAS")
            print("="*50)
            print("1. 📋 Ver todas las recetas")
            print("2. 🛒 Agregar receta al pedido")
            print("3. 📊 Ver pedido actual")
            print("4. 🧹 Limpiar pedido")
            print("5. ✅ Calcular lista de compras")
            print("6. ❌ Salir")
            
            opcion = input("\nSelecciona una opción (1-6): ").strip()
            
            if opcion == "1":
                self.mostrar_recetas()
            elif opcion == "2":
                self.agregar_al_pedido()
            elif opcion == "3":
                self.mostrar_pedido_actual()
            elif opcion == "4":
                self.limpiar_pedido()
            elif opcion == "5":
                self.calcular_y_mostrar_compras()
            elif opcion == "6":
                print("👋 ¡Gracias por usar el sistema! ¡Hasta luego!")
                break
            else:
                print("❌ Opción no válida. Por favor selecciona 1-6.")
    
    def mostrar_recetas(self):
        """Muestra todas las recetas disponibles con detalles"""
        print("\n" + "="*50)
        print("📖 RECETAS DISPONIBLES")
        print("="*50)
        
        for i, receta in enumerate(self.gestor.recetas, 1):
            print(f"\n{i}. 🍽️ {receta}")
            print("   Ingredientes:")
            
            ingredientes = [ing for ing in self.gestor.ingredientes if ing["receta"] == receta]
            for ing in ingredientes:
                print(f"      - {ing['ingrediente']}: {ing['cantidad']} {ing['unidad']}")
    
    def agregar_al_pedido(self):
        """Interfaz para agregar recetas al pedido"""
        print("\n" + "="*50)
        print("🛒 AGREGAR AL PEDIDO")
        print("="*50)
        
        # Mostrar recetas numeradas
        print("\nSelecciona una receta:")
        for i, receta in enumerate(self.gestor.recetas, 1):
            print(f"{i}. {receta}")
        
        print("0. ↩️ Volver al menú principal")
        
        try:
            seleccion = int(input("\nNúmero de receta: "))
            if seleccion == 0:
                return
            
            if seleccion < 1 or seleccion > len(self.gestor.recetas):
                print("❌ Número de receta no válido")
                return
            
            receta_seleccionada = self.gestor.recetas[seleccion - 1]
            
            # Pedir cantidad
            cantidad = int(input(f"¿Cuántas veces prepararás '{receta_seleccionada}'? "))
            if cantidad <= 0:
                print("❌ La cantidad debe ser mayor a 0")
                return
            
            # Agregar al pedido
            if receta_seleccionada in self.pedido_actual:
                self.pedido_actual[receta_seleccionada] += cantidad
                print(f"✅ Actualizado: {receta_seleccionada} = {self.pedido_actual[receta_seleccionada]} veces")
            else:
                self.pedido_actual[receta_seleccionada] = cantidad
                print(f"✅ Agregado: {receta_seleccionada} x {cantidad}")
            
        except ValueError:
            print("❌ Por favor ingresa un número válido")
    
    def mostrar_pedido_actual(self):
        """Muestra el pedido actual"""
        print("\n" + "="*40)
        print("📊 PEDIDO ACTUAL")
        print("="*40)
        
        if not self.pedido_actual:
            print("📝 El pedido está vacío")
            return
        
        total_recetas = sum(self.pedido_actual.values())
        print(f"Total de preparaciones: {total_recetas}")
        print("\nRecetas en el pedido:")
        
        for i, (receta, cantidad) in enumerate(self.pedido_actual.items(), 1):
            print(f"{i}. {receta}: {cantidad} veces")
    
    def limpiar_pedido(self):
        """Limpia el pedido actual"""
        if not self.pedido_actual:
            print("📝 El pedido ya está vacío")
            return
        
        print(f"\n¿Estás seguro de que quieres limpiar el pedido?")
        print(f"Se eliminarán {len(self.pedido_actual)} recetas")
        confirmar = input("(s/n): ").strip().lower()
        
        if confirmar == 's':
            self.pedido_actual.clear()
            print("✅ Pedido limpiado correctamente")
        else:
            print("❌ Operación cancelada")
    
    def calcular_y_mostrar_compras(self):
        """Calcula y muestra la lista de compras final"""
        if not self.pedido_actual:
            print("❌ No hay recetas en el pedido. Agrega algunas recetas primero.")
            return
        
        print("\n🔄 Calculando lista de compras...")
        compras = self.gestor.calcular_compras(self.pedido_actual)
        self.gestor.mostrar_lista_compras(compras, self.pedido_actual)

# Ejecutar el programa
if __name__ == "__main__":
    sistema = InterfazUsuario()
    sistema.mostrar_menu_principal()