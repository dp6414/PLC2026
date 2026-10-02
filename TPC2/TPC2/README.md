# TPC2

## Autor: 
David José Monteiro Andrade Gonçalves; a100113;

![Foto](./foto.png)

## Resumo: 
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da Cheat Sheet:

### Cabeçalhos: linhas iniciadas por "# texto", ou "## texto" ou "### texto"

In: `# Exemplo`

Out: `<h1>Exemplo</h1>`

### Bold: pedaços de texto entre "**":

In: `Este é um **exemplo** ...`

Out: `Este é um <b>exemplo</b> ...`

### Itálico: pedaços de texto entre "*":

In: `Este é um *exemplo* ...`

Out: `Este é um <i>exemplo</i> ...`

### Lista numerada:

In:
```
1. Primeiro item
2. Segundo item
3. Terceiro item
```

Out:
```
<ol>
<li>Primeiro item</li>
<li>Segundo item</li>
<li>Terceiro item</li>
</ol>
```

### Link: [texto](endereço URL)

In: `Como pode ser consultado em [página da UC](http://www.uc.pt)`

Out: `Como pode ser consultado em <a href="http://www.uc.pt">página da UC</a>`

### Imagem: ![texto alternativo](path para a imagem)

In: Como se vê na imagem seguinte: `![imagem dum coelho](http://www.coellho.com) ...`

Out: `Como se vê na imagem seguinte: <img src="http://www.coellho.com" alt="imagem dum coelho"/> ...`

## Resultados: 
Inicialmente comecei por fazer o `mdTOhtml.py` para testar os casos em que apareciam as tags `#` e `*`. Mas depois ao tentar fazer para as listas ordenadas, apercebi-me que não ia cheagr a lado nenhum, fazendo então o `tpc2.py` onde utilizo a função `sub` com a `aux` para fazer as conversões. Na parte dos links e imagem tive que voltar a utilizar outra expressão regular para caputar a `href,link,scr,alt` para depois conseguir converter. No final apercebi-me que no dicionário não era necessário ter as tags destes últimos que referi porque não estavam a fazer nada.
A solução está então no ficheiro `tpc2.py`.