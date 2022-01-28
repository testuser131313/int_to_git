import requests
import json
class fruit:
	def __init__(self):
		self.name='orange'
		self.shape='round'
apple = fruit()
apple.name='apple'
print(apple.name)

comment=False
comment='new comment ggg'
if comment:
	print('is comment')

class test():
	def __init__(self, stee):
		self.stee=stee
	def one_one(self):
		return self.stee
	def two_teo(self):
		return self.stee
	def all(self):
		return self.one_one()+self.two_teo()
print(test(7).all())


