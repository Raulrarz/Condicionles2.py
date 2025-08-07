print("Tipo de trabajo: soldar placa de metal, tubo 2x2 o tubo delgado")
trabajo = input("Ingresa el tipo de trabajo: ")

electrodo = input("Ingresa el electrodo que vas a usar: ")

if trabajo == "placa de metal" and electrodo == "7018":
    print("Soldadura correcta")
elif trabajo == "tubo 2x2" and electrodo == "6013":
    print("Soldadura correcta")
elif trabajo == "tubo delgado" and electrodo == "6011":
    print("Soldadura correcta")
else:
    print("Soldadura incorrecta")
print("Usa el electrodo correcto para el tipo de trabajo que vas a realizar")