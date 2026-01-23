# RAFAELA_MORSIANI_DDF_TECH_012026

**Candidata:** Rafaela Morsiani Kawashita

**Vídeo de Apresentação:** https://youtu.be/UaHwDdPRVxk

**Trello:** https://trello.com/invite/b/696fe6e4eca45a6bff8978ef/ATTIa2fb74d3429d8c54e17420db9854c4dd804625FA/projeto-dadosfera


**Introdução e Objetivo**
   
Este projeto apresenta o desenvolvimento de uma solução de dados para um ecossistema de e-commerce, focando na transformação de dados brutos em insights estratégicos. A solução integra o enriquecimento automático de informações, processamento de grandes volumes de dados e a estruturação de um Data Warehouse para análise.
O projeto demonstrou a capacidade de importat dados de múltiplas origens, processá-los e disponibilizá-los para consumo em um dashboard analítico no Metabase, utilizando a plataforma Dadosfera como base de operações.

**Tecnologias Utilizadas**

O projeto foi desenvolvido integrando tecnologias de ponta para garantir eficiência e escalabilidade:
- Dadosfera: Plataforma de dados SaaS utilizada como base para governança, integração e armazenamento (Data Lakehouse).
- Python (Pandas): Linguagem utilizada para manipulação de dados e orquestração do pipeline de enriquecimento.
- Gemini 2.0 Flash (Google AI): Modelo de linguagem de utilizado para a extração inteligente de metadados das descrições de produtos.
- SQL: Linguagem essencial para a criação de Views e modelagem das tabelas fato e dimensões no Data Warehouse.
- Metabase: Ferramenta de Business Intelligence integrada à Dadosfera para criação de dashboards e visualização dos KPIs de negócio.

**Sobre a Base de Dados - Item 1**

A base de dados foi gerada sinteticamente, representando o dominio de um Ecommerce. O script utilizado consta no arquivo https://colab.research.google.com/drive/1WMRddcXrWZgG7dHqzBtgFg58sBw8zhb8?usp=sharing e quatro arquivos foram gerados, totabilizando mais de 100.000 registros.




**Exploração e Catalogação - Item 2 e 3**

Após a geração da base de dados, foi realizada a integração através do módulo de coleta da Dadosfera. Os seguintes arquivos foram importados: ecommerce_items, ecommerce_orders, ecommerce_products e ecommerce_users. A imagem a seguir apresenta os arquivos na aba de catálogo da Dadosfera.

<img width="1880" height="861" alt="image" src="https://github.com/user-attachments/assets/41cdded1-dd0d-49a3-b484-f3e7cc44b638" />

Após esta etapa, os dados foram catalogados e a tag única "ecommerce_MK" foi implementada. Essa prática permite que diferentes áreas da empresa localizem todo o ecossistema do projeto através de uma única busca.

Para garantir a integridade e organização, os dados percorreram as seguintes zonas: 
- Landing Zone: Ingestão inicial dos arquivos CSV brutos via módulo de Coleta.
- Standardized Zone: Camada onde os dados foram catalogados, tipados e documentados com metadados no módulo Explorar.
- Curated Zone: Tabelas finais estruturadas, prontas para consumo em ferramentas de Analytics e IA.



**Data Quality - Item 4**

Para garantir a confiabilidade e o bom desempenho do projeto, foi desenvolvido um script em Python que aplica as regras de negócio sobre os quatro datasets iniciais, através da utilização da biblioteca Great Expectations. As principais validações incluíram: 
- Verificação de IDs nulos
- Validação de preços, subtotais e quantidades para que não sejam negativos e/ou zero
- Verificação de emails validos.

O script gerou um relatório em JSON que documenta o sucesso de cada validação.
O script utilizado consta no seguinte arquivo: https://colab.research.google.com/drive/1jLocsuyAcuP7KbeYaTgyepixEiKw690a?usp=sharing
<img width="647" height="123" alt="image" src="https://github.com/user-attachments/assets/ad092f73-3071-4e65-bc54-f16e7ec2fd06" />


Além disso, foi implementado um modelo de dados comum que padroniza as chaves de ligação entre as tabelas, permitindo o o reconhecimento das relações entre as tabelas de forma automática.



**Inteligência Artificial e Enriquecimento de Dados - Item 5**

Nesta etapa, dados desestruturados, como a descrição dos produtos, foi transformada em Features estruturadas para análise de negócio, avtravés da utilização de IA.

O dataset ecommerce_products inclui informações sobre materiais e tecnologias do produto e essas informações estavam diluidas em descrições textuais. 

O modelo Gemini 2.5 Flash foi utilizado via API para processar os 176 produtos do catálogo. O Python script foi construido segundo os seguintes passos:

- De modo à otimizar a performance, foi implementado uma lógica de processamento por lotes, onde os produtos eram processados em grupos de 10 registros por vez.
- Foram implementadas pausas estratégicas, de modo a garantir que o fluxo  de dados respeite os limites de taixa da API gratuita e evite assim interrupções no processamento. Além disso, em caso de falha ou erro, o script realiza até 5 tentativas.
- O prompt foi desenhado de modo a forçarA a retornar um JSON Array perfeitamente estruturado;

A partir das descrições brutas dos produtos, a IA generou as seguintes colunas analíticas:
- material: identificação automática de materiais;
- tecnologia: extração de diferencias tecnologicos do produto.

Antes (Texto Bruto): "O Smartphone Apple - Basic é a escolha ideal para quem busca performance. Fabricado com Polímero de alta resistência, este modelo Basic oferece Conexão 5G. Produto original Apple com acabamento premium."

Depois (Features IA): "material": ["Polímero de alta resistência"],
                       "tecnologia": ["Conexão 5G"]

O script utilizado para essa etapa consta no arquivo https://colab.research.google.com/drive/1G3Njh53HrhyosxjKL0d9JMyTnwD5RLBe?usp=sharing



**Modelagem de Dados - Item 6**

Para transformar os dados brutos em uma estrutura analítica, foi-se utilizado os princípios de modelagem Kimball, estruturando o Data Warehouse em um formato estrela com as seguintes camadas:
- Tabela Fato: Items - Atua como núcleo do modelo, registrando cada item vendido.
- Tabelas Dimensão: Products, Users e Orders - Acrescentam o contexto necessário para análise.

O seguinte diagrama foi criado:
<img width="975" height="711" alt="image" src="https://github.com/user-attachments/assets/b1d47826-9814-4d73-b7db-74bff76caed9" />

No modo SQL da Dadosfera, duas visões estratégicas foram desenvolvidas, simplificando o acesso à informação aos usuários finais:
- V_Fato_Vendas_Enriquecida: Essa visão realiza o join da tabela Items com a taabela Orders e também com a tabela Products enriquecida com as features extraídas com IA.
- V_Perfil_Consumidor: Essa visão cruza o histórico de compras, realizando o join da tabela Users com Orders.



**Análise de Dados - Item 7**

Nesta etapa, o módulo de visualização (Metabase) da Dadosfera foi utilizado para converter os dados modelados em um Dashboard, com o objetivo de validar hipóteses de negócio e monitorar a performance do ecommerce MK.

Seis visualizações esratégicas foram criadas, conforme a imagem a seguir.
<img width="885" height="705" alt="image" src="https://github.com/user-attachments/assets/5813a956-94fb-43d3-ad4b-77913c102b7f" />

O dashboard monitora o faturamento total do ecommerce e também a base de usuários.
Com a importação dos features extraídos com IA, gerou-se um gráfico identificando quais tecnologias são responsáveis pelo maior volume financeiro bruto.
Além disso, com os gráficos gerados é possível comparar o faturamento total e o ticket médio por categoria dos produtos, indicando que, embora os eletrônicos tenham um maior volume, a categoria moda mantém um ticket médio mais estável e elevado. Para essa etapa, o query abaixo foi utilizado.

<img width="786" height="561" alt="image" src="https://github.com/user-attachments/assets/fdd5bfd6-3c93-45b2-b234-f7252856d948" />


O dashboard pode ser acessado a partir do seguinte link: https://metabase-treinamentos.dadosfera.ai/dashboard/264



**Pipelines - Item 8**

De forma a garantir a atualização constantes dos dados do Ecommerce MK, foi-se utilizado o módulo de pipelines da Dadosfera. O pipeline orquestrado segue as seguintes etapas:
- Coleta: Conexão direta com os arquivos CSV originais
- Validação: Processamento das tabelas
- Disponibilização: Publicação dos ativos finais para o módulo de visualização em Metabase.

  O pipeline foi configurado para rodar em intervalos programados (a cada 24h), garantindo que os dashboards reflitam sempre a realizade mais recente das vendas.

  <img width="1828" height="611" alt="image" src="https://github.com/user-attachments/assets/fae274fa-628f-4486-851e-18d62f763938" />



**Data App - Item 9**

O Data App foi desenvolvido com base nos dados enriquecidos com IA e os seguintes dashboards foram obtidos.

<img width="1852" height="814" alt="image" src="https://github.com/user-attachments/assets/080e4935-4ab8-4b8b-9ebe-7e8281abe18e" />


O dashboard pode ser acessado através do link: https://rafaelamorsianiddftech012026-65mvjevmmmkwt8xukzm4bo.streamlit.app/









