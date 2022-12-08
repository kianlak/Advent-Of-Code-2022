def part1(datastream_buffer):
    current_packet = []
    sequence_counter = 0
    marker_index = 0
    for x in range(len(datastream_buffer)):
        if datastream_buffer[x] in current_packet:
            sequence_counter = 0
            current_packet.clear()
        elif sequence_counter == 4:
            break
        else:
            current_packet.append(datastream_buffer[x])
            marker_index = x
            sequence_counter += 1
    
    print("Marker found at character: " + str(marker_index))
    
    # for x in range(len(datastream_buffer)):
    #     if sequence_counter == 5:
    #         break 
    #     elif datastream_buffer[x] in current_packet:
    #         sequence_counter = 0
    #     else:
    #         marker_index = x
    #         sequence_counter += 1
    