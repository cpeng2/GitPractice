"""
File: file_reading.py
Name:
---------------------------
This file shows how we can open and
print text files through Python code
"""


def main():
	filepath = "text/JerrySecret1.txt"
	with open(filepath, 'r') as f:
		for line in f:
			print(line, end="")

	filepath = "text/JerrySecret2.txt"
	with open(filepath, 'r') as f:
		for line in f:
			print(line, end="")

	filepath = "text/JerrySecret3.txt"
	with open(filepath, 'r') as f:
		for line in f:
			print(line, end="")

	filepath = "text/JerrySecret4.txt"
	with open(filepath, 'r') as f:
		for line in f:
			print(line, end="")

if __name__ == '__main__':
	main()
