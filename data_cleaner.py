class DataCleaner:
    def clean(self, df):
        df = df.copy()

        # handle missing values
        #df.dropna(inplace=True)
        df = df.dropna(subset=['arr_delay'])

        #create features
        df['is_delayed'] = df['arr_delay'] > 15
        df['delay_minutes'] = df['arr_delay'].clip(lower=0)

        # extract time features
        #df['hour'] = df['CRSDepTime'] // 100
        #df['month'] = df['month']

        return df