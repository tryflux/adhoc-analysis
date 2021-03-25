from typing import List, Dict
from decimal import Decimal
import pandas as pd


def adoption_uplift(
        population_size: int, uplift_amount: int,
        adoption_breakpoints: List[int] = None
) -> Dict[int, str]:
    adoption_breakpoints = adoption_breakpoints or [1, 5, 10, 25, 50, 100]

    return {
        f'{i}%': pounds_minor_to_major(uplift_amount * population_size * i/100)
        for i in adoption_breakpoints
    }

def pounds_minor_to_major(money: int) -> str:
    return f'£{Decimal(money)/Decimal(100):,.2f}'


def remove_outliers(df: pd.DataFrame, by: str, using: str, quantile: float = 0.975):
    """ Removes outliers using the 'by' column values with a value in 'using' outside the quantile specified.
        
        For example the following will remove all rows for customers who have a txn_amount outside the 97.5% quantile:
        remove_outliers(df, by='customer_id', using='txn_amount')
        
    """
    value_cap = df[using].quantile(quantile)
    outliers = df[df[using] > value_cap][by]
    
    return df[~df[by].isin(outliers)]
