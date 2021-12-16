"""
SW 2021-12-16 Advent of code day 15

https://adventofcode.com/2021/day/15
"""

import os
import sys
import datetime
import functools

INPUT_PATH = os.path.join(
    os.path.split(os.path.abspath(__file__))[0],
    "input.txt"
)

TEST_DATA = [
    "D2FE28",
    "38006F45291200",
    "EE00D40C823060",
    "8A004A801A8002F478",
    "620080001611562C8802118E34",
    "C0015000016115A2E0802F182340",
    "A0016C880162017C3686B18A3D4780",
]

TEST_DATA_2 = [
    "C200B40A82",
    "04005AC33890",
    "880086C3E88112",
    "CE00C43D881120",
    "D8005AC2A8F0",
    "F600BC2D8F",
    "9C005AC2F8F0",
    "9C0141080250320F1802104A08",
]

def read_bits(bit_idx, number_bits_to_read, byte_list):
    """
    Reads a number of bits into an integer
    """
    result = 0
    for i in range(0, number_bits_to_read):
        result = (result << 1) + read_bit(bit_idx + i, byte_list)
    return result



def read_bit(bit_idx, byte_list):
    """
    Reads a single bit, result is an integer
    """
    byte_point = bit_idx // 8
    mask = 0b10000000 >> (bit_idx % 8)
    return (byte_list[byte_point] & mask) >> (7 - (bit_idx % 8))


def read_packet_2(byte_list, bit_counter):
    """
    Given byte list, and position to start, read in a packet

    return:

        new bit counter
        packet (list of version, type, payload)
    """
    while True:
        # Read in 3 bits for version
        packet_version = read_bits(bit_counter, 3, byte_list)
        bit_counter = bit_counter + 3
        packet_type = read_bits(bit_counter, 3, byte_list)
        bit_counter = bit_counter + 3
        if packet_type == 4:
            # Literal type
            # Read in groups of 5, first bit indicates whether another group to come
            literal_value = 0
            while True:
                bits = read_bits(bit_counter, 5, byte_list)
                bit_counter = bit_counter + 5
                literal_value = (literal_value << 4) + (bits & 0b00001111)
                if not (0b00010000 & bits):
                    break
            return bit_counter, [packet_version, packet_type, literal_value, ]

        else:
            length_type = read_bit(bit_counter, byte_list)
            bit_counter = bit_counter + 1
            # Going to be a list of more packets
            child_packets = []
            if length_type == 0:
                # Next 15 bits give number of bits to read
                total_bit_length_coming = read_bits(bit_counter, 15, byte_list)
                bit_counter = bit_counter + 15
                end_at = bit_counter + total_bit_length_coming
                # So, read in packets until we reach the end
                while bit_counter < end_at:
                    newbit_counter, this_packet = read_packet_2(byte_list, bit_counter)
                    child_packets = child_packets + [this_packet]
                    bit_counter = newbit_counter
                return bit_counter, [packet_version, packet_type, child_packets]
            else:
                # Next 11 bits give number of packets to read
                packets_coming = read_bits(bit_counter, 11, byte_list)
                bit_counter = bit_counter + 11
                for _ in range(0, packets_coming):
                    newbit_counter, this_packet = read_packet_2(byte_list, bit_counter)
                    child_packets.append(this_packet)
                    bit_counter = newbit_counter
                return bit_counter, [packet_version, packet_type, child_packets]
    # End of func

def version_sum(packet):
    """
    Travels through packet, calculates version sum
    """
    result = 0
    this_version = packet[0]
    result = result + this_version
    # Try if iterable, catch exception
    try:
        for child_packet in packet[2]:
            result = result + version_sum(child_packet)
    except TypeError:
        pass
    return result


def parse_packet(packet, verbose=False):
    """
    Given a packet, looks at the packet type and then evaluates the result
    """
    _, packet_type, packet_payload = packet
    if packet_type == 0:
        # Sum packet
        result = sum([parse_packet(i) for i in packet_payload])
    elif packet_type == 1:
        # Multiply packet
        result = functools.reduce(lambda x, y: x*y, [parse_packet(i) for i in packet_payload], 1)
    elif packet_type == 2:
        result = min([parse_packet(i) for i in packet_payload])
    elif packet_type == 3:
        result = max([parse_packet(i) for i in packet_payload])
    elif packet_type == 4:
        result = packet_payload
    elif packet_type == 5:
        # Greater than
        first = parse_packet(packet_payload[0])
        second = parse_packet(packet_payload[1])
        if first > second:
            result = 1
        else:
            result = 0
    elif packet_type == 6:
        # Less than
        first = parse_packet(packet_payload[0])
        second = parse_packet(packet_payload[1])
        if first < second:
            result = 1
        else:
            result = 0
    elif packet_type == 7:
        first = parse_packet(packet_payload[0])
        second = parse_packet(packet_payload[1])
        if first == second:
            result = 1
        else:
            result = 0
    if verbose:
        print(result)
    return result


def main():
    """
    Main entry point
    """
    time_start = datetime.datetime.now()
    print(f"Time start: {time_start}")

    with open(INPUT_PATH, 'r') as a_file:
        input_line = next(a_file).rstrip("\n")

    print("Test data:")
    for i, line in enumerate(TEST_DATA):
        print(f"Line {i} '{line}: ")
        line_bytes = bytearray.fromhex(line)
        print(line_bytes)
        _, result = read_packet_2(line_bytes, 0)
        # print(f"Result of reading packet: {result}")
        print(f"Version sum: {version_sum(result)}")
        print("")

    input_bytes = bytearray.fromhex(input_line)
    _, input_packet = read_packet_2(input_bytes, 0)
    # print(f"Result of reading input data as packet: {input_packet}")
    print(f"Version sum of input packet: {version_sum(input_packet)}")

    print("\nPart 2:\n")
    for i, line in enumerate(TEST_DATA_2):
        print(f"Line {i} '{line}: ")
        line_bytes = bytearray.fromhex(line)
        print(line_bytes)
        _, result = read_packet_2(line_bytes, 0)
        parse_result = parse_packet(result)
        print(f"Test line parse result: {parse_result}")
        print("")

    input_parsed = parse_packet(input_packet)
    print(f"Evaluated input is {input_parsed}")



    time_end = datetime.datetime.now()
    print(f"Time end: {time_end}")
    print(f"Total time spent: {time_end - time_start}")
    sys.exit(0)

if __name__ == "__main__":
    main()
