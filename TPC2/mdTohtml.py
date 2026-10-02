import re

texto_ = "# TPC1: String binária sem ocorrências de '011'"
er = re.compile(r'(?P<Tag>#+)(?P<Titulo>.*)')
#print(er.search((texto_)))
#print(er.search(texto_).group('Tag'))
#print(er.search(texto_).group('Titulo'))
#print(er.search(texto_).groupdict())
print(er.split(texto_,))

tag = er.search(texto_).group('Tag')
print(tag)


tagdict = {
    "#" : "h1",
    "##" : "h2",
    "###": "h3",
    "**" : "b",
    "*" : "i",
}

def mdTOhtml(texto):
    er1 = re.compile(r'(?P<Tag>[#\*]+)\s*(?P<Conteudo>(.[^\*])*)\s*(?P<teste>[#\*]*)$')
    tag = er1.search(texto).group('Tag')
    tag2 = er1.search(texto).group('teste')
    conteudo = er1.search(texto).group('Conteudo')
    if tag in tagdict:
        tag = tagdict[tag]
    if tag2 in tagdict:
        tag2 = tagdict[tag2]

    if tag2 :
        htmltext = "<" + tag + ">" + conteudo + "</" + tag2 + ">"
    else:
        htmltext = "<" + tag + ">" + conteudo + "</" + tag + ">"

    print(htmltext)

mdTOhtml("# TPC1: String binária sem ocorrências de '011'")
mdTOhtml("** texto em negrito **")
mdTOhtml("### TPC1: String binária sem ocorrências de '011'")

