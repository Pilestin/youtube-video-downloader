import streamlit as st 
from pytube import YouTube, Playlist


st.title("YouTube Video İndirme Uygulaması")
st.write("Lütfen indirmek istediğiniz YouTube Playlist URL'ini girin:")


path = "Downloads/"
st.write("Kaydedilecek klasör : ", path)
    

playlist_url = st.text_input("Video URL")
playlist = Playlist(playlist_url)
print(f"Downloading : {playlist.title}")

st.divider()
st.subheader(playlist.title)
st.write(f"Video Sayısı: {len(playlist.videos)}")
st.divider()

col1, col2 = st.columns(2)
with col1:
    start = st.number_input("Başlangıç", min_value=0, max_value=len(playlist.videos), value=0)
with col2:
    end = st.number_input("Bitiş", min_value=0, max_value=len(playlist.videos), value=len(playlist.videos))

if st.button("İndir"):
    for url in playlist.video_urls[start:end]:
        video = YouTube(url, use_oauth=True)
        st.write(f"{video.title} İndiriliyor...")
        with st.spinner("İndiriliyor..."):
            video.streams.get_highest_resolution().download(path, filename=video.title + ".mp4")
        st.success(f"{video.title} indirildi.")


