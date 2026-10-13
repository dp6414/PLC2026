# TPC3

## Autor: 
David José Monteiro Andrade Gonçalves; a100113;

![Foto](./foto.png)

## Resumo: 
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do
género:

```sql
# DBPedia: obras de Chuck Berry
select ?nome ?desc where {
    ?s a dbo:MusicalArtist.
    ?s foaf:name "Chuck Berry"@en .
    ?w dbo:artist ?s.
    ?w foaf:name ?nome.
    ?w dbo:abstract ?desc
} LIMIT 1000
```
Tokens e outros:
O caráter '#' marca o início de um comentário que se prolonga até ao fim da linha e deve ser
ignorado;
O caráter '?' marca o início de um identificador de uma variável que se prolonga até ao primeiro
caráter não alfanumérico;
O caráter '@' marca o início de um identificador de língua que terá mais 2 carateres;
Qualquer sequência entre aspas é um valor do tipo string;
As outras sequências de alfanuméricos são identificadores de conceitos;
Os carateres '{}.' são delimitadores;
'LIMIT' é uma palavra reservada;
'1000' é um valor numérico.


## Resultados: 
Comecei por fazer o ficheiro json para depois através do 'gerador_analex.py' gerar o analisador léxico. NO tpc3.json, fiz então um id com o nome do tipo de cada token que queria capturar e a sua respetiva expressão regular. Depois gerei então o Analisador Léxico.


