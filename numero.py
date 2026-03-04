class Numero:
    def __init__(self, num_1):
        self.num_1 = num_1 

    def get_numero(self):
        return self.num_1

    def set_numero(self, nuevo_num_1):
        self.num_1 = nuevo_num_1

    def imprimir_numero(self):
        print(f"El número es ➡️: {self.num_1}")
        print()