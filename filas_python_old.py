"""
FILAS EM PYTHON - Tutorial Otimizado e Interativo
=================================================

Uma fila (Queue) é uma estrutura de dados que segue o princípio FIFO (First In, First Out).
Este tutorial demonstra diferentes implementações, operações e casos de uso práticos.

Autor: Tutorial Python
Versão: 2.0 - Otimizada
"""

from collections import deque
import queue
import heapq
import time
import sys
from typing import List, Any

print("=" * 60)
print("1. FILA USANDO collections.deque")
print("=" * 60)

# Criando uma fila com deque
fila = deque()

# INSERÇÃO - Adicionando elementos à fila
print("\n--- INSERÇÃO ---")
fila.append("Primeiro")      # Adiciona no final
fila.append("Segundo")
fila.append("Terceiro")
fila.append("Quarto")
print(f"Fila após inserções: {list(fila)}")

# Inserindo no início (não é comum em filas, mas possível com deque)
fila.appendleft("Antes de todos")
print(f"Após inserir no início: {list(fila)}")

# DELEÇÃO - Removendo elementos da fila
print("\n--- DELEÇÃO ---")
print(f"Fila antes de remover: {list(fila)}")

# Remove do início (comportamento padrão de fila FIFO)
primeiro_elemento = fila.popleft()
print(f"Elemento removido: {primeiro_elemento}")
print(f"Fila após remoção: {list(fila)}")

# Remove do final (não é comum em filas)
ultimo_elemento = fila.pop()
print(f"Último elemento removido: {ultimo_elemento}")
print(f"Fila final: {list(fila)}")

# ORDENAÇÃO - Filas normalmente não são ordenadas, mas podemos converter e ordenar
print("\n--- ORDENAÇÃO ---")
fila_nums = deque([5, 2, 8, 1, 9, 3])
print(f"Fila original: {list(fila_nums)}")

# Converter para lista, ordenar e voltar para deque
fila_ordenada = deque(sorted(fila_nums))
print(f"Fila ordenada: {list(fila_ordenada)}")

# Ordenação reversa
fila_reversa = deque(sorted(fila_nums, reverse=True))
print(f"Fila ordenada (decrescente): {list(fila_reversa)}")

print("\n" + "=" * 60)
print("2. FILA USANDO queue.Queue (Thread-safe)")
print("=" * 60)

# Queue é thread-safe e ideal para programação concorrente
q = queue.Queue()

# INSERÇÃO
print("\n--- INSERÇÃO ---")
q.put("Task 1")
q.put("Task 2")
q.put("Task 3")
print(f"Tamanho da fila: {q.qsize()}")

# DELEÇÃO
print("\n--- DELEÇÃO ---")
print(f"Removendo: {q.get()}")  # Remove e retorna o primeiro elemento
print(f"Removendo: {q.get()}")
print(f"Tamanho da fila após remoções: {q.qsize()}")

print("\n" + "=" * 60)
print("3. FILA DE PRIORIDADE (Priority Queue)")
print("=" * 60)

# Usando heapq para fila de prioridade
pq = []

# INSERÇÃO com prioridade (número menor = maior prioridade)
print("\n--- INSERÇÃO COM PRIORIDADE ---")
heapq.heappush(pq, (3, "Tarefa média prioridade"))
heapq.heappush(pq, (1, "Tarefa alta prioridade"))
heapq.heappush(pq, (5, "Tarefa baixa prioridade"))
heapq.heappush(pq, (2, "Tarefa média-alta prioridade"))

print("Fila de prioridade:", pq)

# DELEÇÃO por prioridade
print("\n--- DELEÇÃO POR PRIORIDADE ---")
while pq:
    prioridade, tarefa = heapq.heappop(pq)
    print(f"Executando: {tarefa} (prioridade: {prioridade})")

print("\n" + "=" * 60)
print("4. FILA PERSONALIZADA COM CLASSE")
print("=" * 60)

class FilaPersonalizada:
    def __init__(self):
        self.items = []
    
    def inserir(self, item):
        """Insere item no final da fila"""
        self.items.append(item)
        print(f"Inserido: {item}")
    
    def remover(self):
        """Remove e retorna o primeiro item da fila"""
        if self.esta_vazia():
            print("Fila vazia!")
            return None
        item = self.items.pop(0)
        print(f"Removido: {item}")
        return item
    
    def esta_vazia(self):
        """Verifica se a fila está vazia"""
        return len(self.items) == 0
    
    def tamanho(self):
        """Retorna o tamanho da fila"""
        return len(self.items)
    
    def frente(self):
        """Retorna o primeiro item sem remover"""
        if self.esta_vazia():
            return None
        return self.items[0]
    
    def ordenar(self, reverso=False):
        """Ordena a fila (quebra o conceito FIFO, mas pode ser útil)"""
        self.items.sort(reverse=reverso)
        print(f"Fila ordenada: {self.items}")
    
    def mostrar(self):
        """Mostra todos os elementos da fila"""
        print(f"Fila atual: {self.items}")

# Testando a fila personalizada
print("\n--- TESTANDO FILA PERSONALIZADA ---")
minha_fila = FilaPersonalizada()

# Inserções
minha_fila.inserir("A")
minha_fila.inserir("C")
minha_fila.inserir("B")
minha_fila.mostrar()

# Ordenação
minha_fila.ordenar()

# Deleções
minha_fila.remover()
minha_fila.remover()
minha_fila.mostrar()

print("\n" + "=" * 60)
print("5. COMPARAÇÃO DE PERFORMANCE")
print("=" * 60)

import time

def benchmark_filas():
    n = 10000
    
    # Testando deque
    start = time.time()
    d = deque()
    for i in range(n):
        d.append(i)
    for i in range(n):
        d.popleft()
    deque_time = time.time() - start
    
    # Testando lista comum
    start = time.time()
    l = []
    for i in range(n):
        l.append(i)
    for i in range(n):
        l.pop(0)  # Operação O(n) - lenta!
    list_time = time.time() - start
    
    print(f"Deque: {deque_time:.4f} segundos")
    print(f"Lista: {list_time:.4f} segundos")
    print(f"Deque é {list_time/deque_time:.1f}x mais rápida para operações de fila!")

benchmark_filas()