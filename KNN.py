''' 
Data Mining Project 1
KNN algorithm
'''

import csv
import random
import math
import operator

 
def loadDataset(filename, split,labels,hardk):
	dividedsets = []
	
	with open(filename, 'rb') as csvfile:
	    lines = csv.reader(csvfile)
	    dataset = list(lines)
	    maxlen = len(dataset)
	    
	    #dividedsets = [dataset[i:i+(len(dataset)/split)] for i in range(0, len(dataset), len(dataset)/split)]
	    uniqlabels = set([i.strip('\r\n') for i in set(labels)])
	    #uniqlabels = [i.strip('\n') for i in set(labels)]
	    '''for n in range(k):
	    	temp = []
	    	if len(temp) < testlen:
	    		for class in uniqlabels:
	    			'''
	    #print uniqlabels
	    #print dataset[0:5]
	    #return			
	    classesdata = []
	    for lab in uniqlabels:
	    	temp = []
	    	for line in dataset:
	    		if lab.strip('\n') == line[-1].strip('\n'):
	    			temp.append(line)
	    	classesdata.append(temp)
	    #print classesdata
	    claslen = len(uniqlabels)
	    for i in range(hardk):
	    #for i in range(claslen):
	    	dividedsets.append([])
	    	 
	    for cdata in classesdata:
	    	#tmp = len(cdata)/split
	    	
	    	divdata = [cdata[i:i+(len(cdata)/hardk)] for i in range(0,len(cdata), len(cdata)/hardk)]
	    	#print len(divdata)#5
	    	#print len(divdata[0]) #14
	    	
	    	#print divdata[0]
	    	#print len(divdata[0])
	    	
	    	for i in range(hardk):
	    	#for i in range(claslen):	
	    		dividedsets[i].append(divdata[i])
	    	#print dividedsets
	    #return
	    finaldata = []
	    for divset in dividedsets:
	    	tmp = []
	    	for x in divset:
	    		tmp += x
	    	finaldata.append(tmp)
	    	
	    #print dividedsets
	    #print len(finaldata) #5
	    #print len(finaldata[0]) #42
	    return finaldata
	    #return dividedsets
	    '''	print divdata
	    	print len(divdata)
	    	print len(cdata)
	    	return
	    	cdata[0:tmp]			
	    for line in dataset:
	    	dividedsets	
	    return dividedsets'''
	    
 
def euclideanDistance(instance1, instance2, length):
	distance = 0
	for x in range(length-2):
		#print len(instance1)  
		#print len(instance2)
		distance += pow((float(instance1[x]) - float(instance2[x])), 2)
		#print distance
	return math.sqrt(distance)
 
def getNeighbors(trainingSet, testInstance, k):
	distances = []
	length = len(testInstance)
	
	for x in range(len(trainingSet)):
		dist = euclideanDistance(testInstance, trainingSet[x], length)
		distances.append((trainingSet[x], dist))
	distances.sort(key=operator.itemgetter(1))
	neighbors = []
	#print distances
	
	for x in range(k):
		neighbors.append(distances[x][0])
	return neighbors
 
def getResponse(neighbors):
	classVotes = {}
	for x in range(len(neighbors)):
		response = neighbors[x][-1]
		if response in classVotes:
			classVotes[response] += 1
		else:
			classVotes[response] = 1
	sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedVotes[0][0]
 
def getAccuracy(testSet, predictions):
	correct = 0
	for x in range(len(testSet)):
		if testSet[x][-1] == predictions[x]:
			correct += 1
	return (correct/float(len(testSet))) * 100.0
	
def main():
	# prepare data
	trainingSet=[]
	testSet=[]
	
	fp = open('/Users/Rehana/Desktop/data/attLabel.csv','rb')
	#fp = open('/Users/Rehana/Desktop/data/irisLabel.csv','rb')
	
	#fp = open('/Users/Rehana/Desktop/data/SeedsLabels.csv','rb')
	lines = fp.readlines()
	fp.close()
	labels = set(lines)
	
	
	#return
	fq = open('/Users/Rehana/Desktop/data/att.csv','r')
	#fq = open('/Users/Rehana/Desktop/data/iris.csv','r')
	#fq = open('/Users/Rehana/Desktop/data/Seedsfinal.csv','r')
	qlines = fq.readlines()
	fq.close()
	
	#return
	fnew = open('mergedatt.csv','w')
	i = 0
	for line in qlines:
		#temp = line.strip('\n')+','+str(lines[i])
		temp = line.strip('\r\n')+','+str(lines[i])
		i +=1
		fnew.write(temp)
	fnew.close()
	k = raw_input('Enter the K Value:')
	k = int(k)
	hardk = 5
	dividedsets = loadDataset('mergedatt.csv', k,labels,hardk)
	#print dividedsets
	allAccuracy = 0.0
	for i in range(hardk):
		testSet = dividedsets[i]
		trainingSet = dividedsets[i+1:]+dividedsets[:i]
		trainingSet = sum(trainingSet,[])
		#print testSet
		print 'Train set: ' + repr(len(trainingSet))
		print 'Test set: ' + repr(len(testSet))
		
		# generate predictions
		#return
		predictions=[]
	
		#print trainingSet[0]
		#print len(trainingSet[0])
		for x in range(len(testSet)):
			neighbors = getNeighbors(trainingSet, testSet[x], k)
		
			result = getResponse(neighbors)
			#print result
			predictions.append(result)
			#print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
		accuracy = getAccuracy(testSet, predictions)
		print('Accuracy: ' + repr(accuracy) + '%')
		allAccuracy += accuracy
	print ('Overall Accuracy after averaging:' + repr(allAccuracy/hardk) + '%')  
	
main()
