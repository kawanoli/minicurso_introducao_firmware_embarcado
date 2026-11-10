import streamlit as st

st.title("💻 Firmware Dia 1: Arquitetura e Bare Metal")
st.markdown("""
Neste primeiro dia de Firmware, vamos descer ao nível do hardware. Entenderemos como o processador "pensa" 
e como controlamos os pinos físicos de um chip escrevendo diretamente em seus registradores.
""")

aba1, aba2, aba3 = st.tabs(["🧠 Micro X Micro", "🏗️ Arquitetura", "⚙️ Bare Metal"])

with aba1:
    st.header("Microcontroladores vs Microcomputadores")
    st.markdown("""
    A principal diferença está no nível de integração e no propósito de uso:
    """)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Microcontroladores (MCU)**\n"
                "* Tudo em um único chip (CPU, RAM, Flash, Periféricos).\n"
                "* Foco em tarefas específicas e determinísticas.\n"
                "* Consumo de energia baixíssimo (mW a µW).\n"
                "* Ex: Arduino (ATmega328), ESP32, STM32.")
    with col2:
        st.success("**Microcomputadores (MPU)**\n"
                   "* CPU potente, mas RAM e Armazenamento são externos.\n"
                   "* Foco em processamento de dados geral e SO complexo.\n"
                   "* Alto consumo de energia (W).\n"
                   "* Ex: Raspberry Pi (Broadcom), PC (Intel/AMD).")

with aba2:
    st.header("Básico de Arquitetura de Computadores")
    st.markdown("""
    Para programar hardware, precisamos entender como a memória e a CPU se comunicam:
    * **Arquitetura de Von Neumann:** Dados e Instruções (código) dividem o mesmo barramento e a mesma memória. É mais simples, mas gera gargalo.
    * **Arquitetura de Harvard:** Barramentos e memórias físicas separadas para Dados e Instruções. A CPU pode ler uma instrução e um dado simultaneamente (muito comum em microcontroladores modernos como ARM Cortex-M).
    """)
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Harvard_architecture.svg/500px-Harvard_architecture.svg.png", caption="Arquitetura de Harvard (Ilustrativa)")

with aba3:
    st.header("Programação Bare Metal")
    st.markdown("""
    **Bare Metal** significa programar "direto no metal", sem nenhum Sistema Operacional por baixo. 
    Seu código é a única coisa rodando no chip.
    """)
    
    st.subheader("O Loop Infinito")
    st.markdown("Todo firmware bare metal possui uma estrutura básica: Inicialização seguida de um loop que nunca termina.")
    st.code("""
int main(void) {
    // 1. Inicialização de Hardware (Clocks, GPIOs, Periféricos)
    init_system();
    
    // 2. Loop Infinito (Super Loop)
    while(1) {
        ler_sensores();
        processar_dados();
        atualizar_atuadores();
    }
}
    """, language="c")