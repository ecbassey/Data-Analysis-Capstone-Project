class Analyzer:
    def __init__(self, df):
        self.df = df
        

    def airline_reliability(self):
        df = self.df.copy()
        df['arr_delay'] = df['arr_delay'] / df['arr_flights']

        return (
            df.groupby('carrier_name')
            #self.df.groupby(['carrier_name', 'carrier'])
            .agg(avg_delay=('arr_delay', 'mean'),
                 delay_rate=('arr_del15', 'mean'),
                 total_flights=('arr_flights', 'sum'))
            .sort_values(by='delay_rate')
        )
    
    def delays_by_hour(self):
        return (
            self.df.groupby('hour')['arr_delay']
            .mean()
            .sort_index()
        )

    def month_with_highest_delay2(self):
        result = (
            self.df.groupby('month')['arr_delay']
            .mean()
            .sort_values(ascending=False)
        )
        return result
    

    def month_with_highest_delay(self):
        df = self.df.copy()
    
        #df['is_delayed'] = df['arr_delay'] > 15
    
        result = (
            df.groupby('month')
            .agg(
                avg_delay=('arr_delay', 'mean'),
                delay_rate_2=('arr_del15', 'mean'),
                total_flights=('month', 'count')
            )
            .sort_values(by='delay_rate_2', ascending=False)
            
        )    
        return result


    def airport_bottlenecks(self):
        #df = self.df.copy()
    
        self.df['arr_delay'] = self.df['arr_delay'] / self.df['arr_flights'] 
    
        return (
            self.df.groupby('airport')
            .agg(
            avg_delay=('arr_delay', 'mean'),
            traffic=('arr_flights', 'sum')
            )
            .sort_values(by='avg_delay', ascending=False)
        )


    def airport_bottlenecks2(self):
        #df = self.df.copy()
    
        #self.df['arr_delay'] = self.df['arr_delay'] / self.df['arr_flights'] 
    
        return (
            self.df.groupby(['airport', 'airport_name'])
            .agg(
            avg_delay=('arr_delay', 'mean'),
            traffic=('arr_flights', 'sum')
            )
            .sort_values(by='traffic', ascending=False)
        )


# df.groupby(['airport', 'airport_name'])

    # def airport_bottlenecks(self):
    #     return (
    #         self.df.groupby('airport')
    #         .agg(avg_delay=('arr_delay', 'mean'),
    #              traffic=('arr_delay/arr_flights', 'mean'))
    #         .sort_values(by='avg_delay', ascending=False)
    #     )
    
    def airport_bottlenecks_test(self):
        return (
            self.df.groupby('airport')
            .agg(avg_delay=('arr_delay', 'mean'),
                 traffic=('airport', 'count'))
            .sort_values(by='avg_delay', ascending=False)
        )
    

    