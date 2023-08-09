def EncodeQR(name):
    if len(name) < 1 or len(name) > 5:
        print("Product name should be 1 to 5 characters long.")
    else:
        encoded_qr = []
        
        for char in name:
            binary_value = format(ord(char), '08b')
            encoded_qr.append(binary_value[1:])
            
        return encoded_qr

product_name = input("Enter Product Name: ")
encoded_result = EncodeQR(product_name)
print(encoded_result)
#padding left, list to string encoded_qr