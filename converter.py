#! python

import conversion_charts as cc

# get methods in the class return a dictionary of
# system -> grade
class ClimbGradeConverter:
  def getBoulderingGrade(self, grade):
    return self.__parseMatrix(cc.BoulderingChart, grade)

  def getClimbingGrade(self, grade):
    return self.__parseMatrix(cc.ClimbingChart, grade)

  def __parseMatrix(self, chart, grade):
    rowIdx = int()

    # first we find our row index
    for i in range(len(chart)):
      found = False
      for j in range(len(chart[i])):
        if grade.upper() == chart[i][j].upper():
          rowIdx = i
          found = True
          break
      if found:
        break

    retval = dict()

    # then we create our return dictionary
    for c in range(len(chart[i])):
      retval[chart[0][c]] = chart[i][c]

    return retval

