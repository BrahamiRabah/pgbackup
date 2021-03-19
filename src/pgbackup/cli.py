from argparse import Action,ArgumentParser

class DriverAction(Action):
    def __call__(self, parser, namespace, values, option_string=None):
        driver, destination = values
        namespace.driver = driver.lower()
        namespace.destination = destination

def create_parser():
    parser = ArgumentParser(description="""
    Backup postgresql database locally or to the S3 bucket
    """)
    parser.add_argument("url", help="URL of the database to backup")
    parser.add_argument("--driver",
            help="how to store the bucket",
            nargs=2,
            action=DriverAction,
            required=True)

    return parser

