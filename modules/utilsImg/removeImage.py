import os

def remove_image(path_image):

        path = path_image
        join_path= os.path.join(path)
        print(join_path)
        os.remove(join_path)

