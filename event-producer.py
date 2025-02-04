from pymongo import MongoClient
import random
import json
from faker import Faker
from datetime import datetime, timedelta

client = MongoClient('mongodb://mongoadmin:secret@localhost:27017/')

db = client["ecommerce_db"]

# Inicializar Faker
fake = Faker()

# Criar coleções
clientes_collection = db["clientes"]
produtos_collection = db["produtos"]
pedidos_collection = db["pedidos"]
itens_pedido_collection = db["itens_pedido"]
carrinho_collection = db["carrinho"]

# Gerar dados fictícios
def gerar_clientes(n=10):
    clientes = []
    for _ in range(n):
        cliente = {
            "cliente_id": fake.uuid4(),
            "nome": fake.name(),
            "email": fake.email(),
            "endereco": fake.address(),
            "data_nascimento": fake.date_of_birth(minimum_age=18, maximum_age=70).isoformat(),
            "preferencias": fake.word()
        }
        clientes.append(cliente)
    return clientes

def gerar_produtos(n=20):
    produtos = []
    for _ in range(n):
        produto = {
            "produto_id": fake.uuid4(),
            "nome": fake.word(),
            "descricao": fake.sentence(),
            "categoria": fake.word(),
            "preco": round(random.uniform(10, 1000), 2),
            "estoque": random.randint(1, 100)
        }
        produtos.append(produto)
    return produtos

def gerar_pedidos(clientes, produtos, n=15):
    pedidos = []
    itens_pedido = []
    for _ in range(n):
        cliente = random.choice(clientes)
        pedido_id = fake.uuid4()
        num_itens = random.randint(1, 5)
        itens = []

        for _ in range(num_itens):
            produto = random.choice(produtos)
            quantidade = random.randint(1, 3)
            item = {
                "item_id": fake.uuid4(),
                "pedido_id": pedido_id,
                "produto_id": produto["produto_id"],
                "quantidade": quantidade,
                "preco_unitario": produto["preco"]
            }
            itens.append(item)
            itens_pedido.append(item)

        pedido = {
            "pedido_id": pedido_id,
            "cliente_id": cliente["cliente_id"],
            "data": fake.date_time_between(start_date="-30d", end_date="now").isoformat(),
            "status": random.choice(["Pendente", "Enviado", "Entregue", "Cancelado"]),
            "total": sum(item["quantidade"] * item["preco_unitario"] for item in itens)
        }
        pedidos.append(pedido)
    
    return pedidos, itens_pedido

def gerar_carrinhos(clientes, produtos):
    carrinhos = []
    for cliente in clientes:
        if random.choice([True, False]):  # Nem todos os clientes terão carrinhos
            num_itens = random.randint(1, 4)
            itens = [{"produto_id": random.choice(produtos)["produto_id"], "quantidade": random.randint(1, 3)} for _ in range(num_itens)]
            total = sum(item["quantidade"] * random.uniform(10, 500) for item in itens)

            carrinho = {
                "carrinho_id": fake.uuid4(),
                "cliente_id": cliente["cliente_id"],
                "itens": itens,
                "total": round(total, 2)
            }
            carrinhos.append(carrinho)
    
    return carrinhos

# Gerar e inserir dados no MongoDB
clientes = gerar_clientes(10)
produtos = gerar_produtos(20)
pedidos, itens_pedido = gerar_pedidos(clientes, produtos, 15)
carrinhos = gerar_carrinhos(clientes, produtos)

clientes_collection.insert_many(clientes)
produtos_collection.insert_many(produtos)
pedidos_collection.insert_many(pedidos)
itens_pedido_collection.insert_many(itens_pedido)
carrinho_collection.insert_many(carrinhos)

print("✅ Dados inseridos com sucesso no MongoDB!")
