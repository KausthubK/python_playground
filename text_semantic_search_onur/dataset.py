import pandas as pd


class Pokedex:
    def __init__(self, data_path: str = "./pokemon.csv"):
        df = pd.read_csv(data_path, sep='\t', encoding='utf-16-le')
        df = df[['national_number', 'english_name', 'description', 'primary_type', 'secondary_type']]
        df['description'] = df.description.apply(self.preprocess_descriptions)
        self.df = df
    
    @staticmethod
    def preprocess_descriptions(text: str):
        return text.lower().strip()
        
    def get_indices(self, idx: list[int]) -> pd.DataFrame:
        return self.df.iloc[idx]
        

    