# ApiPok-Real

Esta API ofrece funcionalidades para calcular el �ndice de Masa Corporal (BMI) de los Pok�mon y proporciona un escalado de su salud en t�rminos de masa, similar al criterio humano. Adicionalmente, permite convertir el precio de un elemento del juego expresado en yenes a otras monedas populares como d�lares, pesos colombianos y euros.

## Funcionalidades

1. **C�lculo del BMI de Pok�mon**  
   - La API toma como entrada el nombre de un Pok�mon para calcular su BMI.
   - Obtiene peso y altura, de la API p�blica "Pok�Api" y conversiona las unidades al sistema internacional.
   - Con base en este �ndice, el estado de salud del Pok�mon es categorizado en niveles similares a los utilizados para humanos (bajo peso, peso normal, sobrepeso, obesidad).
   - Permite entender la relaci�n de masa en t�rminos aproximados de salud humana.

2. **Conversi�n de Moneda**  
   - La API toma como entrada el nombre de un item del juego.
   - Seg�n la wiki del juego en jap�n los precios de los items vienen dados por Yenes, as� que los consulta de la api p�blica "Pok�Api".
   - Obtiene el precio de un elemento de Pok�mon en yenes y lo convierte a otras monedas: 
     - **USD (D�lar estadounidense)**
     - **COP (Peso colombiano)**
     - **EUR (Euro)**
   - Esta funcionalidad es �til para comparar costos de elementos dentro del juego con valores reales en diferentes monedas.

## Instrucciones para Clonar el Repositorio

Para clonar este repositorio en tu m�quina local, sigue los siguientes pasos:

1. **Instalar Git**  
   Asegurarse de poseer Git, recomendado versi�n mas reciente.

2. **Abrir la Terminal o S�mbolo del Sistema**  
   Abre la terminal (Linux/Mac) o el s�mbolo del sistema (Windows).

3. **Navegar a la Carpeta Deseada**  
   Usa el comando `cd` para llegar a la carpeta donde deseas clonar el repositorio. Por ejemplo:
   ```bash
   cd ruta/a/tu/carpeta
   ```
4. **Ejecutar los siguentes comandos para clonar a la carpeta**
   - Reemplazar por la URL, en cuesti�n:
   ```bash
   git clone URL_DEL_REPOSITORIO
   ```
   - Acceda a la carpeta creada, con el nombre del repositorio:
   ```bash
   cd nombre_del_repositorio
   ```
Nota: **Recuerde que puede obtener el enlace en el mismo repositorio, abierto en el navegador, siguendo los pasos de: https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository**

## Pasos para Instalar las Dependencias

Es recomendable utilizar un entorno virtual para gestionar las dependencias de tu proyecto. A continuaci�n, se describen los pasos para crear un entorno virtual e instalar las dependencias.

### 1. Instalar `virtualenv` (si no lo tienes instalado)

Si a�n no tienes `virtualenv` instalado, puedes instalarlo usando `pip`. Abre la terminal y ejecuta el siguiente comando:

```bash
pip install virtualenv
```

En el directorio de instalaci�n de la API, ejecuta los siguentes comandos para crear el entorno virtual:

```bash
virtualenv venv
venv\Scripts\activate
```

### 2. Posteriormente instale los recursos de "flask" y "yfinance".

```bash
pip install flask
pip install yfinance
```

Nota: **Si desea asegurarse de la instalaci�n ejecute el comando:**

```bash
pip list
```

## Endpoints

### `/weight_pokemon`
- **M�todo**: `POST`
- **Par�metros de Entrada**: `name` nombre del Pok�mon. 
- **Descripci�n**: Calcula el BMI del Pok�mon, y devuelve BMI, peso en kilogramos, altura en metros y su categor�a de salud.

### `/price_item`
- **M�todo**: `POST`
- **Par�metros de Entrada**: `name` nombre del item, ya sea de la serie o del juego. 
- **Descripci�n**: Convierte el valor en yenes a USD, COP y EUR, devuelve los precios en cada divisa.

## Ejemplos de Uso

### Ejemplo para C�lculo de BMI

```json
POST /weight_pokemon
{
  "name": pikachu
}
```
### Ejemplo para conversi�n de precio de item

```json
POST /price_item
{
  "name": poke-ball
}
```
