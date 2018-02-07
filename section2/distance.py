import math


def main():

	x1 = int(input("Enter X1: "))
	y1 = int(input("Enter Y1: "))

	x2 = int(input("Enter X2: "))
	y2 = int(input("Enter Y2: "))

	p1 = Point(x1, y1)
	p2 = Point(x2, y2)

	print(p1.distance(p2))
	print(p2.distance(p1))

class Point:

	def __init__(self, x, y):
		self.x = x
		self.y = y


	def distance(self, other):

		return math.sqrt( (self.x - other.x) ** 2 + (self.y - other.y) **2 )

if __name__ == "__main__":
	main()

