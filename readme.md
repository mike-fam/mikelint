# Mikelint
Yet another attempt at a static analysis tool for CSSE1001.

## Prerequisite
You need Python 3.9 or above to run this project. Python 3.8 or below will not work.

## Setting up
1. Clone this repo `git clone https://github.com/mike-fam/mikelint.git`
2. cd into the repo and create a new virtual environment
    ```shell
    cd mikelint
    python3.9 -m venv venv && source venv/bin/activate
    ```
3. Install the required packages
   ```shell
   pip install -r requirements.txt
   ```

## How to use the linter
1. Create a config YAML file, an example of a config file is at `config.example.yaml`. 
   The key-values of the YAML file go from Criteria > Sub-criteria > Analyser/checker.
   
2. Run `python run.py -c config.yaml -s some_file.py`, with `config.yaml` being your 
   configuration file and `some_file.py` being the file to run the analyser on.
   
## How to contribute
TODO