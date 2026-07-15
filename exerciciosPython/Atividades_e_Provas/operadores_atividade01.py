
#aluno Antonio Miguel

print("PASSOU DE ANO?")

AV1 = float(input("digite sua nota da AV1: "))
AV2 = float(input("digite sua nota da AV2: "))
media = (AV1 + AV2) / 2

freq = float(input("digite sua % de frequencia: "))

print("media final: {} \nfrequencia: {}".format(media, freq))

if freq >= 75 and media >= 7:
    print("status: aprovado")
elif freq < 75 or (freq >= 75 and media < 5):
        print("status: reprovado")
elif freq >= 75 and 5.0 <= media <= 6.9:
    print("status: recuperação")
