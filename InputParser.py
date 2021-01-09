import re
class InputParser:

    def isDigit(self,n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def removeSign(self,string):
        if len(string[0]) == 2:
            variable = string[0][1]
        else:
            variable = string[0]
        return variable


    def getSignOfVariable(self,string):

        if string[0][0]=='+':
            return 1
        return -1


    def getCoefficientMatrix(self,listOfEquations:list):

        indexDictionary=self.indexDictionary(listOfEquations)

        numberOfEquations=len(listOfEquations)
        matrix = [[0 for j in range(numberOfEquations) ] for i in range(numberOfEquations)]
        results = [0 for j in range(numberOfEquations)]

        for i in range(len(listOfEquations)):

            equation=listOfEquations[i]
            terms=re.findall(r'([+-][\d]{0,}[*]?[a-zA-Z]?)', equation)


            for term in terms:

                splittedTerm=term.split('*')

                #variable with coefficient = 1 or just single number
                if len(splittedTerm)==1:

                    #check if single number
                    if self.isDigit(splittedTerm[0]):
                        results[i]=float(splittedTerm[0])*-1


                    #variable with coefficient =1
                    else :
                        coefficient=self.getSignOfVariable(splittedTerm)
                        splittedTerm=self.removeSign(splittedTerm)
                        matrix[i][indexDictionary[splittedTerm[0]]]=coefficient


                else:
                    coefficient = splittedTerm[0]
                    matrix[i][indexDictionary[splittedTerm[1]]]=float(coefficient)

        return matrix,results


  # The equation which have all variables.
    def isCompleteEquation(self,equation,numberOfVariables):
      terms = re.findall(r'([+-][\d]{0,}[*]?[a-zA-Z]?)', equation)

      if len(terms) == numberOfVariables + 1:
          return True

      elif len(terms) == numberOfVariables:

          for term in terms:
              splittedTerm = term.split('*')
              if len(splittedTerm)==2:
                  continue
              elif len(splittedTerm)==1 and not self.isDigit(splittedTerm[0]):
                  return True

      return False


  # return index dictionary.
    def indexDictionary(self, listOfEquations):

      dictionaryIndex = {}

      numberOfVariables = len(listOfEquations)

      for equation in listOfEquations:

          if self.isCompleteEquation(equation,numberOfVariables):

              terms = re.findall(r'([+-][\d]{0,}[*]?[a-zA-Z]?)', equation)

              for i in range(len(terms)):
                  term = terms[i]
                  splittedTerm = term.split('*')

                  # variable with coefficient = 1
                  if len(splittedTerm) == 1  :
                      if not self.isDigit(splittedTerm[0]):

                          variable=self.removeSign(splittedTerm)

                      #just a number
                      else :
                          continue

                  else:
                      variable = splittedTerm[1]

                  dictionaryIndex[variable] = i

              break

      return dictionaryIndex



inputParser=InputParser()
listOfEquations=["+2*a1-2*b+2*c+1000*y-7","+2*b-2*c-4","+2*c-1","+3.3y+3"]
matrix,results=inputParser.getCoefficientMatrix(listOfEquations)
print(matrix)
print(results)
