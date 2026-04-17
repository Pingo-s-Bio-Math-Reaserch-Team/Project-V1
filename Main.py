import numpy as np
#idh 1 = mutant
class Participant:
  def __init__(self):
    self.values = dict()
  def initalize(self, headers, values):
    hds = headers.split(" ")
    vals = values.split(" ")
    self.values = dict()

    for i in range(len(hds)):
      self.values[hds[i]] = vals[i]

  def deepcopy(self):
    c = dict()
    p = Participant()
    for i in self.values:
      c[i] = self.values[i]
    p.values = c
    return p

class Consistancy:
    def rDR(self, idh):
        return 1 - idh
    def rDC(self, idh, mgmt):
        if(idh == 0 or mgmt == 0):
            return 1
        else:
            return 0
    def rRC(self, egfr):
        return egfr
    def severity(self, grade, survival):
        if(grade == 1):
            return 1
        if(survival < 24):
            return 1
        return 0
    def eDR(self, idh, egfr):
        return abs(self.rDR(idh) - egfr)
    def eDC(self, idh, mgmt, grade, survival):
        return abs(self.rDC(idh, mgmt) - self.severity(grade, survival))
    def eRC(self, egfr, grade, survival):
        return abs(self.rRC(egfr) - self.severity(grade, survival))
    
    def consistancy(self, p):
        vals = p.vals
        idh = vals["IDH"] 
        egfr = vals["EGFR"]
        mgmt = vals["MGMT"]
        grade = vals["GRADE"]
        surv = vals["SURVIVAL"]
        eDR = self.eDR(idh, egfr)
        eDC = self.eDC(idh, mgmt, grade, surv)
        eRC = self.eRC(egfr, grade, surv)

        print(eDR)
        print(eDC)
        print(eRC)
        return (eDR + eDC + eRC)/3.0

class EncodedCases:
  #Use raw molecular call, ignore WHO text label if conflicting
  #Exclude sample if missing (required for subtype classification)
  def IDHMutationStatus(self, par):
    if(par.values["IDH"] == None):
      return None
    p = par.deepcopy


  #Binarize from beta value: threshold ≥ 0.30 = methylated
  #If MGMT data is missing, fill it in with whatever value appears most in the cohort, 
  #and mark those samples so we know they were filled in and not real measurements
  def MGMTMethylation(self, par):
    print("")   

  #Log2(FPKM+1) normalize; amplified = CNV≥2 OR FPKM ≥ 90th pct
  #Exclude sample from transcriptomic node if RNA-seq missing
  def EGFRExpression(self, par):
    print("")

  #Convert days to months if needed (÷30.44), floor at 0
  #Exclude if OS completely absent; note censored vs. deceased separately
  def overallSurvival(self, par):
    print("")

  #Standardize: 1=Deceased, 0=Living; resolve string variants
  #Exclude if missing (needed for survival interpretation)
  def vitalStatus(self, par):
    print("")
  
  #Map numeric: 2→2, 3→3, 4→4; cross check IDH for label consistency
  #Use IDH status to infer if WHO label absent or ambiguous
  def WHOGrade(self, par):
    print("")



    

    
