with open('org.txt', encoding='utf8') as reader:
    lines = reader.readlines()

    ss = set()
    for line in lines[2:]:
        if line.strip():
            line = line.strip()[1:][:-1].strip()
            line = line.replace('[','').replace(']','').replace("'",'')
            for l in  line.split(','):
                ss.add(l)
    ss = list(ss)
    ss = [s for s in ss if s.strip()]
    for s in ss:
        print(s)