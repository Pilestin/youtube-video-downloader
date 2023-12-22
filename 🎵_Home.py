import streamlit as st 
from pytube import YouTube


st.set_page_config(page_title="YouTube Video İndirme Uygulaması", page_icon=":smiley:", layout="wide", initial_sidebar_state="expanded")

download_path = "Downloads"

def video_donustur(url):
    
    try:
        video = YouTube(url)
        video_stream = video.streams.get_highest_resolution()
        st.write(f"{video.title} Dönüştürülüyor...")
        
        with st.spinner('Bekleyin...'):
            video_stream.download(download_path, filename=video.title)
        st.success(f"{video.title} indirildi.")
    
    except Exception as e:
        st.write(f"Hata: {str(e)}")
      

def main():
    st.title("YouTube Video İndirme Uygulaması")
    st.write("Lütfen indirmek istediğiniz YouTube video URL'lerini girin:")
    
    video_url = st.text_input("Video URL")
    if video_url != "":
        video_donustur(video_url)
       
if __name__ == "__main__":
    main()