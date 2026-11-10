import streamlit as st

st.title("🐧 Firmware Dia 2: Linux Embarcado e RTOS")
st.markdown("""
Hoje subimos uma camada de abstração. Quando o "Super Loop" bare metal não dá mais conta da complexidade, 
precisamos de Sistemas Operacionais para gerenciar as tarefas do nosso produto.
""")

aba1, aba2, aba3 = st.tabs(["🐧 Linux Embarcado", "⏱️ Sistemas de Tempo Real", "🔄 FreeRTOS & Zephyr"])

with aba1:
    st.header("Introdução ao Linux Embarcado e Buildroot")
    st.markdown("""
    Usamos **Linux Embarcado** quando o dispositivo precisa de telas complexas, conexão avançada de rede (Wi-Fi, 4G, VPN), 
    ou processamento de IA local (como um terminal de autoatendimento ou roteador).
    
    **O que é o Buildroot?**
    O Linux de desktop (como Ubuntu) é gigantesco. Para embarcados, não podemos instalar um sistema de 10GB. 
    O Buildroot é uma ferramenta (Baseada em Makefile) que automatiza a construção de um sistema Linux "sob medida", 
    gerando a *Toolchain*, o *Kernel* e o *Root Filesystem* ocupando apenas alguns Megabytes.
    """)
    
    st.code("""
# Fluxo básico de uso do Buildroot
$ make menuconfig  # Abre um menu visual para escolher pacotes (SSH, Python, etc)
$ make             # Compila absolutamente tudo a partir do código-fonte (pode levar horas!)
    """, language="bash")

with aba2:
    st.header("Sistemas de Tempo Real (Real-Time)")
    st.markdown("""
    "Tempo real" não significa ser *rápido*. Significa ser **previsível (determinístico)**.
    Um sistema de tempo real garante que uma tarefa será concluída dentro de um prazo rigoroso (Deadline).
    
    * **Hard Real-Time:** Se o deadline for perdido, é uma falha catastrófica (Ex: Freio ABS, Controle de Voo).
    * **Soft Real-Time:** Se o deadline for perdido, a qualidade do serviço cai, mas não há tragédia (Ex: Decodificação de vídeo/áudio).
    
    **Introdução ao RTOS (Real-Time Operating System)**
    Um RTOS substitui o "Super Loop" por um *Scheduler* (Escalonador) preemptivo. Ele permite criar múltiplas "Tasks" (tarefas) com prioridades diferentes. Se uma tarefa de alta prioridade precisa rodar, o RTOS pausa a tarefa atual imediatamente.
    """)

with aba3:
    st.header("FreeRTOS e Zephyr RTOS")
    
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("FreeRTOS")
        st.markdown("""
        O padrão absoluto da indústria por mais de 15 anos (atualmente mantido pela Amazon/AWS).
        * Simples, leve (usa poucos KBs de RAM).
        * Escrito em C puro (fácil portabilidade).
        """)
        st.code("""
// Exemplo: Criando uma Task no FreeRTOS
xTaskCreate(
    vTaskBlink,    // Função que implementa a task
    "Blink",       // Nome da task
    1000,          // Tamanho da stack
    NULL,          // Parâmetros
    1,             // Prioridade (1 é baixa)
    NULL           // Handle da task
);
        """, language="c")

    with col2:
        st.subheader("Zephyr RTOS")
        st.markdown("""
        O "futuro" moderno (mantido pela Linux Foundation). Projetado para a era da Internet das Coisas (IoT).
        * Usa Device Trees e Kconfig (igual ao Linux).
        * Ecossistema gigante (Bluetooth, Wi-Fi e pilhas de rede já integrados).
        """)
        st.code("""
// Exemplo: Zephyr usa Device Trees para o Hardware
#include <zephyr/kernel.h>
#include <zephyr/drivers/gpio.h>

/* Node do LED no arquivo .dts */
#define LED0_NODE DT_ALIAS(led0)
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(LED0_NODE, gpios);
        """, language="c")