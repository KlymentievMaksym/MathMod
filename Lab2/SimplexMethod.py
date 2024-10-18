import numpy as np

# "Enter the number of limits: "
limits = int(input())

# Enter the number of main coefficients (x1, x2, ..., xn): 
main_coefs = list(map(int, input().split()))
main_coefs_len = len(main_coefs)
for main_coef_index in range(main_coefs_len):
    main_coefs[main_coef_index] = -main_coefs[main_coef_index]
# Z - a1*x1 - a2*x2 - ... - an*xn = 0
main_coefs.insert(0, 1)
main_coefs.extend([0] * (limits + 2))
main_coefs = [main_coefs]

for limit in range(limits):
    # "Enter the coefficients for the limit {}: ".format(limit + 1)
    limit_coefs = list(map(int, input().split()))

    limit_coefs.insert(0, 0)
    limit_coefs.extend([0] * (limits + 2))
    limit_coefs[limit + main_coefs_len + 1] = 1
    # a1*x1 + a2*x2 + ... + an*xn + s{limit+1} = b

    # "Enter the limit value: "
    limit_coefs[-2] = int(input())
    limit_coefs = [limit_coefs]

    main_coefs.extend(limit_coefs)

main_coefs = np.array(main_coefs, dtype='float64')

# k = 0
while main_coefs[0, 1:main_coefs.shape[1]-2].min() < 0:
    # print(main_coefs)#[0, -2])
    pivot_column_index = main_coefs[0, :].argmin()
    pivot_column = main_coefs[:, pivot_column_index]
    for ratio_index in range(limits):
        main_coefs[ratio_index+1, -1] = main_coefs[ratio_index+1, -2] / pivot_column[ratio_index+1]
    ratios = main_coefs[1:, -1]
    while ratios.min() <= 0:
        ratios[ratios.argmin()] = ratios.max()
    pivot_row_index = ratios.argmin() + 1
    pivot_element = main_coefs[pivot_row_index, pivot_column_index]
    main_coefs[pivot_row_index] = main_coefs[pivot_row_index] / pivot_element
    for row_index in range(limits + 1):
        if row_index != pivot_row_index:
            main_coefs[row_index] = main_coefs[row_index] - main_coefs[pivot_row_index] * main_coefs[row_index, pivot_column_index]


print(main_coefs[0, -2])
