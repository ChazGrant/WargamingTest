class FirstTask:
	@staticmethod
	# Плюсы этой реализации в том, что меньше занимает строк кода
	# Минусы в том, что не каждый новичок поймёт(так же присутствует некая часть обфускации)
	def betterIsEven(value):return value%2==0

	@staticmethod
	def isEven(num: int) -> bool:
		"""
			Плюсы у этой реализации в том, что любой новичок разберётся что происходит
			Минусы в том, что занимает много места для такой простой задачи
		"""
		if num % 2 == 0:
			return True
		else:
			return False


class SecondTask:
	"""
		Плюсы: понятен даже для новичка, поддерживает любую размерность
		Минусы: нет
	"""
	def __init__(self, capacity):
		self.capacity = capacity
		self.size = 0

		self.head = 0
		self.tail = -1

		self.queue = [None] * capacity

	def enque(self, value):
		if self.size == self.capacity:
			raise Exception("Очередь заполнена")

		self.size += 1
		self.tail = (self.tail + 1) % self.capacity
		self.queue[self.tail] = value

	def deque(self):
		if not self.size:
			raise Exception("Очередь пуста")

		tmp = self.queue[self.head]
		self.head = (self.head + 1) % self.capacity
		self.size -= 1

		return tmp

	def display(self):
		if not self.size:
			raise Exception("Очередь пуста")

		index = self.head
		for i in range(self.size):
			print(self.queue[index], end=" ")
			index = (index + 1) % self.capacity
		print()

class SecondTaskAlternative():
	"""
		Плюсы: код более структурирован, разбит на больше функций, используется сложная логика
		Минусы: сложнее реализован, по сравнению с предыдущим
	"""
    def __init__(self, max_size=10):
        self.buffer = [None for _ in range(max_size)]
        self.head = 0
        self.tail = 0
        self.max_size = max_size

    def __str__(self):
        items = " ".join([str(item) for item in self.buffer if item])
        return items

    def size(self):
        if self.tail >= self.head:
            return self.tail - self.head
        return self.max_size - self.head - self.tail

    def _is_empty(self):
        return self.tail == self.head

    def _is_full(self):
        return self.tail == (self.head-1) % self.max_size

    def enqueue(self, item):
        if self._is_full():
            raise OverflowError(
                "CircularBuffer is full")
        self.buffer[self.tail] = item
        self.tail = (self.tail + 1) % self.max_size

    def dequeue(self):
        if self._is_empty():
            raise IndexError("CircularBuffer is empty")
        item = self.buffer[self.head]
        self.buffer[self.head] = None
        self.head = (self.head + 1) % self.max_size
        return item


ticks = 0
class ThirdTask:
	@staticmethod
	def selection_sort(array: list) -> None:
		global ticks
		for i in range(len(array) - 1):
			min_idx = i
			for j in range(i, len(array)):
				if array[j] < array[min_idx]:
					min_idx = j
			if (min_idx == i): continue
			ticks += 1
			array[i], array[min_idx] = array[min_idx], array[i]


if __name__ == "__main__":
	print("First task: ")
	print("*" * 10)

	print(FirstTask.isEven(0))

	print("*" * 10)

	print("Second task: ")
	print("*" * 10)

	queue = SecondTask(6)

	queue.enque(5)
	queue.enque(7)
	queue.enque(6)
	queue.enque(1)
	queue.enque(3)
	queue.enque(4)
	# queue.enque(8)
	queue.display()
	print(queue.deque())
	queue.display()
	print(queue.deque())
	queue.display()
	queue.enque(0)
	queue.display()

	print("*" * 10)

	print("Second task alternative: ")
	print("*" * 10)
	
	queue = SecondTaskAlternative(5)
	queue.enqueue(2)
	queue.enqueue(2)
	queue.enqueue(3)
	queue.enqueue(2)
	print(queue)
	queue.dequeue()
	queue.dequeue()
	queue.dequeue()
	print(queue)

	print("*" * 10)

	print("Third task: ")
	print("*" * 10)

	arr = [2, 6, 1, 4, 9, 4, 2, 9, 2]
	ThirdTask.selection_sort(arr)
	print(ticks)
	print(arr)

	ticks = 0
	ThirdTask.selection_sort(arr)
	print(ticks)

	print("*" * 10)