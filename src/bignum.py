# Print out 2 to the 65536 power

# bignum = pow(2,1024)
# math.pow(2,1024) results in an overflow error
# the maximum representable value is
# 1 * 2 ^ ( 2 ^ 10 - 1 )
# which is 2 ^ 1023
print(2**65536)