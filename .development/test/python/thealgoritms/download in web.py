#download de arquivo de tamanho conhecido

BUFF_SIZE = 1024
def download_lengh(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

#or function download in web

def downloand(response, output):
    total_downloaded = 0
    while True:
        date = response.read(BUFF_SIZE)
        total_downloaded += len(date)
        if not date:
            break
        output.write(date)
        print("Downloaded {bytes}".format(bytes=total_downloaded))
#one programmer complete

#conding: utf-8
import io
import sys
import urllib.request as request

def main():
    print("hello_programmer_software")

if __name__ == "__main__":
    main()

#importa a função

def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")

    content_length = response.getheader("Content_Length")
    if content_length:
        length = int(content_length)
        download_length = (response, out_file, length)
    else:
        download = (response, out_file)

    response.close()
    out_file.close()
    print("Finished")

if __name__ == "__main__":
    main()









