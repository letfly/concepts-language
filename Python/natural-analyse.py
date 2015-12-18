import profile

def profile_test():
    total = 1
    for i in xrange(10):
        total = total * (i+1)
        print total
    return total

if __name__ == "__main__":
    profile.run("profile_test()")
