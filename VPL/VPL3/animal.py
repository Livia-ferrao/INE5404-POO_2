from abc import ABC, abstractmethod


class Animal(ABC):
	def __init__(self, tamanhoPasso: int):
		self.__tamanhoPasso = tamanhoPasso

	@property
	def tamanhoPasso(self):
		return self.__tamanhoPasso

	@tamanhoPasso.setter
	def tamanhoPasso(self, tamanhoPasso):
		self.__tamanhoPasso = tamanhoPasso

	def mover(self):
		return 'ANIMAL: DESLOCOU '+str(self.__tamanhoPasso)

	@abstractmethod
	def produzirSom(self):
		pass