# RAFAELA_MORSIANI_DDF_TECH_012026

1. Introdução e Objetivo
   
Este projeto apresenta o desenvolvimento de uma solução de dados para um ecossistema de e-commerce, focando na transformação de dados brutos em insights estratégicos. A solução integra o enriquecimento automático de informações, processamento de grandes volumes de dados e a estruturação de um Data Warehouse para análise.
O projeto demonstrou a capacidade de importat dados de múltiplas origens, processá-los e disponibilizá-los para consumo em um dashboard analítico no Metabase, utilizando a plataforma Dadosfera como base de operações.

2. Tecnologias Utilizadas

O projeto foi desenvolvido integrando tecnologias de ponta para garantir eficiência e escalabilidade:
- Dadosfera: Plataforma de dados SaaS utilizada como base para governança, integração e armazenamento (Data Lakehouse).
- Python (Pandas): Linguagem utilizada para manipulação de dados e orquestração do pipeline de enriquecimento.
- Gemini 2.0 Flash (Google AI): Modelo de linguagem de utilizado para a extração inteligente de metadados das descrições de produtos.
- SQL: Linguagem essencial para a criação de Views e modelagem das tabelas fato e dimensões no Data Warehouse.
- Metabase: Ferramenta de Business Intelligence integrada à Dadosfera para criação de dashboards e visualização dos KPIs de negócio.

3. Sobre a Base de Dados

A base de dados foi gerada sinteticamente, representando o dominio de um Ecommerce. O script utilizado consta no arquivo https://colab.research.google.com/drive/1WMRddcXrWZgG7dHqzBtgFg58sBw8zhb8?usp=sharing e quatro arquivos foram gerados, totabilizando mais de 100.000 registros.

Após a geração da base de dados, foi realizada a integração através do módulo de coleta da Dadosfera. Os seguintes arquivos foram importados: ecommerce_items, ecommerce_orders, ecommerce_products e ecommerce_users.


4. Exploração e Catalogação

Para garantir a integridade e organização, os dados percorreram as seguintes zonas: 
- Landing Zone: Ingestão inicial dos arquivos CSV brutos via módulo de Coleta.
- Standardized Zone: Camada onde os dados foram catalogados, tipados e documentados com metadados no módulo Explorar.
- Curated Zone: Tabelas finais estruturadas, prontas para consumo em ferramentas de Analytics e IA.

5. Data Quality

PAra garantir a confiabilidade e o bom desempenho do projeto, foi desenvolvido um script em Python que aplica as regras de negocio sobre os quatro datasets iniciais, através da utilização da biblioteca Great Expectations. As principais validações incluíram: 
- Verificação de IDs nulos
- Validação de preços, subtotais e quantidades para que não sejam negativos e/ou zero
- Verificação de emails validos.

O script gerou um relatório que documenta o sucesso de cada validação.
O script utilizado consta no seguinte arquivo: https://colab.research.google.com/drive/1jLocsuyAcuP7KbeYaTgyepixEiKw690a?usp=sharing

Além disso, foi implementado um modelo de dados comum que padroniza as chaves de ligação entre as tabelas, permitindo o o reconhecimento das relações entre as tabelas de forma automática.


6. Inteligência Artificial e Enriquecimento de Dados (Item 5)

Nesta etapa, dados desestruturados, como a descrição dos produtos, foi transformada em Features estruturadas para análise de negócio, avtravés da utilização de IA.

O dataset ecommerce_products inclui informações sobre materiais e tecnologias do produto e essas informações estavam diluidas em descrições textuais. 

O modelo Gemini 2.0 Flash foi utilizado via API para processar os 176 produtos do catálogo. O Python script foi construido segundo os seguintes passos:

- Para lidar com os limites da API gratuita, foi implementado uma lógica de exponencial backoff e pausas estratégicas, garantindo que a pipeline fosse resiliente a falhas de conexão e limites de cota;
- Após identificar que o formato CSV corrompia dados complexos de IA, o prompt foi alterado de forma a garantir que a IA retornasse os dados em formato JSON, facilitando a integração automática;

A partir das descrições brutas dos produtos, a IA generou as seguintes colunas analíticas:
- material: identificação automática de materiais;
- tecnologia: extração de diferencias tecnologicos do produto.

Antes (Texto Bruto): "O Smartphone Apple - Plus é a escolha ideal para quem busca performance. Fabricado com Polímero de alta resistência, este modelo Plus oferece Bateria de 5000mAh. Produto original Apple com acabamento premium."

Depois (Features IA): "material_ia": ["Alumínio", "Vidro"],
        "tecnologia_ia": ["iOS", "Tela Retina", "Câmera avançada", "Processador Apple Silicon", "5G"]












8. Arquitetura da Solução
Explique as etapas que você percorreu:

Coleta/Ingestão: Upload dos arquivos CSV para a Dadosfera.

Processamento: Uso de Python e Gemini 2.0 Flash para extração de atributos técnicos.

Armazenamento/Modelagem: Estruturação no Snowflake seguindo o modelo Kimball (Star Schema).

3. Modelagem Dimensional (Item 6)
Este é um dos pontos mais importantes. Insira o diagrama que você montou e explique:

Tabela Fato: FCT_ITEMS (métrica de vendas).

Tabelas Dimensão: DIM_PRODUCTS, DIM_USERS, DIM_ORDERS.

Justificativa: Por que usar Star Schema? (Facilidade de uso no Metabase e performance de consulta).

4. Inteligência Artificial e Enriquecimento (Item 5 e 8)
Como você usou o Gemini 2.0 Flash para gerar valor:

O que foi feito: Extração automática de materiais e tecnologias a partir das descrições dos produtos.

Resiliência do Pipeline: Mencione que você implementou lógica de Rate Limiting (pausas de 4.5s) para lidar com as cotas da API gratuita, garantindo que todos os 176 produtos fossem processados sem erros de "429 Too Many Requests".

5. Análise de Dados (Item 7)
Coloque prints do seu Dashboard e explique cada um dos 5 gráficos:

Ex: "Gráfico 5: Distribuição de Materiais - Criado a partir dos dados extraídos pela IA, permitindo identificar que 40% dos produtos utilizam tecnologia sustentável."
