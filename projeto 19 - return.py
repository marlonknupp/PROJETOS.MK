def calculadora (operacao):
    
    def soma (a , b):
        return(a + b)
    
    def mult (a , b):
        return a * b
    
    def div (a , b):
        return a / b
    
    def sub (a , b):
        return(a - b)
    
    if operacao == "+":
       return soma
    
    if operacao == "*":
       return mult
    
    if operacao == "-":
       return sub
    
    if operacao == "/":
       return div
    
op = calculadora("+")
print(op(2,2))
op = calculadora("-")
print(op(2,2))
op = calculadora("*")
print(op(2,2))
op = calculadora("/")
print(op(2,2))

    
