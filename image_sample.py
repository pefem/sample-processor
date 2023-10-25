import logging
from typing import TypeVar
from sample_interface import CreateSample
from PIL import Image, UnidentifiedImageError

# -------------------------------------------------

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler(r"logs\image_sample.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# -------------------------------------------------


class ImageSample(CreateSample):

    sample_list = []

    # -------------------------------------------------

    def __init__(
        self,
        path: str, 
        sample_size: int=250,
        number_of_samples: int=3,
    ) -> None:
        self.path = path
        self.sample_size = sample_size
        self.number_of_samples = number_of_samples
    
    # -------------------------------------------------
    
    def __repr__(self) -> str:
        return f"ImageSample(size: {self.sample_size}, sample_number: {self.number_of_samples})"
    
    # -------------------------------------------------
    
    @property
    def sample_size(self) -> int:
        return self.__sample_size
    
    # -------------------------------------------------
    
    @sample_size.setter
    def sample_size(self, value: int) -> None:
        size_list = self.origin_size(self.load_origin())

        if (value > size_list[0]) or (value > size_list[1]):
            raise ValueError("Sample size is too large, use a smaller value")
        else:
            self.__sample_size = value
    
    # -------------------------------------------------
  
    def load_origin(self):
        try: 
            with Image.open(self.path).convert("RGB") as image_obj:
                return image_obj
        except (FileNotFoundError, UnidentifiedImageError):
            logger.error("Invalid Image or Defined Path")
            return None
    
    # -------------------------------------------------
        
    def origin_size(self, origin_object) -> tuple:
        return origin_object.size
    
    # -------------------------------------------------
    
    def display_origin(self, origin_object) -> None:
        origin_object.show()
    
    # -------------------------------------------------

    def origin_format(self, origin_oject) -> None:
        origin_oject.format
    
# -------------------------------------------------
# END OF FILE
# -------------------------------------------------

