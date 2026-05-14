import pandas as pd

df = df.read_csv('../data/lettuce_dataset')

df = df.drop_duplicates()

df.to_csv('../data/lechugas_clean, index=false')

print("proceso de limpieza terminado exitosamente.")