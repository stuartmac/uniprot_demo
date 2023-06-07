import unittest
from uniprot_demo.protein_domains import get_protein_domains

class TestProteinDomains(unittest.TestCase):

    def test_get_protein_domains(self):
        uniprot_id = "P42345"
        domains_df = get_protein_domains(uniprot_id)
        self.assertIsNotNone(domains_df)
        self.assertGreater(len(domains_df), 0)
        self.assertIn("Start", domains_df.columns)
        self.assertIn("End", domains_df.columns)
        self.assertIn("Description", domains_df.columns)

if __name__ == "__main__":
    unittest.main()
