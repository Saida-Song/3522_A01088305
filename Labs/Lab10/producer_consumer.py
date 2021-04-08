from time import sleep
import city_processor
import threading


class CityOverheadTimeQueue:
	"""
	A Queue stores overhead times of the cities
	"""

	def __init__(self):
		"""
		Attributes of a Queue.
		"""
		self.data_queue = []
		self.access_queue_lock = threading.Lock()

	def put(self, overhead_time: city_processor.CityOverheadTimes) -> None:
		"""
		Put a CityOverheadTimes into the queue.
		:param overhead_time: a CityOverheadTimes object
		"""
		with self.access_queue_lock:
			self.data_queue.append(overhead_time)

	def get(self):
		"""
		Return the first object in the queue and delete it from the queue
		"""
		with self.access_queue_lock:
			return self.data_queue.pop(0)

	def __len__(self):
		"""
		Return the length of the queue.
		:return: an int
		"""
		return len(self.data_queue)


class ProducerThread(threading.Thread):
	"""
	A Producer class that requests from an endpoint and add it to the queue.
	"""

	def __init__(self, cities: list, queue: CityOverheadTimeQueue):
		"""
		Attributes of the class.
		:param cities: a list of City objects
		:param queue: a CityOverheadTimeQueue object
		"""
		super().__init__()
		self.cities = cities
		self.queue = queue

	def run(self) -> None:
		"""
		Add CityOverheadTimes objects to the queue.
		"""
		times = 0
		for city in self.cities:
			self.queue.put(city_processor.ISSDataRequest.get_overhead_pass(city))
			times += 1
			if times % 5 == 0:
				sleep(1)


class ConsumerThread(threading.Thread):
	"""
	A Consumer class that requests from an endpoint and add it to the queue.
	"""

	def __init__(self, queue: CityOverheadTimeQueue):
		"""
		Attributes of the class.
		:param queue: a CityOverheadTimeQueue object
		"""
		super().__init__()
		self.queue = queue
		self.data_incoming = True

	def run(self) -> None:
		"""
		Get an CityOverheadTimes object from the queue and print it to the console.
		"""
		while self.data_incoming or len(self.queue) > 0:
			if len(self.queue) == 0:
				sleep(0.75)
				continue
			print(self.queue.get())
			sleep(0.5)


def main():
	"""
	Driver function of the program.
	"""
	test_queue = CityOverheadTimeQueue()
	cities = city_processor.CityDatabase("city_locations.xlsx").city_db

	splitter = len(cities) // 3
	test_producer1 = ProducerThread(cities[:splitter], test_queue)
	test_producer2 = ProducerThread(cities[splitter:splitter * 2], test_queue)
	test_producer3 = ProducerThread(cities[splitter * 2:], test_queue)
	test_consumer = ConsumerThread(test_queue)

	test_producer1.start()
	test_producer2.start()
	test_producer3.start()
	test_consumer.start()

	test_producer1.join()
	test_producer2.join()
	test_producer3.join()
	test_consumer.data_incoming = False
	test_consumer.join()


if __name__ == '__main__':
	main()
