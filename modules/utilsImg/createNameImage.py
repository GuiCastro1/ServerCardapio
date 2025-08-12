import uuid

def generate_unique_filename(fixed_extension='webp'):
    unique_filename = uuid.uuid4()
    return f'{unique_filename}.{fixed_extension}'
