"""
Capital One, has two levels of customer acquisition strategies for customers that are opening credit cards.
For high spending customers, Capital One will give clients a one time bonus of 800 dollars.
For everyone else, they give a 100 dollar bonus.

Write a function in Python that takes a list of client spends as floats
and figures out the threshold to divide the high spending vs low spending customers.

SOLUTION

Let's look at the problem in terms of benefits. We value customers with high costs because
we get more from commissions or interest.
Therefore, it is important for us to attract and retain such customers.
When calculating bonuses, we should be guided by the fact that we will not only receive new customers
(or leave old ones) but also receive at least as much as we spent.

We will consider the threshold based on customer spending data (this can be aggregated data
for a month or a one-time payment of a client).

Next, we will encounter some problems:

1) there can be a lot of data and one machine
can not cope with their processing using traditional approaches.

2) It is necessary to take into account outliers in the data:
some customers may spend more than any other customer once or several times on a regular basis,
but this is an exception
(imagine that the richest person in the world uses this service and spends as much as no one can not).

We need to either get rid of outliers or use methods that will not suffer from them.

For example, we can take the 3rd quartile (Q3) -
this is the average value between the median and the highest value in the data set.
It is also known as the upper quartile or the 75th empirical quartile,
and 75% of the data is below this point.
Alternatively we can take any other percentile (for example, the 80th).

The advantage of choosing the nth percentile is that we can predict how many bonuses we have to pay.
If we take the 3rd quartile, we can assume that 75% of the costs of future customers
will fit the criterion for a bonus of $ 100.
This gives you the opportunity to calculate which percentile is the most beneficial for you.

TODO: Different output than the expected
"""

import math
import numpy as np


def get_threshold(spends, margin=0.1):
    median = np.median(spends)
    percentile_n = (800 - median * margin)

    if percentile_n > 1:
        percentile_n = 1
    elif percentile_n < 0:
        percentile_n = 0.1

    percentile_n *= 100
    percentile_n = math.ceil(percentile_n)

    return  np.percentile(spends, percentile_n)


input = [704, 704, 795, 1103, 1127, 1461, 1528, 1559, 1658, 1823, 2011,
         2031, 2063, 2154, 2291, 2293, 2335, 2338, 2517, 2526, 2977, 3014,
         3100, 3335, 3359, 3532, 3543, 3561, 3858, 3977, 4097, 4120, 4164,
         4339, 4463, 4549, 4637, 4785, 5132, 5199, 5360, 5799, 6027, 6028,
         6082, 6194, 6242, 6660, 6940, 6959]

print("\n\t\t ============== Test Cases ==============")

print("\n--------------------Test case A-----------------------")
result = get_threshold(input)
print('Input : THE ABOVE INPUT')
print("Expected result: $4223.5")
print("Actual result   {}".format(result))
result = 0