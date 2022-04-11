from tkinter import E
import requests
from bs4 import BeautifulSoup
import time
import os
from PIL import Image

def sorry():
    print("Desculpe, mas não conseguimos acessar o matérial desse link, entre e veja você mesmo!")

def busca():
    n1 = str(input("O que vc deseja buscar? ")).strip()
    sites = google(n1, brainlys=True, wikipedias=True, Brasil_escolas=True, Toda_materias=True, Mundo_educs=True, info_escolas=True, youtubes=True)
    catalogados = ["info_escola", "mundo_educ", "Toda_materia", "Brasil_escola", "wikipedia", "brainly", "youtube"]
    wikipedia2 = False
    info_escola2 = False
    mundo_educ2 = False
    toda_materia2 = False
    brasil_escola2 = False
    brainly2 = False
    youtube2 = False
    for c in sites:
        c = c.lower()
        if catalogados[0].lower() == c:
            info_escola2 = True
        if catalogados[1].lower() == c:
            mundo_educ2 = True
        if catalogados[2].lower() == c:
            toda_materia2 = True
        if catalogados[3].lower() == c:
            brasil_escola2 = True
        if catalogados[4].lower() == c:
            wikipedia2 = True
        if catalogados[5].lower() == c:
            brainly2 = True
        if catalogados[6].lower() == c:
            youtube2 = True
    if wikipedia2 == False:
        sites = google(f"{n1} wikipedia", wikipedias=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    if info_escola2 == False:
        sites = google(f"{n1} info escola", info_escolas=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    if mundo_educ2 == False:
        sites = google(f"{n1} mundo educação", Mundo_educs=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    if toda_materia2 == False:
        sites = google(f"{n1} toda materia", Toda_materias=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    if brasil_escola2 == False:
        sites = google(f"{n1} brasil escola", Brasil_escolas=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    if brainly2 == False:
        sites = google(f"{n1} brainly", brainlys=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    if youtube2 == False:
        sites = google(f"{n1} youtube", youtubes=True)
        for c in sites:
            c = c.lower()
            if catalogados[0].lower() == c:
                info_escola2 = True
            if catalogados[1].lower() == c:
                mundo_educ2 = True
            if catalogados[2].lower() == c:
                toda_materia2 = True
            if catalogados[3].lower() == c:
                brasil_escola2 = True
            if catalogados[4].lower() == c:
                wikipedia2 = True
            if catalogados[5].lower() == c:
                brainly2 = True
            if catalogados[6].lower() == c:
                youtube2 = True
    print(wikipedia2, info_escola2, mundo_educ2, toda_materia2, brasil_escola2, brainly2, youtube2)
    print(catalogados)

def info_escola(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        res = soup.find('article', {'class':'entry'})
        print('!-' * 50)
        print('Info Escola: \n')
        print(url)
        print(res.text)
        print('!-' * 50)
    except:
        print('!-' * 50)
        print('Info Escola: \n')
        print(url)
        sorry()
        print('!-' * 50)

def youtube(url):
    print('^-' * 50)
    print('Youtube: \n {}'.format(url))
    print('\n' + '^-' * 50)

def mundo_educ(url):
    print('%==' * 50 + '\n')
    print('Mundo Educação: ')
    print(url)
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        conteudo = soup.find("div", {"class":"content"})
        ps = conteudo.find_all("p")
        for c in ps:
            n1 = "Leia Também:" in c.text
            n2 = "Leia mais:" in c.text
            if n1 == False and n2 == False:
                c = c.text
                print(f"{str(c)}\n")
    except:
        sorry()
    print('%==' * 50)

def Toda_materia(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        ps = soup.find_all('p')

        print('*::' * 50)
        print('Toda_Materia: ')
        print(url)
        for c in ps:
            print(f'{c.text}')
            print('')
        print('*::' * 50)
    except:
        print('*::' * 50)
        print('Toda_Materia: ')
        print(url)
        sorry()
        print('*::' * 50)

def Brasil_escola(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        textoConteudo = soup.find("div", {"class", "texto-conteudo"})
        div = textoConteudo.find_all("div")[4]
        p = div.find('p')

        print('+--' * 50)
        print('Brasil Escola: \n')
        print(url)
        print('{}'.format(p.text))
        print('+--' * 50)
    except:
        print('+--' * 50)
        print('Brasil Escola: \n')
        sorry()
        print('+--' * 50)

def wikipedia(url):
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')

        conteudo = soup.find('div', {'class':'mw-parser-output'})
        try:
            resumo = conteudo.find_all('p')
            quero = []
            quero.append(resumo[0])
            quero.append(resumo[1])
        except:
            pass
        else:
            print('/\\' * 50)
            print('Wikipedia: \n')
            print(url)
            for c in quero:
                c = c.text
                print(c)
            print('/\\' * 50)
    except:
        print('/\\' * 50)
        print('Wikipedia: \n')
        print(url)
        sorry()
        print('/\\' * 50)

def download(foto):
    certo = requests.get(foto)
    with open('brainly_foto.png', 'wb') as f:
        f.write(certo.content)
    imagem = Image.open('brainly_foto.png')
    imagem.show()

def dow_res(foto):
    certo = requests.get(foto)
    with open('brainly_foto_res.png', 'wb') as f:
        f.write(certo.content)
    imagem = Image.open('brainly_foto_res.png')
    imagem.show()

def brainly(url):
    print('=' * 100)
    print('BRAINLY: ')
    print(f'{url} \n')
    try:
        req = requests.get(url)
        soup = BeautifulSoup(req.text, 'html.parser')
        div = soup.find_all('div', {'class':'brn-qpage-next-question-box-content'})
        res = imgs = []
        yes = n1 = False
        for c in div:
            try:
                escrito = c.find('span', {'class':'sg-text sg-text--break-words brn-qpage-next-question-box-content__secondary'})
                res.append(escrito.text)
                time.sleep(1)
                try:
                    img = c.find_all('img')
                    if img != '[]':
                        yes = True
                        for i in img:
                            imgs.append(i['src'])
                            download(i['src'])
                except Exception as erro:
                    print(erro)
            except:
                n1 = True
                
        print('Pergunta: ')
        if n1 == False:    
            for c in res:
                print(c)
                    
        else:
            res2 = soup.find('div', {'class':'brn-qpage-next-question-box__content'})
            res2 = res2.text 
            res2 = res2.split('\n')
            res2 = res2[5]
            print(res2)
        
        if yes == True:
            time.sleep(1)
            try:
                os.unlink('brainly_foto.png')
            except:
                pass

        print('\nResposta: ') #RESPOSTA: 

        auto = soup.find_all('div', {'class':'brn-qpage-next-answer-box-author__description'})
        res1 = soup.find_all('div', {'class':'sg-text sg-text--break-words brn-rich-content js-answer-content'})
                                                
        for c in range(0, len(auto)):
            try:
                res_img = res1[c].find('img')
                res_img = res_img['src']
            except:
                foi = False
            else:
                foi = True
            print('=' * 100)
            autor = auto[c].text
            resposta = res1[c].text
            autor = autor.split('\n')
            autor = autor[4]
            print(f'{autor}: ')
            print(resposta)
            if foi == True:
                dow_res(res_img)
                print('foto: {}'.format(res_img))
                time.sleep(1)
                os.unlink('brainly_foto_res.png')
            print('=' * 100)
            time.sleep(1)
    except:
        sorry()
        print('=' * 100)

def google(pesquisa, brainlys=False, wikipedias=False, Brasil_escolas=False, Toda_materias=False, Mundo_educs=False, info_escolas=False, youtubes=False):
    sites = []
    links = []
    links2 = []
    adiciona = True
    url = f"https://www.google.com/search?q={pesquisa}&oq={pesquisa}&aqs=chrome..69i57j46i433j0i433l3j46i433j0i433j69i60.947j0j7&sourceid=chrome&ie=UTF-8"
    req = requests.get(url)
    soup = BeautifulSoup(req.text, 'html.parser')
    main = soup.find("div", {"id":"main"})
    divs = main.find_all("div")
    for div in divs:
        ignorar = div.find("div", {"class":"KP7LCb"})
        if str(ignorar) == "None":
            limitador = div.find("div", {"class":"kCrYT"})
            try:
                ass = limitador.find("a")
                h3 = limitador.find("h3", {"class":"zBAuLc"})
            except:
                pass
            else:
                if str(ass) != "None" and str(h3) != "None":
                    for i in links:
                        if i == ass['href']:
                            adiciona = False
                    if adiciona == True:
                        links.append(ass['href'])
                        #print(ass['href'])
                    adiciona = True
    #print(links)
    #time.sleep(5)
    for c in links:
        c = c[7:]
        c = c.split("&sa=")
        c = c[0]
        dominio = c[8:]
        dominio = dominio.split('/')
        linkada2 = dominio[0]
        if linkada2 == "www.youtube.com" and youtubes == True:
            try:
                c = c.split(r"%3Fv%3D")
                c = f"{c[0]}?v={c[1]}"
            except:
                pass
        if linkada2 == 'brainly.com.br' and brainlys == True:
                brainly(c)
                sites.append("brainly")
        if linkada2 == 'pt.wikipedia.org' and wikipedias == True:
            if '%25C3%25A7' in c:
                c = c.replace('%25C3%25A7', 'ç')

            if '%25C3%25AA' in c:
                c = c.replace('%25C3%25AA', 'ê')

            if '%25C3%25A1' in c:
                c = c.replace('%25C3%25A1', 'á')

            if '%25C3%25AD' in c:
                c = c.replace('%25C3%25AD', 'í')

            if '%25C3%25B3' in c:
                c = c.replace('%25C3%25B3', 'ó')
            
            if '%25C3%25A2' in c:
                c = c.replace('%25C3%25A2', 'â')
            
            #print('Wikipedia!')
            wikipedia(c)
            sites.append("wikipedia")
        if linkada2 == 'brasilescola.uol.com.br' and Brasil_escolas == True: 
            Brasil_escola(c)
            sites.append("brasil_escola")
        if linkada2 == 'www.todamateria.com.br' and Toda_materias == True:
            Toda_materia(c)
            sites.append("toda_materia")
        if linkada2 == 'mundoeducacao.uol.com.br' and Mundo_educs == True:
            mundo_educ(c)
            sites.append("Mundo_educ")
        if linkada2 == 'www.infoescola.com' and info_escolas == True:
            info_escola(c)
            sites.append("info_escola")
        if linkada2 == 'www.youtube.com' and youtubes == True:
            youtube(c)
            sites.append("youtube")
        #print('=' * 100)
        #time.sleep(1)
    return sites
                    

if __name__ == "__main__":
    busca()