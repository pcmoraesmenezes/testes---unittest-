import requests


class People():
    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name
        self.data_obtained = False

    def obtain_all_data(self):
        answer = requests.get('https://jsonplaceholder.typicode.com/users/1')

        if answer.ok:
            return 'Connected'
        return 'Error 404'
