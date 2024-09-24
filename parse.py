from langchain_openai import ChatOpenAI

chat = ChatOpenAI(model="gpt-4o-mini")

base_prompt = """# 指示
下記の「入力」を読み込み、コード一覧と、リアルタイム取引が「○」のコード一覧を出力せよ。

# 入力例
コード 銘柄名 寄付取引 リアルタイム取引 コード 銘柄名 寄付取引 リアルタイム取引
1301極洋 ○ - 1882東亜道路 ○ -
1332ニッスイ ○ ○ 1884日本道路 ○ ○

# 出力例
```
# コード一覧
1301
1332
1882
1884

# リアルタイム取引コード一覧
1332
1884
```

# 入力
"""

for i in range(18):
    with open(f"text/page-{i}.txt", "r", encoding="utf-8") as f:
        content = f.read()
    prompt = base_prompt + content
    ans = chat.invoke(prompt)
    with open(f"result/page-{i}.txt", "w", encoding="utf-8") as f:
        f.write(ans.content)
