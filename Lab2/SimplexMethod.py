import numpy as np

# "Enter the number of limits: "
limits = int(input())

# Enter the number of main coefficients (x1, x2, ..., xn): 
main_coefs = np.array(map(int, input().split()))
main_coefs_len = len(main_coefs)

main_coefs.insert(0, 1)
main_coefs.extend([0] * (limits + 1))
main_coefs = [main_coefs]

for limit in range(limits):
    # "Enter the coefficients for the limit {}: ".format(limit + 1)
    limit_coefs = list(map(int, input().split()))

    limit_coefs.insert(0, 0)
    limit_coefs.extend([0] * (limits + 1))
    limit_coefs[limit + 3] = 1

    # "Enter the limit value: "
    limit_coefs[-1] = int(input())
    limit_coefs = [limit_coefs]

    main_coefs.extend(limit_coefs)

main_coefs = np.array(main_coefs)

# pivot_column = np.min(main_coefs[1:main_coefs.shape[0]], axis=0)

print(main_coefs)
print()
print(main_coefs[:, 1:main_coefs.shape[1]-1])
print()
# print(pivot_column)
