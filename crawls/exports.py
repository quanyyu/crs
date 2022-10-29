
def get_name():
    return 'exports'

if __name__ == '__main__':
    import redis 
    r = redis.Redis()
    res = r.zrange('https://www.ddyueshu.com/4_4440/', 0, -1)
    text = ""
    for r in res:
        string = r.decode("utf-8")
        if not string.startswith("第"):
            string = "第" + string
        text += string + "\n\n"
    with open("/mnt/d/damingwenkui.txt", "w") as f:
        f.write(text)