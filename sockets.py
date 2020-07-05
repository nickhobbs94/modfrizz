#!/usr/bin/python3
import socket, sys

"""
Construct the bytes array to send in order to poll holding registers.
Function code: 0x03
"""
def constructPollHoldingRegisters(unitID, address, length):
  transactionIdentifier = (0x0001).to_bytes(2, byteorder='big')
  protocolIdentifier = (0x0000).to_bytes(2, byteorder='big')
  remainingPacketLength = (6).to_bytes(2, byteorder='big')
  functionCode = (0x03).to_bytes(1, byteorder='big')

  outPacket = transactionIdentifier + protocolIdentifier + remainingPacketLength
  outPacket += unitID.to_bytes(1, byteorder='big')
  outPacket += functionCode
  outPacket += (address-1).to_bytes(2, byteorder='big')
  outPacket += length.to_bytes(2, byteorder='big')
  return outPacket



if __name__ == "__main__":
  s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((sys.argv[1], 502))
  y = (0x0001000000060103c34f0002).to_bytes(12, byteorder='big')
  x = constructPollHoldingRegisters(1, 50000, 2)
  print(y,x)
  s.sendall(x)
  print(s.recv(1000))

