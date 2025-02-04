# Bootcamp: Arquiteto(a) de Dados

## Documento de Arquitetura e Repositório do Projeto E-commerce Amazonas LTDA

**Autor:** Walter Gabriel Ferreira Gonzaga  
**Professor:** João Paulo Faria  
**Módulo:** Desafio Final  

## Tecnologias Utilizadas
- Hackolade  
- MongoDB  
- MongoDB Compass  
- Docker  
- Docker Compose  
- Python  
- AWS  

![image](https://github.com/user-attachments/assets/90080559-8301-44dd-b4be-75f2b43e23b8)


---

## Sumário
1. [Introdução](#1-introdução)  
   1.1. [Contexto e Objetivos](#11-contexto-e-objetivos)  
   1.2. [Descrição do Sistema](#12-descrição-do-sistema)  
2. [Estrutura de Dados Proposta](#2-estrutura-de-dados-proposta)  
   2.1. [Modelagem de Dados Não-Relacional](#21-modelagem-de-dados-não-relacional)  
   2.2. [Coleções Principais](#22-coleções-principais)  
   2.3. [Esquema Desnormalizado](#23-esquema-desnormalizado)  
3. [Plano de Escalabilidade](#3-plano-de-escalabilidade)  
   3.1. [Estratégias de Sharding e Replicação](#31-estratégias-de-sharding-e-replicação)  
   3.2. [Infraestrutura com Docker e AWS](#32-infraestrutura-com-docker-e-aws)  
   3.3. [Particionamento e Replicação](#33-particionamento-e-replicação)  
   3.4. [Crescimento de Dados e Alta Concorrência](#34-crescimento-de-dados-e-alta-concorrência)  
4. [Implementação Utilizando AWS Atlas ou DynamoDB](#4-implementação-utilizando-aws-atlas-ou-dynamodb)  
   4.1. [MongoDB Atlas](#41-mongodb-atlas)  
   4.2. [DynamoDB](#42-dynamodb)  
5. [Modelo Hackolade](#5-modelo-hackolade)  
6. [Explicação do Projeto Prático](#6-explicação-do-projeto-prático)  

---

## 1. Introdução

### 1.1 Contexto e Objetivos
A "Amazonas", uma loja tradicional que vende uma vasta gama de produtos, decidiu expandir para o mercado digital. O objetivo é criar um e-commerce robusto, capaz de lidar com o crescimento rápido e exponencial de clientes e transações. Para garantir alta performance, disponibilidade, escalabilidade e elasticidade, a loja escolheu adotar uma arquitetura de dados moderna utilizando bancos de dados não-relacionais, como o MongoDB, e serviços de cloud computing da AWS.

O objetivo principal é garantir que a aplicação de e-commerce possa escalar horizontalmente, utilizando infraestrutura Docker e AWS para criar clusters de servidores que podem variar de 3 a 10 máquinas durante os períodos de pico, garantindo alta disponibilidade.

### 1.2 Descrição do Sistema
O sistema será baseado em um banco de dados NoSQL, adotando o MongoDB. As coleções serão desnormalizadas para otimizar a performance e evitar o uso de joins, o que é crucial para sistemas distribuídos e de alta performance.

---

## 2. Estrutura de Dados Proposta

### 2.1 Modelagem de Dados Não-Relacional
O modelo de dados será projetado para um ambiente de alto desempenho e escalabilidade, garantindo integridade e rapidez nas consultas.

### 2.2 Coleções Principais
- **Clientes:** cliente_id, nome, email, endereço, data_nascimento, preferências (Relacionamento com Pedidos).
- **Produtos:** produto_id, nome, descrição, categoria, preço, estoque (Sem relacionamento direto, mas vinculado a Pedidos).
- **Pedidos:** pedido_id, cliente_id, data, status, total (Relacionamento com Itens do Pedido).
- **Itens do Pedido:** item_id, pedido_id, produto_id, quantidade, preço_unitário (Relacionamento com Produtos e Pedidos).
- **Carrinho:** carrinho_id, cliente_id, itens (array de itens temporários), total (Relacionamento com Clientes).

### 2.3 Esquema Desnormalizado
A desnormalização será aplicada para melhorar a escalabilidade e reduzir a necessidade de operações de agregação complexas.

---

## 3. Plano de Escalabilidade

### 3.1 Estratégias de Sharding e Replicação
A escalabilidade horizontal será implementada utilizando sharding e replicação no MongoDB.

**Sharding:** será aplicado nas coleções **Pedidos** e **Itens do Pedido** com chave de sharding baseada em `pedido_id` ou `cliente_id`.

**Replicação:** coleções críticas como **Produtos** e **Clientes** terão replicação para garantir alta disponibilidade.

### 3.2 Infraestrutura com Docker e AWS

- **Docker:** instâncias do MongoDB serão empacotadas em contêineres Docker.
- **AWS EC2:** servidores serão provisionados dinamicamente usando Auto Scaling Groups.

### 3.3 Particionamento e Replicação

- **Particionamento:** coleções **Pedidos** e **Itens do Pedido** serão distribuídas conforme `pedido_id` ou `cliente_id`.
- **Replicação:** coleções **Clientes** e **Produtos** serão replicadas para manter disponibilidade e resiliência.

### 3.4 Crescimento de Dados e Alta Concorrência

- **Crescimento de Dados:** escalabilidade dinâmica com novos shards conforme aumento de dados.
- **Alta Concorrência:** utilização de cache otimizado e distribuição de carga para suportar acessos simultâneos.

---

## 4. Implementação Utilizando AWS Atlas ou DynamoDB

### 4.1 MongoDB Atlas
O MongoDB Atlas permitirá escalabilidade automática, distribuição de dados entre regiões e gerenciamento simplificado.

### 4.2 DynamoDB
Se optar por usar DynamoDB, as tabelas serão estruturadas com chaves de partição otimizadas para consultas eficientes.

---

## 5. Modelo Hackolade
O modelo será desenhado na ferramenta **Hackolade** utilizando o template do **MongoDB**, garantindo uma visualização estruturada do esquema de dados.

---

## 6. Explicação do Projeto Prático
------------------------------------------------------------------------------------------------------
Digite no bash os sequintes comandos para criar uma network, um volume para persistencia dos dados e o container com a imgaem do mongodb:

$ docker volume create vol1

$ docker network create net1

$ docker run -d --network net1 -h mongo --name mongo -e MONGO_INITDB_ROOT_USERNAME=mongoadmin -e MONGO_INITDB_ROOT_PASSWORD=secret -p 27017:27017 -v vol1/data/db mongo


Assim seu container será criado:
![image](https://github.com/user-attachments/assets/b389a4c3-5a7e-4a7b-a3cb-04e992199c3d)


Baixe o mongodb compass para visualizar em interface gráfica os bancos, coleções e documentos: https://www.mongodb.com/products/tools/compass
Agora é encessário conectar o mangodb que está na porta 27017 como configurado no docker, no mongodb compass: mongodb://mongoadmin:secret@localhost:27017
![image](https://github.com/user-attachments/assets/9e5d09a7-4143-4b30-b0b7-7157db6d81ea)

Agora é possível visualizar o banco de dados:
![image](https://github.com/user-attachments/assets/7e6ef45b-1400-4450-bd1c-b320041d247c)

Com nosso arquivo “event-producer.py” vamos gerar dados fake e aleatórios para inputar no banco de dados NoSQL utilizando a biblioteca do pymongo:
![image](https://github.com/user-attachments/assets/7cb23506-e03f-42c4-aebc-d71958c335e4)

Podemos ver as coleções criadas e os documentos inseridos pelo mongodb compass:
![image](https://github.com/user-attachments/assets/41df1480-173f-4a5a-a7c1-59bb6ec4da0a)
![image](https://github.com/user-attachments/assets/01e8ea5c-746f-451a-824e-ab96fec814f8)

