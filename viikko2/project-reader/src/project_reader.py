from urllib import request

import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        data = toml.loads(content)["tool"]["poetry"]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(
            data["name"],
            data["description"],
            data["license"],
            data["authors"],
            data["dependencies"],
            data["group"]["dev"]["dependencies"],
        )
