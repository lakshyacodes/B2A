msg='''
What you want to do?
1)binary-to-ascii
2)ascii-to-binary
'''
print(msg)
user_want = int(input(">> "))
if(user_want==1):
	message='Enter String!'
	print(message)
	test_str = input(">> ")
	res = ' '.join(format(ord(i), '08b') for i in test_str)
	print("Binary: " + str(res))
else:
	test_str = input(">> ")
	test_str="".join(test_str.split())
	type(int(test_str))
	binary_int = int(test_str, 2);  
	byte_number = binary_int.bit_length() + 7 // 8
	binary_array = binary_int.to_bytes(byte_number, "big")
	ascii_text = binary_array.decode()
	print(ascii_text)