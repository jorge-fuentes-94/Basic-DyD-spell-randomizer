🎲 D&D 5th Edition Spell Randomizer

Una herramienta interactiva desarrollada en Python para generar hechizos aleatorios de D&D 5e, perfecta para DMs que buscan inspiración rápida y jugadores explorando nuevas opciones mágicas.






































📋 Descripción

El D&D 5th Edition Spell Randomizer es una aplicación de consola que utiliza la API oficial de D&D 5e para generar hechizos aleatorios con filtros personalizables. Diseñada especialmente para Dungeon Masters y jugadores que buscan inspiración mágica, variedad en sus personajes, o simplemente quieren explorar el vasto repertorio de hechizos de D&D de manera divertida.

🎯 Objetivos del Proyecto

•
Demostrar integración con APIs externas de manera práctica y funcional

•
Resolver un problema real de la comunidad de juegos de rol

•
Combinar pasión personal (D&D) con competencias técnicas (Python)

•
Crear una herramienta útil para la comunidad de jugadores

•
Mostrar creatividad en la aplicación de tecnología a hobbies

✨ Características

🔧 Funcionalidades Principales

•
🎲 Generación Aleatoria: Obtiene hechizos aleatorios de la API de D&D 5e

•
🔍 Filtros Avanzados: Filtra por nivel, escuela de magia, clase, y más

•
📊 Información Completa: Muestra descripción, componentes, tiempo de lanzamiento

•
⚡ Respuesta Rápida: Integración eficiente con la API oficial

•
🎮 Interfaz Intuitiva: Menú fácil de usar para DMs en sesiones activas

•
📝 Exportación: Guarda hechizos favoritos para referencia futura

🏗️ Características Técnicas

•
API Integration: Consumo de REST API con manejo de errores

•
Data Processing: Procesamiento y formateo de datos JSON

•
Error Handling: Gestión robusta de errores de red y API

•
Caching: Cache local para mejorar rendimiento

•
Modular Design: Código organizado y reutilizable

🚀 Instalación y Uso

Prerrequisitos

•
Python 3.8 o superior

•
Conexión a internet (para acceder a la API de D&D 5e)

•
Biblioteca requests para llamadas HTTP

Instalación

1.
Clonar el repositorio

2.
Instalar dependencias

3.
Ejecutar la aplicación

Uso Básico

Generar Hechizo Aleatorio Simple

Bash


$ python spell_randomizer.py

🧙‍♂️ D&D 5e Spell Randomizer
═══════════════════════════════

🎲 Generando hechizo aleatorio...

✨ FIREBALL ✨
Nivel: 3rd
Escuela: Evocation
Tiempo de Lanzamiento: 1 action
Rango: 150 feet
Componentes: V, S, M (a tiny ball of bat guano and sulfur)
Duración: Instantaneous

📜 Descripción:
A bright streak flashes from your pointing finger to a point you choose 
within range and then blossoms with a low roar into an explosion of flame...

🎯 Clases que pueden usarlo: Sorcerer, Wizard


Uso con Filtros

Bash


# Hechizos de nivel 1 solamente
python spell_randomizer.py --level 1

# Hechizos de la escuela de Evocation
python spell_randomizer.py --school evocation

# Hechizos para Wizard de nivel 3 o menor
python spell_randomizer.py --class wizard --max-level 3


🏗️ Arquitectura del Proyecto

Estructura de Archivos

Plain Text


Basic-DyD-spell-randomizer/
├── spell_randomizer.py       # Aplicación principal
├── api_client.py            # Cliente para D&D 5e API
├── spell_formatter.py       # Formateo de datos de hechizos
├── cache_manager.py         # Gestión de cache local
├── config.py               # Configuración de la aplicación
├── requirements.txt        # Dependencias del proyecto
├── README.md              # Documentación
└── data/
    ├── spell_cache.json   # Cache de hechizos (generado)
    └── favorites.json     # Hechizos favoritos del usuario


Componentes Principales

🌐 Cliente de API (api_client.py)

Python


class DnDAPIClient:
    """
    Cliente para interactuar con la API oficial de D&D 5e.
    
    Attributes:
        base_url (str): URL base de la API
        session (requests.Session): Sesión HTTP reutilizable
        cache (dict): Cache local de respuestas
    """
    
    BASE_URL = "https://www.dnd5eapi.co/api"
    
    def __init__(self):
        self.session = requests.Session()
        self.cache = {}
    
    def get_all_spells(self):
        """Obtiene la lista completa de hechizos disponibles."""
        
    def get_spell_details(self, spell_index):
        """Obtiene detalles completos de un hechizo específico."""
        
    def get_random_spell(self, filters=None):
        """Genera un hechizo aleatorio con filtros opcionales."""


✨ Formateador de Hechizos (spell_formatter.py)

Python


class SpellFormatter:
    """
    Formatea la información de hechizos para presentación.
    """
    
    @staticmethod
    def format_spell_display(spell_data):
        """
        Formatea un hechizo para mostrar en consola.
        
        Args:
            spell_data (dict): Datos del hechizo desde la API
            
        Returns:
            str: Hechizo formateado para display
        """
        
    @staticmethod
    def format_spell_summary(spell_data):
        """Crea un resumen conciso del hechizo."""
        
    @staticmethod
    def format_components(components):
        """Formatea los componentes del hechizo (V, S, M)."""


🎲 Generador Principal (spell_randomizer.py)

Python


class SpellRandomizer:
    """
    Clase principal para la generación de hechizos aleatorios.
    """
    
    def __init__(self):
        self.api_client = DnDAPIClient()
        self.formatter = SpellFormatter()
        self.cache_manager = CacheManager()
    
    def generate_random_spell(self, **filters):
        """
        Genera un hechizo aleatorio con filtros opcionales.
        
        Args:
            **filters: Filtros como level, school, class, etc.
            
        Returns:
            dict: Datos del hechizo seleccionado
        """
        
    def interactive_mode(self):
        """Modo interactivo con menú de opciones."""
        
    def batch_generate(self, count=5):
        """Genera múltiples hechizos aleatorios."""


🎮 Casos de Uso Prácticos

Para Dungeon Masters

Caso 1: Inspiración Rápida en Sesión

Python


# Durante una sesión, necesitas un hechizo para un NPC mago
randomizer = SpellRandomizer()

# Hechizo de nivel apropiado para el encuentro
spell = randomizer.generate_random_spell(
    level=3,
    school="evocation"  # Para un mago combativo
)

print(f"El mago enemigo lanza: {spell['name']}")


Caso 2: Creación de NPCs

Python


# Crear un mago NPC con hechizos temáticos
wizard_spells = []

for level in range(1, 4):  # Mago de nivel 5
    spell = randomizer.generate_random_spell(
        level=level,
        class="wizard"
    )
    wizard_spells.append(spell)

print("Hechizos del NPC Mago:")
for spell in wizard_spells:
    print(f"- {spell['name']} (Nivel {spell['level']})")


Para Jugadores

Caso 3: Exploración de Opciones

Python


# Jugador explorando hechizos para su próximo nivel
sorcerer_options = []

for _ in range(10):  # 10 opciones aleatorias
    spell = randomizer.generate_random_spell(
        level=2,
        class="sorcerer"
    )
    sorcerer_options.append(spell)

# Mostrar opciones para que el jugador elija
for i, spell in enumerate(sorcerer_options, 1):
    print(f"{i}. {spell['name']} - {spell['school']}")


Caso 4: Desafío de Roleplay

Python


# Generar hechizo aleatorio para roleplay creativo
mystery_spell = randomizer.generate_random_spell()

print(f"Tu personaje encuentra un pergamino con: {mystery_spell['name']}")
print("¿Cómo reacciona tu personaje a este hechizo desconocido?")


🔧 Funcionalidades Avanzadas

Sistema de Filtros

Python


# Filtros disponibles
filters = {
    'level': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],  # Nivel del hechizo
    'school': [
        'abjuration', 'conjuration', 'divination', 
        'enchantment', 'evocation', 'illusion', 
        'necromancy', 'transmutation'
    ],
    'class': [
        'bard', 'cleric', 'druid', 'paladin', 
        'ranger', 'sorcerer', 'warlock', 'wizard'
    ],
    'ritual': [True, False],  # Si es ritual
    'concentration': [True, False],  # Si requiere concentración
    'casting_time': ['action', 'bonus_action', 'reaction', 'minute', 'hour']
}

# Ejemplo de uso avanzado
spell = randomizer.generate_random_spell(
    level=2,
    school='enchantment',
    class='bard',
    ritual=False,
    concentration=True
)


Cache Inteligente

Python


class CacheManager:
    """Gestiona el cache local para mejorar rendimiento."""
    
    def __init__(self, cache_file="data/spell_cache.json"):
        self.cache_file = cache_file
        self.cache = self.load_cache()
    
    def get_cached_spell(self, spell_index):
        """Obtiene hechizo del cache si existe."""
        
    def cache_spell(self, spell_index, spell_data):
        """Guarda hechizo en cache."""
        
    def is_cache_expired(self, timestamp, hours=24):
        """Verifica si el cache ha expirado."""


Exportación y Favoritos

Python


class FavoritesManager:
    """Gestiona hechizos favoritos del usuario."""
    
    def add_favorite(self, spell_data):
        """Añade hechizo a favoritos."""
        
    def remove_favorite(self, spell_name):
        """Remueve hechizo de favoritos."""
        
    def export_favorites(self, format='json'):
        """Exporta favoritos en diferentes formatos."""
        
    def import_spell_list(self, file_path):
        """Importa lista de hechizos desde archivo."""


📊 Integración con D&D 5e API

Endpoints Utilizados

EndpointPropósitoEjemplo/spellsLista todos los hechizosGET /api/spells/spells/{index}Detalles de hechizo específicoGET /api/spells/fireball/magic-schoolsEscuelas de magiaGET /api/magic-schools/classesClases de personajeGET /api/classes

Manejo de Respuestas

Python


def handle_api_response(response):
    """
    Maneja respuestas de la API con error handling robusto.
    
    Args:
        response (requests.Response): Respuesta HTTP
        
    Returns:
        dict: Datos procesados o None si hay error
    """
    try:
        if response.status_code == 200:
            return response.json()
        elif response.status_code == 404:
            print("❌ Hechizo no encontrado")
            return None
        elif response.status_code == 429:
            print("⏳ Límite de API alcanzado, esperando...")
            time.sleep(1)
            return None
        else:
            print(f"❌ Error de API: {response.status_code}")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Error de conexión: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ Error procesando respuesta: {e}")
        return None


🎯 Valor para la Comunidad D&D

Problemas que Resuelve

Para DMs

•
Inspiración rápida durante sesiones activas

•
Variedad en NPCs magos con hechizos únicos

•
Preparación eficiente de encuentros mágicos

•
Exploración del contenido oficial de D&D

Para Jugadores

•
Descubrimiento de hechizos menos conocidos

•
Planificación de personajes con opciones variadas

•
Roleplay creativo con hechizos inesperados

•
Aprendizaje del sistema de magia de D&D

Casos de Uso Reales

Sesión de Juego Típica

Plain Text


DM: "El mago enemigo prepara un hechizo..."
[Ejecuta randomizer con filtros apropiados]
DM: "Lanza Hypnotic Pattern! Todos hagan salvación de Sabiduría"
Jugadores: "¡Wow, no esperábamos ese hechizo!"


Creación de Personaje

Plain Text


Jugador: "Quiero un hechicero único, no los hechizos típicos"
[Usa randomizer para generar lista de opciones]
Jugador: "¡Chromatic Orb! Nunca había considerado ese hechizo"


🧪 Testing y Validación

Tests de Funcionalidad

Python


import unittest
from spell_randomizer import SpellRandomizer

class TestSpellRandomizer(unittest.TestCase):
    
    def setUp(self):
        self.randomizer = SpellRandomizer()
    
    def test_api_connection(self):
        """Verifica conexión con la API."""
        spells = self.randomizer.api_client.get_all_spells()
        self.assertIsNotNone(spells)
        self.assertGreater(len(spells['results']), 0)
    
    def test_spell_generation(self):
        """Verifica generación de hechizos aleatorios."""
        spell = self.randomizer.generate_random_spell()
        self.assertIsNotNone(spell)
        self.assertIn('name', spell)
        self.assertIn('level', spell)
    
    def test_filters(self):
        """Verifica funcionamiento de filtros."""
        spell = self.randomizer.generate_random_spell(level=1)
        self.assertEqual(spell['level'], 1)


Validación con la Comunidad

•
Beta testing con grupos de D&D locales

•
Feedback de DMs experimentados

•
Validación de utilidad en sesiones reales

•
Mejoras iterativas basadas en uso real

🔮 Futuras Mejoras

Funcionalidades Planificadas




Interfaz Gráfica: GUI con tkinter para uso más intuitivo




Bot de Discord: Integración para usar en servidores de D&D




Filtros Avanzados: Por componentes, duración, rango




Listas Personalizadas: Crear y compartir listas temáticas




Integración Roll20: Plugin para plataformas de juego online




Modo Campaña: Seguimiento de hechizos usados por sesión




Generador de NPCs: Crear magos completos con trasfondos




Estadísticas: Análisis de hechizos más/menos usados

Mejoras Técnicas




Base de Datos Local: SQLite para mejor rendimiento




API Propia: Servicio web para múltiples clientes




Sincronización: Backup en la nube de favoritos




Offline Mode: Funcionamiento sin conexión




Internacionalización: Soporte para múltiples idiomas




Performance: Optimización de llamadas a API




Testing: Suite completa de tests automatizados




Documentación: API docs y guías de usuario

🛠️ Tecnologías Utilizadas

TecnologíaVersiónPropósitoPython3.8+Lenguaje de programaciónRequests2.28+Cliente HTTP para APIJSONEstándarProcesamiento de datosD&D 5e APIv1Fuente de datos de hechizosArgparseEstándarInterfaz de línea de comandos

🎯 Habilidades Demostradas

Competencias Técnicas

•
API Integration: Consumo de APIs REST externas

•
Data Processing: Manipulación y formateo de JSON

•
Error Handling: Gestión robusta de errores de red

•
Caching: Optimización de rendimiento con cache local

•
CLI Design: Interfaces de línea de comandos intuitivas

•
Modular Programming: Código organizado y reutilizable

Competencias Creativas

•
Problem Solving: Identificación y solución de problemas reales

•
User Experience: Diseño centrado en el usuario final

•
Community Focus: Desarrollo para una comunidad específica

•
Creative Application: Uso creativo de tecnología en hobbies

•
Domain Knowledge: Comprensión profunda del dominio (D&D)

🌟 Conexión con La Guarida de Jorge

Este proyecto forma parte del ecosistema de La Guarida de Jorge, donde la pasión por los juegos de rol se encuentra con la tecnología:

Integración con Contenido

•
Videos explicativos en YouTube sobre el uso de la herramienta

•
Streams en Twitch usando el randomizer en sesiones en vivo

•
TikToks creativos mostrando hechizos aleatorios generados

•
Comunidad Discord para feedback y sugerencias

Eventos y Colaboraciones

•
TechRol 2024: Presentación de la herramienta en el evento

•
Sesiones públicas: Uso en partidas transmitidas

•
Colaboraciones: Con otros creadores de contenido de D&D

•
Workshops: Enseñanza de programación aplicada a D&D

👨‍💻 Autor

Jorge Fuentes Jiménez

•
GitHub: @jorge-fuentes-94

•
LinkedIn: Jorge Fuentes Jiménez

•
La Guarida de Jorge:

•
TikTok

•
YouTube

•
Instagram



•
Email: jf7494@gmail.com

Experiencia en D&D

•
15+ años como Dungeon Master

•
Organizador de TechRol 2024 (evento tech + rol)

•
Creador de contenido en múltiples plataformas

•
Gestor de comunidad en Discord y redes sociales

📄 Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo LICENSE para más detalles.

🤝 Contribuciones

¡Las contribuciones de la comunidad D&D y programadores son muy bienvenidas!

Cómo Contribuir

1.
Fork el proyecto

2.
Crea una rama para tu feature (git checkout -b feature/NuevaFuncionalidad)

3.
Commit tus cambios (git commit -m 'Añadir nueva funcionalidad')

4.
Push a la rama (git push origin feature/NuevaFuncionalidad)

5.
Abre un Pull Request

Ideas de Contribución

•
Nuevos filtros para hechizos

•
Mejoras en la interfaz de usuario

•
Optimizaciones de rendimiento

•
Tests adicionales

•
Documentación mejorada

•
Traducciones a otros idiomas

📞 Soporte y Comunidad

Soporte Técnico

•
Issues: GitHub Issues

•
Email: jf7494@gmail.com

•
Discord: La Guarida de Jorge

Comunidad D&D

•
Feedback: Comparte tu experiencia usando la herramienta

•
Sugerencias: Ideas para nuevas funcionalidades

•
Casos de uso: Cómo usas el randomizer en tus partidas

•
Colaboraciones: Proyectos relacionados con D&D + Tech





⭐ ¡Si esta herramienta mejora tus sesiones de D&D, no olvides darle una estrella! ⭐

🎲 ¡Que tengas excelentes aventuras mágicas! 🎲

