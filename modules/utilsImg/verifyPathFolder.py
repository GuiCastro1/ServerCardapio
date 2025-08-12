import os
from flask import current_app

def verify_path_folder(type):
    
    base_path = current_app.static_folder
    # '../', '../', 'static', 
    upload_path = os.path.join(base_path, 'IMG', type)

    try:
        os.makedirs(upload_path, exist_ok=True)
        print(f'Caminho de upload verificado: {upload_path}')
        return True, upload_path
             
    except OSError as e:
        print(f'Erro ao verificar/criar caminho {upload_path}: {e}')
        return False, None
    

def extrair_caminho_relativo(path_absoluto):
    # Garante que a barra é sempre a mesma (Windows usa \, mas no front é /)
    path_absoluto = path_absoluto.replace('\\', '/')
    
    # Acha a posição de "static/"
    idx = path_absoluto.find("ServerCardapio/")
    
    # Retorna apenas o que vem depois de "static/"
    if idx != -1:
        return path_absoluto[idx + len("ServerCardapio/"):]
    else:
        return path_absoluto  # fallback (devolve tudo se "static/" não for encontrado)


