#!/usr/bin/python3
import socket, sys

"""
Construct the bytes array to send in order to poll holding registers.
Function code: 0x03
"""
def constructPollHoldingRegisters(unitID, address, length):
  transactionIdentifier = (0x0001).to_bytes(2, byteorder='big') #TODO: increment this
  protocolIdentifier = (0x0000).to_bytes(2, byteorder='big')
  remainingPacketLength = (6).to_bytes(2, byteorder='big')
  functionCode = (0x03).to_bytes(1, byteorder='big')

  outPacket = transactionIdentifier + protocolIdentifier + remainingPacketLength
  outPacket += unitID.to_bytes(1, byteorder='big')
  outPacket += functionCode
  outPacket += (address-1).to_bytes(2, byteorder='big')
  outPacket += length.to_bytes(2, byteorder='big')
  return outPacket

def printRegisters(payload):
  for a,b in zip(payload[::2], payload[1::2]):
    print(hex(a*0x100 + b))

def parseHeader(inPacket):
  packetLength = len(inPacket)

  transactionIdentifier = int.from_bytes(inPacket[:2], byteorder='big')
  protocolIdentifier = int.from_bytes(inPacket[2:4], byteorder='big')
  remainingLength = int.from_bytes(inPacket[4:6], byteorder='big')

  unitID = int.from_bytes(inPacket[6:7], byteorder='big')
  functionCode = int.from_bytes(inPacket[7:8], byteorder='big')
  byteCount = int.from_bytes(inPacket[8:9], byteorder='big')

  return(inPacket[-byteCount:])

if __name__ == "__main__":
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((sys.argv[1], 502))
  x = constructPollHoldingRegisters(1, 50000, 2)
  s.sendall(x)
  print(x)
  inPacket = s.recv(1000)
  print(inPacket)
  
  payload = parseHeader(inPacket)
  printRegisters(payload)


