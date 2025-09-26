# 🐍 Tutorial: Filas e Dicionários em Python

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)

> Tutorial completo sobre **inserção, ordenação e deleção** de elementos em **Filas (Queues)** e **Dicionários** em Python.

## 📚 Sobre o Projeto

Este repositório contém um tutorial abrangente que ensina os conceitos fundamentais de manipulação de duas estruturas de dados essenciais em Python:

- **🗂️ Filas (Queues)**: FIFO, LIFO, Priority Queues
- **📖 Dicionários**: Operações de inserção, deleção e ordenação

### 🎯 Objetivos de Aprendizagem

Após completar este tutorial, você será capaz de:

- ✅ Entender diferentes tipos de filas e quando usar cada uma
- ✅ Implementar inserção, deleção e ordenação em filas
- ✅ Dominar operações avançadas em dicionários
- ✅ Escolher a estrutura de dados mais eficiente para cada situação
- ✅ Otimizar performance usando as melhores práticas
- ✅ Criar sistemas práticos usando estas estruturas

## 📁 Estrutura do Projeto

```
📂 python-filas-dicionarios/
├── 📄 README.md                           # Este arquivo
├── 📓 tutorial_filas_dicionarios.ipynb    # Jupyter Notebook interativo
├── 🐍 filas_python.py                     # Exemplos práticos de filas
├── 🐍 dicionarios_python.py               # Exemplos práticos de dicionários
└── 📄 requirements.txt                    # Dependências do projeto
```

## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- Jupyter Notebook (opcional, mas recomendado)

### 📥 Instalação

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/python-filas-dicionarios.git
   cd python-filas-dicionarios
   ```

2. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Execute os exemplos:**
   ```bash
   # Para filas
   python filas_python.py
   
   # Para dicionários
   python dicionarios_python.py
   ```

4. **Abra o tutorial interativo:**
   ```bash
   jupyter notebook tutorial_filas_dicionarios.ipynb
   ```

## 📖 Conteúdo Detalhado

### 🗂️ Filas (Queues)

| Tópico | Descrição | Arquivo |
|--------|-----------|---------|
| **FIFO Queue** | First In, First Out com `collections.deque` | `filas_python.py` |
| **LIFO Queue** | Last In, First Out (pilhas) | `filas_python.py` |
| **Priority Queue** | Filas com prioridade usando `heapq` | `filas_python.py` |
| **Thread-Safe** | Filas seguras para concorrência | `filas_python.py` |
| **Performance** | Comparação `deque` vs `list` | `tutorial_filas_dicionarios.ipynb` |

**Métodos Principais:**
- `append()` / `appendleft()` - Inserção
- `pop()` / `popleft()` - Remoção
- `put()` / `get()` - Thread-safe
- `heappush()` / `heappop()` - Priority Queue

### 📖 Dicionários

| Tópico | Descrição | Arquivo |
|--------|-----------|---------|
| **Inserção** | `dict[key]`, `update()`, `setdefault()` | `dicionarios_python.py` |
| **Deleção** | `del`, `pop()`, `popitem()`, `clear()` | `dicionarios_python.py` |
| **Ordenação** | Por chave, valor, múltiplos critérios | `dicionarios_python.py` |
| **Especiais** | `defaultdict`, `Counter`, `OrderedDict` | `dicionarios_python.py` |
| **Avançado** | Filtragem, aninhamento, performance | `tutorial_filas_dicionarios.ipynb` |

**Operações Principais:**
- **Inserção**: Atribuição direta, `update()`, dictionary comprehensions
- **Deleção**: `del`, `pop()` (com valor padrão), `popitem()`
- **Ordenação**: `sorted()` com `key`, `operator.itemgetter()`

## 🧪 Exemplos Práticos

### 1. Sistema de Atendimento Bancário
```python
# Fila de prioridade para banco
from collections import deque
import heapq

class BancoAtendimento:
    def __init__(self):
        self.fila_comum = deque()
        self.fila_prioritaria = []
    
    def adicionar_cliente_prioritario(self, nome, prioridade=1):
        heapq.heappush(self.fila_prioritaria, (prioridade, nome))
    
    def chamar_proximo(self):
        if self.fila_prioritaria:
            return heapq.heappop(self.fila_prioritaria)[1]
        elif self.fila_comum:
            return self.fila_comum.popleft()
```

### 2. Sistema de Inventário
```python
# Gerenciamento de produtos
class Inventario:
    def __init__(self):
        self.produtos = {}
    
    def adicionar_produto(self, codigo, nome, preco, estoque):
        self.produtos[codigo] = {
            'nome': nome, 'preco': preco, 'estoque': estoque
        }
    
    def ordenar_por_preco(self):
        return dict(sorted(self.produtos.items(), 
                          key=lambda x: x[1]['preco']))
```

## ⚡ Comparação de Performance

| Operação | `deque` | `list` | Complexidade |
|----------|---------|--------|--------------|
| Append | ✅ O(1) | ✅ O(1) | Mesma performance |
| Pop Left | ✅ O(1) | ❌ O(n) | **deque é muito mais rápida!** |
| Pop Right | ✅ O(1) | ✅ O(1) | Mesma performance |

| Dicionário | Acesso | Inserção | Deleção |
|------------|--------|----------|---------|
| `dict[key]` | O(1) | O(1) | - |
| `dict.get()` | O(1) | - | - |
| `dict.pop()` | - | - | O(1) |
| `sorted(dict)` | - | - | O(n log n) |

## 🎯 Exercícios Inclusos

O tutorial inclui exercícios práticos para consolidar o aprendizado:

1. **📊 Sistema de Atendimento Bancário**
   - Implementação completa com filas de prioridade
   - Gerenciamento de clientes comuns e prioritários
   
2. **📦 Sistema de Inventário**
   - CRUD completo para produtos
   - Ordenação por diferentes critérios
   - Relatórios de estoque baixo

3. **🔄 Desafios Adicionais**
   - Cache com LRU (Least Recently Used)
   - Sistema de pedidos em restaurante
   - Análise de logs com contadores

## 🤝 Como Contribuir

1. **Fork** o projeto
2. **Crie** uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. **Commit** suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. **Push** para a branch (`git push origin feature/AmazingFeature`)
5. **Abra** um Pull Request

### 💡 Ideias para Contribuição

- 📝 Adicionar mais exemplos práticos
- 🧪 Criar testes unitários
- 🌐 Traduzir para outros idiomas
- 📊 Adicionar visualizações gráficas
- 🔧 Otimizar exemplos de performance

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🙏 Agradecimentos

- **Python Software Foundation** pela excelente documentação
- **Jupyter Project** pela plataforma interativa
- **Comunidade Python** pelas melhores práticas e otimizações

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas:

- 🐛 **Issues**: [GitHub Issues](https://github.com/seu-usuario/python-filas-dicionarios/issues)
- 📧 **Email**: seu-email@exemplo.com
- 💬 **Discussões**: [GitHub Discussions](https://github.com/seu-usuario/python-filas-dicionarios/discussions)

## 🔗 Links Úteis

- 📚 [Documentação Oficial do Python](https://docs.python.org/3/)
- 📖 [Python Collections Module](https://docs.python.org/3/library/collections.html)
- 🎯 [Python Performance Tips](https://wiki.python.org/moin/PythonSpeed/PerformanceTips)
- 📊 [Big O Complexity](https://www.bigocheatsheet.com/)

---

<div align="center">

**⭐ Se este tutorial foi útil, não esqueça de dar uma estrela no repositório! ⭐**

Made with ❤️ for the Python community

</div>