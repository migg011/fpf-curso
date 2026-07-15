#atividade 1

class Dispositivo:
    rede_padrao = "Rede Doméstica V.2"
    total_ativos = 0

    def __init__(self, id_serie, localizacao):
        self.id_serie = id_serie
        self.localizacao = localizacao
        self.status = "Desconectado"

        Dispositivo.total_ativos += 1

id_serie_input = input("digite o id de série: ")
localizacao_input = input("digite a localização: ")

dispositivo_usuario = Dispositivo(id_serie_input, localizacao_input)

print(f"\nid: {dispositivo_usuario.id_serie}")
print(f"localização: {dispositivo_usuario.localizacao}")
print(f"status: {dispositivo_usuario.status}")
print(f"rede padrão: {Dispositivo.rede_padrao}")
print(f"total de ativos: {Dispositivo.total_ativos}")

#atividade 02

class Estrela:
    tipo_corpo = "corpo celeste"
    total_estrelas_catalogadas = 0

    def __init__(self, nome, massa):
        self.nome = nome
        self.massa = massa
        self.em_atividade = True

        Estrela.total_estrelas_catalogadas += 1

estrela_a = Estrela("alpha Centauri", 1.1)
estrela_b = Estrela("sirius", 2.0)

print(f"\n\nnome: {estrela_a.nome}")
print(f"massa: {estrela_a.massa}")
print(f"em atividade: {estrela_a.em_atividade}")

print(f"\nnome: {estrela_b.nome}")
print(f"massa: {estrela_b.massa}")
print(f"em atividade: {estrela_b.em_atividade}")

print(f"\ntipo de corpo: {Estrela.tipo_corpo}")
print(f"total de estrelas catalogadas: {Estrela.total_estrelas_catalogadas}")