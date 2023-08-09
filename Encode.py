def EncodeQR(name):
    pad = 0b10000000
    if len(name) < 1 or len(name) > 5:
        print("Product name should be 1 to 5 characters long.")
    else:
        encoded_qr = []
        for char in name:
            binary_value = format(ord(char), '08b')
            shift = pad << 1
            encoded_qr.append(str(bin(shift)[2:]) + binary_value)
            
        return ''.join(encoded_qr)

product_name = input("Enter Product Name: ")
encoded_result = EncodeQR(product_name)
print(encoded_result)
