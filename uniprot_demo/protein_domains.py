import requests
import pandas as pd
from xml.etree import ElementTree
from .config import read_config
import requests_cache

config = read_config()

cache_expiration_seconds = config["cache_expiration_seconds"]
requests_cache.install_cache("uniprot_cache", expire_after=cache_expiration_seconds)

UNIPROT_API_BASE = "https://www.uniprot.org/uniprot/"

def get_protein_domains(uniprot_id):
    """
    Query the UniProt API for protein domains and parse the results into a pandas DataFrame.

    Args:
        uniprot_id (str): The UniProt ID of the protein.

    Returns:
        pandas.DataFrame: A DataFrame containing the protein domains.
    """
    url = UNIPROT_API_BASE + uniprot_id + ".xml"
    response = requests.get(url)
    response.raise_for_status()

    tree = ElementTree.fromstring(response.content)
    namespace = {"uniprot": "http://uniprot.org/uniprot"}

    protein_domains = []

    for feature in tree.findall(".//uniprot:feature[@type='domain']", namespace):
        begin = int(feature.find("uniprot:location/uniprot:begin", namespace).attrib["position"])
        end = int(feature.find("uniprot:location/uniprot:end", namespace).attrib["position"])
        description = feature.attrib["description"]
        protein_domains.append({"Start": begin, "End": end, "Description": description})

    return pd.DataFrame(protein_domains)
