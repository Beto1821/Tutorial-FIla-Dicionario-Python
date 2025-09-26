"""
DICIONÁRIOS EM PYTHON - Inserção, Ordenação e Deleção

Dicionários são estruturas de dados chave-valor muito eficientes em Python.
A partir do Python 3.7+, os dicionários mantêm a ordem de inserção.
"""

from collections import OrderedDict, defaultdict, Counter
import operator

print("=" * 60)
print("1. DICIONÁRIO BÁSICO - Inserção, Deleção e Ordenação")
print("=" * 60)

# Criando um dicionário
pessoa = {}

# INSERÇÃO - Várias formas de inserir elementos
print("\n--- INSERÇÃO ---")

# Forma 1: Atribuição direta
pessoa['nome'] = 'João'
pessoa['idade'] = 30
pessoa['cidade'] = 'São Paulo'

# Forma 2: Usando update()
pessoa.update({'profissao': 'Programador', 'salario': 5000})

# Forma 3: Usando setdefault() - só insere se a chave não existir
pessoa.setdefault('email', 'joao@email.com')
pessoa.setdefault('nome', 'Maria')  # Não vai sobrescrever

print(f"Dicionário após inserções: {pessoa}")

# DELEÇÃO - Várias formas de remover elementos
print("\n--- DELEÇÃO ---")
print(f"Antes da deleção: {pessoa}")

# Forma 1: del
del pessoa['cidade']
print(f"Após deletar 'cidade': {pessoa}")

# Forma 2: pop() - remove e retorna o valor
salario = pessoa.pop('salario', 0)  # 0 é o valor padrão se não encontrar
print(f"Salário removido: {salario}")
print(f"Após pop 'salario': {pessoa}")

# Forma 3: popitem() - remove e retorna o último item (Python 3.7+)
ultimo_item = pessoa.popitem()
print(f"Último item removido: {ultimo_item}")
print(f"Após popitem(): {pessoa}")

# Forma 4: clear() - remove todos os elementos
pessoa_copia = pessoa.copy()
pessoa_copia.clear()
print(f"Após clear(): {pessoa_copia}")

print("\n" + "=" * 60)
print("2. ORDENAÇÃO DE DICIONÁRIOS")
print("=" * 60)

# Criando um dicionário com notas de alunos
notas = {
    'Ana': 8.5,
    'Bruno': 7.2,
    'Carlos': 9.1,
    'Diana': 6.8,
    'Eduardo': 8.9
}

print(f"Dicionário original: {notas}")

# ORDENAÇÃO POR CHAVE (alfabética)
print("\n--- ORDENAÇÃO POR CHAVE ---")
por_nome = dict(sorted(notas.items()))
print(f"Ordenado por nome: {por_nome}")

por_nome_reverso = dict(sorted(notas.items(), reverse=True))
print(f"Ordenado por nome (decrescente): {por_nome_reverso}")

# ORDENAÇÃO POR VALOR
print("\n--- ORDENAÇÃO POR VALOR ---")
por_nota = dict(sorted(notas.items(), key=lambda x: x[1]))
print(f"Ordenado por nota (crescente): {por_nota}")

por_nota_reverso = dict(sorted(notas.items(), key=lambda x: x[1], reverse=True))
print(f"Ordenado por nota (decrescente): {por_nota_reverso}")

# Usando operator.itemgetter para performance
por_nota_fast = dict(sorted(notas.items(), key=operator.itemgetter(1)))
print(f"Ordenado por nota (operator.itemgetter): {por_nota_fast}")

print("\n" + "=" * 60)
print("3. DICIONÁRIOS ESPECIAIS")
print("=" * 60)

# defaultdict - valor padrão para chaves inexistentes
print("\n--- DEFAULTDICT ---")
contador_palavras = defaultdict(int)
texto = "python é ótimo python é poderoso python é fácil"

for palavra in texto.split():
    contador_palavras[palavra] += 1

print(f"Contador de palavras: {dict(contador_palavras)}")

# Counter - especializado para contagem
print("\n--- COUNTER ---")
counter = Counter(texto.split())
print(f"Counter: {counter}")
print(f"Palavra mais comum: {counter.most_common(1)}")
print(f"3 palavras mais comuns: {counter.most_common(3)}")

# OrderedDict - mantém ordem (menos necessário no Python 3.7+)
print("\n--- ORDEREDDICT ---")
od = OrderedDict()
od['primeiro'] = 1
od['segundo'] = 2
od['terceiro'] = 3
print(f"OrderedDict: {od}")

# Move item para o final
od.move_to_end('primeiro')
print(f"Após mover 'primeiro' para o final: {od}")

print("\n" + "=" * 60)
print("4. OPERAÇÕES AVANÇADAS COM DICIONÁRIOS")
print("=" * 60)

# Dicionário de produtos
produtos = {
    'notebook': {'preco': 2500, 'estoque': 10, 'categoria': 'eletrônicos'},
    'mouse': {'preco': 25, 'estoque': 50, 'categoria': 'eletrônicos'},
    'livro': {'preco': 45, 'estoque': 30, 'categoria': 'educação'},
    'caneta': {'preco': 2, 'estoque': 100, 'categoria': 'escritório'}
}

print(f"Produtos: {produtos}")

# INSERÇÃO DE NOVOS PRODUTOS
print("\n--- INSERINDO NOVOS PRODUTOS ---")
produtos['teclado'] = {'preco': 80, 'estoque': 20, 'categoria': 'eletrônicos'}
produtos['papel'] = {'preco': 15, 'estoque': 60, 'categoria': 'escritório'}
print(f"Após inserções: {list(produtos.keys())}")

# ORDENAÇÃO POR DIFERENTES CRITÉRIOS
print("\n--- ORDENAÇÃO AVANÇADA ---")

# Por preço
por_preco = dict(sorted(produtos.items(), key=lambda x: x[1]['preco']))
print("\nProdutos ordenados por preço:")
for produto, dados in por_preco.items():
    print(f"  {produto}: R${dados['preco']}")

# Por estoque
por_estoque = dict(sorted(produtos.items(), key=lambda x: x[1]['estoque'], reverse=True))
print("\nProdutos ordenados por estoque (maior para menor):")
for produto, dados in por_estoque.items():
    print(f"  {produto}: {dados['estoque']} unidades")

# Por categoria e depois por preço
por_categoria_preco = dict(sorted(produtos.items(), 
                                key=lambda x: (x[1]['categoria'], x[1]['preco'])))
print("\nProdutos ordenados por categoria e depois por preço:")
for produto, dados in por_categoria_preco.items():
    print(f"  {produto}: {dados['categoria']} - R${dados['preco']}")

# DELEÇÃO CONDICIONAL
print("\n--- DELEÇÃO CONDICIONAL ---")
print(f"Produtos antes da deleção: {list(produtos.keys())}")

# Remove produtos com estoque baixo (menos de 15)
produtos_baixo_estoque = [k for k, v in produtos.items() if v['estoque'] < 15]
for produto in produtos_baixo_estoque:
    removido = produtos.pop(produto)
    print(f"Removido {produto}: estoque baixo ({removido['estoque']})")

print(f"Produtos após deleção: {list(produtos.keys())}")

# FILTRAGEM E CRIAÇÃO DE NOVOS DICIONÁRIOS
print("\n--- FILTRAGEM ---")

# Produtos caros (acima de R$50)
produtos_caros = {k: v for k, v in produtos.items() if v['preco'] > 50}
print(f"Produtos caros: {produtos_caros}")

# Produtos eletrônicos
eletronicos = {k: v for k, v in produtos.items() if v['categoria'] == 'eletrônicos'}
print(f"Eletrônicos: {list(eletronicos.keys())}")

print("\n" + "=" * 60)
print("5. CLASSE PERSONALIZADA PARA DICIONÁRIO ORDENADO")
print("=" * 60)

class DicionarioOrdenado:
    def __init__(self):
        self.dados = {}
    
    def inserir(self, chave, valor):
        """Insere um item no dicionário"""
        self.dados[chave] = valor
        print(f"Inserido: {chave} = {valor}")
    
    def remover(self, chave):
        """Remove um item do dicionário"""
        if chave in self.dados:
            valor = self.dados.pop(chave)
            print(f"Removido: {chave} = {valor}")
            return valor
        else:
            print(f"Chave '{chave}' não encontrada")
            return None
    
    def ordenar_por_chave(self, reverso=False):
        """Ordena o dicionário pelas chaves"""
        self.dados = dict(sorted(self.dados.items(), reverse=reverso))
        print(f"Ordenado por chave (reverso={reverso})")
    
    def ordenar_por_valor(self, reverso=False):
        """Ordena o dicionário pelos valores"""
        self.dados = dict(sorted(self.dados.items(), key=lambda x: x[1], reverse=reverso))
        print(f"Ordenado por valor (reverso={reverso})")
    
    def filtrar(self, condicao):
        """Filtra o dicionário baseado em uma condição"""
        filtrado = {k: v for k, v in self.dados.items() if condicao(k, v)}
        return filtrado
    
    def mostrar(self):
        """Mostra o conteúdo do dicionário"""
        print(f"Dicionário: {self.dados}")
    
    def estatisticas(self):
        """Mostra estatísticas do dicionário"""
        if not self.dados:
            print("Dicionário vazio")
            return
        
        print(f"Número de itens: {len(self.dados)}")
        if all(isinstance(v, (int, float)) for v in self.dados.values()):
            valores = list(self.dados.values())
            print(f"Valor mínimo: {min(valores)}")
            print(f"Valor máximo: {max(valores)}")
            print(f"Valor médio: {sum(valores) / len(valores):.2f}")

# Testando a classe personalizada
print("\n--- TESTANDO CLASSE PERSONALIZADA ---")
meu_dict = DicionarioOrdenado()

# Inserções
meu_dict.inserir('banana', 3.50)
meu_dict.inserir('maçã', 4.20)
meu_dict.inserir('laranja', 2.80)
meu_dict.inserir('uva', 8.00)
meu_dict.mostrar()

# Estatísticas
print("\n--- ESTATÍSTICAS ---")
meu_dict.estatisticas()

# Ordenação
print("\n--- ORDENAÇÕES ---")
meu_dict.ordenar_por_valor(reverso=True)
meu_dict.mostrar()

meu_dict.ordenar_por_chave()
meu_dict.mostrar()

# Filtragem
print("\n--- FILTRAGEM ---")
caros = meu_dict.filtrar(lambda k, v: v > 4.0)
print(f"Frutas caras: {caros}")

# Deleção
print("\n--- DELEÇÃO ---")
meu_dict.remover('banana')
meu_dict.mostrar()

print("\n" + "=" * 60)
print("6. DICAS DE PERFORMANCE E BOAS PRÁTICAS")
print("=" * 60)

import time
import sys

def benchmark_dicionarios():
    n = 100000
    
    # Comparando diferentes formas de criar dicionários
    print("Comparando criação de dicionários:")
    
    # Dict comprehension
    start = time.time()
    dict1 = {i: i**2 for i in range(n)}
    time1 = time.time() - start
    
    # Dict() constructor
    start = time.time()
    dict2 = dict((i, i**2) for i in range(n))
    time2 = time.time() - start
    
    # Loop tradicional
    start = time.time()
    dict3 = {}
    for i in range(n):
        dict3[i] = i**2
    time3 = time.time() - start
    
    print(f"Dict comprehension: {time1:.4f}s")
    print(f"Dict constructor: {time2:.4f}s")
    print(f"Loop tradicional: {time3:.4f}s")
    print(f"Dict comprehension é {time2/time1:.1f}x mais rápida que constructor")
    
    # Testando acesso vs busca
    print(f"\nTestando acesso vs get():")
    chave_existente = n // 2
    chave_inexistente = n + 1000
    
    # Acesso direto (pode gerar KeyError)
    start = time.time()
    for _ in range(10000):
        try:
            valor = dict1[chave_existente]
        except KeyError:
            valor = None
    time_access = time.time() - start
    
    # Usando get()
    start = time.time()
    for _ in range(10000):
        valor = dict1.get(chave_existente)
    time_get = time.time() - start
    
    print(f"Acesso direto: {time_access:.4f}s")
    print(f"Usando get(): {time_get:.4f}s")

benchmark_dicionarios()

print("\n--- BOAS PRÁTICAS ---")
print("1. Use dict comprehensions para criar dicionários rapidamente")
print("2. Use get() para acessar chaves que podem não existir")
print("3. Use defaultdict quando precisar de valores padrão")
print("4. Use Counter para contagem de elementos")
print("5. Dicionários são ordenados desde Python 3.7+")
print("6. Use items() para iterar sobre chaves e valores")
print("7. Use keys() e values() quando precisar apenas de um deles")