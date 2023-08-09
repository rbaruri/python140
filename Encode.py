def EncodeQR(name):
    pad = 0b10000000
    if len(name) < 1 or len(name) > 5:
        print("Product name should be 1 to 5 characters long.")
    else:
        enc_qr = []
        for char in name:
            binary_value = format(ord(char), '08b')
            shift = int(pad) << 1
            enc_qr.append('{0:08b}'.format(shift) + binary_value)
            
        return ''.join(enc_qr)

product_name = input("Enter Product Name: ")
enc_res = EncodeQR(product_name)
print(enc_res)
