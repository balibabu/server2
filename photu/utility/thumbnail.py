from PIL import Image
from io import BytesIO

class Thumbnail:

    def __init__(self,file_data, size=(256, 256)):
        try:
            with Image.open(BytesIO(file_data)) as img:
                self.width, self.height = img.size
                img.thumbnail(size)
                width, height = img.size
                cropped_img = img.crop((width*.2, height*.2, width*.8, height*.8))

                thumbnail_buffer = BytesIO()
                cropped_img.save(thumbnail_buffer,img.format)
            self.thumb = thumbnail_buffer.getvalue()
        except Exception as e:
            print(f"Error creating thumbnail: {e}")
            raise e
    
    def thumbnail(self):
        return self.thumb
    
    def resolution(self):
        return self.width, self.height
            