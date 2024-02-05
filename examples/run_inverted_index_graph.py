import json

import click
from compgraph import algorithms


@click.command()
@click.argument('input_filepath', type=str)
@click.argument('output_filepath', type=str)
def main(input_filepath: str, output_filepath: str) -> None:
    graph = algorithms.inverted_index_graph(input_stream_name=input_filepath,
                                            doc_column='doc_id',
                                            text_column='text',
                                            result_column='tf_idf',
                                            from_file=True)

    result = graph.run()
    with open(output_filepath, 'w') as out:
        for row in result:
            print(json.dumps(row), file=out)


if __name__ == '__main__':
    main()
