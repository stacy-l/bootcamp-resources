def print_string(string):
	print(string)

print_string("always runs")

if __name__ == "__main__":
# 	executed only if the script is run directly. Will not execute if imported.
	print_string("don't run on import")