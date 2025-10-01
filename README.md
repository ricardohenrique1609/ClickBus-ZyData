# 🚌 Projeto ClickBus - Inteligência de Marketing e Vendas  

Um pipeline completo de **Machine Learning + Segmentação RFM + Lógica de Campanhas** para prever comportamento de compra de clientes, sugerir próximos trechos e apoiar decisões de marketing com dashboards no **Power BI**.  

---

## 📌 Estrutura do Projeto  
PROJETO_CLICKBUS/
├── dados/
├── conversor.py                  → Anonimiza clientes e normaliza cidades dos dados brutos.
├── clickbus_tratado 1.csv       → Conjunto de dados original.
└── clickbus_tratado_final.csv   → Conjunto de dados limpo, pronto para os scripts.
├── outputs/
├── clientes_segmentados.csv                 → Saída da segmentação RFM por cliente.
├── predicoes_clickbus_hierarquico.csv      → Saída bruta com as predições do modelo de ML.
└── predicoes_com_campanhas.csv             → Arquivo final acionável com as campanhas.
└── scripts/
├── modelo.py
├── Classificador Gatekeeper (compra em 7 dias?)
├── Regressores de curto (0-7d) e longo prazo (>7d)
└── Classificador de próximo trecho
├── perfil_viagem.py             → Segmentação de clientes via RFM e análise de perfil.
└── promocoes.py                 → Aplicar a lógica de negócio para gerar campanhas de marketing.


---

## 🚀 Etapas realizadas  

### 1. **Tratamento dos Dados**  
- Normalização de cidades e IDs de clientes (`conversor.py`).  
- Padronização de campos de origem/destino de viagem.  

### 2. **Modelagem Hierárquica de ML (`modelo.py`)**  
- **Gatekeeper** → classifica se o cliente vai comprar em até 7 dias.  
- **Regressor Curto Prazo** → previsão de dias até próxima compra (0 a 7 dias).  
- **Regressor Longo Prazo** → previsão para clientes de longo prazo (> 7 dias).  
- **Classificador de Próximo Trecho** → prevê o próximo destino da viagem.  

### 3. **Segmentação Inteligente (`perfil_viagem.py`)**  
- Recência, Frequência e Valor Monetário (**RFM Score**).  
- Segmentos criados: **VIP, Frequente Econômico, Gastador Ocasional, Inativo, Regular**.  
- Identificação do tipo de viagem preferido (Somente Ida / Ida e Volta).  

### 4. **Regras de Campanhas (`promocoes.py`)**  
- Junção de predições com a segmentação RFM.  
- Lógica de campanhas:  
  - **Preditiva VIP / Preditiva Padrão**  
  - **Reativação (Churn)**  
  - **Fidelização VIP**  
  - **Manutenção (sem ação imediata)**  
- Geração de **texto de oferta personalizado** por cliente.  

### 5. **Visualização no Power BI**  
- Dashboards com insights de clientes, próximas compras e campanhas sugeridas.  
- Gráficos de recência, frequência, valor, além de performance dos modelos.  

---

## 🧠 Tecnologias usadas  

- **Python** → Pandas, NumPy, scikit-learn  
- **Modelos ML** → RandomForestClassifier, RandomForestRegressor  
- **RFM Analysis** → Segmentação estatística  
- **Power BI** → Visualização dos resultados finais  
- **Excel/CSV** → Entrada e saída dos dados processados  

---

## 📈 Resultados  

- Previsão de clientes que comprarão em até 7 dias.  
- Estimativa de dias até a próxima compra.  
- Previsão do próximo trecho da viagem.  
- Segmentação completa dos clientes via RFM.  
- Sugestão de campanhas personalizadas e textos automáticos.  
- Exportação acionável para integração com BI e Marketing.  

---

## 🧰 Trabalho futuro  

- Melhorar hiperparâmetros dos modelos para ganho de precisão.  
- Implementar atualização automática diária dos dados.  
- Integrar API para recomendação em tempo real.  
- Expansão para novos segmentos e campanhas dinâmicas.  

---

## 📷 Power BI  
<img width="900" height="560" alt="image" src="https://github.com/user-attachments/assets/30093a0d-4e8d-413e-aa4c-3af749842866" />


---
- Link do Power BI
  https://app.powerbi.com/links/QuS1JEqMg6?ctid=11dbbfe2-89b8-4549-be10-cec364e59551&pbi_source=linkShare
---

## 👨‍💻 Autores

**Ricardo Henrique Ramos Silva**  
**Tiago Sousa Leite**  
**Daniel Gallo**  
**Rodrigo Oshiro**
**Bruno souza**  


