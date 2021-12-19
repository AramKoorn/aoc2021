f = open('input.txt', 'r')
line = f.readlines()
line = line[0]

mp = {
 '0': '0000',
 '2': '0010',
 '3': '0011',
 '4': '0100',
 '5': '0101',
 '6': '0110',
 '7': '0111',
 '8': '1000',
 '9': '1001',
 'A': '1010',
 'B': '1011',
 'C': '1100',
 'D': '1101',
 'E': '1110',
 'F': '1111'
 }
mp_flipped = {v: k for k, v in mp.items()}


class Parser:
 def __init__(self, hex_string):
  self.hex_string = hex_string

 def to_binary(self):
  string = ""
  for x in self.hex_string:
   string += x.replace(x, mp[x])
  self.binary_string = string

 def packet_version(self, string):
  return int(string[:3], 2)

 def type_id(self, string):
  return int(string[3:6], 2)





if __name__ == '__main__':
 p = Parser(line)
 p.to_binary()
 p.binary_string
 p.packet_version(p.binary_string)
 p.type_id(p.binary_string)

x = 2
