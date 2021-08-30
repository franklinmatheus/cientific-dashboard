import pandas as pd

scopus = pd.read_csv("data_cleaned.txt",sep="\t",
    on_bad_lines='warn',
    quotechar="\"",
    engine="python",
    verbose=True,
    skip_blank_lines=True)