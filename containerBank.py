class containerBank:
    
    def __init__(self,
                cylNum,
                cylSize,
                manifoldConnectionType = 'threaded', #'threaded' or 'welded'
                reserve = 0, #1 or 0
                dischargeTime = 10 #s
    ):
        self._cylNum = cylNum
        self._cylSize = cylSize
        self._manifoldConnectionType = manifoldConnectionType
        self._reserve = reserve
        self._manifoldSection = []
        self._errorExist = False
        self._error = 'no error'
        self._endX = 0.0
        self._endY = 0.0
        self._endZ = 0.0
        self._Dx = 0.0 #m length of the container bank
        self._Dy = 0.0 #m width of the container bank
        self._Dz = 0.0 #m height of the container bank
        self._dischargeTime = dischargeTime #s
    
    def printManifold(self):
        if self._errorExist == False:
            print("=====================================================")
            print("number of sections is {}".format(len(self._manifoldSection)))
            #print("-----------------------------------------------------")
            #print("strt,end,len,elv,pipsz,pipsch,pipConcTyp,elb,sT,tT,cpl,dirt,pTp,slcVlv,nozQD,contn")
            #print("-----------------------------------------------------")
            for input in self._manifoldSection:
                print(input)
            #print("-----------------------------------------------------")
        else:
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            print(self._error)
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            
    def printContainerBankSize(self):
        if not self._errorExist:
            print("the container bank is approximately {} m tall, {} m deep and {} m long".format(round(self._Dz),round(self._Dy,3),round(self._Dx)))
            print("the end of the manifold is approximately at ({},{},{}) m".format(round(self._endX,3),round(self._endY,3),round(self._endZ,3)))

#==========================================================================

class containerBankSapp70(containerBank):
    __cylSizeData = [15,30,34,45,60,80,120,150,180]#liter
    __length1Data = [0.6,0.87,0.77,0.97,1.32,1.67,1.2,1.7,1.7]#meter
    __cylDiameterData = [0.204,0.229,0.267,0.267,0.267,0.267,0.360,0.360,0.406]#mm
    __cylHeightData = [0.694,0.972,0.865,1.071,1.425,1.794,1.546,1.888,1.783]#mm
    __length1 = dict(zip(__cylSizeData,__length1Data))
    __cylDiameter = dict(zip(__cylSizeData,__cylDiameterData))
    __cylHeight = dict(zip(__cylSizeData,__cylHeightData))
    __height1 = __length1
    __hoseZ = {25:0.405,50:0.520} #hosediameter mm : hoseheight m
    __hoseX = {25:0.0815,50:0.1442} #hosediameter mm : hoseheight m
    __cvZ = {25:0.073,50:0.096} #checkvalve mm : checkvaleheight m
    __pipeSchedule = 40 #for the first section
    __pipeConnectionType = 'threaded' #for the first section
    __pipeSizeData = [65,80,100,150]#mm
    __maxMassFlowRateData = [36.1,55.9,99.1,223.3]#kg/s
    __pipeSizeSelector = dict(zip(__maxMassFlowRateData,__pipeSizeData))
    __bracketDimension = 0.041 #m
    __15To45ManifoldLength = {2:0.65,3:1.0,4:1.35}#port number:m overall length
    __60To150ManifoldLength = {2:0.808,3:1.416,4:1.924,5:2.432,6:2.940,7:3.448,8:3.956,9:4.464,10:4.972}#port number:m overall length
    
    def __init__(self
                , reserve # 0 or 1
                , manifoldType # 'end , 'center', 'u'
                , cylNum # number of cylinders
                , cylSize # 15, 30, 34, 45, 60, 80, 120, 150, 180
                , leftCylNum # number of cylinders in the 'left' or 'first row' (0 for end manifolds and modular)
                , manifoldConnectionType # 'welded' or 'threaded'
                #, actualFill #kg in each cylinder
                #, dischargeTime #s (10s for Sapp+)
                ):
        __dischargeTime = 10
        super().__init__(cylNum, cylSize, manifoldConnectionType, reserve, __dischargeTime)
        self.__manifoldType = manifoldType
        if cylSize not in self.__cylSizeData:
            print('error: cylinder size is not available.')
        self.__leftCylNum = leftCylNum
        #self.__actualFill = actualFill
        #self.dischargeTime = 10 #s
        #self.avgFlowRate = self._cylNum*self.__actualFill/self._dischargeTime
        self.__inputToInputLength = 0.35 if self._cylSize < 60 else  0.5
        
       
    def __calculatePipe1Size(self):
        if(self._cylSize < 60):
            return 25
        else:
            return 50
            
    def __calculatePipeSize(self):
        #for c,i in enumerate(self.__maxMassFlowRateData,0):
        #    if self.__maxMassFlowRateData[c]>self.avgFlowRate:
        #        return self.__pipeSizeSelector[i]
        #else:
        #    self._errorExist = True
        #    self._error = 'pipe size not found'
        #    return 0
        return 0
    
    def calculateAllSections(self):
        if(self._cylNum == 1):
            if(self._reserve == 0):
                self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                     self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                     0, 0, 0, 0, 
                                     0, 0, 0, 0, 1])
            elif(self._reserve == 1):
                if(self.__manifoldType == 'end'):
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                     self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                     0, 0, 0, 0, 
                                     0, 0, 0, 0, 1])
                    self._manifoldSection.append([2, 3, self.__inputToInputLength + 0.3, 0, 
                                     65 if self._cylSize < 60 else 80, 80, self._manifoldConnectionType,
                                     0, 1, 1, 0, 
                                     0, 0, 0, 0, 1])
                elif(self.__manifoldType == 'center'):
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                     self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                     0, 0, 0, 0, 
                                     0, 0, 0, 0, 1])
                    self._manifoldSection.append([2, 3, 0.5, 0.1, 
                                     65 if self._cylSize < 60 else 80, 80, self._manifoldConnectionType,
                                     1, 1, 0, 0, 
                                     0, 0, 0, 0, 1])
                else: 
                    self._errorExist = True
                    self._error = "error: for modular system with main and reserve, only 'center' or 'end' manifold possible."
                    return
            else:
                self._errorExist = True
                self._error = "error: reserve is either 1 or 0"
                return
        elif(self._cylNum>1 and self._cylNum<=12):
            if(self.__manifoldType == 'end'):
                if self._reserve == 0:
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                         self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                         0, 0, 0, 0, 
                                         0, 0, 0, 0, 1])
                    for i in range(1,self._cylNum+1):
                        self._manifoldSection.append([i+1, i+2, 0.3 if i == self._cylNum else self.__inputToInputLength, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1 if i==1 else 0, 0 if i==1 else 1, 0, 
                                         0, 0, 0, 0, i])
                elif self._reserve == 1:
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                         self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                         0, 0, 0, 0, 
                                         0, 0, 0, 0, 1])
                    for i in range(1,self._cylNum+1):
                        self._manifoldSection.append([i+1, i+2, 0.3 + self.__inputToInputLength * self._cylNum if i == self._cylNum else self.__inputToInputLength, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1 if i==1 else 0, 0 if i==1 else 1, 0, 
                                         0, 0, 0, 0, i])
                else:
                    self._errorExist = True
                    self._error = "reserve should be 0 or 1"
                    return
            elif(self.__manifoldType == 'center'):
                if (self._reserve == 0):
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                         self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                         0, 0, 0, 0, 
                                         0, 0, 0, 0, 1])
                    for i in range(1,self.__leftCylNum+1):
                        self._manifoldSection.append([i+1, i+2, 0.3 if i==self.__leftCylNum else self.__inputToInputLength, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1 if i==1 else 0, 0 if i ==1 else 1, 0, 
                                         0, 0, 0, 0, i if i<=self.__leftCylNum else self._cylNum - self.__leftCylNum])
                    self._manifoldSection.append([self.__leftCylNum+2, self.__leftCylNum+3, 0.5, 0.1, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1, 0, 0, 
                                         0, 0, 0, 0, self._cylNum])
                elif(self._reserve == 1):
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                         self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                         0, 0, 0, 0, 
                                         0, 0, 0, 0, 1])
                    for i in range(1,self._cylNum+1):
                        self._manifoldSection.append([i+1, i+2, 0.3 if i==self._cylNum else self.__inputToInputLength, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1 if i==1 else 0, 0 if i ==1 else 1, 0, 
                                         0, 0, 0, 0, i if i<=self._cylNum else self._cylNum])
                    self._manifoldSection.append([self._cylNum+2, self._cylNum+3, 0.5, 0.1, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1, 0, 0, 
                                         0, 0, 0, 0, self._cylNum])
                else:
                    self._errorExist =True
                    self._error = "error: reserve is either 1 or 0"
                    return
            elif(self.__manifoldType == 'u'):
                if(self._reserve == 0):
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                         self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                         0, 0, 0, 0, 
                                         0, 0, 0, 0, 1])
                    for i in range(1,self.__leftCylNum+1):
                        self._manifoldSection.append([i+1, i+2, self.__inputToInputLength, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         1 if i==self.__leftCylNum else 0, 1 if i==1 else 0, 0 if i ==1 else 1, 0, 
                                         0, 0, 0, 0, i])
                    self._manifoldSection.append([self.__leftCylNum+2, self.__leftCylNum+3, 0.5, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1, 0, 0, 
                                         0, 0, 0, 0, self._cylNum])
                elif(self._reserve ==1):
                    self._manifoldSection.append([1, 2, self.__length1[self._cylSize], self.__height1[self._cylSize], 
                                         self.__calculatePipe1Size(), self.__pipeSchedule, self.__pipeConnectionType,
                                         0, 0, 0, 0, 
                                         0, 0, 0, 0, 1])
                    for i in range(1,self._cylNum+1):
                        self._manifoldSection.append([i+1, i+2, self.__inputToInputLength, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         1 if i==self.__leftCylNum else 0, 1 if i==1 else 0, 0 if i ==1 else 1, 0, 
                                         0, 0, 0, 0, i])
                    self._manifoldSection.append([self._cylNum+2, self._cylNum+3, 0.5, 0, 
                                         self.__calculatePipeSize(), 80, self._manifoldConnectionType,
                                         0, 1, 0, 0, 
                                         0, 0, 0, 0, self._cylNum])
                else:
                    self._errorExist = True
                    self._error = "error: reserve is either 1 or 0"
                    return
            else:
                self._erroeExist = True
                self._error = "error: manifold is either 'end', 'center', or 'u'"
                return
        else:
            self._errorExist = True
            self._error = "error: cylNum should be between 1 and 12"
            return
        
    def calculteDimensions(self):
        if(self._cylNum == 1):
            if(self._reserve == 0):
                self._Dx = self.__cylDiameter[self._cylSize]
                self._Dy = self.__cylDiameter[self._cylSize]+self.__bracketDimension
                self._Dz = self.__cylHeight[self._cylSize]+self.__hoseZ[self.__calculatePipe1Size()]
                self._endX = self._Dx
                self._endY = self.__cylDiameter[self._cylSize]/2.0 + self.__bracketDimension
                self._endZ = self._Dz 
            elif(self._reserve == 1):
                if(self.__manifoldType == 'end'):
                    self._Dx = 2 * 0.3 + self.__inputToInputLength #self.__cylDiameter[self._cylSize]
                    self._Dy = self.__bracketDimension + self.__cylDiameter[self._cylSize]
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = 0.0
                    self._endY = self.__bracketDimension + self.__cylDiameter[self._cylSize]/2.0
                    self._endZ = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                elif(self.__manifoldType == 'center'):
                    self._Dx = 2 * 0.3 + self.__inputToInputLength
                    self._Dy = self.__bracketDimension + self.__cylDiameter[self._cylSize]
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = self._Dx / 2.0
                    self._endY = self.__bracketDimension + self.__cylDiameter[self._cylSize]/2.0
                    self._endZ = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                else: 
                    self._errorExist = True
                    self._error = "error: for modular system with main and reserve, only 'center' or 'end' manifold possible."
                    return
            else:
                self._errorExist = True
                self._error = "error: reserve is either 1 or 0"
                return
        elif(self._cylNum>1 and self._cylNum<=12):
            if(self.__manifoldType == 'end'):
                if self._reserve == 0:
                    self._Dx = (self._cylNum - 1) * self.__inputToInputLength + 0.6
                    self._Dy = self.__cylDiameter[self._cylSize]+self.__bracketDimension
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = 0.0
                    self._endY = self.__cylDiameter[self._cylSize]/2.0 + self.__bracketDimension
                    self._endZ = self._Dz
                elif self._reserve == 1:
                    self._Dx = (2 * self._cylNum - 1) * self.__inputToInputLength + 0.6
                    self._Dy = self.__cylDiameter[self._cylSize]+self.__bracketDimension
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = 0.0
                    self._endY = self.__cylDiameter[self._cylSize]/2.0 + self.__bracketDimension
                    self._endZ = self._Dz
                else:
                    self._errorExist =True
                    self._error = "error: reserve is either 1 or 0"
                    return
            elif(self.__manifoldType == 'center'):
                if (self._reserve == 0):
                    self._Dx = (self._cylNum - 1) * self.__inputToInputLength + 0.6
                    self._Dy = self.__cylDiameter[self._cylSize]+self.__bracketDimension
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = (self._cylNum - self.__leftCylNum - 1) * self.__inputToInputLength + 0.6
                    self._endY = self.__cylDiameter[self._cylSize]/2.0 + self.__bracketDimension
                    self._endZ = self._Dz
                elif(self._reserve == 1):
                    self._Dx = (2 * self._cylNum - 1) * self.__inputToInputLength + 0.6
                    self._Dy = self.__cylDiameter[self._cylSize]+self.__bracketDimension
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = self._Dx / 2.0 
                    self._endY = self.__cylDiameter[self._cylSize]/2.0 + self.__bracketDimension
                    self._endZ = self._Dz
                else:
                    self._errorExist =True
                    self._error = "error: reserve is either 1 or 0"
                    return
            elif(self.__manifoldType == 'u'):
                if(self._reserve == 0):
                    self._Dx = (self.__leftCylNum - 1) * self.__inputToInputLength + 0.8
                    self._Dy = 2*(self.__cylDiameter[self._cylSize]+self.__bracketDimension)
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = (self._cylNum - self.__leftCylNum - 1) * self.__inputToInputLength + 0.8
                    self._endY = self._Dy/2.0
                    self._endZ = self._Dz
                elif(self._reserve ==1):
                    self._Dx = (self._cylNum - 1) * self.__inputToInputLength + 0.8
                    self._Dy = 2*(self.__cylDiameter[self._cylSize]+self.__bracketDimension)
                    self._Dz = self.__cylHeight[self._cylSize] + self.__hoseZ[self.__calculatePipe1Size()] + self.__cvZ[self.__calculatePipe1Size()]
                    self._endX = (self._cylNum - 1) * self.__inputToInputLength + 0.8
                    self._endY = self._Dy/2.0
                    self._endZ = self._Dz
                else:
                    self._errorExist = True
                    self._error = "error: reserve is either 1 or 0"
                    return
            else:
                self.erroeExist = True
                self._error = "error: manifold is either 'end', 'center', or 'u'"
                return
        else:
            self._errorExist = True
            self._error = "error: cylNum should be between 1 and 12"
            return
            
#==========================================================================        

class containerBankIFlow300(containerBank):
    
    __dischargeT = 60 #60s or 120s this does not need to be an input sice the cylSize is an input
    def __init__(self
                , cylNum #number of cylinders
                , cylSize # 80, 140
                , manifoldConnectionType # 'threaded' or 'welded'
                , reserve # 1 or 0
                 ):
        super().__init__(cylNum, cylSize, manifoldConnectionType, reserve)
        
    
    def _calculateAllSections(self):
        if (self._cylSize == 140):
            #has to have a manifold
            #end manifold only?
            pass
        elif(self._cylSize == 80):
            #manifold or hose chain connection
            if(self.__dischargeT == 60):
                #only 2 containers in hose chain possible
                #it can be in 2 rows (2*2 = 4 containers)page 8 with the end connected to the pipe section
                pass
            elif(self.__dischargeT == 120):
                #2 or 3 containers in hose chain possible?
                #it can be in 2 rows (2*2 = 4 containers)page 8
                #it can be in 2 rows (2*3 = 6 containers)page 9 with the end connected to the pipe section
                #it can discharge to a manifold with up to three on hose chain
                pass
            else:
                #error, only 60 or 120s discharge possible
                pass
        else:
            #error: only 80 or 140 containers are possible
            pass
    
    def calculteDimensions(self):
        pass
    #print("strt,end,len,elv,pipsz,pipsch,elb,sT,tT,cpl,selVlv,nozDQ,contN")
