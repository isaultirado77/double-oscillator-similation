# Sistema Masa-Resorte con Método de Euler-Cromer

Este proyecto simula el comportamiento de un sistema masa-resorte utilizando el **método de Euler-Cromer** para resolver las ecuaciones diferenciales del movimiento oscilatorio. El sistema consiste en una masa conectada a dos resortes idénticos fijados a paredes opuestas.

## Descripción del Proyecto

La simulación modela el movimiento de una masa de 0.03 kg bajo la influencia de dos resortes, cada uno con una constante de resorte de 4 N/m y una longitud en reposo de 0.5 m. La posición inicial de la masa se encuentra en el centro del sistema con una velocidad inicial hacia la derecha.

### Características
- Implementación del **método de Euler-Cromer** para resolver las ecuaciones del movimiento.
- Visualización del sistema en 3D utilizando **VPython**.
- Gráfica en tiempo real de la posición de la masa en función del tiempo.
- Código modular, fácil de leer y extender.

## Estructura del Código

### Clases Principales
1. **`Oscillator`**: Modela la física del sistema, incluyendo:
   - Cálculo de las fuerzas de los resortes.
   - Actualización de la posición y velocidad de la masa.

2. **`Simulation`**: Controla la simulación, incluyendo:
   - Creación de los elementos visuales (masa, resortes y paredes).
   - Ejecución del bucle de simulación.
   - Graficación de los resultados en tiempo real.

## Requisitos

Para ejecutar este proyecto, necesitas:
- Python 3.7 o superior.
- Librería VPython.

Puedes instalar VPython con:
```bash
pip install vpython
```

## Ejecución

1. Clona este repositorio:
```bash
git clone <URL-del-repositorio>
```
2. Navega al directorio del proyecto:
```bash
cd oscilador-armonico
```
3. Ejecuta el script principal:
```bash
python src/oscilador_armonico.py
```

## Resultados

La simulación produce:
- Una visualización 3D del sistema masa-resorte.
- Una gráfica de posición vs. tiempo.

### Ejemplo de Parámetros Iniciales
- Masa de la partícula: `0.03 kg`
- Constante del resorte: `4 N/m`
- Longitud en reposo: `0.5 m`
- Velocidad inicial: `12.5 m/s`
- Tiempo total de simulación: `1.5 s`
- Número de pasos: `1000`

El período de oscilación calculado es aproximadamente **0.38 segundos**, y se observa que este no depende de la amplitud del movimiento, validando la naturaleza armónica del sistema.
