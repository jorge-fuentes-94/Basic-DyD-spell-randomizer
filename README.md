# D&D 5e Spell Randomizer

Script de consola que saca un conjuro aleatorio de D&D 5e usando la [D&D 5e API](https://www.dnd5eapi.co/). Lo hice para practicar llamadas a APIs con la biblioteca estándar de Python (`urllib` y `json`).

## Cómo funciona

1. Pregunta si quieres filtrar por escuela de magia y por nivel (0–9); se pueden dejar en blanco.
2. Pide a la API la lista de conjuros con esos filtros.
3. Elige uno al azar, pide su ficha y muestra nombre, nivel, escuela y descripción.

## Cómo probarlo

No necesita instalar nada:

```bash
python spellrandomizer.py
```

## Limitaciones

- La API devuelve los textos en inglés.
- No valida la entrada: una escuela o un nivel mal escritos dan una lista vacía y el script falla.
- El número aleatorio va de 0 a `count`, así que de vez en cuando elige una posición fuera de la lista.
