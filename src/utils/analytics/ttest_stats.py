from scipy.stats import ttest_ind_from_stats

def ttest_2samp_stats(var_of_interest, group_desc, mean_1, mean_2, std_1, std_2, noobs_1, noobs_2, alpha):

    print(var_of_interest, "mean of group 1 = ", mean_1)
    print(var_of_interest, "mean of group 2 = ", mean_2)
    print("std of group 1 =",std_1)
    print("std of group 2 =",std_2)

    tset, pval = ttest_ind_from_stats(mean1=mean_1, std1=std_1, nobs1=noobs_1,
                         mean2=mean_2, std2=std_2, nobs2=noobs_2)
    print("\np-value is", pval)

    if pval < alpha:    # alpha value is 0.05 or 5%
       print("\nWe can reject the null hypothesis:\nmean {} between {} groups is different at significance level {}".format(var_of_interest, group_desc, alpha))
    else:
      print("\nWe FAIL to reject null hypothesis:\nmean {} between {} groups is not different at significance level {}".format(var_of_interest, group_desc, alpha))