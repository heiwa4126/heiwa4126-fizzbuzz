# heiwa4126.fizzbuzz

Python 用の FizzBuzz ジェネレータパッケージ。
このプロジェクトは PyPI と GitHub Copilot の練習です。

## インストール

```sh
pip install heiwa4126.fizzbuzz
```

## 使用方法

このパッケージは、FizzBuzz のジェネレータを提供します。以下のように使用できます:

```python
from heiwa4126.fizzbuzz import fizzbuzz

for item in fizzbuzz(15):
    print(item)
```

このコードは、1 から始まり、"Fizz"、"Buzz"、または "FizzBuzz" を適切に出力します。

```python
from heiwa4126.fizzbuzz import fizzbuzz

for item in fizzbuzz(15):
    print(item)
# or
print("\n".join(fizzbuzz(15)))
```

## GitHub Copilot

このコードのひな形は GitHub Copilot を使って以下のプロンプトで作りました。

```text
@workspace /new fizzbuzzを生成するpythonプロジェクト。pypiで配布可能なディレクトリ構成で、プロジェクト名はheiwa4126_fizzbuzz。fizzbuzzはジェネレータで実装。
```

## 開発メモ

[煩雑な開発メモ](docs/development-note.md) は GitHub で見てね。
