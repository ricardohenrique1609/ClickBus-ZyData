import pandas as pd
import re

# Arquivo de entrada e saída
input_file = "clickbus_tratado 1.csv"
output_file = "clickbus_tratado_final.csv"

# Lista de cidades brasileiras para o mapeamento
city_list = [
    "São Paulo","Rio de Janeiro","Belo Horizonte","Curitiba","Porto Alegre","Brasília",
    "Salvador","Fortaleza","Recife","Florianópolis","Manaus","Natal","Belém","Goiânia",
    "Vitória","Campinas","Santos","Ribeirão Preto","Maceió","João Pessoa","Teresina",
    "Palmas","Aracaju","São Luís","Caxias do Sul","Blumenau","Niterói","Uberlândia",
    "Londrina","Anápolis","Sorocaba","Maringá","Bauru","Juiz de Fora","Vitória da Conquista",
    "Cuiabá","Campo Grande","Belo Jardim"
]

# Função para mapear cidades
def map_city(label):
    if pd.isna(label):
        return label
    s = str(label).strip()
    m = re.search(r'(\d+)$', s)  # pega número no final
    if m:
        idx = int(m.group(1)) - 1
        return city_list[idx % len(city_list)]
    return s

# Dicionário para armazenar os clientes já vistos
cliente_map = {}
contador = 1

# Função para mapear clientes incrementais
def map_cliente(label):
    global contador
    if pd.isna(label):
        return label
    s = str(label).strip()
    if s not in cliente_map:
        cliente_map[s] = f"cliente{contador}"
        contador += 1
    return cliente_map[s]

# Ler o arquivo
df = pd.read_csv(input_file)

# Colunas que podem ter cidades
cols_city = [
    "place_origin_departure",
    "place_destination_departure",
    "place_origin_return",
    "place_destination_return"
]

# Colunas que podem ter clientes
cols_nome = [
    "fk_contact",   # <- a que você mostrou
    # se tiver mais, só adicionar aqui
]

# Aplicar mapeamento de cidades
for c in cols_city:
    if c in df.columns:
        df[c] = df[c].apply(map_city)

# Aplicar mapeamento de clientes
for c in cols_nome:
    if c in df.columns:
        df[c] = df[c].apply(map_cliente)

# Salvar novo CSV tratado
df.to_csv(output_file, index=False)

print(f"Arquivo tratado salvo como: {output_file}")
