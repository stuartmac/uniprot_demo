import json
import os

DEFAULT_CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.json")

def read_config(config_file_path=None):
    """
    Read the configuration file from the specified path or the default path if no path is specified.

    Args:
        config_file_path (str, optional): The path to the custom configuration file. Defaults to None.

    Returns:
        dict: The configuration as a dictionary.
    """
    if config_file_path is None:
        config_file_path = os.environ.get("MY_UNIPROT_MODULE_CONFIG", DEFAULT_CONFIG_FILE)

    with open(config_file_path, "r") as f:
        return json.load(f)
