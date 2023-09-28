import os
import zipfile
from kaggle.api.kaggle_api_extended import KaggleApi

# Инициализация Kaggle API
api = KaggleApi()
api.authenticate()

# Загрузка датасета
dataset_path = "rajyellow46/wine-quality"
api.dataset_download_files(dataset_path, path="./data", unzip=True)

print("Data downloaded successfully!")
