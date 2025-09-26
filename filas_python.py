"""
FILAS EM PYTHON - Tutorial Otimizado e Interativo
=================================================

Uma fila (Queue) é uma estrutura de dados que segue o princípio FIFO
(First In, First Out). Este tutorial demonstra diferentes implementações,
operações e casos de uso práticos.

Autor: Tutorial Python
Versão: 2.0 - Otimizada
"""

from collections import deque
import queue
import heapq
import time
from typing import List, Any, Optional


class FilaOtimizada:
    """Classe otimizada para operações de fila com métodos úteis."""
    
    def __init__(self):
        self._fila = deque()
    
    def inserir(self, elemento: Any) -> None:
        """Insere elemento no final da fila."""
        self._fila.append(elemento)
    
    def remover(self) -> Optional[Any]:
        """Remove e retorna o primeiro elemento da fila."""
        if self._fila:
            return self._fila.popleft()
        return None
    
    def primeiro(self) -> Optional[Any]:
        """Retorna o primeiro elemento sem remover."""
        return self._fila[0] if self._fila else None
    
    def ultimo(self) -> Optional[Any]:
        """Retorna o último elemento sem remover."""
        return self._fila[-1] if self._fila else None
    
    def vazia(self) -> bool:
        """Verifica se a fila está vazia."""
        return len(self._fila) == 0
    
    def tamanho(self) -> int:
        """Retorna o tamanho da fila."""
        return len(self._fila)
    
    def limpar(self) -> None:
        """Remove todos os elementos da fila."""
        self._fila.clear()
    
    def listar(self) -> List[Any]:
        """Retorna uma lista com todos os elementos."""
        return list(self._fila)
    
    def ordenar(self) -> None:
        """Ordena a fila (quebra temporariamente o princípio FIFO)."""
        elementos = sorted(self._fila)
        self._fila.clear()
        self._fila.extend(elementos)
    
    def __str__(self) -> str:
        return f"Fila({list(self._fila)})"
    
    def __len__(self) -> int:
        return len(self._fila)


def demonstracao_basica():
    """Demonstração básica de operações com filas."""
    print("=" * 60)
    print("DEMONSTRAÇÃO BÁSICA - OPERAÇÕES COM FILAS")
    print("=" * 60)
    
    # Usando collections.deque (mais eficiente)
    fila = deque()
    
    print("\n1. INSERÇÃO (append)")
    elementos = ["Cliente 1", "Cliente 2", "Cliente 3", "Cliente 4"]
    for elemento in elementos:
        fila.append(elemento)
        print(f"   Inserido: {elemento} | Fila: {list(fila)}")
    
    print("\n2. REMOÇÃO (popleft) - FIFO")
    while fila:
        removido = fila.popleft()
        print(f"   Atendido: {removido} | Restam: {list(fila)}")
    
    print("\n3. FILA COM NÚMEROS PARA ORDENAÇÃO")
    fila_nums = deque([5, 2, 8, 1, 9, 3])
    print(f"   Original: {list(fila_nums)}")
    
    # Ordenar (quebra temporariamente FIFO)
    fila_ordenada = deque(sorted(fila_nums))
    print(f"   Ordenada: {list(fila_ordenada)}")


def demonstracao_queue_module():
    """Demonstração usando o módulo queue (thread-safe)."""
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO - queue.Queue (THREAD-SAFE)")
    print("=" * 60)
    
    fila = queue.Queue(maxsize=5)  # Fila com tamanho máximo
    
    print("\n1. Inserindo elementos:")
    for i in range(1, 6):
        item = f"Task {i}"
        fila.put(item)
        print(f"   Inserido: {item} | Tamanho: {fila.qsize()}")
    
    print("\n2. Removendo elementos:")
    while not fila.empty():
        item = fila.get()
        print(f"   Processado: {item} | Restam: {fila.qsize()}")


def demonstracao_fila_prioridade():
    """Demonstração de fila de prioridade usando heapq."""
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO - FILA DE PRIORIDADE (heapq)")
    print("=" * 60)
    
    fila_prioridade = []
    
    print("\n1. Inserindo com prioridade (menor número = maior prioridade):")
    tarefas = [
        (3, "Tarefa Normal"),
        (1, "Tarefa Urgente"),
        (2, "Tarefa Importante"),
        (4, "Tarefa Baixa Prioridade")
    ]
    
    for prioridade, tarefa in tarefas:
        heapq.heappush(fila_prioridade, (prioridade, tarefa))
        print(f"   Adicionada: {tarefa} (prioridade {prioridade})")
    
    print("\n2. Processando por prioridade:")
    while fila_prioridade:
        prioridade, tarefa = heapq.heappop(fila_prioridade)
        print(f"   Executando: {tarefa} (prioridade {prioridade})")


def demonstracao_classe_otimizada():
    """Demonstração da classe FilaOtimizada."""
    print("\n" + "=" * 60)
    print("DEMONSTRAÇÃO - CLASSE FILA OTIMIZADA")
    print("=" * 60)
    
    fila = FilaOtimizada()
    
    print("\n1. Operações básicas:")
    for i in range(1, 6):
        fila.inserir(f"Item {i}")
    
    print(f"   Fila criada: {fila}")
    print(f"   Primeiro elemento: {fila.primeiro()}")
    print(f"   Último elemento: {fila.ultimo()}")
    print(f"   Tamanho: {fila.tamanho()}")
    
    print("\n2. Removendo elementos:")
    while not fila.vazia():
        removido = fila.remover()
        print(f"   Removido: {removido} | Restam: {fila.tamanho()}")


def benchmark_performance():
    """Benchmark de performance entre diferentes implementações."""
    print("\n" + "=" * 60)
    print("BENCHMARK DE PERFORMANCE")
    print("=" * 60)
    
    n = 100000
    
    # Benchmark deque
    start_time = time.time()
    fila_deque = deque()
    for i in range(n):
        fila_deque.append(i)
    for i in range(n):
        fila_deque.popleft()
    tempo_deque = time.time() - start_time
    
    # Benchmark lista (ineficiente para filas)
    start_time = time.time()
    fila_lista = []
    for i in range(n):
        fila_lista.append(i)
    for i in range(n):
        fila_lista.pop(0)  # Ineficiente - O(n)
    tempo_lista = time.time() - start_time
    
    print(f"\nResultados para {n:,} operações:")
    print(f"   deque:     {tempo_deque:.4f}s")
    print(f"   lista:     {tempo_lista:.4f}s")
    print(f"   deque é {tempo_lista/tempo_deque:.1f}x mais rápida!")


def menu_interativo():
    """Menu interativo para testar operações de fila."""
    print("\n" + "=" * 60)
    print("MENU INTERATIVO - TESTE SUA PRÓPRIA FILA")
    print("=" * 60)
    
    fila = FilaOtimizada()
    
    while True:
        print("\n" + "-" * 40)
        print(f"Fila atual: {fila}")
        print(f"Tamanho: {fila.tamanho()}")
        print("-" * 40)
        print("1. Adicionar elemento")
        print("2. Remover elemento")
        print("3. Ver primeiro elemento")
        print("4. Ver último elemento")
        print("5. Ordenar fila")
        print("6. Limpar fila")
        print("7. Simulação de atendimento")
        print("0. Voltar ao menu principal")
        
        try:
            opcao = input("\nEscolha uma opção (0-7): ").strip()
            
            if opcao == "0":
                break
            elif opcao == "1":
                elemento = input("Digite o elemento para adicionar: ").strip()
                if elemento:
                    fila.inserir(elemento)
                    print(f"✅ '{elemento}' adicionado à fila!")
                else:
                    print("❌ Elemento não pode estar vazio!")
                    
            elif opcao == "2":
                removido = fila.remover()
                if removido:
                    print(f"✅ '{removido}' removido da fila!")
                else:
                    print("❌ Fila vazia!")
                    
            elif opcao == "3":
                primeiro = fila.primeiro()
                if primeiro:
                    print(f"👆 Primeiro: '{primeiro}'")
                else:
                    print("❌ Fila vazia!")
                    
            elif opcao == "4":
                ultimo = fila.ultimo()
                if ultimo:
                    print(f"👇 Último: '{ultimo}'")
                else:
                    print("❌ Fila vazia!")
                    
            elif opcao == "5":
                if not fila.vazia():
                    fila.ordenar()
                    print("✅ Fila ordenada!")
                else:
                    print("❌ Fila vazia!")
                    
            elif opcao == "6":
                fila.limpar()
                print("✅ Fila limpa!")
                
            elif opcao == "7":
                simulacao_atendimento()
                
            else:
                print("❌ Opção inválida!")
                
        except KeyboardInterrupt:
            print("\n\n👋 Saindo...")
            break
        except Exception as e:
            print(f"❌ Erro: {e}")


def simulacao_atendimento():
    """Simula um sistema de atendimento com senhas."""
    print("\n" + "=" * 50)
    print("SIMULAÇÃO - SISTEMA DE ATENDIMENTO")
    print("=" * 50)
    
    fila_atendimento = FilaOtimizada()
    contador_senha = 1
    
    while True:
        print(f"\n--- PAINEL DE ATENDIMENTO ---")
        print(f"Pessoas na fila: {fila_atendimento.tamanho()}")
        
        if not fila_atendimento.vazia():
            print(f"Próximo: {fila_atendimento.primeiro()}")
        
        print("\n1. Retirar senha")
        print("2. Chamar próximo")
        print("3. Ver fila completa")
        print("0. Voltar")
        
        opcao = input("\nOpção: ").strip()
        
        if opcao == "0":
            break
        elif opcao == "1":
            nome = input("Nome: ").strip()
            if nome:
                senha = f"#{contador_senha:03d} - {nome}"
                fila_atendimento.inserir(senha)
                print(f"🎫 Senha retirada: {senha}")
                contador_senha += 1
            else:
                print("❌ Nome não pode estar vazio!")
                
        elif opcao == "2":
            proximo = fila_atendimento.remover()
            if proximo:
                print(f"📢 Chamando: {proximo}")
                input("   Pressione ENTER após o atendimento...")
                print("✅ Atendimento concluído!")
            else:
                print("❌ Ninguém na fila!")
                
        elif opcao == "3":
            if fila_atendimento.vazia():
                print("   Fila vazia!")
            else:
                print("   Fila atual:")
                for i, pessoa in enumerate(fila_atendimento.listar(), 1):
                    print(f"     {i}. {pessoa}")


def main():
    """Função principal com menu de opções."""
    print("🐍 " + "=" * 58 + " 🐍")
    print("   TUTORIAL COMPLETO DE FILAS EM PYTHON - VERSÃO 2.0")
    print("🐍 " + "=" * 58 + " 🐍")
    
    while True:
        print("\n" + "=" * 50)
        print("MENU PRINCIPAL")
        print("=" * 50)
        print("1. Demonstração básica (deque)")
        print("2. Demonstração queue.Queue (thread-safe)")
        print("3. Demonstração fila de prioridade (heapq)")
        print("4. Demonstração classe otimizada")
        print("5. Benchmark de performance")
        print("6. Menu interativo")
        print("0. Sair")
        
        try:
            opcao = input("\nEscolha uma opção (0-6): ").strip()
            
            if opcao == "0":
                print("\n👋 Obrigado por usar o tutorial! Até mais!")
                break
            elif opcao == "1":
                demonstracao_basica()
            elif opcao == "2":
                demonstracao_queue_module()
            elif opcao == "3":
                demonstracao_fila_prioridade()
            elif opcao == "4":
                demonstracao_classe_otimizada()
            elif opcao == "5":
                benchmark_performance()
            elif opcao == "6":
                menu_interativo()
            else:
                print("❌ Opção inválida! Escolha um número de 0 a 6.")
                
            if opcao != "0":
                input("\n⏸️  Pressione ENTER para continuar...")
                
        except KeyboardInterrupt:
            print("\n\n👋 Saindo... Até mais!")
            break
        except Exception as e:
            print(f"❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()