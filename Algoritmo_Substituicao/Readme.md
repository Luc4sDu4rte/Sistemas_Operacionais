Crie um simulador para a execução dos algoritmos de substituição de páginas. Para isso teremos 1 matriz com 10 linhas e 6 colunas para modelar as molduras de páginas na memória RAM e outra matriz 100 linhas e 6 colunas que vai representar as páginas em SWAP. Os campos da matriz são:  Número de Página (N), Instrução (I), Dado (D), Bit de Acesso R, Bit de Modificação M e o tempo de Envelhecimento (T).

- Crie inicialmente a matriz 100x6 (MATRIZ SWAP), onde ela deverá ser preenchida da seguinte forma:

--> A coluna N terá os números de 0 a 99, sequencialmente ( linha 0 -> N = 0, linha 1 -> N = 1, linha 2 -> N = 2...)

--> A coluna I terá os números de 1 a 100, sequencialmente ( linha 0 -> I = 1, linha 1 -> I = 2, linha 2 -> I = 3...)

--> A coluna D terá números de 1 a 50, sorteados ale aleatoriamente. 

 --> A coluna R = 0.

--> A coluna M = 0.

-->A coluna T terá números aleatórios de 100 a 9999.

A matriz 10x6 (MATRIZ RAM) possui os mesmos campos. A MATRIZ RAM será preenchida da seguinte maneira:

--> Para cada linha da matriz MATRIZ RAM, Sorteie um número de 0 a 99. Copie dos dados para a linha da MATRIZ RAM a partir da MATRIZ  SWAP, usando como índice para a linha o número que foi sorteado. Ou seja, serão sorteadas 10 linhas da matriz MATRIZ SWAP e copiadas para a MATRIZ RAM.

Posteriormente para a execução do simulador,  será sorteado um número de 1 a 100, referente a instrução (campo I) que está sendo requisitada para a execução na CPU. Será feito uma pesquisa no campo I da matriz MATRIZ RAM para verificar se o valor da instrução está carregado na memória RAM. 

Caso esteja, duas operações serão realizadas:

1) O bit de acesso R vai receber o valor 1.

2) A página terá 30% de chance de sofrer uma modificação. Ou seja, caso a probabilidade seja atingida, duas ações serão realizadas:

2.1) O campo Dado (D) será atualizado da seguinte maneira: D = D + 1;

2.2) O campo Modificado será atualizado: M = 1;

Caso o número de instrução sorteado não esteja presente na MATRIZ RAM, deverá ser utilizado um algoritmo de substituição de página para realizar a substituição.

Obs1.: O simulador deverá executar 1000 instruções para cada algoritmo de substituição de página.

Obs2.: Os algoritmos de substituição de páginas para serem implementados são; NRU, FIFO, FIFO-SC,  RELÓGIO e WS-CLOCK (implementar TODOS).

Obs3.: Para a implementação do algoritmo WS-Clock, sortear um número para verificar o envelhecimento da página (EP). O valor de EP deve ser na faixa de 100 a 9999.  Caso o EP <= T, a página ainda está no conjunto de trabalho. Caso  EP > T, a página não fará parte do conjunto de trabalho.

Obs4.: A cada 10 Instruções, o Bit R deve ser zerado para todas as páginas na memória RAM.

Obs5.: Cada vez que uma página que tiver o Bit M=1, e esta for retirada da memória, Ela deve ser salva em SWAP com o Bit M=0.

Obs6.: No início da execução deve ser impresso as MATRIZ RAM e a MATRIZ SWAP, e ao final das 1000 instruções deve ser impresso novamente ambas as matrizes.