# Corretor-XML
Corretor de Procedimentos TISS XML que detecta procedimentos com prefixo incorreto (19 ou 20) quando codigoTabela = 00 e corrige automaticamente.
<br>
Esse programa foi feito para ajudar na execução de uma tarefa que antes era feita manualmente de tirar os erros de um arquivo XML na Unimed Lorena.
<br>
<br>
O código lê um arquivo .xml e identifica os campos de código de tabela e código de procedimento, se o código da tabela for 00 ele verifica a linha abaixo para ver se o erro existe, o erro é caso o código do procedimento venha com um 19 ou 20 no começo do código que não deveria vir, caso o erro exista o programa tira esse prefixo e corrige o arquivo.
<br>
<br>
Versão 1.0: Programa totalmente funcional com funcionalidade de selecionar arquivo e onde salvar, mostra os erros encontrados e pede confirmação tudo pelo terminal.
<br>
<br>
Versão 2.0: Adição de uma interfaçe gráfica usando tkinter e tranformação do programa em um aplicativo executável(utilizei o copilot para me auxiliar a fazer isso já que não tinha noção sobre como transformar um código python em executavel .exe).

