# heiwa4126-fizzbuzz

この Python プロジェクトは、FizzBuzz のジェネレータを実装します。

PyPI と GitHub Copilot の練習。

## インストール

このパッケージは PyPI からインストールできます。次のコマンドを実行してください:

```sh
pip install heiwa4126-fizzbuzz
```

## 使用方法

このパッケージは、FizzBuzz のジェネレータを提供します。以下のように使用できます:

```python
from heiwa4126_fizzbuzz import fizzbuzz

for item in fizzbuzz(15):
    print(item)
```

このコードは、1 から始まり、"Fizz"、"Buzz"、または "FizzBuzz" を適切に出力します。

## GitHub Copilot

このコードのひな形は GitHub Copilot を使って以下のプロンプトで作りました。

```console
@workspace /new fizzbuzzを生成するpythonプロジェクト。pypiで配布可能なディレクトリ構成で、プロジェクト名はheiwa4126_fizzbuzz。fizzbuzzはジェネレータで実装。
```

## 開発関連

※ Windows ではうまく動かないかも

```sh
# とりあえずサンプル実行
heiwa4126_fizzbuzz/fizzbuzz.py

# ユニットテスト実施
python3 -m unittest

# ビルド (先に pip3 install build が必要)
python3 -m build

# (pyproject.tomlの場合) ローカルユーザにインストール
pip3 install --user -U dist/*.whl
## or
pip3 install --user -U dist/*.tar.gz

# (setup.pyの場合) ローカルユーザにインストール
pip3 install . --user -U

# ローカルユーザからアンインストール
pip3 uninstall heiwa4126_fizzbuzz
```

デフォルトでは

- $HOME/.local/lib/python3.10/site-packages/heiwa4126_fizzbuzz-0.0.1.dist-info/
- $HOME/.local/lib/python3.10/site-packages/heiwa4126_fizzbuzz/
- $HOME/.local/lib/python3.10/site-packages/tests/

のような場所にインストールされる。

## PyPI への登録

1. [アカウントを作成する · PyPI](https://pypi.org/account/register/)

(続く)
