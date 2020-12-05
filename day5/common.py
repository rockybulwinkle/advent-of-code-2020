def split_range(sym, start, stop):
    len_ = stop-start+1
    if sym == "F":
        stop -= len_//2
    elif sym == "B":
        start += len_//2
    else:
        raise Exception(f"Invalid symbol: {sym}")
    return start,stop

def repeat_split_helper(syms, stop=127):
    syms=syms.replace("L", "F")
    syms=syms.replace("R", "B")
    start=0
    for i in syms:
        start,stop = split_range(i, start, stop)

    return start,stop

def repeat_split(syms, stop=127):
    start,stop = repeat_split_helper(syms, stop)
    assert start==stop
    return start

def seatid(syms):
    assert len(syms) == 10
    row = repeat_split(syms[:7])
    col = repeat_split(syms[7:], stop=7)
    return 8*row + col


if __name__ == "__main__":
    #Let's put a few unit tests here
    #test the inner function a little
    assert split_range('F', 0, 127) == (0,63)
    assert split_range('B', 0, 63) == (32,63)

    #test the intermediate steps of the supplied example
    assert repeat_split_helper("FB") == (32,63)
    assert repeat_split_helper("FBF") == (32,47)
    assert repeat_split_helper("FBFB") == (40,47)
    assert repeat_split_helper("FBFBB") == (44,47)
    assert repeat_split_helper("FBFBBF") == (44,45)
    assert repeat_split_helper("FBFBBFF") == (44,44)

    assert seatid("BFFFBBFRRR") == 567
    assert seatid("FFFBBBFRRR") == 119
    assert seatid("BBFFBBFRLL") == 820

