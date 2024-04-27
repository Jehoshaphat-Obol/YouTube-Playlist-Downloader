from pytube import Playlist


# Function to download YouTube playlist
def download_playlist(playlist_url, output_path='./'):
    playlist = Playlist(playlist_url)

    print(f"Downloading Playlist: {playlist.title}")

    for video in playlist.videos:
        try:
            print(f"Downloading Video: {video.title}")
            video.streams.filter(progressive=True, file_extension='mp4').first().download(output_path)
            print(f"Downloaded {video.title}")
        except Exception as e:
            print(f"Error downloading {video.title}: {e}")

    print("Download completed.")

# Example usage
if __name__ == "__main__":
    playlist_url = input("Enter the url of the playlist: \n")
    output_path = input("Save To: ")
    download_playlist(playlist_url, output_path)

