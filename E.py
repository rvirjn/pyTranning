import re
def get_words(lines):
    pattern = re.compile('^def')
    return pattern.match(lines)

if __name__ == "__main__":
    print get_words("deeef sajsd .ajkdsfjasfj ajsdlflkhf ,"
                    "vbxcb m . def ravi"
                    "def ranjan")

