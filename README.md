# 🚌 Projeto ClickBus - Inteligência de Marketing e Vendas  

Um pipeline completo de **Machine Learning + Segmentação RFM + Lógica de Campanhas** para prever comportamento de compra de clientes, sugerir próximos trechos e apoiar decisões de marketing com dashboards no **Power BI**.  

---

## 📌 Estrutura do Projeto  

📁 PROJETO_CLICKBUS/
├── 📁 dados/
│   ├── 📄 conversor.py → Anonimiza clientes e normaliza cidades dos dados brutos.
│   ├── 📊 clickbus_tratado 1.csv → Dataset original.
│   └── 📊 clickbus_tratado_final.csv → Dataset limpo, pronto para os scripts.
│
├── 📁 outputs/
│   ├── 📊 clientes_segmentados.csv → Saída da segmentação RFM por cliente.
│   ├── 📊 predicoes_clickbus_hierarquico.csv → Saída bruta com as predições do modelo de ML.
│   └── 📊 predicoes_com_campanhas.csv → Arquivo final acionável com as campanhas.
│
└── 📁 scripts/
    ├── 📄 modelo.py → Pipeline hierárquico de Machine Learning:
    │   ├── Classificador Gatekeeper (compra em 7 dias?)
    │   ├── Regressores de curto (0-7d) e longo prazo (>7d)
    │   └── Classificador de próximo trecho
    ├── 📄 perfil_viagem.py → Segmentação de clientes via RFM e análise de perfil.
    └── 📄 promocoes.py → Aplica a lógica de negócio para gerar as campanhas de marketing.

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

*<img width="1200" height="550" alt="image" src="https://github.com/user-attachments/assets/5d24531d-b28a-41ac-b51e-353758cb47c3" />*  <img width="1379" height="769" alt="image" src="https://github.com/user-attachments/assets/5b89d849-c628-4585-92e5-2399f665381a" />



---


---

⭐️ Se esse projeto te ajudou, deixe uma estrela no repositório!

