from SOS_MULHER import *
vitima_1 = Vitima("Maria", "123.456.789-67","mariajosedasilva@gmail.com","1974","MPU001", True, "10/09/2026")

policial_1 = policial("Sebastião", "143.094.609-43", "joãoPereiraNogueira@gmail.com", "2019", "Batalhao 11", "Sargento")

medida_1 = MedidaProtetiva("PROC001", "10/09/2026", "Ativa", "19/03/2027")

notificacao_1 = Notificacao(1, "vitima acionou o botão SOS", "10/09/2026", False )

Ocorrencia_1 = Ocorrencia(2, "10/09/2026", "Aberta", "Ocorrencia registrada", "Ameaca")

localizacao_1 = Localização(-10.1230, "08/09/2026",-83.10943, "TornozeleiraEletrônica")

agressor_1 = Agressor(3, "Rogério", "065.112.067-42", localizacao_1, 13421)

vitima_1.medidas = []
vitima_1.medidas.append(medida_1)  # Relacionamento: Vitima possui 0..* Medidas Protetivas

vitima_1.notificacoes = []
vitima_1.notificacoes.append(notificacao_1)  # Relacionamento: Vitima possui 0..* Notificacoes

vitima_1.ocorrencias = []
vitima_1.ocorrencias.append(Ocorrencia_1)  # Relacionamento: Vitima possui 0..* Ocorrencias

policial_1.ocorrencias = []
policial_1.ocorrencias.append(Ocorrencia_1)  # Relacionamento: Policial atende 0..* Ocorrencias

notificacao_1.ocorrencias = []
notificacao_1.ocorrencias.append(Ocorrencia_1)  # Relacionamento: Notificacao possui 0..* Ocorrencias

Ocorrencia_1.localizacoes = []
Ocorrencia_1.localizacoes.append(localizacao_1)  # Relacionamento: Ocorrencia possui 1..* Localizacoes

agressor_1.Localizacao = localizacao_1  # Relacionamento: Agressor possui 1 Localizacao

medida_1.agressores = []
medida_1.agressores.append(agressor_1)  # Relacionamento: Medida Protetiva se relaciona com 1..* Agressores