from containerBank import containerBankSapp70
from containerBank import containerBankIFlow300

''' Sapphire 70 bar
reserve # 0 or 1
manifoldType # 'end , 'center', 'u'
cylNum # number of cylinders
cylSize # 15, 30, 34, 45, 60, 80, 120, 150, 180
leftCylNum # number of cylinders in the 'left' or 'first row' (0 for end manifolds and modular)
manifoldConnectionType # 'w' or 'th'
actualFill # kg of novec in each cylinder
dischargeTime #seconds
'''

def testModular():
    print('\n----testing modular systems----')
    containerBank1 = containerBankSapp70(0, 'end', 1,60, 0, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    
    containerBank1 = containerBankSapp70(1, 'end', 1,15, 0 ,'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    containerBank1 = containerBankSapp70(1, 'center', 1,15, 0, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()

    containerBank1 = containerBankSapp70(1, 'end', 1,60, 0, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    containerBank1 = containerBankSapp70(1, 'center', 1,60, 0, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()

def testEndManifold():
    print('\n----testing end manifolded systems----')
    containerBank1 = containerBankSapp70(0, 'end', 2, 15, 0, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    containerBank1 = containerBankSapp70(0, 'end', 3, 15, 0, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'end', 4, 15, 0, 'w')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'end', 5, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'end', 12, 15, 0, 'w')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(1, 'end', 5, 60, 0, 'w')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(1, 'end', 2, 60, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(1, 'end', 5, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
def testCenterManifold():
    print('\n----testing center manifolded systems----')
    containerBank1 = containerBankSapp70(0, 'center', 6, 15, 3, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'center', 3, 15, 2, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(1, 'center', 2, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(1, 'center', 5, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
def testUManifold():
    print('\n----testing U manifolded systems----')
    containerBank1 = containerBankSapp70(0, 'u', 2, 15, 2, 'th')#, 15, 10)
    containerBank1.calculateAllSections()
    containerBank1.printManifold()
    containerBank1.calculteDimensions()
    containerBank1.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'u', 4, 60, 2, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'u', 9, 15, 5, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(1, 'u', 5, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(2, 'u', 5, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
    containerBank2 = containerBankSapp70(0, 'u', 14, 15, 0, 'th')#, 15, 10)
    containerBank2.calculateAllSections()
    containerBank2.printManifold()
    containerBank2.calculteDimensions()
    containerBank2.printContainerBankSize()
    
testModular()
testEndManifold()
testCenterManifold()
testUManifold()

''' iFlow 300 bar
cylNum #number of cylinders
cylSize # 80, 140
manifoldConnectionType # 'th' or 'w'
reserve # 1 or 0

'''
def testHose():
    inergenManifold = containerBankIFlow300(1,80,'th',0)
    
    inergenManifold = containerBankIFlow300(2,80,'th',0) 
    
    inergenManifold = containerBankIFlow300(3,80,'th',0) 
    # three in a chain(120s) or 2 and 1(120s,60s)
    
    inergenManifold = containerBankIFlow300(4,80,'th',0) 
    # can depend on time
    # 2+2 with tee or 3+1 with tee
    
    inergenManifold = containerBankIFlow300(5,80,'th',0)
    # can be manifolded or with hose
    # if 120s can be only hose otherwise has to be manifolded
    
    inergenManifold = containerBankIFlow300(6,80,'th',0)
    
    inergenManifold = containerBankIFlow300(1,80,'th',1)
    
    inergenManifold = containerBankIFlow300(2,80,'th',1)
    
    inergenManifold = containerBankIFlow300(3,80,'th',1)
    
    inergenManifold = containerBankIFlow300(4,80,'th',1)
    
    inergenManifold = containerBankIFlow300(5,80,'th',1)
    
    inergenManifold = containerBankIFlow300(6,80,'th',1)
    
    
