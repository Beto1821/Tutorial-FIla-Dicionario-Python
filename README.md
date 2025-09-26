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

## 🚀 Início Rápido (5 minutos)

### ⚡ **PASSOS ESSENCIAIS:**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/Beto1821/python-filas-dicionarios.git
   cd python-filas-dicionarios
   ```

2. **🔥 CRIE O AMBIENTE VIRTUAL (.venv):**
   ```bash
   python -m venv .venv
   ```

3. **🔥 ATIVE O AMBIENTE VIRTUAL:**
   ```bash
   source .venv/bin/activate  # macOS/Linux
   ```

4. **Instale as dependências:**
   ```bash
   pip install jupyter notebook ipykernel
   ```

5. **Abra o Jupyter:**
   ```bash
   jupyter notebook tutorial_filas_dicionarios.ipynb
   ```

---

## 🚀 Como Usar

### Pré-requisitos

- Python 3.7 ou superior
- pip (gerenciador de pacotes Python)

### 📥 Instalação e Configuração

#### 1. **Clone o repositório:**
```bash
git clone https://github.com/seu-usuario/python-filas-dicionarios.git
cd python-filas-dicionarios
```

#### 2. **Crie e ative um ambiente virtual (.venv):**

**No macOS/Linux:**
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
source .venv/bin/activate

# Verificar se está ativo (deve aparecer (.venv) no prompt)
which python
```

**No Windows:**
```bash
# Criar ambiente virtual
python -m venv .venv

# Ativar ambiente virtual
.venv\Scripts\activate

# Verificar se está ativo (deve aparecer (.venv) no prompt)
where python
```

#### 3. **Instale as dependências:**
```bash
# Com ambiente virtual ativo
pip install -r requirements.txt

# Ou instalar manualmente:
pip install jupyter notebook ipykernel
```

#### 4. **Registre o ambiente virtual como kernel do Jupyter:**
```bash
# Garantir que o Jupyter use o Python do ambiente virtual
python -m ipykernel install --user --name=.venv --display-name="Python (.venv)"
```

### 🎯 Executando o Tutorial

#### **Opção 1: Jupyter Notebook (Recomendado)**
```bash
# Com (.venv) ativo, execute:
jupyter notebook tutorial_filas_dicionarios.ipynb
```

**Isso irá:**
- ✅ Abrir uma nova aba no seu navegador
- ✅ Carregar o notebook interativo
- ✅ Permitir executar células individualmente
- ✅ Mostrar outputs em tempo real

**Navegação no Jupyter:**
- **Executar célula**: `Shift + Enter`
- **Executar e criar nova célula**: `Alt + Enter`
- **Executar célula sem avançar**: `Ctrl + Enter`

#### **Opção 2: VS Code com Jupyter Extension**
```bash
# Abrir VS Code na pasta do projeto
code .

# No VS Code:
# 1. Instale a extensão "Jupyter"
# 2. Abra o arquivo tutorial_filas_dicionarios.ipynb
# 3. Selecione o kernel "Python (.venv)"
# 4. Execute as células com Shift+Enter
```

#### **Opção 3: Executar scripts Python diretamente**
```bash
# Para filas
python filas_python.py

# Para dicionários
python dicionarios_python.py
```

### 🔧 Solução de Problemas

#### **Erro: "jupyter: command not found"**
```bash
# Certifique-se que o ambiente virtual está ativo
source .venv/bin/activate  # macOS/Linux
# ou
.venv\Scripts\activate     # Windows

# Reinstale o Jupyter
pip install jupyter notebook
```

#### **Kernel não encontrado no Jupyter**
```bash
# Liste os kernels disponíveis
jupyter kernelspec list

# Adicione o kernel do ambiente virtual
python -m ipykernel install --user --name=.venv --display-name="Python (.venv)"
```

#### **Pacote não encontrado no notebook**
```bash
# Instale o pacote no ambiente virtual ativo
pip install nome-do-pacote

# Reinicie o kernel do Jupyter
# No notebook: Kernel -> Restart
```

### 📱 Primeira Execução - Passo a Passo

1. **Abra o terminal e navegue até a pasta:**
   ```bash
   cd ~/Desktop/meus\ scripts/python/fila
   ```

2. **Ative o ambiente virtual:**
   ```bash
   source .venv/bin/activate
   ```

3. **Verifique se o Jupyter está instalado:**
   ```bash
   jupyter --version
   ```

4. **Abra o notebook:**
   ```bash
   jupyter notebook tutorial_filas_dicionarios.ipynb
   ```

5. **No navegador que abriu:**
   - Clique na primeira célula (imports)
   - Pressione `Shift + Enter`
   - Continue executando célula por célula

6. **Para sair:**
   ```bash
   # No terminal, pressione Ctrl+C para parar o Jupyter
   # Para desativar o ambiente virtual:
   deactivate
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
- 📧 **Email**: beto1821@uol.com.br
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