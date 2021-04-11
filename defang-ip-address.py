def defangIPaddr(address):
    address_as_list = list(address)
    length_of_address = len(address_as_list)
    for i in range(length_of_address):
        if address_as_list[i] == ".":
            address_as_list[i] = "[.]"
    return "".join(address_as_list)

if __name__ == "__main__":
    address = "1.1.1.1"
    if "1[.]1[.]1[.]1" == defangIPaddr(address):
        print("Test Case Passed")
    else:
        print("Test Case Failed")