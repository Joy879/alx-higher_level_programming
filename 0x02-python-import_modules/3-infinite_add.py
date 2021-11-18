#!/usr/bin/python3
if __name__ == "__main__":
    """Find the sum of arguments."""
    import sys
    sum = 0
    if (len(sys.argv) > 1):
        for i in range(1, len(sys.argv)):
            sum += (int(sys.argv[i]))
    print("{:d}".format(sum))
