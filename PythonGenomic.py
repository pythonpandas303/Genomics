import os
#Change file path if necessary
os.chdir('C:/Users/megal/Desktop/PGS')
#Change file name if necessary
fa="dna2.fasta"

###This is the function to define a sequence based on FastA conventions. 
def sequ(fa):
	f= open(fa, "r")
	file = f.readlines()
	#print file
	sequences = []
	seq = ""
	for f in file:
		if not f.startswith('>'):
			f = f.replace(" ", "")
			f = f.replace("\n", "")
			seq = seq + f
		else:
			sequences.append(seq)
			seq = ""

	# Adding the last sequence
	sequences.append(seq)

	sequences = sequences[1:]
	
	return sequences
	
# Function to find all indicies 	
def find_index(sequence,n):
		start_position = n-1
		start_indexs = []
		stop_indexs = []
		for i in range(n-1, len(sequence), 3):
			if sequence[i:i+3] == "ATG":
				start_indexs.append(i)
		

		# Find all stop codon indexs
		for i in range(n-1, len(sequence), 3):
			stops =["TAA", "TGA", "TAG"]
			if sequence[i:i+3] in stops:
				stop_indexs.append(i)
		ind=[start_position,start_indexs,stop_indexs]
		#print ind
		return ind
		
#Function to find reading frames				
def find_orf(sequence,n):
		ind=find_index(sequence,n)
		start_position = ind[0]
		start_indexs = ind[1]
		stop_indexs = ind[2]
		orf = []
		mark = 0
		for i in range(0,len(start_indexs)):
			for j in range(0, len(stop_indexs)):
				if start_indexs[i] < stop_indexs[j] and start_indexs[i] > mark:
					orf.append(sequence[start_indexs[i]:stop_indexs[j]+3])
					mark = stop_indexs[j]+3
					break
		return orf


	
#
#This function answers question 6
def Ques6(fa):
	sequences=sequ(fa)

	n = 1
	lengths = []
	for i in sequences:
		# print("["+str(n)+"]")
		orfs = find_orf(i,1) + find_orf(i,2) + find_orf(i,3)
		for j in orfs:
			lengths.append(len(j))
		n += 1
	print(max(lengths))



# Find the sequence with the identifier offered
def find_identifier(num):
	f = open(fa, "r")
	file = f.readlines()
	seq = ""
	identifier = 0
	for i in range(0, len(file)):
		if num in file[i]:
			identifier = i

	for f in file[identifier+1:]:
		if not f.startswith('>'):
			f = f.replace(" ", "")
			f = f.replace("\n", "")
			seq = seq + f
		else:
			break
			
	lengths = []
	orfs = find_orf(seq,1) + find_orf(seq,2) + find_orf(seq,3)
	for j in orfs:
		lengths.append(len(j))

	print(max(lengths))
	
	
#This function finds repeats, replace with number offered when executing the function. 
def find_length(num):
	f = open(fa, "r")
	file = f.readlines()

	sequences = []
	seq = ""
	for f in file:
		if not f.startswith('>'):
			f = f.replace(" ", "")
			f = f.replace("\n", "")
			seq = seq + f
		else:
			sequences.append(seq)
			seq = ""

	# Add the last seq
	sequences.append(seq)

	sequences = sequences[1:]

	def get_all_repeats(sequence):
		length = len(sequence)
		repeats = []
		for i in range(length):
			repeats.append(sequence[i:i + (num*2)])
		return repeats

	all_six_repeats = []
	for i in sequences:
		repeats_list = get_all_repeats(i)
		for j in repeats_list:
			all_six_repeats.append(j)

	def most_common(lst):
		return max(set(lst), key=lst.count)

	print(most_common(all_six_repeats))
	print(all_six_repeats.count(most_common(all_six_repeats)))
    



print(Ques6(fa))

#Punto 7
print('gi|142022655|gb|EQ086233.1|16')
print('String')
num="gi|142022655|gb|EQ086233.1|16"
print(find_identifier(num))


num=12
print(find_length(num))