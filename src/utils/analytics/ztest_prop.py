from statsmodels.stats.proportion import proportions_ztest
import numpy as np

def ztest_proportions_2samp(var_of_interest, group_desc, success_1, success_2, noobs_1, noobs_2, alpha):
    print('sample 1 size = ', noobs_1)
    print('proportion of successes 1 = ', success_1/noobs_1)  
    print('sample 2 size = ',noobs_2)
    print('proportion of successes 2 = ', success_2/noobs_2)   

    successes = np.array([success_1, success_2])
    n = np.array([noobs_1, noobs_2])

    stat, pval = proportions_ztest(count=successes, nobs=n,  alternative='two-sided')

    if pval < alpha:  
        print("\nWe can reject the null hypothesis:\n{} between {} groups is different at significance level {}".format(var_of_interest, group_desc, alpha))
    else:
        print("\nWe FAIL to reject the null hypothesis:\n{} between {} groups is not different at significance level {}".format(var_of_interest, group_desc, alpha))
