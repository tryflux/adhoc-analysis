import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency
    
def chi_assoc(var1, var2, count_var, data, alpha):
    df = data
    print(df.head(3))
    # generate Contingency Table for the two variables
    cont_table=pd.pivot_table(df,values=[count_var],
                                index=[var1],columns=[var2],
                                aggfunc=np.sum)
    print(cont_table)
    # replace missing value with zeros
    cont_table2=cont_table.replace(np.nan,0)
    xsq,pval,dof,expected=chi2_contingency(cont_table2)
    
    print("")
    print(f"p-value is {pval}")
    print(f"chi-squared value is {xsq}")
    print(f"dof is {dof}")
    print("")

    if pval < alpha:    # alpha value is 0.05 or 5%
        print(f"We can reject the null hypothesis:\nThere is association between {var1} and {var2} significance level {alpha}")
    else:
        print(f"We FAIL to reject null hypothesis:\nThere is no association between {var1} and {var2} at significance level {alpha}")