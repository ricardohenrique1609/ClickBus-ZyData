# ==============================================================================
# SCRIPT: aplicar_logica_promocional.py
# RESPONSABILIDADE: Ler as predições puras e aplicar as regras de negócio.
# QUEM EXECUTA: O analista de marketing/BI, talvez todo dia.
# ==============================================================================

import pandas as pd
import warnings
warnings.filterwarnings("ignore")

print("🟢 Iniciando script de aplicação da lógica de promoções...")

# --- ARQUIVOS DE ENTRADA E SAÍDA ---
# !!! ATENÇÃO: Verifique se os caminhos e nomes dos arquivos abaixo estão corretos !!!

# Este é o arquivo gerado pelo seu script de ML
path_predicoes_raw = '../outputs/predicoes_clickbus_hierarquico.csv' 

# Este é o arquivo que contém a segmentação RFM dos seus clientes
path_segmentos = '../outputs/clientes_segmentados.csv' 

# Este é o nome do arquivo final que será gerado
path_output_final = '../outputs/predicoes_com_campanhas.csv'


# 1. CARREGAR OS DADOS NECESSÁRIOS
try:
    predicoes = pd.read_csv(path_predicoes_raw)
    print(f"✅ Arquivo de predições '{path_predicoes_raw}' carregado com sucesso.")
except Exception as e:
    print(f"❌ ERRO: Não foi possível carregar o arquivo de predições.")
    print(f"   Verifique se o arquivo existe em: '{path_predicoes_raw}'")
    print(f"   Você rodou o script de ML primeiro?")
    print(e)
    exit()

try:
    df_segmentos = pd.read_csv(path_segmentos)
    # Selecionamos apenas as colunas que vamos usar para a junção
    df_segmentos = df_segmentos[['cliente_id', 'segmento_inteligente']]
    print(f"✅ Arquivo de segmentos '{path_segmentos}' carregado com sucesso.")
except Exception as e:
    print(f"❌ ATENÇÃO: Não foi possível carregar os dados de segmentação.")
    print(f"   Verifique se o arquivo existe em: '{path_segmentos}'")
    print(f"   A coluna de campanha ficará incompleta.")
    print(e)
    # Criamos um dataframe vazio para o script não quebrar
    df_segmentos = pd.DataFrame(columns=['cliente_id', 'segmento_inteligente'])

# 2. UNIR AS PREDIÇÕES COM OS SEGMENTOS DOS CLIENTES
df_final = pd.merge(predicoes, df_segmentos, on='cliente_id', how='left')
df_final['segmento_inteligente'] = df_final['segmento_inteligente'].fillna('Desconhecido')

# 3. DEFINIR A FUNÇÃO COM A LÓGICA DAS CAMPANHAS
def definir_campanha(row):
    # !!! ATENÇÃO: Ajuste os nomes dos segmentos abaixo para bater EXATAMENTE com os nomes no seu arquivo !!!
    segmentos_alto_valor = ['Cliente VIP', 'Frequente Econômico', 'Campeões', 'Fiéis'] # Exemplo
    segmentos_em_risco = ['Inativo', 'Gastador Ocasional', 'Em Risco'] # Exemplo

    segmento = row['segmento_inteligente']
    compra_prevista = row['ira_comprar_7_dias']

    # Prioridade 1: Ação Preditiva (maior chance de conversão)
    if compra_prevista == 1:
        if segmento in segmentos_alto_valor:
            return 'Preditiva VIP'
        else:
            return 'Preditiva Padrão'

    # Prioridade 2: Reativação (maior risco de perda)
    if segmento in segmentos_em_risco:
        return 'Reativação (Risco de Churn)'

    # Prioridade 3: Fidelização (manter os melhores clientes engajados)
    if segmento in segmentos_alto_valor:
        return 'Fidelização VIP'
    
    # Se não se encaixar em nenhuma regra prioritária
    return 'Manutenção (Sem Ação Imediata)'

# 4. APLICAR A LÓGICA PARA CRIAR A NOVA COLUNA
df_final['campanha_sugerida'] = df_final.apply(definir_campanha, axis=1)
print("✅ Lógica de campanha aplicada.")

# 5. (BÔNUS) GERAR TEXTO PERSONALIZADO DA OFERTA
def gerar_texto_oferta(row):
    campanha = row['campanha_sugerida']
    trecho = row['proximo_trecho']
    
    if campanha == 'Preditiva VIP':
        return f"Oferta VIP para sua viagem a {trecho}! Use o cupom VIP15."
    if campanha == 'Preditiva Padrão':
        return f"Planejando viajar para {trecho}? Use o cupom VIAGEM10 e ganhe 10% off."
    if campanha == 'Reativação (Risco de Churn)':
        return "Sentimos sua falta! Use o cupom VOLTA25 para 25% de desconto em qualquer trecho."
    if campanha == 'Fidelização VIP':
        return "Obrigado por ser VIP! Acumule pontos em dobro na sua próxima viagem."
    
    return None # Nenhuma oferta para o grupo de manutenção

df_final['texto_oferta'] = df_final.apply(gerar_texto_oferta, axis=1)
print("✅ Textos de ofertas personalizadas gerados.")

# 6. SALVAR O RESULTADO FINAL ACIONÁVEL
print("\n💾 Salvando arquivo final acionável...")
print("Amostra do arquivo final:")
print(df_final.head(10))

df_final.to_csv(path_output_final, index=False)
print(f"\n✅ Arquivo final com campanhas gerado em '{path_output_final}'")
print("🏁 Script finalizado com sucesso!")