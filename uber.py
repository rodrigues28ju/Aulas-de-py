proibidas = ["assediada", "assedio"]
texto = ("motorista muito bom mas me se senti assediada")
resultado = "assediada" in proibidas
if resultado:
    print("Reclamação Atendida")
    autorizacaoMotorista = False
