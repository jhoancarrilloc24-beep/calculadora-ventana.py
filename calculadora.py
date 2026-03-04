class Calculadora:
    def __init__(self, tipo_operacion,fecha_de_uso):
        self.tipo_operacion = tipo_operacion
        self.fecha_de_uso = fecha_de_uso
        self.resultado = ""
        
    def get_tipo_operacion(self):
        return self.tipo_operacion
    
    def set_tipo_operacion(self, nuevo_tipo_operacion):
        self.tipo_operacion = nuevo_tipo_operacion
        
    def get_resultado(self):
        return self.resultado
    
    def set_resultado(self, nuevo_resultado):
        self.resultado = nuevo_resultado
    
    def get_fecha_de_uso(self):
        return self.fecha_de_uso
    
    def set_fecha_de_uso(self,nueva_fecha_de_uso):
        self.fecha_de_uso = nueva_fecha_de_uso
        
    def realizar_operacion(self, numero1, numero2):
        oper = self.get_tipo_operacion()
        if oper == "suma":
            self.set_resultado(numero1 + numero2)
        elif oper == "resta":
            self.set_resultado(numero1 - numero2)
        elif oper == "multiplicacion":
            self.set_resultado(numero1 * numero2)
        elif oper == "division":
            if numero2 != 0:
                self.set_resultado(numero1 / numero2)
            else:
                self.set_resultado("Error no se puede dividir por cero")
        else:
            self.set_resultado("Operación no soportada")
    
    def guardar_info(self, entry_resultado):
        objetos = entry_resultado if isinstance(entry_resultado, (list, tuple)) else [entry_resultado]
        with open("calculadora datos.txt", "a", encoding="utf-8") as archivo:
            for obj in objetos:
                archivo.write(f"\n")
                archivo.write("informacion de la calculadora 📂\n")
                archivo.write(f"tipo operacion: {obj.get_tipo_operacion()}\n")
                archivo.write(f"resultado: {obj.get_resultado()}\n")
                archivo.write(f"fecha de uso: {obj.get_fecha_de_uso()}\n")
                archivo.write('-' * 40 + "\n")
    
    def imprimir_calculadora(self):
        print("Datos de la calculadora 📠")
        print(f"Tipo de operación: {self.get_tipo_operacion()}")
        print(f"Resultado: {self.get_resultado()}")
        print(f"Fecha de uso: {self.get_fecha_de_uso()}")
        print() 