O Jantar dos filósofos foi proposto por Dijkstra em 1965 como um problema de sincronização. A partir de então todos os algoritmos propostos como soluções de sincronização acabaram sendo relacionados ou testados contra o problema do Jantar dos filósofos.

DEFINIÇÃO DO PROBLEMA DO JANTAR DOS FILÓSOFOS

Cinco filósofos estão sentados em uma mesa redonda para jantar. Cada filósofo tem um prato com espaguete à sua frente. Cada prato possui um garfo para pegar o espaguete. O espaguete está muito escorregadio e, para que um filósofo consiga comer, será necessário utilizar dois garfos. 

Lembre-se que é apenas uma analogia. Nesse sentido, cada filósofo alterna entre duas tarefas: comer ou pensar. Quando um filósofo fica com fome, ele tenta pegar os garfos à sua esquerda e à sua direita; um de cada vez, independente da ordem. Caso ele consiga pegar dois garfos, ele come durante um determinado tempo e depois recoloca os garfos na mesa. Em seguida ele volta a pensar.

Por definição, o problema em questão é:

Cada filósofo deve executar as tarefas de comer e pensar sem nunca ficar travado.

Definção do problema:

Cada filósofo deve, alternadamente, refletir e comer.

Para que um filósofo coma, ele deve possuir dois garfos

Os dois garfos devem ser aqueles logo a sua esquerda e a sua direita

Para pegar um garfo

Somente pode ser pego por um filósofo

Somente pode ser pego não estiver em uso por nenhum outro filósofo

Após comer, o filósofo deve liberar o garfo que utilizou

Um filósofo pode segurar o garfo da sua direita ou o da sua esquerda assim que estiverem disponíveis

Mas, só pode começar a comer quando ambos estiverem sob sua posse.