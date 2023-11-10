import sympy as sp

def find_polinomial(koefisiens, x):
    polinom = 0
    degree = len(koefisiens)-1
    for i, koefisien in enumerate(koefisiens):
        polinom += koefisien * (x **(degree - i))
    return polinom


def main():
    user_input = input("Which one do you want to count today, polynomial or integral ? ")

    if user_input == "polynomial":
        degree = int(input("Please input the degree of the polynomial : "))
        koefisiens = []

        for i in range(degree + 1):
            if (degree - i) > 0:
                koefisien = float(input(f"Please input the coefficient x^{degree - i} : "))
            else:
                koefisien = float(input(f"Please input the coefficient constant : "))
            koefisiens.append(koefisien)


        x = float(input("Please input the number of x : "))

        result = find_polinomial(koefisiens, x)

        print(f"The result of the polynomial at x = {x} is : {result}")

    elif user_input == "integral":
        number_input = input("Enter a number in terms of 'x': ")
    
        x = sp.symbols('x')
    
        try:
            number = sp.sympify(number_input)  
            integral = sp.integrate(number, x)
        
            print("Integral :", integral + sp.Symbol('C'))

        except sp.SympifyError:
            print("Invalid expression. Please enter a valid mathematical expression.")

    return()

if __name__=="__main__":
    main()
