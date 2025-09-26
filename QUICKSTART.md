# 🚀 Guia de Início Rápido

## ⚡ Execução Rápida (5 minutos)

### 1. Clone e Execute
```bash
git clone https://github.com/seu-usuario/python-filas-dicionarios.git
cd python-filas-dicionarios
python filas_python.py
```

### 2. Exemplos Essenciais

#### 🗂️ Fila Simples
```python
from collections import deque

# Criar fila
fila = deque()

# Adicionar elementos
fila.append("Primeiro")
fila.append("Segundo")

# Remover elementos (FIFO)
primeiro = fila.popleft()  # "Primeiro"
```

#### 📖 Dicionário Básico
```python
# Criar dicionário
pessoa = {}

# Inserção
pessoa["nome"] = "João"
pessoa.update({"idade": 30, "cidade": "SP"})

# Ordenação por valor
ordenado = dict(sorted(pessoa.items(), key=lambda x: x[1]))

# Deleção segura
idade = pessoa.pop("idade", 0)  # Remove e retorna, ou 0 se não existir
```

### 3. Para Tutorial Completo
```bash
jupyter notebook tutorial_filas_dicionarios.ipynb
```

## 📊 Comparação Rápida

| Operação | Use | Evite |
|----------|-----|-------|
| Fila FIFO | `deque()` | `list.pop(0)` |
| Dicionário | `dict.get()` | `dict[key]` sem verificar |
| Ordenação | `operator.itemgetter()` | `lambda` simples |

**⚡ Dica**: `deque` é até 100x mais rápida que `list` para operações FIFO!