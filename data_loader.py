class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_csv(self):
        import pandas as pd
        df = pd.read_csv(self.file_path)
        return df

    def load_multiple_files(self, file_list):
        import pandas as pd
        dfs = [pd.read_csv(f) for f in file_list]
        return pd.concat(dfs, ignore_index=True)