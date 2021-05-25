import argparse

if __name__ == "__main__":
	parser = argparse.ArgumentParser()

# 	parser.add_argument("number", help="the number to exponentiate", type=int)
# 	parser.add_argument("power", help="the exponent", type=int)
# 	parser.add_argument("-b", "--base", help="the base to display the result it", type=str,
# 		choices=["dec", "hex", "bin"], default="dec")

	args = parser.parse_args()
	
# 	print(args.number ** args.power)

# 	result = args.number ** args.power
# 	if args.base == 'dec':
# 		print(result)
# 	elif args.base == 'bin':
# 		print(bin(result))
# 	else:
# 		print(hex(result))