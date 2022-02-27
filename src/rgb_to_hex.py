rgb = lambda *args: "".join(map(lambda x: "{:02X}".format(x), list(map(lambda x: (x if x > 0 else 0) if x < 255 else 255, list(args)))))
