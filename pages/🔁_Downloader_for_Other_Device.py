import streamlit as st 
from pytube import YouTube

st.set_page_config(page_title="YouTube Video İndirme Uygulaması", page_icon="🔁", layout="wide", initial_sidebar_state="expanded")

st.title("Localhost'ta çalışan uygulamaya başka bir cihazdan erişip indirme yapmak için kullanın.")
st.write("Lütfen indirmek istediğiniz YouTube video URL'lerini girin:")


def video_donustur(url):
    
    try:
        video = YouTube(url)
        video_stream = video.streams.get_highest_resolution()
        st.write(f"{video.title} Dönüştürülüyor...")
        
        with st.spinner('Bekleyin...'):
            file_path = video_stream.download(path, filename=video.title)
            file = open(file_path, "rb") 
            contents = file.read()
            st.download_button(label="İndir", data= contents, file_name= video.title + ".mp4")
            st.success(f"{video.title} indirildi.")
            file.close()
            
    except Exception as e:
        st.write(f"Hata: {str(e)}")
      


path = st.text_input("Klasör (varsayılan Downloads/)")
path = path if path != "" else "Downloads"

video_url = st.text_input("Video URL")

if video_url != "":
    video_donustur(video_url)