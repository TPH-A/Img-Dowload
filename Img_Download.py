import requests
i = 0
while True:
    url = input("Input image url:")
    print("Downloading......")
    gets = requests.get(url = url)
    if url == "q":
        break
    i += 1
    file = open("download{}.png".format(i), "wb+")
    file.write(gets.content)
    file.close()
    try:
        gets = requests.get(url = url)
    except:
        print("Download error!")
    else:
        print("Dowload!")
