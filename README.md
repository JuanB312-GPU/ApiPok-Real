# ApiPok-Real

Esta API ofrece funcionalidades para calcular el Índice de Masa Corporal (BMI) de los Pokémon y proporciona un escalado de su salud en términos de masa, similar al criterio humano. Adicionalmente, permite convertir el precio de un elemento del juego expresado en yenes a otras monedas populares como dólares, pesos colombianos y euros.

## Funcionalidades

1. **Cálculo del BMI de Pokémon**  
   - La API toma como entrada el nombre de un Pokémon para calcular su BMI.
   - Obtiene peso y altura, de la API pública "PokéApi" y conversiona las unidades al sistema internacional.
   - Con base en este índice, el estado de salud del Pokémon es categorizado en niveles similares a los utilizados para humanos (bajo peso, peso normal, sobrepeso, obesidad).
   - Permite entender la relación de masa en términos aproximados de salud humana.

2. **Conversión de Moneda**  
   - La API toma como entrada el nombre de un item del juego.
   - Según la wiki del juego en japón los precios de los items vienen dados por Yenes, así que los consulta de la api pública "PokéApi".
   - Obtiene el precio de un elemento de Pokémon en yenes y lo convierte a otras monedas: 
     - **USD (Dólar estadounidense)**
     - **COP (Peso colombiano)**
     - **EUR (Euro)**
   - Esta funcionalidad es útil para comparar costos de elementos dentro del juego con valores reales en diferentes monedas.

## Instrucciones para Clonar el Repositorio

Para clonar este repositorio en tu máquina local, sigue los siguientes pasos:

1. **Instalar Git**  
   Asegurarse de poseer Git, recomendado versión mas reciente.

2. **Abrir la Terminal o Símbolo del Sistema**  
   Abre la terminal (Linux/Mac) o el símbolo del sistema (Windows).

3. **Navegar a la Carpeta Deseada**  
   Usa el comando `cd` para llegar a la carpeta donde deseas clonar el repositorio. Por ejemplo:
   ```bash
   cd ruta/a/tu/carpeta
   ```
4. **Ejecutar los siguentes comandos para clonar a la carpeta**
   - Reemplazar por la URL, en cuestión:
   ```bash
   git clone URL_DEL_REPOSITORIO
   ```
   - Acceda a la carpeta creada, con el nombre del repositorio:
   ```bash
   cd nombre_del_repositorio
   ```
Nota: **Recuerde que puede obtener el enlace en el mismo repositorio, abierto en el navegador, siguendo los pasos de: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository**

## Pasos para Instalar las Dependencias

Es recomendable utilizar un entorno virtual para gestionar las dependencias de tu proyecto. A continuación, se describen los pasos para crear un entorno virtual e instalar las dependencias.

### 1. Instalar `virtualenv` (si no lo tienes instalado)

Si aún no tienes `virtualenv` instalado, puedes instalarlo usando `pip`. Abre la terminal y ejecuta el siguiente comando:

```bash
pip install virtualenv
```

En el directorio de instalación de la API, ejecuta los siguentes comandos para crear el entorno virtual:

```bash
virtualenv venv
venv\Scripts\activate
```

### 2. Posteriormente instale los recursos de "flask" y "yfinance".

```bash
pip install flask
pip install yfinance
```

Nota: **Si desea asegurarse de la instalación ejecute el comando:**

```bash
pip list
```

## Endpoints

### `/weight_pokemon`
- **Método**: `POST`
- **Parámetros de Entrada**: `name` nombre del Pokémon. 
- **Descripción**: Calcula el BMI del Pokémon, y devuelve BMI, peso en kilogramos, altura en metros y su categoría de salud.

### `/price_item`
- **Método**: `POST`
- **Parámetros de Entrada**: `name` nombre del item, ya sea de la serie o del juego. 
- **Descripción**: Convierte el valor en yenes a USD, COP y EUR, devuelve los precios en cada divisa.

## Ejemplos de Uso

### Ejemplo para Cálculo de BMI

```json
POST /weight_pokemon
{
  "name": pikachu
}
```
### Ejemplo para conversión de precio de item

```json
POST /price_item
{
  "name": poke-ball
}
```
