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

## Endpoints

### `/calculate_bmi`
- **Método**: `POST`
- **Parámetros de Entrada**: `weight` (peso en kilogramos), `height` (altura en metros)
- **Descripción**: Calcula el BMI del Pokémon y devuelve su categoría de salud.

### `/convert_currency`
- **Método**: `POST`
- **Parámetros de Entrada**: `amount` (cantidad en yenes)
- **Descripción**: Convierte el valor en yenes a USD, COP y EUR.