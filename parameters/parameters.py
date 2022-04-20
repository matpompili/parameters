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

        self._load(yaml_folder)


    def _load(self, yaml_folder: pathlib.Path):
        """Load parameters into the object by parsing the yaml files.

        Raises:
            FileNotFoundError: the folder containing the yaml files does not exist.
        """
        yaml = YAML()

        if yaml_folder.exists():
            for suffix in ["yaml", "yml"]:
                for file in yaml_folder.glob(f"*.{suffix}"):
                    file_name = file.with_suffix("").name
                    with open(file, "r", encoding="UTF-8") as file_handle:
                        loaded_dict = yaml.load(file_handle)
                        if loaded_dict is not None:
                            self.__setattr__(file_name, Addict(loaded_dict))
        else:
            raise FileNotFoundError(f"The folder {yaml_folder} does not exist.")
