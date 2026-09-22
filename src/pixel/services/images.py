from io import BytesIO
from PIL import Image

MAX_BYTES = 5 *1024 * 1024
MAX_SIDE = 4096
ALLOWED_FORMATS = {"JPEG","PNG"}


def check_image(data: bytes) -> tuple[str,int,int]:
    if not data:
        raise ValueError("请提供图片")

    if len(data) > MAX_BYTES:
        raise ValueError("图片过大,请提供不超过5MB的图片")

    with Image.open(BytesIO(data)) as image:
        image_format = image.format
        width, height = image.size

        if image_format not in ALLOWED_FORMATS :
            raise ValueError("请传入JPEG或PNG格式的图片")
        if width > MAX_SIDE or height > MAX_SIDE:
            raise ValueError("图片的宽和高都不能超过 4096 像素")

        image.load()
        
        return image_format, width, height
