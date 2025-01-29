/*
 * Ejemplo sencillo para un microcontrolador ARM Cortex-M4
 * Encender un LED con un botón utilizando GPIO
 */

#include "stm32f4xx.h" // Biblioteca específica del microcontrolador

void GPIO_Init(void) {
    // Habilitar el reloj para el puerto GPIOA y GPIOC
    RCC->AHB1ENR |= RCC_AHB1ENR_GPIOAEN | RCC_AHB1ENR_GPIOCEN;

    // Configurar PA5 como salida (LED)
    GPIOA->MODER &= ~GPIO_MODER_MODER5_Msk; // Limpiar configuración
    GPIOA->MODER |= GPIO_MODER_MODER5_0;   // Configurar como salida

    // Configurar PC13 como entrada (Botón)
    GPIOC->MODER &= ~GPIO_MODER_MODER13_Msk; // Configurar como entrada
    
    // Configurar resistencias de pull-up para PC13
    GPIOC->PUPDR &= ~GPIO_PUPDR_PUPDR13_Msk; // Limpiar configuración
    GPIOC->PUPDR |= GPIO_PUPDR_PUPDR13_0;    // Activar pull-up
}

void delay_ms(uint32_t ms) {
    // Función de retardo básico
    for (uint32_t i = 0; i < ms * 4000; i++) {
        __NOP(); // Instrucción "No Operation" para consumir tiempo
    }
}

int main(void) {
    GPIO_Init(); // Inicializar GPIO

    while (1) {
        // Leer el estado del botón (PC13)
        if ((GPIOC->IDR & GPIO_IDR_ID13) == 0) { // Si el botón está presionado
            GPIOA->ODR |= GPIO_ODR_OD5; // Encender el LED (PA5)
        } else {
            GPIOA->ODR &= ~GPIO_ODR_OD5; // Apagar el LED (PA5)
        }

        delay_ms(50); // Retardo para evitar rebotes
    }
}