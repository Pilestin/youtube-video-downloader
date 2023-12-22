# youtube-video-downloader 


This project is a Streamlit-based application that facilitates downloading YouTube videos. It encompasses different functionalities on separate pages.

### 🎵 Home Page

On this page, users can input individual YouTube video URLs to download videos.

### 🎶 Playlist Downloader Page

This page is designed for downloading YouTube playlists. Users input the playlist URL, select a download range, and initiate the download process.

### 🔁 Downloader for Other Devices
This page allows accessing and downloading videos from a localhost application using another device. Users input the video URL and then download the file by clicking the download button.

## Installation

To run this project locally, follow these steps:
1. Clone the Repository 
    
   ``` git clone https://github.com/Pilestin/youtube-video-downloader.git ```
2. Change the working directory
   
   ``` cd youtube-video-downloader ```

3. Install the required packages

   ``` pip install -r requirements.txt ```

4. run app
   
    ``` streamlit run 🎵_Home.py ```

## Usage

If you don't want to use streamlit, you can use the script/playlist_downloader.py file to run the application.

``` python script/playlist_downloader.py  ```

Once the application is running, access it via your web browser using the provided local URL (usually something like http://localhost:8501).

İf you want to use another device, you can use the local URL like 
Network URL: http://192.168.0.105:8501

Your downloaded videos will be saved in the project folder in ../Downloads