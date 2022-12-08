# Finds the marker of the datastream buffer

def part2(datastream_buffer):
    current_packet = []         # Keeps track of current packet that is acceptable
    message_marker_index = 0    # The message marker index
    
    # Will go through each character of datastream_buffer 
    # and add them into current_packet. After every addition 
    # into current_packet, we check to see if there is a duplicate 
    # character, if there is, we remove every character up till the 
    # instance of the duplicate character. We keep doing this process 
    # until curren_packet has 14 elements in it on the start of the 
    # iteration. 
    
    for x in range(len(datastream_buffer)):
        # Checks for final 4 unique character packet
        if len(current_packet) == 14:
            marker_index = x
            break

        current_packet.append(datastream_buffer[x])
        
        # Checks for duplicate character, and makes sure that it's not checking for the newest addition into current_packet
        if (datastream_buffer[x] in current_packet) and (current_packet.index(datastream_buffer[x]) != (len(current_packet) - 1)):
            # Remove until duplicate iteration
            for _ in range(current_packet.index(datastream_buffer[x]) + 1):
                current_packet.pop(0)
    
    print("Message marker found at character: " + str(marker_index))    