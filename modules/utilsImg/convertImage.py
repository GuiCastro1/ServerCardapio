from PIL import Image 
import os

def convert_image(img, name, path_upload):
    #ver se pasta existe def ✔
        #pegar o path da pasta ✔
            #criar nome unico para o arquivo✔
                #retornar o path da imagem e salvar 

    #remover image no delete
    #mudar image no update

    with Image.open(img) as img_convert:
        img_convert.save(os.path.join(path_upload, name), format='WEBP')