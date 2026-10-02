import re

dict = {
    "#" : ("<h1>","</h1>"),
    "##" : ("<h2>","</h2>"),
    "###" : ("<h3>","</h3>"),
    "**" : ("<b>","</b>"),
    "*" : ("<i>","</i>"),
    "1." : ("<ol>\n   <li>","</li>"),
    "2." : ("   <li>","</li>"),
    "3." : ("   <li>","</li>\n</ol>"),
}

texto = """1. Primeiro item 
2. Segundo item 
3. Terceiro item

# O Princepezinho
## Primeiro Capitulo
### Era uma vez...

[link para o google] (google.com)

![imagem de aluno](uminho.com)

*Italico*

** BOLD **
"""


def aux(elem):
    chave = elem.group(1)   
    conteudo = elem.group(2)

    if chave == "**":
        conteudo = conteudo[:-2]

    elif chave == "*":
        conteudo = conteudo[:-1]

    elif chave == "[":
        match = re.match(r'(.*?)\]\s*\((.*?)\)', conteudo)

        texto_link = match.group(1)
        url = match.group(2)

        return '<a href="' + url + '">' + texto_link + '</a>'
    
    elif chave == "![":
        match = re.match(r'(.*?)\]\s*\((.*?)\)', conteudo)

        alt = match.group(1)
        src = match.group(2)

        return '<img src="' + src + '" alt="' + alt + '">'

    inicio = dict[chave][0]
    fim = dict[chave][1]

    return inicio + conteudo + fim


def mdTOhtml(text):
    er = re.compile(r'(!\[|\[|\d\.|[#\*]+)\s*(.*)')
    resultado = er.sub(aux, text)
    print(resultado)

mdTOhtml(texto)
