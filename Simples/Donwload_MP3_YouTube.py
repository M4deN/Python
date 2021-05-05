from pytube import YouTube
import moviepy.editor as mp
import re
import os

link = input("Digite O Link Do Video Que Deseja Baixar: ")
path = input("Digite O Diretório Que Deseja Salvar O Video: ")
yt = YouTube(link)

print("Baixando....")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download Completo!!")

print("Convertendo Arquivo, Aguarde.....")

for file in os.listdir(path):
    if re.search('mp4',file):
        mp4_path = os.path.join(path,file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)

print("Concluido Com Sucesso!!")

#pip install pytube#
#pip install moviepy#
