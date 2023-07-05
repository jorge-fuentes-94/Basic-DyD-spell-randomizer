from urllib.request import urlopen
import json
import random

def apiCall (school, level):
    url =""
    if school != "" and level !="":
       url = "https://www.dnd5eapi.co/api/spells?Level="+level+"&school="+school
    elif school == "" and level !="":
        url ="https://www.dnd5eapi.co/api/spells?Level="+level
    elif school != "" and level =="":
        url = "https://www.dnd5eapi.co/api/spells?&school="+school
    elif school == "" and level == "":
        url = "https://www.dnd5eapi.co/api/spells"
    return url

def spellSort(random_number,spell_list):
    spell_url = spell_list["results"][random_number-1]["url"]
    return spell_url

def spellCall (spell_url):
    url = urlopen("https://www.dnd5eapi.co"+spell_url)
    spell_dict= json.loads(url.read())
    spell= f"""
    El hechizo que ha salido es {spell_dict["name"]}, que es un hechizo de nivel {spell_dict["level"]} de la escuela de {spell_dict["school"]["name"]}.
    
    {spell_dict["desc"]}.
    
    """
   
    
    return spell
    
school = input("¿Quieres que el hechizo sea de alguna escuela en concreto? En caso de que no dejalo en blanco. ")
level = input("¿Quieres que sean hechizos de algún nivel en concreto? Introduce un número del 0 al 9 y dejalo en blanco para todos. ")



response = urlopen(apiCall(school,level))
spell_list = json.loads(response.read())

random_number = random.randint(0,spell_list["count"])

spell_url = spellSort(random_number,spell_list)
spell = spellCall(spell_url)

print (spell)





