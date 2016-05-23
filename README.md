# Algoritmos Infraestrutura de Software

Algoritmos de escalonamento e paginação

## Algoritmos de Escalonamento

### RR (Round-Robin) [+] (http://escalonamentoprocessos.blogspot.com.br/2010/10/algoritmos-de-escalonamento.html)

A política SCHED RR (Round Robin _ alternância circular) funciona do mesmo modo que a FIFO, entretanto com ela os processos de tempo real podem ser interrompidos pelo relógio, ou melhor, eles executam durante uma determinada fatia do tempo do processador, assim que o tempo acaba eles são postos no final da fila de execução. Esta estratégia garante uma atribuição justa do tempo de processador para todos os processos Round Robin.

### FCFS (First-Come, First Served) [+] (https://joaoricardao.files.wordpress.com/2012/07/algoritmos_escalonamento.pdf)

A estratégia FIFO (First In, First Out) implementada no kernel do Linux consiste no conceito: primeiro processo de tempo-real a entrar é o primeiro a sair. Os processos FIFO de tempo real não podem ser antecipados por outro processo que não seja FIFO de tempo real, esses processos também não trabalham com fatias de tempo, ou seja, eles podem dispor do processador praticamente o tempo que necessitarem.

## Algoritmos de Paginação

### FIFO (First-in, First-out) [+]( http://escalonamentoprocessos.blogspot.com.br/2010/12/memoria-virtual-paginacao-por-demanda-e.html)

É um algoritmo de substituição de páginas de baixo custo e de fácil implementação que consiste em substituir a página que foi carregada há mais tempo na memória (a primeira página a entrar é a primeira a sair). Esta escolha não leva em consideração se a página está sendo muito utilizada ou não, o que não é muito adequado pois pode prejudicar o desempenho do sistema. Por este motivo, o FIFO apresenta uma deficiência denominada anomalia de Belady: a quantidade de falta de páginas pode aumentar quando o tamanho da memória também aumenta.
Por estas razões, o algoritmo FIFO puro é muito pouco utilizado. Contudo, sua principal vantagem é a facilidade de implementação: uma lista de páginas ordenada pela “idade”. Dessa forma, na ocorrência de uma falta de página a primeira página da lista será substituída e a nova será acrescentada ao final da lista.

### LRU (Least Recently Used) [+]( http://escalonamentoprocessos.blogspot.com.br/2010/12/memoria-virtual-paginacao-por-demanda-e.html)

É um algoritmo de substituição de página que apresenta um bom desempenho substituindo a página menos recentemente usada. Esta política foi definida baseada na seguinte observação: se a página está sendo intensamente referenciada pelas instruções é muito provável que ela seja novamente referenciada pelas instruções seguintes e, de modo oposto, aquelas que não foram acessadas nas últimas instruções também é provável que não sejam acessadas nas próximas. Apesar de o LRU apresentar um bom desempenho ele também possui algumas deficiências [CAS03] quando o padrão de acesso é sequencial (em estruturas de dados do tipo vetor, lista, árvore), dentro de loops, etc. Diante dessas deficiências foram propostas algumas variações do LRU, dentre eles destacamos o LRU-K. Este algoritmo não substitui aquela que foi referenciada há mais tempo e sim quando ocorreu seu k-último acesso. Por exemplo, LRU-2 substituirá a página que teve seu penúltimo acesso feito há mais tempo e LRU-3 observará o antepenúltimo e assim por diante. 
A implementação do LRU também pode ser feita através de uma lista, mantendo as páginas mais referenciadas no início (cabeça) e a menos referenciadas no final da lista. Portanto, ao substituir retira-se a página que está no final da lista. O maior problema com esta organização é que a lista deve ser atualizada a cada nova referência efetuada sobre as páginas, o que torna alto o custo dessa manutenção.