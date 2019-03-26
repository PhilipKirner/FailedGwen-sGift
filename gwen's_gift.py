import sys

def comb(A,n,k,p,lo):
  """
    n>=1, k<=n, p: position to fill, lo: first number to pick
    print all possible subsets of k out of n
  """
  if p == len(A):
	  print(A)
  else:
	  for i in range(1,(n-1)):
		  print("\n",A)
		  print(i)
		  if(p>1):
			  print("sum: ",i+A[p-1]+A[p-2])
			  print("n: ",n)
			  print("%: ",i+A[p-1]+A[p-2] % n)
			  if((i+A[p-1]+A[p-2]) % n ==0):
				  continue
		  if(p>0):
			  if((i+A[p-1]) % n ==0):
				  print("sum: ",i+A[p-1]+A[p-2])
				  print("n: ",n)
				  print("%: ",i+A[p-1]+A[p-2] % n)
				  continue
		  A[p] = i
		  comb(A,n,k,p+1,i+1)
	  
  

if __name__ == "__main__":
  d = len(sys.argv)>3
  n = int(sys.argv[1])
  k = int(sys.argv[2])
  A = []
  for i in range(n-1):
      A.append(0)
  if d: print("n:",n,"k:",k)
  comb(A,n,k,0,0)
  

"""sequence length n-1 , first 1,1,1,1 -> n-1,n-1,n-1
3, 2
1,1 pass
1,2 fail
2,2 pass
return 2,2
total % 3 = fail
[0]+[1] % 3 = fail"""
