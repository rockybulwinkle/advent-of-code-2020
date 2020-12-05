def debug(name, message):
    if name is not None:
        print(name, message)

class Passport:
    def __init__(self, string):
        """
        Example contents of string:
        ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
        byr:1937 iyr:2017 cid:147 hgt:183cm
        """
        fields = string.split(' ')
        tags = (i.split(':') for i in fields)

        self.attrs = dict()
        for k,v in tags:
            self.attrs[k] = v
            #yeah, maybe I shouldn't do this, but that passport line is
            #moving too quick to waste time typing self.attrs
            setattr(self, k, v)

    def has_attr(self, name):
        return name in self.attrs
    
    def valid_p1(self):
        valid=True
        #check that all required fields are present
        if \
                "byr" not in self.attrs or \
                "iyr" not in self.attrs or \
                "hgt" not in self.attrs or \
                "hcl" not in self.attrs or \
                "ecl" not in self.attrs or \
                "pid" not in self.attrs:
                    valid=False
        
        if len(self.attrs) not in [7,8]:
            valid=False

        #make sure that, if 8 fields, the 8th is cid
        if len(self.attrs) == 8 and "cid" not in self.attrs:
            valid=False

        #make sure that, if 7 fields, cid is missing
        if len(self.attrs) == 7 and "cid" in self.attrs:
            valid=False

        return valid
    
    def valid_p2(self):
        if not self.valid_p1():
            return False
        
        def check_numeric(val, len_, min_, max_, name=None):
            if len_ is not None and len(val) != len_:
                debug(name, "numeric failed len check")
                return False

            val = int(val)
            if val not in range(min_, max_+1):
                return False

            return True

        def check_height(val):
            if val.strip() != val:
                print("Not sure if this would happen, space in height")
                return False
            unit = val[-2:]
            val = val[:-2]
            if unit=="in":
                return check_numeric(val, None, 59, 76)
            elif unit=="cm":
                return check_numeric(val, None, 150, 193)
            else:
                return False

        def check_hair(val):
            if len(val) != 7: return False
            if val[0] != "#": return False
            if val.lower() != val:
                print("Wasn't sure if that would happen, mixed case in hair")
                return False
            try:
                int(val[1:], 16) #just let it throw the exception if it's invalid, catch it in caller
            except ValueError:
                return False

            return True

        def check_eyes(val):
            return val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

        #put it in a dict for eaiser debug
        valid = dict()
        valid['byr'] = check_numeric(self.byr, 4, 1920, 2002)
        valid['iyr'] = check_numeric(self.iyr, 4, 2010, 2020, 'iyr')
        valid['eyr'] = check_numeric(self.eyr, 4, 2020, 2030)
        valid['hgt'] = check_height(self.hgt)
        valid['hcl'] = check_hair(self.hcl)
        valid['ecl'] = check_eyes(self.ecl)
        valid['pid'] = check_numeric(self.pid, 9, 0, 999999999)
        print(valid)
        return all(valid.values())
    
    def __str__(self):
        return str(self.attrs)

def load_passports(fname):
    with open(fname, "r") as f:
        entries = [[]] #list of lists
        for line in f:
            line = line.strip()
            if not line:
                entries.append(list())
            else:
                entries[-1].append(line)

    retval = list()
    for line in entries:
        if line:
            retval.append(Passport(" ".join(line)))

    return retval
