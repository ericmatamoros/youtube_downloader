import streamlit as st
from pytube import YouTube
import os

# Set the default download directory
default_directory = "/Users/ericmatamoros/Desktop/"

# Set the title of the app
st.title("YouTube Video Downloader")

# Add some instructions
st.write("""
    Enter the URL of the YouTube video you want to download and specify the download directory.
""")

# Create a text input box for the YouTube URL
url = st.text_input("YouTube URL")

# Create a text input box for the download directory, with a default value
download_directory = st.text_input("Download Directory", value=default_directory)

# Create a button to start the download
if st.button("Download Video"):
    if url and download_directory:
        try:
            if not os.path.exists(download_directory):
                os.makedirs(download_directory)
                
            # Display a progress message
            st.write("Downloading...")

            # Use pytube to download the video
            yt = YouTube(url)
            stream = yt.streams.first()
            stream.download(download_directory)
            
            # Display a success message
            st.success("Download completed!")
        except Exception as e:
            # Display an error message if the download fails
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a valid YouTube URL and specify a download directory.")