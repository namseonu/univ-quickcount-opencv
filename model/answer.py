import re


# the answers of the number of people in the images
def extract_index_from_image_file_name(index):
    match = re.search(r'^(\d+)_', index)
    if match:
        return int(match.group(1))
    else:
        return None


# the answers of the number of people in the images
class Answer:
    IMAGE_PATH = "./image/"

    # there are 5 images in the game set
    IMAGES = [
        IMAGE_PATH + "01_people_by_AdinaVoicu.jpg",
        IMAGE_PATH + "02_people_by_Pexels.jpg",
        IMAGE_PATH + "03_people_by_StefanSchweihofer.jpg",
        IMAGE_PATH + "04_people_by_StockSnap.jpg",
        IMAGE_PATH + "05_people_by_WernerHieber.jpg"
    ]

    ANSWERS = [
        # there are 12 people in the image 01_people_by_AdinaVoicu.jpg
        12,

        # there are 1 person in the image 02_people_by_Pexels.jpg
        1,

        # there are 4 people in the image 03_people_by_StefanSchweihofer.jpg
        4,

        # there are 9 people in the image 04_people_by_StockSnap.jpg
        9,

        # there are 6 people in the image 05_people_by_WernerHieber.jpg
        6,
    ]

    @staticmethod
    def get_images():
        return Answer.IMAGES

    @staticmethod
    def get_answers():
        return Answer.ANSWERS
