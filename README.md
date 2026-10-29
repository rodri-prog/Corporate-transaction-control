# LatAm Corporate Spending Management & Intelligent Audit
# Gestão de Gastos Corporativos e Auditoria Inteligente na LatAm

---

###  Select Language / Selecione o Idioma
*   [English Version](#-english-version)
*   [Versão em Português](#-versão-em-português)

---

## 🇺🇸 English Version

 **[CLICK HERE TO ACCESS THE INTERACTIVE LOOKER STUDIO DASHBOARD](https://datastudio.google.com/reporting/8f4372dd-2131-4131-a75f-9910919193df)**

###  Project Objective
The main objective of this project is to build an end-to-end data ecosystem that bridges raw corporate card transaction data and agile business decision-making across Latin America (Brazil, Mexico, and Colombia). By combining data analyst pipeline workflows, artificial intelligence mechanics, and advanced statistical analysis, the project transforms cold financial records into structured executive insights and interactive visualizations for non-technical stakeholders.

###  Business Problems Solved
1. **Revenue Leakage from Lack of Audit Visibility (Fraud/Errors):**
   * *The Problem:* Reviewing thousands of high-velocity corporate transactions manually to spot misuse or fraud is humanly impossible, causing quiet financial losses.
   * *The Solution:* An automated statistical model running a **Z-Score algorithm** flags anomalous, high-risk spend spikes instantly, allowing compliance teams to execute preventive card blocks.
2. **Operational Overhead & Reporting Delays (Manual Excel Tasks):**
   * *The Problem:* Teams spending daily hours copy-pasting numbers to calculate platform volumes, billings, fees, and typing executive updates for directors.
   * *The Solution:* A robust Python ETL pipeline **automates the entire workflow**. Raw logs are fetched, cleaned, and aggregated seamlessly, reducing human effort to zero.
3. **Communication Bottlenecks with Non-Technical Stakeholders:**
   * *The Problem:* Board members and business executives lack the time or technical background to interpret raw SQL databases or Python scripts.
   * *The Solution:* The integrated automation **translates core operational KPIs into standard executive language** (text summaries), paired with an interactive visual dashboard for rapid comprehension.

###  Tech Skills Mapping that I used
* **Descriptive Statistics & Exploratory Modeling:** Applied to understand spending patterns via population distribution metrics (Mean, Median, Standard Deviation).
* **Trend, Pattern & Anomaly Identification:** Solved via vectorially calculating a parameterized **Z-Score > 3** threshold to isolate extreme financial outliers.
* **Reporting Workflow Automation:** Managed by a Python pipeline that sanitizes data tables and exports metrics automatically.
* **AI Tool Integration Interests:** Structured programmatically to support LLM (OpenAI API) pipelines for autonomous report drafting.
* **High-Impact Dashboards (BI):** Delivered as a central monitoring terminal utilizing **Looker Studio** for corporate oversight.

### Technical Execution
* **Step 1 - Raw Data Layer:** The base file `transacoes_corporativas_latam.csv` simulates Clara's multi-currency regional environment (BRL, MXN, COP converted to USD) and business verticals (SaaS, Marketing, Travel, Office Supplies).
* **Step 2 - ETL & AI Text Automation:** The `pipeline_automacao.py` script sanitizes duplicates/nulls, applies a 1.5% fee revenue calculation column (`EmpresaX_free_usd`), and outputs an automated text notification summary (`relatorio_executivo_ia.txt`).
* **Step 3 - Advanced Statistical Audit:** The `analise_estatistica.py` script processes the clean data layer, evaluates statistical deviations, and isolates critical threats into a dedicated file (`auditoria_alertas_fraude.csv`).
* **Step 4 - BI Visual Delivery:** Interactive charts translate the engineering data into visual insights (Total processed volume, fees earned, geographical spending density, and a specialized fraud monitoring panel).

---

## 🇧🇷 Versão em Português

 **[CLIQUE AQUI PARA ACESSAR O DASHBOARD INTERATIVO NO LOOKER STUDIO](https://datastudio.google.com/reporting/8f4372dd-2131-4131-a75f-9910919193df)**

###  Objetivo do Projeto
O objetivo principal deste projeto é construir um ecossistema de dados de ponta a ponta que atue como uma ponte estratégica entre dados brutos de transações de cartões corporativos e tomadas de decisão ágeis na América Latina (Brasil, México e Colômbia). Combinando pipelines de analista de dados, inteligência artificial e análise estatística avançada, o projeto transforma registros financeiros frios em insights estruturados e visualizações interativas para stakeholders não técnicos.

###  Problemas de Negócio que o Projeto Soluciona
1. **Vazamento de Receita por Falta de Auditoria (Fraudes/Erros):**
   * *O problema:* Analisar milhares de transações de alta velocidade manualmente "no olho" para encontrar fraudes ou uso indevido de cartões é impossível, gerando prejuízos financeiros invisíveis.
   * *A solução:* Um modelo estatístico automatizado baseado no **algoritmo de Z-Score** sinaliza picos de gastos anômalos e de alto risco instantaneamente, permitindo que os times de compliance executem bloqueios preventivos.
2. **Sobrecarga Operacional e Lentidão em Relatórios (Esforço Manual em Excel):**
   * *O problema:* Analistas gastando horas diárias copiando e colando números para calcular volumes da plataforma, taxas e redigindo resumos executivos para a diretoria.
   * *A solução:* Um pipeline de ETL em Python **automatiza todo o fluxo de trabalho**. Os dados brutos são extraídos, limpos e consolidados sem esforço humano.
3. **Barreira de Comunicação com Stakeholders Não Técnicos:**
   * *O problema:* Diretores e executivos de negócios não têm tempo ou conhecimento técnico para interpretar bancos de dados SQL ou códigos Python.
   * *A solução:* A automação integrada **traduz KPIs operacionais em linguagem executiva natural** (resumos em formato de texto), complementada por um dashboard visual interativo de rápida compreensão.

###  Mapeamento de Habilidades que usei
* **Estatística Descritiva e Modelagem Exploratória:** Aplicada para entender os padrões de consumo por meio de métricas de distribuição (Média, Mediana, Desvio Padrão).
* **Identificação de Tendências, Padrões e Anomalias:** Resolvida via cálculo vetorial parametrizado com a regra de **Z-Score > 3** para isolar outliers financeiros extremos.
* **Automação de Fluxos de Trabalho de Relatórios:** Gerenciada por um pipeline em Python que limpa as tabelas e exporta métricas automaticamente.
* **Interesse/Experiência em Ferramentas de IA:** Estruturado programaticamente para suportar conexões com LLMs (API da OpenAI) para redação autônoma de relatórios.
* **Dashboards de Alto Impacto (BI):** Entregue como um terminal central de monitoramento utilizando o **Looker Studio**.

###  Execução Técnica 
* **Passo 1 - Camada de Dados Brutos:** O arquivo base `transacoes_corporativas_latam.csv` simula o ambiente multimoedas regional da Clara (BRL, MXN, COP convertidos para USD) e verticais de consumo (SaaS, Marketing, Viagens, Escritório).
* **Passo 2 - Pipeline ETL & Automação Textual por IA:** O script `pipeline_automacao.py` elimina duplicados/nulos, aplica a regra de negócio de receita por taxa de 1.5% (`EmpresaX_free_usd`) e gera um e-mail executivo automatizado (`relatorio_executivo_ia.txt`).
* **Passo 3 - Auditoria Estatística Avançada:** O script `analise_estatistica.py` processa a base limpa, avalia os desvios estatísticos e isola as ameaças críticas em um arquivo exclusivo (`auditoria_alertas_fraude.csv`).
* **Passo 4 - Entrega Visual no BI:** Gráficos interativos traduzem a engenharia de dados em insights visuais (Volume total processado, receita de taxas, densidade geográfica de gastos e painel operacional de fraudes).

