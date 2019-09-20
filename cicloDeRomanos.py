
def convertir():
  for i in range(1, 3901):
      Arabigo = int(i)
      Roman = ""
      RomanoConst = [[1000, 900, 500, 100, 90, 50, 40, 10, 9, 5, 4, 1], ['M', 'CM', 'D', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']]

      for i in range(len(RomanoConst[0])):
          if (Arabigo // RomanoConst[0][i] >= 1):

              Roman += Arabigo // RomanoConst[0][i] * RomanoConst[1][i]
              Arabigo -= Arabigo // RomanoConst[0][i] * RomanoConst[0][i]
      print(Roman)

def main():
  convertir()

if __name__ == '__main__':
  main()
