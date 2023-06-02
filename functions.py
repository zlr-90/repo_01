import numpy as np
from PIL import Image

def convol(A, B):

	try:
		len(np.shape(A)) == 2 and len(np.shape(B) == 2)
		print("lenth(A) -->  OK ")
		print("lenth(B) -->  OK ")		
	except:
		print("len(A) and len(B) must equals 2")

	u_a, v_a = np.shape(A)
	u_b, v_b = np.shape(B)

	q_u = u_a//u_b
	r_u = u_a%u_b

	q_v = v_a//v_b
	q_v = v_a%v_b

	

	C = np.ones((u_a-1, v_a-1))
	x = np.ones((1, u_b))
	y = np.ones((v_b, 1)) 
	

	amount = 0

	for i in range(3, u_a-3, 1):
		for j in range(3, v_a-3, 1):
			amount = A[i:i+u_b, j:j+v_b]*B
			C[i,j] = x@amount@y
	
	return C 
	
	
im = Image.open("image.png")
A = np.array(im)
A  = A[:,:,0]

im1  = Image.fromarray(A)
im1.show()

B = np.array([[0, 1, 0], [1, 0, 1], [0, 1, 0]])

C  = convol(A, B) 

im2 = Image.fromarray(C)
im2.show()
