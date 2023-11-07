class Project:
    def __init__(
        self, name, description, license, authors, dependencies, dev_dependencies
    ):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def _stringify_list(self, items):
        if len(items) == 0:
            return "-"

        return "\n" + "\n".join([f"- {item}" for item in items]) + "\n"

    def __str__(self):
        return "\n".join(
            [
                f"Name: {self.name}",
                f"Description: {self.description or '-'}",
                f"License: {self.license}",
                f"Authors: {self._stringify_list(self.authors)}",
                f"Dependencies: {self._stringify_list(self.dependencies)}",
                f"Development dependencies: {self._stringify_list(self.dev_dependencies)}",
            ]
        ).strip()
