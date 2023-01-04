def draw_matrix(matrix):
	newmatrix = copy.deepcopy(matrix)
	for i in range(len(newmatrix)):
		for p in range(len(newmatrix[i])):
			if type(newmatrix[i][p])==float:
				newmatrix[i][p] = Fraction(newmatrix[i][p]).limit_denominator(100)
				

	highest=0
	for k in newmatrix:
		for l in k:
			if len(str(l))>highest:
				highest=len(str(l))
	dstring="%"+str(highest)+"s"
	for m in newmatrix:
		for n in m:
			print(dstring % n, end = " ")
		print(end="\n")
from fractions import Fraction
import os
import copy
import math
matrix = [
	[0,1,1,1,1,0,0,0],
	[1,0,1,1,0,1,0,0],
	[1,1,0,1,0,0,1,0],
  [1,1,1,0,0,0,0,1]
]
print("ADD: aRb+cRd=Rd OR aRb+cRd | Add a times row b to c times row d")
print("Multiply: aRb | Multiply row b by a")
print("Swap: Ra=Rb | Swap row a and b")
while True:
	draw_matrix(matrix)
	command = input().lower()
	# os.system('clear')
	print("\n\n\n")
	if "+" in command:
		assignto=int(command.split("r")[-1].replace('=', ''))-1
		if "=" in command:
			additive = command[:command.find("=")].split("+")
		else:
			additive = command.split("+")

		term1=additive[0].split("r")
		term1multiple=float(-1 if term1[0]=="-" else term1[0] if term1[0]!="" else 1)
		term1row=int(term1[1])-1
			
		term2=additive[1].split("r")
		term2multiple=float(-1 if term2[0]=="-" else term2[0] if term2[0]!="" else 1)
		term2row=int(term2[1])-1

		for i in range(len(matrix)):
			if i==term1row:
				row1=matrix[i]
			if i==term2row:
				row2=matrix[i]
			
		row3=[0]*len(row1)
		for k in range(len(row1)):
			newnumber=(row1[k]*term1multiple)+(row2[k]*term2multiple)
			if math.floor(newnumber) < newnumber < math.ceil(newnumber):
				row3[k]=float(newnumber)
			else:
				row3[k]=int(newnumber)
		matrix[assignto]=row3

	elif "=" in command:
		sawp= command.split("=")

		term1=sawp[0].split("r")
		term1row=int(term1[1])-1
		matrixrow1=matrix[term1row]

		term2=sawp[1].split("r")
		term2row=int(term2[1])-1
		matrixrow2=matrix[term2row]

		matrix[term1row]=matrixrow2
		matrix[term2row]=matrixrow1

	else:
		string=command.split("r")
		multiple=float(string[0] if string[0]!="-" else -1)
		row=int(string[1])-1
		matrixrow=matrix[row]
		row2=[0]*len(matrixrow)
		for k in range(len(matrixrow)):
			newnumber=matrixrow[k]*multiple
			if math.floor(newnumber) < newnumber < math.ceil(newnumber):
				row2[k]=float(newnumber)
			else:
				row2[k]=int(newnumber)
		matrix[row]=row2