import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

train = pd.read_csv('./data/train_mini_pjt.csv')
test = pd.read_csv('./data/test_V2.csv')

train.info()
