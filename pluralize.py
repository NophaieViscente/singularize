import re
import unidecode

def pluralize (original_text:str) -> str :

    # Dict that contains the exceptions at the pluralize.
    exceptions = { 
    'males' : 'mal',
    'consules' : 'consul',
    'meis' : 'mel',
    'feis' : 'fel',
    'cais' : 'cal',
    }

    #Remove acentos e deixa tudo minuscula
    word_to_make_plural = unidecode.unidecode(original_text.strip()).lower()

    for plural,word in exceptions.items() :
        if word == word_to_make_plural :
            return plural
    
    # Palavras terminadas em ['a','e','i','o','u','ae'] que apenas recebem 's'
    if re.match(r"^([a-zA-Z]*)(a|e|i|o|u|ae)$",word_to_make_plural) is not None:
        word_with_plural = re.sub(r"^([a-zA-Z]*)(a|e|i|o|u|ae)$",r"\1\2s",word_to_make_plural)
        return word_with_plural

    # Palavras terminadas em ['r', 'z', 'n', 'as'] que recebem 'es'
    if re.match(r"^([a-zA-Z]*)(r|z|n|as)$",word_to_make_plural) is not None:
        word_with_plural = re.sub(r"^([a-zA-Z]*)(r|z|n|as)$",r"\1\2es",word_to_make_plural)
        return word_with_plural
    
    # Palavras terminadas em 'al' que recebem 'ais'
    if re.match(r"^([a-zA-Z]*)al$",word_to_make_plural) is not None :
        word_with_plural = re.sub(r"^([a-zA-Z]*)al$",r"\1ais",word_to_make_plural)
        return word_with_plural
    
    # Palavras terminadas em 'el' que recebem 'eis'
    if re.match(r"^([a-zA-Z]*)el$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)el$",r"\1eis",word_to_make_plural)
        return word_with_plural
    
    # Palavras terminadas em 'ol' que recebem 'ois'
    if re.match(r"^([a-zA-Z]*)ol$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)ol$",r"\1ois",word_to_make_plural)
        return word_with_plural

    # Palavras terminadas em 'ul' que recebem 'uis'
    if re.match(r"^([a-zA-Z]*)ul$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)ul$",r"\1uis",word_to_make_plural)
        return word_with_plural

    # Palavras terminadas em 'il' que recebem 'is'
    if re.match(r"^([a-zA-Z]*)il$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)il$",r"\1is",word_to_make_plural)
        return word_with_plural
    
    # Palavras terminadas em 'm' que recebem 'ns'
    if re.match(r"^([a-zA-Z]*)m$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)m$",r"\1ns",word_to_make_plural)
        return word_with_plural
    
    # Palavras terminadas em 'es' que recebem 'eses'
    if re.match(r"^([a-zA-Z]*)es$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)es$",r"\1eses",word_to_make_plural)
        return word_with_plural
    
    # Palavras terminadas em 'ao' que recebem 'oes'
    if re.match(r"^([a-zA-Z]*)ao$",word_to_make_plural) :
        word_with_plural = re.sub(r"^([a-zA-Z]*)ao$",r"\1oes",word_to_make_plural)
        return word_with_plural
    
    return word_to_make_plural