from pytube import YouTube

link = input("Digite O Link Do Video Que Deseja Baixar: ")
path = input("Digite O Diretório Que Deseja Salvar O Video: ")
yt = YouTube(link)

print("Titulo: ", yt.title)
print("Número De Views: ",yt.views)
print("Tamanho Do Video: ", yt.length,"Segundos")
print("Avaliação Do Video: ", yt.rating)

ys =yt.streams.get_highest_resolution()

print("Baixando....")
ys.download(path)
print("Download Completo!")
