import unittest
import pandas as pd
from intelliviz import IntelliViz, IntelliVizError
import timeit
import numpy as np
import json
import csv


filepath = open('/Users/ --- /Testing_Datasets/testing_datasets.json').read()
path = '/Users/s.hussey/shane_workspace/DS5010_Spring2023/Project'
testing_datasets = json.loads(filepath)