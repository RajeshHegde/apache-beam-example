import argparse
import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions

from my_package.transform import filter_cart_requests
from my_package.transform import load_apache_logs

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", dest="input", required=True)
    parser.add_argument("--output", dest="output", required=True)
    args = parser.parse_args()

    with beam.Pipeline(options=PipelineOptions()) as p:
        data = load_apache_logs(p, args.input)
        output = data | "FILTER" >> beam.Filter(filter_cart_requests)

        output | "WRITE" >> beam.io.WriteToText(args.output)


if __name__ == '__main__':
    run()
