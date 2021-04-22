import os
import base64
import streamlit as st
from pytube import YouTube

st.title('YouDown')
url = st.text_input('Cole aqui a url do Youtube para converter em Audio')
enviar = st.button('Rodar')


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}" color = "red ">Download {file_label}</a>'
    return href


if enviar:
    try:

        # criando objeto YouTube
        yt = YouTube(url)

        # acessando audio streams do YouTube obj
        stream = yt.streams.filter(only_audio=True).first()
        # downloading a video: stream = yt.streams.first()

        # download PARA directory
        stream.download()

        st.write("Aguarde .....")

        local = stream.download()

        st.markdown(get_binary_file_downloader_html(
            local, 'Mp4 audio'),
                    unsafe_allow_html=True)

    except:
        st.write("Servidor nao responde! Tente novamente mais tarde!")




