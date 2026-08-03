import kagglehub
from kagglehub import KaggleDatasetAdapter

path = kagglehub.dataset_download("desolution01/messy-employee-dataset")
file_path = "C:/Users/adigo/Desktop/Hobby/Data_analysis/Messy employee data/Messy_Employee_dataset.csv"

df = kagglehub.load_dataset(
  KaggleDatasetAdapter.PANDAS,
  "desolution01/messy-employee-dataset",
  file_path)

df.head()