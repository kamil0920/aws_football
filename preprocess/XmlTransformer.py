import os
import pandas as pd
from preprocess.XmlProcessor import XmlProcessor


class XmlTransformer:
    def __init__(self, csv_path, column_mappings):
        self.data = pd.read_csv(csv_path)
        self.processor = XmlProcessor(self.data, column_mappings)

    def transform(self, output_dir=None, filename=None):
        self.data = self.processor.process_data()

        if output_dir:
            full_path = os.path.join(output_dir, filename)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            self.data.to_csv(full_path, index=False)
        else:
            print("Transformation completed, but no output file was specified.")

        return self.data


def xml_transformation():
    column_mappings = {
        ('shoton', 'team', 'home'),
        ('shoton', 'team', 'away'),
        ('possession', 'homepos', 'home'),
        ('possession', 'awaypos', 'away')
    }

    transformer = XmlTransformer("../data/match_details.csv", column_mappings)
    transformer.transform("../data/transform/", "match_details_transformed.csv")


if __name__ == "__main__":
    xml_transformation()
