import math
import sys

def has_changed(v1, v2):
    for i in range(len(v1)):
        if v1[i]!=v2[i]:
            return True
    return False

def distance_calculator(v1, v2 ): #distance between the vectors
    assert(len(v1)==len(v2))
    distance = 0
    for c in range(len(v1)) :
        coordinates_d = (v1[c] - v2[c])**2
        distance += coordinates_d

    return distance

def update_centroid (i, k_centroids, clusters, vectors_length): # update of k_centroids[i]

    folder = clusters[i] ## contains all the cluster's vectors
    folder_length = len(folder) ## =: number of vectors in the folder (in the cluster..) 


        
    for c in range (vectors_length): #for each cordinate

        cor_sum = 0

        for j in range (folder_length): 
            cor_sum += folder[j][c]
                
        k_centroids[i][c] = (float ( cor_sum/(folder_length) ))  


def k_mean(k,max_iter=200):
    file_content = []
    while True:
        try:
            file_content.append( [ float(word) for word in input().split(',')  ] ) # each row is an array 
        except EOFError:
            break
    
 # file_content is an array, so each item of his is a vector (array) - an array in which each member is a Real number..
 # file_content[i] is a vector 

    #initialization of the clusters(as empty one's):
    clusters = [ ] #each item is a "folder". each folder (might) contain several vectors
    vectors_length = 0
    for i in range(k):
        if(i==0):
            vectors_length = len( file_content[i] )
        clusters.append( [] )  


    #initialization of the (k) centroids:
    k_centroids = []
    for i in range(k):
        k_centroids.append( file_content[i].copy() )

    indicator = True # True's meaning: **no** conversion
    counter = 0 
    while (indicator and counter < max_iter ):
        indicator = False 
        for xi in file_content:
                    min_distance=math.inf
                    cluster_index=-1 # "cluster_index" is the (serial) number of the folder, which xi belongs to

                    for j in range(k):
                        current_distance = distance_calculator(xi, k_centroids[j])
                        min_distance = min (min_distance, current_distance)
                        
                        if(min_distance==current_distance):
                            cluster_index = j
                                                                
                    clusters[cluster_index].append(xi)
                    
        # done adding the vector's to their right folders.
        

        # now we will update the centroids:
        for i in range(k):
            old_centroid = k_centroids[i].copy()
            update_centroid (i ,k_centroids, clusters.copy(), vectors_length)
            if ( has_changed (old_centroid, k_centroids[i].copy()) ):
                 indicator=True
            clusters[i].clear() #restart the cluster
    
        counter+=1
    
    for vector in k_centroids: #round.4.digits
        for c in range(vectors_length): 
           vector[c] = ('{:.4f}'.format(vector[c]))   


    # for centroid in k_centroids: print (centroid, end='\n')

    for vector in k_centroids:
            for c in range(len(vector)):
                if c != (len(vector)-1):
                    print(vector[c],end=',')
                else:
                    print(vector[c])

                 

input_k = int(sys.argv[1])  
if(len(sys.argv)>2):
    input_iters=int(sys.argv[2])
    k_mean(input_k,input_iters)
else:
    k_mean(input_k)

    
       

 




