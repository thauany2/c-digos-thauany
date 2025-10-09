import streamlit as st

st.sidebar.title("penteados")
st.sidebar.image("logo.png")
st.sidebar.write("Escolha o penteado do seus sonhos!!❤️")
penteado = ["casamento","debutante","aniversario","madrinha"]
opcao = st.sidebar.selectbox("Selecione o moledo de penteado :", penteado)

#### PRINCIPAL
st.title("penteados perfeitos - penteados")

st.image(f"{opcao}.png")
st.markdown(f'## Você quer fazer o modelo: {opcao}')
st.markdown('---')

horario = st.text_input(f"qual horario {opcao} você quer fazer o penteado?")
dia = st.text_input(f"qual é o dia que vc deseja fazer o penteado {opcao} ?")

### copiar daqui pra frente --- define a diaria
if opcao == "casamento" :
    diaria = 1500

elif opcao == "debutante" :
    diaria = 200

elif opcao == "aniversario" :

    diaria = 300

elif opcao == "madrinha" :
    diaria = 1000


if st.button("calcular"):
    hora = int(horario)
    dia = float(dia)

    total_hora = hora * horario
    total_dia = dia * 0.15 
    aluguel_total  = total_hora+total_dia

    st.warning(f"você fez o penteado {opcao} por {hora} dia que fez{dia}dia . O valor total a pagar é R$ {aluguel_total :.2f}")
    


