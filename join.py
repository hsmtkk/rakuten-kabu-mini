with open("code.txt", "w", encoding="utf-8") as f:
    for i in range(18):
        with open(f"result/page-{i}.txt", "r", encoding="utf-8") as g:
            content = g.read()
        f.write(content)
