from segon_bindata import BinaryData
test = BinaryData(16)
test.valueOfNumber(650)
print(str(test))
test2 = BinaryData(16)
test2.valueOfNumber(327)
print(str(test2))

test.logicOr(test2)
print(str(test))