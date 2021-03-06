class henon():
	# init params, the classical henon map have values of a=1.4 and b=0.3
	def __init__(self, a=1.4, b=0.3, x=0.0, y=0.0):
		self.a = a
		self.b = b
		self.x = x
		self.y = y


	# return current position
	def point(self):
		p = (self.x, self.y)

		return p

	
	# return next position meanwhile set current position to it
	def next_point(self):
		a = self.a
		b = self.b
		xn = self.x
		yn = self.y

		self.x = 1.0 - a*xn**2 + yn
		self.y = b*xn
		p = (self.x, self.y)

		return p



# return all points
def get_all(a=1.4, b=0.3, x=0.0, y=0.0, count=1):
	h = henon(a, b, x, y)	
	h_list = []
	
	for i in range(count):
		curr_pos = h.point()
		h_list.append(curr_pos[0])
		h_list.append(curr_pos[1])
		try:
			h.next_point()
		except Exception as err_get_next_point:
			print 'err_get_next_point: %s' % err_get_next_point

	return h_list
