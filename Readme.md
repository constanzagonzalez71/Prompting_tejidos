# POC – Fast Prompting para patrones de tejido

**Autora:** Constanza Nidia González  
**Curso/Comisión:** Inteligencia Artificial – Generación de Prompts – 84180  
**Proyecto:** Diseño asistido por IA para la creación de patrones de tejido en diferentes talles  

---

## 🎯 Introducción
Este proyecto demuestra cómo las técnicas de **Fast Prompting** (Zero-shot, One-shot y Few-shot) pueden aplicarse para **automatizar la generación de patrones de tejido adaptables a distintos talles y grosores de lana**.  

Se vincula con mi emprendimiento de cursos y proyectos tejidos, donde la adaptación de patrones a distintos talles representa un desafío constante en tiempo y complejidad técnica.

---

## 🚩 Problema
En el diseño y confección de prendas tejidas, adaptar un patrón a diferentes talles y grosores de hilo requiere:  
- Cálculos complejos y conocimientos técnicos avanzados.  
- Tiempo considerable para ajustar puntos, vueltas y medidas.  
- Guías claras para estudiantes y clientes.  

**Problema central:**  
¿Cómo aprovechar la inteligencia artificial para automatizar la generación de patrones de tejido en distintos talles y grosores de lana, reduciendo el tiempo de diseño y mejorando la accesibilidad para tejedores y alumnos?

---

## 💡 Propuesta de solución
Se utilizarán **modelos de IA generativos (texto–texto y texto–imagen)** para crear una herramienta que asista en el diseño de prendas personalizadas.

### a) Texto–texto
- Transformar muestras de tejido en patrones detallados para distintos talles.  
- Crear instrucciones paso a paso adaptadas a cada prenda (suéteres, chalecos, enteritos, etc.).  
- Generar automáticamente **tablas de talles** con distribución de puntos y vueltas.

### Tabla de talles de ejemplo

| Talle | Largo delantero (cm) | Largo espalda (cm) | Sisa (cm) | Puntos iniciales |
|-------|--------------------|------------------|-----------|----------------|
| 2     | 20                 | 20               | 16        | 44             |
| 4     | 22                 | 22               | 17        | 48             |
| 6     | 24                 | 24               | 18        | 52             |

---

## ✅ Prompts por técnica de Fast Prompting

### Zero-shot
```text
Genera un patrón para un suéter tejido en talle 4 y talle 6, usando lana grosor 8/6 y agujas nº 5.
Incluye cantidad de puntos iniciales, distribución en delantero y espalda, sisa y cuello, 
aclarando diferencias de puntos entre talles.

### Few-shot
```text
Patrón de ejemplo: Suéter talle 2, lana semigruesa, agujas 5.
Puntos iniciales: 44
Distribución: Delantero 22 puntos, espalda 22 puntos
Sisa: 16 cm
Cuello: 4 cm
Ahora genera el mismo patrón para talle 4 y 6.

Genera una ilustración estilo esquema textil de un suéter infantil talle 6 en dos colores 
(mostaza y celeste pastel), mostrando vista frontal y trasera con detalles en punto Santa Clara y Jersey.

✅ Objetivos
Objetivo general

Automatizar la creación de patrones de tejido adaptables mediante técnicas de Fast Prompting.

Objetivos específicos

Aplicar Zero-shot, One-shot y Few-shot prompting para generar patrones de tejido.

Construir prompts texto–imagen para acompañar los patrones.

Estimar costos de implementación y optimizar número de llamadas a la API.

Evaluar la mejora de la solución frente a la entrega anterior.

🛠️ Metodología

Definir contexto: muestra, talles, tipo de prenda.

Experimentar con técnicas de Fast Prompting: Zero-shot, One-shot, Few-shot.

Construir prompts para diagramas (texto–imagen).

Estimar tokens y costos de llamadas a la API.

Comparar resultados y analizar la claridad y precisión de los patrones generados.

🔧 Herramientas y tecnologías

Python 3.10 y GOOGLE_API



Técnicas de prompting: Zero-shot, One-shot, Few-shot

Librerías opcionales: Pandas, Matplotlib/Seaborn (visualización de tablas de talles)

🔍 Conclusión

Al finalizar, el proyecto permitirá generar patrones de tejido adaptables a distintos talles, acompañados de diagramas de referencia, optimizando tiempo de diseño y mejorando la experiencia de alumnos y clientes.

Instagram del emprendimiento: @amigurumisbyconi