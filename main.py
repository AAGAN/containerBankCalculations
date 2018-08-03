import sys
from containerBank import containerBankSapp70

''' Sapphire 70 bar
reserve # 0 or 1
manifoldType # 'end , 'center', 'u'
cylNum # number of cylinders
cylSize # 15, 30, 34, 45, 60, 80, 120, 150, 180
leftCylNum # number of cylinders in the 'left' or 'first row' (0 for end manifolds and modular)
manifoldConnectionType # 'w' or 'th'
'''
error = 0
if len(sys.argv) == 7:
    reserve = sys.argv[1]
    manifoldType = sys.argv[2]
    cylNum = sys.argv[3]
    cylSize = sys.argv[4]
    leftCylNum = sys.argv[5]
    manifoldConnectionType = sys.argv[6]
else:
    print(" wrong number of arguments provided!")
    print(" reserve # 0 or 1 \n manifoldType # 'end , 'center', 'u' \n cylNum # number of cylinders \n cylSize # 15, 30, 34, 45, 60, 80, 120, 150, 180 \n leftCylNum # number of cylinders in the 'left' or 'first row' (0 for end manifolds and modular) \n manifoldConnectionType # 'w' or 'th'")
    error = 1    

def main():
    containerBank = containerBankSapp70(int(reserve), manifoldType, int(cylNum),int(cylSize), int(leftCylNum), manifoldConnectionType)
    containerBank.calculateAllSections()
    containerBank.printManifold()
    containerBank.calculteDimensions()
    containerBank.printContainerBankSize()
    
if __name__ == '__main__' and error == 0:
    main()