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

## Endpoints

### `/calculate_bmi`
- **M�todo**: `POST`
- **Par�metros de Entrada**: `weight` (peso en kilogramos), `height` (altura en metros)
- **Descripci�n**: Calcula el BMI del Pok�mon y devuelve su categor�a de salud.

### `/convert_currency`
- **M�todo**: `POST`
- **Par�metros de Entrada**: `amount` (cantidad en yenes)
- **Descripci�n**: Convierte el valor en yenes a USD, COP y EUR.