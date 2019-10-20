from nagini import Nagini

if __name__ == "__main__":
    print("Connecting to vROps")
    vcops = Nagini(host="", user_pass=("admin", ""))
    print("Completed")
