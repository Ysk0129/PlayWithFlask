
if __name__ == "__main__":

    wago = []
    with open("wago.121808.pn") as f:
        for l in f.readlines():
            line = l.replace("\t", "").replace(" ", "").replace("）", "）,").split(",")
            
            value = "1" if line[0].startswith("ポジ") else "-1"
            key = line[1].rstrip("\n")
            if key != "":
                wago.append("SET " + "\"" + key + "\"" + " " + "\"" + value + "\"" + "\r\n")

    with open("evaluation_dictionary.txt", "w") as f:
        [f.write(l) for l in wago]
