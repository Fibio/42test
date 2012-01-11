from PIL import Image


def resize(img, output_size=(350, 350)):

    """ Return image size for preview """

    if img and hasattr(img, "url"):
        image = Image.open(img)
        m_width = float(output_size[0])
        m_height = float(output_size[1])
        w_k = image.size[0] / m_width
        h_k = image.size[1] / m_height
        if output_size < image.size:
            if w_k > h_k:
                new_size = (m_width, image.size[1] / w_k)
            else:
                new_size = (image.size[0] / h_k, m_height)
        else:
            new_size = image.size
        new_size = tuple(map(int, new_size))
        return new_size
    return None
