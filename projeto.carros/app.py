import streamlit as st

st.sidebar.title("Aluguel de carros")
st.sidebar.image("logo.porsche.jfif")
st.sidebar.write("Escolha o carro do seus sonhos!!❤️")
carros = ["Bmw","porsche","argo","Gtr 34"]
opcao = st.sidebar.selectbox("Selecione o moledo de carro :", carros)

#### PRINCIPAL
st.title("thauany carros - Aluguel de carros")

st.image(f"{opcao}.png")
st.markdown(f'## Você alugou o modelo: {opcao}')
st.markdown('---')

dias = st.text_input(f"por quantos dias o {opcao} foi alugado?")
km = st.text_input(f"quantos km você rodou com o {opcao}?")

### copiar daqui pra frente --- define a diaria
if opcao == "Bmw" :
    diaria = 550

elif opcao == "porsche" :
    diaria = 1000

elif opcao == "argo" :

    diaria = 800

elif opcao == "Gtr 34" :
    diaria = 1500


if st.button("calcular"):
    dias = int(dias)
    km = float(km)

    total_dias = dias * diaria 
    total_km = km * 0.15 
    aluguel_total  = total_dias+total_km

    st.warning(f"você alugou o {opcao} por {dias} dias e rodou{km}km . O valor total a pagar é R$ {aluguel_total :.2f}")


