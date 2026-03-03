import numpy as np
#A is input Trafic cars
A=np.array([
    [200,150],#Zone 1
    [100,250]# Zone 2
])#  R-1,R-2


T=np.array([
    [0.8,0.2],# Behavior of traffic from Zone 1 :Probability
    [0.3,0.7]# Behavior of traffic from Zone 2  :Probability
])


#Signal optimization 
A_new=np.dot(A,T)


print("Original Trafic Matrix")
print("\n",A)

# Original Trafic Matrix

#  [[200 150] zone-1
#  [100 250]] zone-2
#    R1   R2

print("\nTransformation Matrix:")
print("\n",T)

# Transformation Matrix:

#  [[0.8 0.2] zone-1
#  [0.3 0.7]] zone-2
#    R1   R2

print("\nNew Trafic Matrix after signal optimisation")
print("\n",A_new)

# New Trafic Matrix after signal optimisation

#  [[205. 145.] zone-1
#  [155. 195.]] zone-2
#    R1   R2

# def Optimization(A,T):
#     np.dot(A,Optimization(A,T))

#  After signal Optimisation (after 1Hr)

#Here, In Zone-1: In Route-2 out of 150 vehicle, 5 vehicle move to route 1
#In zone-2: In Route-2 out of 250 vehicle, 55 moves towars Route-1



while(1):
    n=int(input("\n1.Show current Traffic\n2.Optimize the Traffic\n3.Exit\nEnter your choice:"))
    if(n==1):
        print("Original Trafic Matrix")
        print("\n",A)
        continue
    elif(n==2):
        print("\nNew Trafic Matrix after signal optimisation")
        print("\n",A_new)
        continue
    elif(n==3):
        exit(0)
    else:
        print("\nNot Valid choice")
