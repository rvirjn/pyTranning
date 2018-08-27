def get_paragraphs(lines):
    para = []
    for line in lines:
        if line.strip() == "":
            if para:
                yield "".join(para)
                para = []
        else:
            para.append(line)
        if para:
            yield ''.join(para)


if __name__ == "__main__":
    lines = open('E.py')
    for item in get_paragraphs(lines):
        for item in (count(item)):
            print item


