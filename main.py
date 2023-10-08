# WRITTED BY: 0xRobert, 2023, github.com/zahanzo, linkedin.com/in/0xrobert
from urllib.request import urlopen, Request
from urllib.error import HTTPError
from bs4 import BeautifulSoup as bs
import random
from tkinter.messagebox import showinfo
from tkinter import ttk, Tk, Label, Frame, Button, Entry, StringVar, LEFT
import os

# variaveis
root = Tk()
choises = ["https://pt.pornhub.com", ""]
result = None
http = None
page = None
cats = ['', '111', '13', '28', '37', '29', '17' ,'35', '3', '16',
        '65', '4', '57', '41', '105']
final_url = ""
html_output = ""
rand = 0

# abrir o arquivo html com o video, ou o github
def openBrowser(src):
    if src == 'v':
        os.system(f"start {os.getcwd()+'/output/video.html'}")
    else:
        os.system("start https://github.com/zahanzo")
 

# pega um video aleatorio
def randomVideo(src):
    global final_url, result, page, html_output, http

    try:
        http = Request(final_url, None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
        page = urlopen(http)
    except HTTPError:
        pass
    if page.getcode() == 404:
        showinfo(root, message='ERRO: Nenhum video foi encontrado.')
        return 1
    rand = random.randint(0, 69)
    while True:
        page = None
        http = None
        if rand <= 0:
            rand = random.randint(0, 69)

        try:
            http = Request(f"{final_url}&page={rand}", None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
            page = urlopen(http)
        except HTTPError:
            try:
                http = Request(f"{final_url}?page={rand}", None, {'User-agent' : 'Mozilla/5.0 (Windows; U; Windows NT 5.1; de; rv:1.9.1.5) Gecko/20091102 Firefox/3.5.5'})
                page = urlopen(http)
            except HTTPError:
                rand = int(rand / 2)

        if page != None:
            if page.getcode() == 200:
                break
        

    soup = bs(page.read(), 'lxml')
    if src == 'q':
        try:
            result = soup.find("body").find(class_="wrapper").find(class_="container").find(class_="gridWrapper").find(class_="nf-videos").find(class_="sectionWrapper videoSearch tjWrap").find(class_="videos search-video-thumbs").find(class_="pcVideoListItem js-pop videoblock videoBox").find(class_="fade fadeUp videoPreviewBg linkVideoThumb js-linkVideoThumb img")
        except:
            result = soup.find("body").find(class_="wrapper").find(class_="container").find(class_="gridWrapper").find(class_="nf-videos").find(class_="sectionWrapper videoSearch tjWrap").find(class_="videos search-video-thumbs freeView").find(class_="pcVideoListItem js-pop videoblock videoBox").find(class_="fade fadeUp videoPreviewBg linkVideoThumb js-linkVideoThumb img")
    
    else:
        try:
            result = soup.find("body").find(class_="wrapper").find(class_="container").find(class_="gridWrapper").find(class_="nf-videos").find(class_="nf-videos videos search-video-thumbs").find(class_="pcVideoListItem js-pop videoblock videoBox").find(class_="fade fadeUp videoPreviewBg linkVideoThumb js-linkVideoThumb img")
        except:
            result = soup.find("body").find(class_="wrapper").find(class_="container").find(class_="nf-videos").find(class_="sectionWrapper").find(class_="nf-videos videos search-video-thumbs incategories").find(class_="pcVideoListItem js-pop videoblock videoBox").find(class_="fade fadeUp videoPreviewBg linkVideoThumb js-linkVideoThumb img")
    
    # salvar resultado no video.html
    with open("output/video.html", "w", encoding="utf-8") as file:
        file.write("""<!DOCTYPE html>
                    <head lang='pt-BR'>
                    <meta charset='utf-8' />
                    <meta name='viewport' content='width=device-width, initial-scale=1' />
                    <link rel="stylesheet" type="text/css" href="style.css" media="screen" />
                    </head>
                    <body>
                        <div class='center'>"""
                        f"<a href='{page.url}'> <h6>{page.url}</h6> </a>"+
                        """</div>
                        <div class="center">"""+
                        f"<iframe src='https://pt.pornhub.com{result.get('href').replace('/view_video.php?viewkey=', '/embed/')}' frameborder='1' width='560' height='315' scrolling='no' allowfullscreen></iframe><br>"+
                        f"<a href='https://pt.pornhub.com{result.get('href')}'><h3>{result.find('img').get('alt')}</h3></a>"+
                        """</div>
                        </body>
                        </html""")
    
    # abrir video.html no browser
    openBrowser('v')

# função do botão
def call_btn():
    global final_url

    # Categorias, e pesquisa:
    if search.get() != "":
        if combo.current() > 0:
            final_url = choises[0] + f"/video/search?search={search.get()}&filter_category={cats[combo.current()]}"
        else:
            final_url = choises[0] + f"/video/search?search={search.get()}"
        # gerar video pela pesquisa
        randomVideo('q')
    # Categoria selecionada:
    elif combo.current() > 0:
        if   combo.current() == 1:  choises[1] = "/video?c=111"
        elif combo.current() == 2:  choises[1] = "/video?c=13"
        elif combo.current() == 3:  choises[1] = "/video?c=28"
        elif combo.current() == 4:  choises[1] = "/categories/teen"
        elif combo.current() == 5:  choises[1] = "/video?c=29"
        elif combo.current() == 6:  choises[1] = "/video?c=17"
        elif combo.current() == 7:  choises[1] = "/video?c=3"
        elif combo.current() == 8:  choises[1] = "/video?c=3"
        elif combo.current() == 9:  choises[1] = "/video?c=16"
        elif combo.current() == 10: choises[1] = "/video?c=65"
        elif combo.current() == 11: choises[1] = "/video?c=4"
        elif combo.current() == 12: choises[1] = "/video?c=57"
        elif combo.current() == 13: choises[1] = "/video?c=41"
        elif combo.current() == 14: choises[1] = "/video?c=105"
        final_url = choises[0] + choises[1]

        # gerar video pela categoria
        randomVideo('c')

    # gerar video pesquisado em categoria
    elif combo.current() > 0 and search.get() != '':
        final_url = choises[0] + f"/video/search?search={search.get()}&filter_category={cats[combo.current()]}"
    else:
        showinfo(root, message="Você precisa digitar algo, ou escolher alguma categoria.")


### GUI
fontePadrao = ("Arial", "10")
primeiroContainer = Frame(pady=10)
primeiroContainer.pack()

segundoContainer = Frame(padx=20)
segundoContainer.pack()

terceiroContainer = Frame(padx=20)
terceiroContainer.pack()

quartoContainer = Frame(pady=20)
quartoContainer.pack()

titulo = Label(primeiroContainer, text="Pesquisar:", font=("Arial", "10", "bold"))
titulo.pack()

search = Entry(segundoContainer, width=30, font=fontePadrao)
search.pack(side=LEFT)

category = Label(terceiroContainer, text="Categoria(Opcional):", font=("Arial", "8", "bold"))
category.pack()

combo_vv = StringVar(terceiroContainer)
combo_v = combo_vv.get()
combo = ttk.Combobox(terceiroContainer, width=27, textvariable=combo_v, state='readonly', justify="center")
combo["values"] = ( 'Nenhuma', 'Japonesas', 'Boquete', 'Madura', 'Novinha', 'MILF',
                           'Negras', 'Anal', 'Amador', 'Gozada', 'Trio', 'Bundão',
                           'Compilação', 'POV', '60FPS' )
combo.current(0)
combo.pack()

done = Button(quartoContainer, text="Pronto.", font=("Calibri", "8"), width=12, command=call_btn)
done.pack()

link = Label(root, text="github.com/zahanzo", fg="blue", cursor="hand2")
link.bind("<Button-1>", openBrowser)
link.pack(side="bottom")
### GUI

root.title("Porn Generator ~ by 0xrobert")
root.geometry("350x200")
root.mainloop()
