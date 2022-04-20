"""TODO docstring

Matteo Pompili, 2022
"""

import pathlib
from typing import Union
from addict import Addict

from ruamel.yaml import YAML

from .yaml_utils import _lint_yaml_file
import logging

_logger = logging.getLogger("parameters")


class Parameters(Addict):
    """TODO docstring"""

    # RESTRICTED_KEYS = ["load, _yaml_folder"]

    def __init__(self, yaml_folder: Union[str, pathlib.Path]):
        super().__init__()
        if isinstance(yaml_folder, str):
            yaml_folder = pathlib.Path(yaml_folder)
        self._yaml_folder : pathlib.Path = yaml_folder
        self._did_load : bool = False

    def load(self):
        """Load parameters into the object by parsing the yaml files.

        Raises:
            FileNotFoundError: the folder containing the yaml files does not exist.
        """
        _logger.info("Loading parameters from file")

        yaml = YAML()

        if self._yaml_folder.exists():
            for file in self._yaml_folder.glob("*.yaml"):
                with open(file, "r", encoding="UTF-8") as file_handle:
                    loaded_dict = yaml.load(file_handle)
                    file_name = file.name.removesuffix(".yaml")
                    if loaded_dict is not None:
                        self.__setattr__(file_name, yaml.load(file_handle))
        else:
            raise FileNotFoundError()

        self._did_load = True

