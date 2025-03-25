# MaxMin Select - Algoritmo de Seleção Simultânea do Maior e do Menor Elementos

## Descrição do Projeto
Este projeto implementa o algoritmo MaxMin Select utilizando a abordagem de Divisão e Conquista. O objetivo do algoritmo é encontrar simultaneamente o maior e o menor elemento de uma sequência de números com um número reduzido de comparações.

## Lógica do Algoritmo
1. O problema é resolvido recursivamente:
   - Se houver apenas um elemento, ele é tanto o maior quanto o menor.
   - Se houver dois elementos, a comparação direta retorna o menor e o maior.
   - Para mais de dois elementos, o array é dividido em duas metades.
   - Cada metade é processada recursivamente para obter os valores mínimos e máximos.
   - Os resultados das duas metades são combinados, comparando os mínimos e os máximos.

## Como Executar o Projeto
### Requisitos
- Python 3 instalado

### Passos para rodar o código
1. Clone este repositório ou copie os arquivos.
2. Execute o script `main.py` com o comando:
   ```bash
   python main.py
   ```
3. O script imprimirá o menor e o maior elemento da lista.

## Análise da Complexidade

### Contagem de Operações
O algoritmo realiza:
- 1 comparação quando há dois elementos.
- Para `n` elementos, divide o array em dois subproblemas de tamanho `n/2`.
- Após a resolução dos subproblemas, são feitas 2 comparações adicionais para combinar os resultados.
- Isso resulta em uma complexidade de `O(n)`, pois cada elemento é comparado um número constante de vezes.

### Aplicação do Teorema Mestre
A recorrência do problema é:
```
T(n) = 2T(n/2) + O(1)
```
Identificamos:
- `a = 2` (duas chamadas recursivas)
- `b = 2` (tamanho reduzido pela metade a cada passo)
- `f(n) = O(1)`

Calculamos:
```
log_b a = log_2 2 = 1
```
Como `f(n) = O(1) = O(n^0)`, temos `p = 0`.
Pelo Teorema Mestre, `O(n^p) = O(n^0)`, e como `log_b a > p`, a complexidade é:
```
O(n)
```
Ou seja, o algoritmo executa em tempo linear `O(n)`, sendo mais eficiente que a abordagem ingênua de comparar todos os elementos diretamente.

