import os
import pandas as pd
from preprocess.XmlProcessor import XmlProcessor


class XmlTransformer:
    def __init__(self, data, column_mappings):
        self.processor = XmlProcessor(data, column_mappings)

    def transform(self, output_dir=None, filename=None):
        processed_data = self.processor.process_data()

        if output_dir:
            full_path = os.path.join(output_dir, filename)
            if not os.path.exists(output_dir):
                os.makedirs(output_dir)
            processed_data.to_csv(full_path, index=False)
        else:
            print("Transformation completed, but no output file was specified.")

        return processed_data


def xml_transformation(data):
    column_mappings = {
        ('shoton', 'team', 'home'),
        ('shoton', 'team', 'away'),
        ('possession', 'homepos', 'home'),
        ('possession', 'awaypos', 'away')
    }

    transformer = XmlTransformer(data, column_mappings)
    return transformer.transform("../data/transform/", "match_details_transformed.csv")


if __name__ == "__main__":
    pd_csv = pd.read_csv('../data/match_details.csv')
    transformation = xml_transformation(pd_csv)