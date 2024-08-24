# Python katas

## Running a Python file
To run a Python file, simply run `python3` followed by the file path and name, e.g. to run `even_numbers.py`:
```bash
python3 lib/even_numbers.py
```
For the majority of the files in this repo there will be no output since they are simply functions that are tested and are not called outside of the tests.

## Virtual environments
To create a virtual environment, e.g. called katas_venv:
```bash
python3 -m venv .katas_venv
```

To activate a virtual environment, e.g. to activate the already created, katas_venv:
```bash
python3 -m source .katas_venv/bin/activate
```

To deactivate a virtual environment:
```bash
deactivate
```

## Pytest
NOTE: if pytest is not installed, run `python3 -m pip install pytest`

To run all tests, run `pytest`

To run all with verbose messaging, run `pytest -v`

To run a specific test, run, e.g. `pytest tests/test_even_numbers.py`

To run a specific test with verbose messaging, run, e.g. `pytest -v tests/test_even_numbers.py`

To run a specific test function (scenario), run, e.g. `pytest tests/test_even_numbers.py::test_get_last_n_even_numbers_returns_a_list_of_the_last_n_numbers_from_input_list`

To run all tests that match a regex pattern, run, e.g. `pytest -k "eve"`
This example will run `test_even_numbers.py` and `test_dna_reverse_complement.py`.