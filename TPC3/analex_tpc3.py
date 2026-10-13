
import sys
import re

def tokenize(input_string):
    reconhecidos = []
    linha = 1
    mo = re.finditer(r'(?P<LIMIT>LIMIT)|(?P<VAR>\?[a-z]*)|(?P<ID_LINGUA>@[a-z]{2,})|(?P<ID_CONCEITOS>[A-Za-z0-9]+(:[A-Za-z0-9]+)?)|(?P<DELIMITADOR>\{*|\}*)|(?P<STRING>"[^"]*")|(?P<INT>\d*)|(?P<SKIP>[ \t])|(?P<NEWLINE>\n)|(?P<ERRO>.)', input_string)
    for m in mo:
        dic = m.groupdict()
        if dic['LIMIT']:
            t = ("LIMIT", dic['LIMIT'], linha, m.span())

        elif dic['VAR']:
            t = ("VAR", dic['VAR'], linha, m.span())
    
        elif dic['ID_LINGUA']:
            t = ("ID_LINGUA", dic['ID_LINGUA'], linha, m.span())
    
        elif dic['ID_CONCEITOS']:
            t = ("ID_CONCEITOS", dic['ID_CONCEITOS'], linha, m.span())
    
        elif dic['DELIMITADOR']:
            t = ("DELIMITADOR", dic['DELIMITADOR'], linha, m.span())
    
        elif dic['STRING']:
            t = ("STRING", dic['STRING'], linha, m.span())
    
        elif dic['INT']:
            t = ("INT", dic['INT'], linha, m.span())
    
        elif dic['SKIP']:
            t = ("SKIP", dic['SKIP'], linha, m.span())
    
        elif dic['NEWLINE']:
            t = ("NEWLINE", dic['NEWLINE'], linha, m.span())
    
        elif dic['ERRO']:
            t = ("ERRO", dic['ERRO'], linha, m.span())
    
        else:
            t = ("UNKNOWN", m.group(), linha, m.span())
        if not dic['SKIP'] and t[0] != 'UNKNOWN': reconhecidos.append(t)
    return reconhecidos

for linha in sys.stdin:
    for tok in tokenize(linha):
        print(tok)    

