import pandas as pd

def load_dataset(csv_name):
  if csv_name == './data/train_mini_pjt.csv':
    train = pd.read_csv(csv_name)
    return train

  elif csv_name == './data/test_V2.csv':
    test = pd.read_csv(csv_name)
    return test
