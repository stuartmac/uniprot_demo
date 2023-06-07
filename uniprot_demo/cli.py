"""Console script for uniprot_demo."""
import os
import sys
import click
from .protein_domains import get_protein_domains


@click.command()
@click.argument('uniprot_id')
@click.option('-o', '--output', type=click.Path(), help='Output file path for the results in CSV format')
@click.option('--config', type=click.Path(), help='Custom configuration file path')
def main(uniprot_id, output, config):
    """Query protein domains from the UniProt API."""
    if config is not None:
        os.environ["MY_UNIPROT_MODULE_CONFIG"] = config

    domains_df = get_protein_domains(uniprot_id)

    if output:
        domains_df.to_csv(output, index=False)
    else:
        click.echo(domains_df)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
