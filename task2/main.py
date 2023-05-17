from os import path
import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, disk_file_path, file_name):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
        }
        upload_url = r'https://cloud-api.yandex.net/v1/disk/resources/upload'
        params = {"path": file_name, "overwrite": "true"}
        # print(params)
        response = requests.get(upload_url, headers=headers, params=params)
        response_data = response.json()

        href = response_data["href"]
        # print(href)
        response = requests.put(href, data=open(disk_file_path, 'rb'))
        print(response.status_code)


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    file_name = 'push_me.txt'
    path_to_file = path.join('files', file_name)

    token = ''

    uploader = YaUploader(token)
    result = uploader.upload(path_to_file, file_name)
