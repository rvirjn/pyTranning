from nagini import Nagini

if __name__ == "__main__":
    print("Connecting to vROps")
    vcops = Nagini(host="vrops01svr01.rainpole.local", user_pass=("admin", "VMware1!"))
    print("Completed")
