from .verifyPathFolder import verify_path_folder, extrair_caminho_relativo
from .createNameImage import generate_unique_filename
from .convertImage import convert_image

def process_image(image, type):

    y = type
    x = verify_path_folder(y)

    if x :
        print(x[1])

        z = generate_unique_filename()
        print(z)
        # i = 'teste.jpg'
        p = x[1]

        convert_image(image,z,p)

        newPath = extrair_caminho_relativo(p)

        response = f'{newPath}/{z}'

        return response

# r = process_image()

# print(r)
        