from pytube import YouTube
print("ingrese por favor el url del video.")
video_url = ""
Yt = YouTube(video_url)
video = Yt.streams.get_highest_resolution()
video.download(output_path=".", filename="video_descargado.mp4")
print("Descarga completada.")
