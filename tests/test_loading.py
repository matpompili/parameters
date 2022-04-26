"""Test correct loading of the yaml file into the Parameters class."""
import subprocess
import unittest
from typing import Any, Optional

from parameters import Parameters

# from quantify_core.data.handling import gen_tuid

# from lib.data_saving import unix_timestamp_from_tuid
# from lib.parameters import Parameters
# from nodes.example_node.parameters import update_parameter_file


class TestLoadingParameters(unittest.TestCase):
    """TestParameters class."""

    parameters: Optional[Parameters] = None
    files_involved = [
        "tests/test_yaml_folder/group_a.yaml",
        "tests/test_yaml_folder/group_b.yml",
    ]

    def setUp(self) -> None:
        self.parameters: Parameters = Parameters(yaml_folder="tests/test_yaml_folder")
        self.assertIsNotNone(self.parameters)

    def tearDown(self) -> None:
        self.parameters = None
        self.assertIsNone(self.parameters)
        for file in self.files_involved:
            subprocess.run(f"git checkout HEAD -- {file}", shell=True, check=True)

    def test_00_load(self):
        self.assertIsNotNone(self.parameters.group_a)
        self.assertIsNotNone(self.parameters.group_b)
        self.assertRaises(AttributeError, lambda: self.parameters.group_c)

    def test_01_scalar(self):
        self.assertEqual(self.parameters.group_a.a_int, 1)
        self.assertIsInstance(self.parameters.group_a.a_int, int)
        self.assertEqual(self.parameters.group_a.a_float, 1.0)
        self.assertIsInstance(self.parameters.group_a.a_float, float)
        self.assertEqual(self.parameters.group_a.a_bool, True)
        self.assertIsInstance(self.parameters.group_a.a_bool, bool)

        self.assertEqual(self.parameters.group_b.b_int, -1)
        self.assertIsInstance(self.parameters.group_b.b_int, int)
        self.assertEqual(self.parameters.group_b.b_float, -1.0)
        self.assertIsInstance(self.parameters.group_b.b_float, float)
        self.assertEqual(self.parameters.group_b.b_bool, False)
        self.assertIsInstance(self.parameters.group_b.b_bool, bool)

    def test_02_dict(self):
        pass


    # def test_01_load_overrides(self):
    #     """Test Parameters.load() overrides local copy."""
    #     self.parameters.test_a["a_new_key"] = 42
    #     self.assertEqual(self.parameters.test_a["a_new_key"], 42)
    #     # Test that calling load() again ovverides the local copy.
    #     self.parameters.load()
    #     self.assertNotIn("a_new_key", self.parameters.test_a)

    # def test_02_values(self):
    #     """Test the loaded values."""
    #     self.assertEqual(self.parameters.test_a["a_int"], 1)
    #     self.assertEqual(self.parameters.test_b["b_int"], -1)

    #     self.assertEqual(self.parameters.test_a["a_float"], 1.0)
    #     self.assertEqual(self.parameters.test_b["b_float"], -1.0)

    #     self.assertEqual(self.parameters.test_a["a_bool"], True)
    #     self.assertEqual(self.parameters.test_b["b_bool"], False)

    # def test_03_update_values(self):
    #     """Test that the update function works."""
    #     self.assertIsNotNone(self.parameters.calibration)

    #     # Test automatic TUID generation works
    #     update_tuid = gen_tuid()
    #     update_parameter_file("test_a", {"a_int": 2}, add_cal_text="test")
    #     self.parameters.load()
    #     self.assertEqual(self.parameters.test_a["a_int"], 2)
    #     self.assertEqual(self.parameters.calibration["cal_a_int_value"], 2)
    #     self.assertAlmostEqual(
    #         unix_timestamp_from_tuid(self.parameters.calibration["cal_a_int_tuid"][0:26]),
    #         unix_timestamp_from_tuid(update_tuid),
    #         delta=0.1,
    #     )
    #     self.assertEqual(self.parameters.calibration["cal_a_int_tuid"][26:31], "-test")

    #     # Test delayed update TUID makes sense
    #     update_tuid = gen_tuid()
    #     delay = 5.0
    #     time.sleep(delay)
    #     update_parameter_file("test_a", {"a_int": 0}, add_cal_text="test")
    #     self.parameters.load()
    #     self.assertAlmostEqual(
    #         unix_timestamp_from_tuid(self.parameters.calibration["cal_a_int_tuid"][0:26]),
    #         unix_timestamp_from_tuid(update_tuid) + delay,
    #         delta=0.1,
    #     )

    #     # Test manual TUID generation works
    #     update_tuid = gen_tuid()
    #     update_parameter_file("test_a", {"a_int": 3}, add_cal_text="test", cal_tuid=update_tuid)
    #     self.parameters.load()
    #     self.assertEqual(self.parameters.test_a["a_int"], 3)
    #     self.assertEqual(self.parameters.calibration["cal_a_int_value"], 3)
    #     self.assertEqual(self.parameters.calibration["cal_a_int_tuid"][0:26], update_tuid)

    #     # Test that updating float works
    #     update_parameter_file("test_b", {"b_float": -1.5})
    #     self.parameters.load()
    #     self.assertAlmostEqual(self.parameters.test_b["b_float"], -1.5, delta=1e-14)

    #     # Test that updating bool works
    #     self.assertEqual(self.parameters.test_b["b_bool"], False)
    #     update_parameter_file("test_b", {"b_bool": True})
    #     self.parameters.load()
    #     self.assertEqual(self.parameters.test_b["b_bool"], True)

    # def test_04_check_yamllint(self):
    #     """Make sure the updates keep yamllint happy."""
    #     call = subprocess.run(
    #         "pipenv run yamllint -s nodes/example_node/parameters", shell=True, capture_output=True, check=False
    #     )
    #     if call.returncode != 0:
    #         print(call.stdout)
    #         print(call.stderr)

    #     self.assertEqual(call.returncode, 0)


if __name__ == "__main__":
    unittest.main()
