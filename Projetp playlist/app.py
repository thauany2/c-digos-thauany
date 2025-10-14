import streamlit as st

st.sidebar.image("logo.png")

# Dados de exemplo
generos_de_musica = ["Romance", "funk", "internacional"]

# Dicionário relacionando gêneros aos seus livro_por_genero  

musica_por_genero = { 
  "Romance": ["Die whit a smile", "All of me", "Thinking out Loud"],
  "Funk": ["Sequência feiticeira", "Construção de amor", "Ela é profissional"],
  "Internacional": ["Feel it", "Like a boy", "Ride or die,pt.2"]

  }
# Selectbox para escolher o gênero                
genero_selecionado = st.sidebar.selectbox("Selecione o gênero:", generos_de_musica)

# Selectbox para escolher o livro (apenas do gênero selecionado)
if genero_selecionado:
    artista_selecionado = st.sidebar.selectbox(
        "Selecione a música:", 
     musica_por_genero[genero_selecionado]
    )


# Mostrar apenas o livro selecionado
if genero_selecionado and artista_selecionado:
    st.write(f"**musica selecionada:** {artista_selecionado}")
    st.write(f"**Gênero:** {genero_selecionado}")

# Mostrar a música 
    if genero_selecionado == 'Romance' and artista_selecionado == "Die whit a smile":
        st.video("https://www.youtube.com/watch?v=kPa7bsKwL-c&list=RDkPa7bsKwL-c&start_radio=1")
    elif genero_selecionado == 'Romance' and artista_selecionado == "All of me":
        st.video("https://www.youtube.com/watch?v=450p7goxZqg")
    elif genero_selecionado == 'Romance' and artista_selecionado == "Thinking out Loud":
        st.video("https://www.youtube.com/watch?v=lp-EO5I60KA")
    
    if genero_selecionado == 'funk' and artista_selecionado == "Sequência feiticeira":
        st.video("https://www.youtube.com/watch?v=_zKnEm9xPWw")
    elif genero_selecionado == 'funk' and artista_selecionado == "Construção de amor":
        st.video("https://www.youtube.com/watch?v=nuwD3tHRygo")
    elif genero_selecionado == 'funk' and artista_selecionado == "Ela é profissional":
        st.video("https://www.youtube.com/watch?v=T_WGwPOZREA")
    
    if genero_selecionado == 'internacional' and artista_selecionado == "Feel it":
        st.video("https://www.youtube.com/watch?v=vZi8ET9k11g")
    elif genero_selecionado == 'internacional' and artista_selecionado == "Like a boy":
        st.video("https://www.youtube.com/watch?v=_HKH7Emy1SY")
    elif genero_selecionado == 'internacional' and artista_selecionado == "Ride or die,pt.2":
        st.video("https://www.youtube.com/watch?v=z7KKPtF6vtM")