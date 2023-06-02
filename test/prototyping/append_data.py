import numpy as np
import pandas as pd

from plottr.utils.testdata.testdata import get_1d_scalar_cos_data
from plottr.data.datadict import DataDict, datadict_to_dataframe 


dd = get_1d_scalar_cos_data()
df = datadict_to_dataframe(dd)

