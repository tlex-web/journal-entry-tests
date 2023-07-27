This is a template jupyter notebook to perform journal entry tests upon request of the financial audit team.

## Instructions

Make sure that you are not saving this repository on a network drive, as this may cause issues with the virtual environment because the resolved network path may differ from the path used to create the virtual environment.

First of all, you need to download the journal entry test template from the [JET repository](https://github.com/tlex-web/journal-entry-tests.git) and save it to your local machine. To do so, run the following command:

```bash
git clone https://github.com/tlex-web/journal-entry-tests.git
```

You need to create a virtual environment for python using the `venv` module. To do so, open a command prompt and run the following command, assuming you are in the root folder of the JET repository and have at least Python 3.10 installed on your machine:

```bash
python.exe -m venv venv
```

Once the virtual environment is created, you need to activate it. To do so, run the following command:

```bash
\venv\scripts\activate.bat
```

Once the virtual environment is activated, you need to install the dependencies. To do so, run the following command:

```bash
pip install -r requirements.txt
```

You can now run the notebook. To do so, run the following command:

```bash
jupyter-lab
```

Once the notebook is running, you can open the notebook by clicking on the `JET.ipynb` file in the file browser.

**_or_**

You can also open and run the notebook directly in Visual Studio Code. To do so, open the `JET.ipynb` file in Visual Studio Code and click on the `Run Cell` button in the top right corner of the notebook.

## Input

The following information is required to run the journal entry test:

- **Journal Entry Test Date**: The date the journal entry test was performed.
- **Journal Entry Test Performed By**: The name of the person who performed the journal entry test.
- **Journal Entry Test Reviewed By**: The name of the person who reviewed the journal entry test.
- **Journal Entry Test Reviewed Date**: The date the journal entry test was reviewed.
- **General Ledger**: The general ledger of the company.
- **Trial Balance**: The trial balance of the company.

The `General Ledger` and `Trial Balance` files must be in CSV format. The `General Ledger` file must at least contain the following columns:

- **Account**: The account number.
- **Account Description**: The account description.
- **Debit**: The debit amount.
- **Credit**: The credit amount.
- **Date**: The date of the transaction.
- **Journal Entry**: The journal entry number.
- **Journal Entry Description**: The journal entry description.

The `Trial Balance` file must at least contain the following columns:

- **Account**: The account number.
- **Account Description**: The account description.
- **Debit**: The debit amount.
- **Credit**: The credit amount.

The `General Ledger` and `Trial Balance` files must be saved in the `data` folder. The `General Ledger` file must be named `general_ledger.csv` and the `Trial Balance` file must be named `trial_balance.csv`.

## Output

The notebook is designed to automatically generate the following file structure:

```
.
├── JET.ipynb
├── JET.pdf
├── JET.html
├── /data/
    ├── /data/general__ledger.csv
    ├── /data/trial_balance.csv
    ├── /data/data.csv
├── /helpers/helpers.py
└── /results/
    ├── /JB0/results.xlsx | no_result.txt
    ├── /JB1/results.xlsx | no_result.txt
    ├── /JB2/results.xlsx | no_result.txt
    ├── /JB3/results.xlsx | no_result.txt
    ├── /JB4/results.xlsx | no_result.txt
    ├── /JB5/results.xlsx | no_result.txt
    ├── /JB6/results.xlsx | no_result.txt
    ├── /JB7/results.xlsx | no_result.txt
    ├── /JB8/results.xlsx | no_result.txt
    ├── /JB9/results.xlsx | no_result.txt
    └── /JB10/results.xlsx | no_result.txt
```

The `JET.ipynb` notebook is the template notebook that you downloaded from the JET repository. The `JET.pdf` and `JET.html` files are copies of the notebook in PDF and HTML format. The `data` folder contains the data used to perform the journal entry test. The `results` folder contains the results of the journal entry test. The results are stored in Excel format. If no results are found for a journal entry test, a `no_result.txt` file is created in the corresponding journal entry test folder. The `helpers.py` file contains the helper functions used to perform the journal entry test.

## Dependencies

The following dependencies are required to run the journal entry test:

- [Python 3.10](https://www.python.org/downloads/release/python-310/)
- [Jupyter Notebook latests release](https://jupyter.org/)
- [Pandas latests release](https://pandas.pydata.org/)
- [Numpy latests release](http://www.numpy.org/)
- [Matplotlib latests release](https://matplotlib.org/)
- [Seaborn latests release](https://seaborn.pydata.org/)
- [XlsxWriter latests release](https://xlsxwriter.readthedocs.io/)

Please note that the notebook is designed to automatically install the required dependencies if they are not already installed on your machine. In case the automatic installation fails, please install the dependencies manually using the `pip install` command to install the dependencies listed in the `requirements.txt` lock file.
