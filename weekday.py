import datetime

def now():
    return datetime.datetime.now()

def weekday():
    t = now()
    return t.strftime('%A')

if __name__ == "__main__":
    print weekday()

def test_weekday(monkeypatch):
    faketime = 2016, 1, 1
    def fakenow():
        return datetime.datetime(*fakenow)
