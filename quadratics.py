#quadratics.py em
#example of source code and terminal output
def roots(a,b,c):
	D = (b*b - 4*a*c)**0.5 #DISCRIMINANT
	x_1 = (-b + D) / (2 * a)
	x_2 = (-b - D) / (2 * a)
	print ('x1: {0}'.format(x_1))
	print ('x2: {0}'.format(x_2))
	
if __name__ == '__main__':
	a = input ('Enter a: ')
	b = input ('Enter b: ')
	c = input ('Enter c: ')
	roots(float(a),float(b),float(c))
	
'''
terminal output

Enter a: 10
Enter b: 10
Enter c: 10
x1: (-0.4999999999999999+0.8660254037844387j)
x2: (-0.5000000000000001-0.8660254037844387j)
'''
