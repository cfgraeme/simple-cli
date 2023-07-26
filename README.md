# Simple CLI

## Running and Testing

This project has been dockerized to ensure a reasonable level of predictability across different user setups.

To run, make sure docker is installed first, then use the docker-compose commands:

docker-compose run cli
docker-compose run tests

### Running and Testing Without Docker

Install python 3.11, then run the following:

```sh
pip install -r requirements.txt
```

now you can run
```sh
python main.py
```

and

```sh
python -m pytest
```

## Thoughts and Considerations

In order to stay within the time limit and make sure I had working containers, I did not create quite as large of a test suite as I would have liked.

I added some functionality for EXITing the CLI and NOOP operations for empty lines.