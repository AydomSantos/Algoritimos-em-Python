from datetime import datetime
import collections

class Veiculo:
    def __init__(self, placa, tipo):
        self.__placa = placa
        self.__tipo = tipo
        self.__hora_entrada = None
        self.vaga = None  # Adicionado para rastrear a vaga ocupada

    @property
    def placa(self):
        return self.__placa

    @property
    def tipo(self):
        return self.__tipo

    @property
    def hora_entrada(self):
        return self.__hora_entrada

    @hora_entrada.setter
    def hora_entrada(self, value):
        self.__hora_entrada = value

class Vaga:
    def __init__(self, numero, tipo):
        self.__numero = numero
        self.__tipo = tipo
        self.__ocupada = False
        self.__veiculo = None

    @property
    def numero(self):
        return self.__numero

    @property
    def tipo(self):
        return self.__tipo

    @property
    def ocupada(self):
        return self.__ocupada

    @property
    def veiculo(self):
        return self.__veiculo

    def ocupar(self, veiculo):
        self.__veiculo = veiculo
        self.__ocupada = True

    def liberar(self):
        self.__veiculo = None
        self.__ocupada = False

class Estacionamento:
    def __init__(self, nome, capacidade_carro, capacidade_moto):
        self.__nome = nome
        self.__capacidade_carro = capacidade_carro
        self.__capacidade_moto = capacidade_moto
        self.__vagas = []
        self.__vagas_livres_por_tipo = {'carro': collections.deque(), 'moto': collections.deque()}
        self.__veiculos_estacionados = {}  # Dicionário: {placa: Veiculo}
        self.__historico = []
        self.__faturamento = 0
        self.__criar_vagas(capacidade_carro, capacidade_moto)
    def __criar_vagas(self, qtd_carro, qtd_moto):
        numero = 1
        for _ in range(qtd_carro):
            vaga = Vaga(numero, 'carro')
            self.__vagas.append(vaga)
            self.__vagas_livres_por_tipo['carro'].append(vaga)
            numero += 1

        for _ in range(qtd_moto):
            vaga = Vaga(numero, 'moto')
            self.__vagas.append(vaga)
            self.__vagas_livres_por_tipo['moto'].append(vaga)
            numero += 1

    def encontrar_vaga_livre(self, tipo_veiculo):
        if tipo_veiculo in self.__vagas_livres_por_tipo and self.__vagas_livres_por_tipo[tipo_veiculo]:
            return self.__vagas_livres_por_tipo[tipo_veiculo][0]
        return None

    def ocupar_vaga(self, veiculo, vaga):
        if vaga and not vaga.ocupada:
            vaga.ocupar(veiculo)
            try:
                self.__vagas_livres_por_tipo[veiculo.tipo].remove(vaga)
            except ValueError:
                print(f"Erro ao remover vaga {vaga.numero} da lista de livres de {veiculo.tipo}.")
            return True
        return False

    def liberar_vaga(self, vaga):
        if vaga and vaga.ocupada:
            vaga.liberar()
            self.__vagas_livres_por_tipo[vaga.tipo].append(vaga)
            return True
        return False

    def registrar_entrada(self, placa, tipo):
        if placa in self.__veiculos_estacionados:
            print(f"Veículo com placa {placa} já está estacionado.")
            return

        veiculo = Veiculo(placa, tipo)
        vaga_livre = self.encontrar_vaga_livre(tipo)

        if vaga_livre:
            veiculo.hora_entrada = datetime.now()
            veiculo.vaga = vaga_livre  # Associa a vaga ao veículo
            if self.ocupar_vaga(veiculo, vaga_livre):
                self.__veiculos_estacionados[placa] = veiculo
                print(f"Veículo {placa} ({tipo}) entrou no estacionamento às {veiculo.hora_entrada.strftime('%H:%M:%S')} - Vaga {vaga_livre.numero}")
                self.__historico.append(f"Entrada - {veiculo.placa} ({veiculo.tipo}) - Vaga {vaga_livre.numero} - {veiculo.hora_entrada.strftime('%H:%M:%S')}")
            else:
                print(f"Erro ao ocupar a vaga para o veículo {placa}.")
        else:
            print(f"Não há vagas disponíveis para {tipo} no momento.")

    def registrar_saida(self, placa):
        if placa in self.__veiculos_estacionados:
            veiculo = self.__veiculos_estacionados[placa]
            vaga_ocupada = veiculo.vaga

            if vaga_ocupada:
                hora_saida = datetime.now()
                tempo_estacionado = hora_saida - veiculo.hora_entrada
                minutos_estacionados = int(tempo_estacionado.total_seconds() / 60)
                valor_a_pagar = self.__calcular_valor_estacionamento(minutos_estacionados)
                self.__faturamento += valor_a_pagar

                self.liberar_vaga(vaga_ocupada)
                del self.__veiculos_estacionados[placa]
                veiculo.vaga = None
                print(f"Veículo {placa} saiu do estacionamento às {hora_saida.strftime('%H:%M:%S')}, ficou estacionado por {minutos_estacionados} minutos e o valor a pagar é R${valor_a_pagar:.2f}")
                self.__historico.append(f"Saída - {veiculo.placa} ({veiculo.tipo}) - Vaga {vaga_ocupada.numero} - {hora_saida.strftime('%H:%M:%S')} - {minutos_estacionados} minutos - R${valor_a_pagar:.2f}")
            else:
                print(f"Erro: Veículo {placa} não tem vaga associada.")
        else:
            print(f"O veículo {placa} não está estacionado.")

    def __calcular_valor_estacionamento(self, minutos_estacionados):
        valor_por_hora = 5.00
        valor_total = (minutos_estacionados // 60) * valor_por_hora
        return valor_total

    def gerar_relatorio(self):
        print(f"\n{'='*30}")
        print(f"Relatório - {self.__nome}")
        print(f"Vagas totais: {len(self.__vagas)}")
        print(f"Vagas livres: {sum(len(lista) for lista in self.__vagas_livres_por_tipo.values())}")
        print(f"Faturamento total: R${self.__faturamento:.2f}")
        print(f"Veículos estacionados: {len(self.__veiculos_estacionados)}")
        print(f"Histórico de movimentações: {len(self.__historico)} registros")
        print(f"{'='*30}\n")

