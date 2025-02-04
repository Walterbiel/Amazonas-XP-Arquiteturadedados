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

**Repositório do Projeto:** [GitHub](https://github.com/Walterbiel/Amazonas-XP-Arquiteturadedados)

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
A implementação do projeto será documentada e detalhada, abordando desde a modelagem inicial até a implantação final na AWS, garantindo um ambiente funcional e escalável para o e-commerce **Amazonas**.

---

Este documento serve como guia para a arquitetura de dados do projeto e-commerce **Amazonas LTDA**, facilitando a implementação e manutenção do sistema.

