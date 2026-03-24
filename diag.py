meses= input("Ingrese el número de meses: ")
salario = input("Ingrese el salario mensual: ")
def calcular_salario_total(meses, salario):
    try:
        meses = int(meses)
        salario = float(salario)
        if meses < 0 or salario < 0:
            raise ValueError("Los valores no pueden ser negativos.")
        salario_total = meses * salario
        return salario_total
    except ValueError as e:
        print(f"Error: {e}")
        return None