"""TODO docstring

Matteo Pompili, 2022
"""

import pathlib
from typing import List, Union

from addict import Addict
from ruamel.yaml import YAML


class Parameters:
    """TODO docstring"""

    def __init__(self, yaml_folder: Union[str, pathlib.Path], auto_load: bool = True):
        super().__init__()
        self._keys: List[str] = []
        self._yaml_folder = pathlib.Path(yaml_folder)
        self._successful_load = False

        if auto_load:
            self.load()

    def load(self):
        """Load parameters into the object by parsing the yaml files.

        Raises:
            FileNotFoundError: the folder containing the yaml files does not exist.
        """
        yaml = YAML()

        if self._yaml_folder.exists():
            for suffix in ["yaml", "yml"]:
                for file in self._yaml_folder.glob(f"*.{suffix}"):
                    file_name = file.with_suffix("").name
                    with open(file, "r", encoding="UTF-8") as file_handle:
                        loaded_dict = yaml.load(file_handle)
                        if loaded_dict is not None:
                            self.__setattr__(file_name, Addict(loaded_dict))
                            self._keys.append(file_name)
        else:
            raise FileNotFoundError(f"The folder {self._yaml_folder} does not exist.")

        yaml = None
        self._successful_load = True

    @property
    def __dict__(self):
        """Return the parameters as a dictionary."""
        if self._successful_load:
            return {key: self.__getattribute__(key) for key in self._keys}
        else:
            return {}

    def __repr__(self) -> str:
        """Return a string representation of the object."""

        if self._successful_load:
            return str(
                f'Parameters object, loading from "{self._yaml_folder}":\n'
                + self.__dict__.__repr__()
            )
        else:
            return f"Parameters object, did not load yaml folder yet."
