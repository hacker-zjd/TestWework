import os
import yaml


class YamlUntil:
    def __init__(self):
        self._path = os.path.join(os.path.dirname(__file__), "../data/data.yml")
        if not os.path.exists(self._path):
            raise FileNotFoundError("No such file: data.yml")
        with open(self._path) as f:
            self.data = yaml.safe_load(f)

    def get_data(self) -> dict:
        return self.data['data']


# if __name__ == '__main__':
#     until = YamlUntil()
#     data = until.get_data()
#     print(data['info'][0][0])
