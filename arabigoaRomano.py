Arabic = int(input("Dame un numero: "))
Romano = ""
RomanoDict = [[1000, 900, 500, 100, 90, 50, 40, 10, 9, 5, 4, 1], ['M', 'CM', 'D', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']]

for i in range(len(RomanoDict[0])):
    if (Arabic // RomanoDict[0][i] >= 1):

        Romano += Arabic // RomanoDict[0][i] * RomanoDict[1][i]
        Arabic -= Arabic // RomanoDict[0][i] * RomanoDict[0][i]
print(Romano)
