'''
Input: Pathnames of files.
There should be no upper bound on the number of files.Program should be able to handle thousands of files.
'''
file = glob.glob("/home/bhaskari/python/my_directory/*.txt")





# list to store the hashes as they are calculated
storeHash = []

#Open the files that need to be checked for integrity, compute  their hashes and store them in a List.
for f in file:
    with open(f, 'rb') as getsha1:

                currentItem = getsha1.read()
                # calculate hash  and save them in the storeHash
                storeHash.append(sha1(currentItem).hexdigest())

if (len(storeHash) % 2 != 0) :
        storeHash.append(storeHash[-1])

        '''
        Merkle Tree is a complete binary tree,
        so if the number of inputs from CSV are odd, we duplicate the last record's hash in the list
        '''


while (len(storeHash)> 1) :
        # we run the loop till we don't get a single hash

        j = 0;

        for i in range(0, len(storeHash) - 1) :

                storeHash[j] = sha1(str(storeHash[i] + storeHash[i+1])).hexdigest()
                # hash of the i th leaf and i + 1 th leaf are concatenated
                # to find the hash parent to the both

                i += 2
                j += 1


        lastDelete = i - j;

        del storeHash[-lastDelete:];
        # as we now have the hash to the upper level of the tree, we delete the extra space in the array.
        # in each iteration of this loop the size of the storeHash list is halved.

#Compute Top Hash and print to a file 
merkleFile = open('merkle.csv', 'w')
# create the file for saving the merkle root

write = writer(merkleFile)

write.writerow(storeHash)
# write to the file in simple text mode


#Compute Top Hash and print to screen 
print(' '.join(storeHash))
