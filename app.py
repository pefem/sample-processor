import logging
import random
from image_sample import ImageSample

# -------------------------------------------------

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s:%(name)s:%(message)s")

file_handler = logging.FileHandler(r"logs\app.log")
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

# -------------------------------------------------


def generate_random_samples(img_sample_obj) -> None:

    """
    generates a specified number of image sample objects

    """

    img_obj = img_sample_obj.load_origin()
    range_start = 0

    for index, _ in enumerate(range(img_sample_obj.number_of_samples), start=1):

        logger.info(f"creating sample {index}")

        left = random.randrange(range_start, img_sample_obj.origin_size(img_obj)[0] - img_sample_obj.sample_size)
        upper = random.randrange(range_start, img_sample_obj.origin_size(img_obj)[1] - img_sample_obj.sample_size)
        right = left + img_sample_obj.sample_size
        lower = upper + img_sample_obj.sample_size

        img_sample_obj.sample_list.append(img_obj.crop((left, upper, right, lower)))
        
        logger.info(f"Sample {index} created")

# -------------------------------------------------

def samples_to_folder(sample_list: list) -> None:

    """
    saves randomly generated samples to file/folder

    """
    if sample_list:
        for index, img_object in enumerate(sample_list, start=1):
            img_object.save(f"random_samples\\sample_{index}.jpg")
    else:
        logger.info("No Available Samples to Load to Folder")

# -------------------------------------------------

def main():
    img_sample_obj = ImageSample(r"images\buildings.jfif")

    generate_random_samples(img_sample_obj=img_sample_obj)
    samples_to_folder(img_sample_obj.sample_list)

# -------------------------------------------------

if __name__ == "__main__":
    main()
