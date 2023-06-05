
primer_var = input("Escriba la primera palabra: ")
segundo_var = input("Escriba la segunda palabra: ")

if len(primer_var)>len(segundo_var):
    print("La palabra con mas caracteres es:", primer_var, "con", len(primer_var), "caracteres.")
else:
    print("La palabra con mas caracteres es:", segundo_var, "con", len(segundo_var), "caracteres.")

