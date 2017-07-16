__author__ = 'chinmay'
import midi
filename = "unicorn"
pattern = midi.read_midifile(filename+".mid")
#print pattern
flip_pattern = midi.Pattern()

def flip_note(event, flip_note):
    note = event.data[0]
    new_note = 2*flip_note - note
    if (new_note < 0):
        print ("negative new_note: %i", new_note)
        new_note = 1
    elif (new_note > 256):
        print ("Above threshold??: %i", new_note)

    newevt = midi.events.NoteOnEvent()
    newevt.data[0] = new_note
    newevt.data[1] = event.data[1]
    newevt.tick = event.tick
    newevt.channel = event.channel

    """
    print "******"
    print event
    print newevt
    print "******"
    """
    return newevt
first_event_flag = True
anchorevt = midi.events.NoteOnEvent()
for track in pattern:
    #first_event_flag = True
    flip_track = midi.Track()
    #anchorevt = midi.events.NoteOnEvent()
    for event in track:
        if isinstance(event,midi.events.NoteOnEvent) == True:
            if first_event_flag == True:
                first_event_flag = False
                anchorevt = event
                print anchorevt
                flip_track.append(event)
            else:
                flip_track.append(flip_note(event, anchorevt.data[0]))
        else:
            flip_track.append(event)
    flip_pattern.append(flip_track)

#print "************************************"
#print flip_pattern

try:
    midi.write_midifile(filename+"_flipped.mid", flip_pattern)
except ValueError:
    print ValueError
