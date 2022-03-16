# Minera-Referencias

# Apresentação
Esse script foi construído para mineração de dados de referências bibliográficas, no formato da ABNT – Associação Brasileira de Normas Técnicas, de arquivos de texto com extensão .pdf e .txt, para elaboração de análises de redes teórico-filosóficas através do Gephi.

# Contexto e usos

O presente script foi elaborado por Fernando Borges, programador Python e Ronald Canabarro, historiadora. Foi desenvolvido para atender a uma demanda específica de um projeto de doutorado, cuja necessidade é extrair as informações de referências bibliográficas de dissertações e teses defendidas na área de avaliação em História, no Brasil. Especificamente aquelas que investigam sobre as dissidências sexuais e desobediências de gênero. O corpus utilizado como teste para a execução e extração dos dados foi de 171 arquivos. Os dados extraídos são organizados em formato .csv (figura 1) para importação e uso no Gephi - software de visualização e exploração para todos os tipos de gráficos e redes de código aberto e gratuito - para a elaboração de análises de redes. 

Assim, nessa análise, busco observar três dados: o nome da autoria da dissertação ou tese (Source), o nome da autoria citada (Target) e o ano de defesa da tese ou dissertação (Year). Portanto, não estão incluídas nessa mineração de dados os títulos das publicações, tampouco editora, ano e cidade. 

Entre os usos possíveis estão a extração de referencias bibliográficas de teses, dissertações e artigos, desde que usem como normas de citações a ABNT e estejam em formato .pdf ou .txt. Essas informações permitem analisar o número de autores citados e as interligações entre eles através da rede formada, permitindo análises de redes teórico-filosóficas utilizadas por determinado corpus analisado, incluindo a análise temporal das refrências bibliográficas.

# Passo-a-passo

- Primeiro de tudo certifique-se de renomear os arquivos que deseja extrair as referências bibliográficas, de formato ABNT, com o nome do SOBRENOME_NomeAAAA, ex.: AMORIM_Graziele_Regina_de2015. Esse formato é que garantirá as informações da primeira e terceira coluna, nome do autor citante e ano de publicação da pesquisa. 

Lembre-se que esses devem estar em extensão .pdf ou .txt. 

- Crie uma pasta nos seus documentos e em seguida faça download de todas as pastas e arquivos aqui disponibilizados. Sugestão de nome para a pasta: MNinera-referencias
- Agora basta salvar os arquivos já renomeados, na pasta ARQUIVOS. 
- Uma vez realizados esses passos, faça um duplo clique no ícone - app.exe. 
- Os dados de cada arquivo serão extraídos para um novo, com extensão .csv, na pasta ARQUIVOS. 

A tabela conterá três colunas: Source (nome da autoria citante), Target (nome da autoria citada) e Year (ano de defesa/publicação). Essa são as informações no formato que se consegue utilizar importando para o Gephi fazer análise de redes.

Figura 1 – Imagem modelo de tabela de referencias bibliográficas extraídas

https://github.com/ronaldcanabarro/minera-referencias/blob/main/modelo_tabela_referencias.png 

Sobre o Gephi, ver: "Gephi: Guia Básico de Interface" - Disponível em: http://www.encurtador.com.br/dqRT4

# Filtros e regras do Script

1)	Busca todos os arquivos presentes na pasta 'Arquivos' e filtra apenas os que tiverem como extensão '.pdf', '.PDF', '.txt' ou '.TXT';
2)	Abre o arquivo de acordo com a extensão origem (pdf ou txt); 
3)	Primeiro filtro busca palavras chaves como 'REFERÊNCIAS', 'Referências', 'Bibliografia', 'BIBLIOGRAFIA' e usa para fragmentar o texto tendo como condicional que a última porção (onde devem estar as referências) não deve conter a palavra 'INTRODUÇÃO' ou '.......' uma vez que estas comumente se encontram antes do referencial bibliográfico e não neste;
4)	Todos os valores '\n' são retirados e todos os itens vazios extraídos da lista com todas as palavras, fazendo com que uma lista ['KARVAT,', ' ', 'Erivan', '\nCassiano', 'et', '\n\nal.'] mude para ['KARVAT,', 'Erivan', 'Cassiano', 'et', 'al.'];
5)	Segundo filtro busca separar os parágrafos de cada referência tendo como condicionais que o início do parágrafo comece como o nome do autor em caixa alta seguido de virgula, como por ex. "JOÃO,". E que tenha anteriormente uma palavra com ponto final indicando o fim de uma linha ex. "Rio de Janeiro: Dois Pontos, 1987.";
6)	Terceiro filtro separa as palavras anteriores junto a primeira palavra inteiramente em caixa baixa, primeiro valor numérico ou símbolo; 
7)	Quarto filtro é para manter um padrão de término no nome de cada autor apenas com o ponto final na última palavra ex ['POLLAK,', 'Michael.', 'Junior.'] mude para ['POLLAK,', 'Michael.'];
8)	Por fim, salva a lista/tabela de acordo com a origem do arquivo (pdf ou txt). Como por ex.: ARAUJO_Joao_Diogo_Trindade_Cordeiro2018PDF. 

# Observações pertinentes:

Entre os dados que não importamos estão as citações que não começam com um nome de autor, mas de uma revista, jornal, título de artigo, relatório ou lei. Como por exemplo: RELATÓRIO de Direitos Humanos. 2013. Disponível em http://www.sdh.gov.br/assuntos/lgbt/dados-estatisticos/Relatorio2013.pdf acessado em 02 de março de 2017. 
Os autores citados, independente de quantas vezes aparecerem, farão parte da tabela. 


# Problemas e inconsistências dessa versão:

Alguns arquivos .pdf possuem níveis de proteção e não permitem a extração, assim que, caso o script não execute, sugiro converter seu .pdf para .txt. 

Observe se as referências estão em formato ABNT, ou seja, no formato SOBRENOME, Nome. E de que haja um título que identifique as Referências Bibliográficas, que podem ser reconhecidas como Bibliografia, REFERENCIAS, e suas variações já expostas anteriormente. Caso contrário será necessário editar seu .txt para uso, inserindo o título adequado. 

Dentre as possibilidades que as normas da ABNT permitiam (na última versão isso foi alterado), era o uso de underline (___) para indicar que é o mesmo autor da linha acima. Por esse motivo inserimos essa regra no script, todavia, em alguns casos, que ainda não identificamos o porquê, os dados não são extraídos corretamente. 

Algumas abreviações de nomes de universidades em maiúscula como PUC, UPF, por exemplo, podem ser importados às vezes como se fossem nomes de autorias. Estamos trabalhando em criar dicionários de palavras que devem ser excluídas.

Caso as referencias bibliográficas contenham número ou marcadores como - ou >, o nome do autor não será extraído. Indicado editar o .txt nesse caso.

Em casos de sobrenomes que tem maiúsculas e minúsculas juntas, como MacRAE e casos em que o sobrenome possua hífen ao meio também podem gerar problemas de extração. Possível editar também.

Sobrenomes com trema também estão tendo problemas de mineração.

Na tabela final em formato .csv é importante retirar os pontos finais e os ponto e vírgulas para não gerar problemas na importação para o Gephi.







