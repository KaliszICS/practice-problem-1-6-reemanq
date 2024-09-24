import os.path
import sys
import PP1_6

def test_q1_1(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	input_values = ["5", "9"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_6.input = mock_input

	PP1_6.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: 14\n"

def test_q2_1(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	input_values = ["55", "10"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_6.input = mock_input

	PP1_6.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: 5\n"

def test_q3_1(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	PP1_6.q3()
	captured = capsys.readouterr()
	assert captured.out == "hello Mr. Kalisz have you seen my work yet?\n"

def test_q4_1(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	input_values = ["11", "2.2"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_6.input = mock_input

	PP1_6.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: 24\n"

def test_q1_2(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	input_values = ["2", "4"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_6.input = mock_input

	PP1_6.q1()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: 6\n"

def test_q2_2(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	input_values = ["7", "5"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_6.input = mock_input

	PP1_6.q2()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: 1\n"

def test_q3_2(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	PP1_6.q3()
	captured = capsys.readouterr()
	assert captured.out == "hello Mr. Kalisz have you seen my work yet?\n"

def test_q4_2(capsys):

	try:
		exists = os.path.exists("PP1_6.py")
		assert exists
	except:
		sys.exit()

	input_values = ["5.2", "1.4"]

	def mock_input(s):
		print(s, end='')
		return input_values.pop(0)
	PP1_6.input = mock_input

	PP1_6.q4()
	captured = capsys.readouterr()
	assert captured.out == "Input a number: Input a number: 7\n"

