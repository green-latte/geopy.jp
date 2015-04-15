import sys
from location import Location

if __name__ == "__main__":
    argvs = sys.argv
    if len(argvs) != 2:
        print('Usage: # python %s filename' % argvs[0])
        quit()

    zipcode = argvs[-1]
    location = Location(zipcode)
    print(location.address)