from bson import binary
from pip._vendor import requests
from pymongo import MongoClient

client = MongoClient("localhost", 27017)
collection = client["images"]["image"]


def save_image(url, filename):
    image_data = requests.get(url, timeout=10).content
    image1 = {"aa": binary.Binary(image_data)}
    collection.insert_one(image1)


save_image("http://ugcuploadzdg.sun0769.com/wz/uploads/attached/2016/03/b128f2fc1ae336e739570c13d3853de6.png",
           "test1.jpg")
