from PIL import Image
from io import BytesIO

class Thumbnail:

    def __init__(self,file_data, size=(128, 128)):
        try:
            with Image.open(BytesIO(file_data)) as img:
                self.width, self.height = img.size
                img.thumbnail(size)
                thumbnail_buffer = BytesIO()
                img.save(thumbnail_buffer,img.format)
            self.thumb = thumbnail_buffer.getvalue()
        except Exception as e:
            print(f"Error creating thumbnail: {e}")
            raise e
    
    def thumbnail(self):
        return self.thumb
    
    def resolution(self):
        return self.width, self.height
            