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
from heiwa4126.fizzbuzz import fizzbuzz

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

- 以下のコマンドは Windows ではうまく動かないかも。[Python Packaging User Guide のドキュメント読んでアレンジしてください](https://packaging.python.org/en/latest/tutorials/installing-packages/)。
- Linux や Mac では `pip3` のとこは `python3 -m pip` でもいいです。

```sh
# このレポジトリをクローン
git clone https://github.com/heiwa4126/heiwa4126-fizzbuzz.git
cd heiwa4126-fizzbuzz

# とりあえずサンプル実行
heiwa4126_fizzbuzz/fizzbuzz.py

# ユニットテスト実施
python3 -m unittest

# 開発とデプロイ用のパッケージインストール
pip3 install -U --user -r requirements-dev.txt

# ビルド (先に pip3 install build が必要)
python3 -m build

# ビルド & インストール
pip3 install --user -U .
## または
pip3 install --user -U -e . # 昔の `python setup.py develop` 相当

# (pyproject.tomlの場合) ビルド後、ローカルユーザにインストール
pip3 install --user -U dist/*.whl
## またはソースからビルド & インストール
pip3 install --user -U dist/*.tar.gz

# ローカルユーザからアンインストール
pip3 uninstall heiwa4126-fizzbuzz
## または
pip3 uninstall heiwa4126_fizzbuzz
```

デフォルトでは

- $HOME/.local/lib/python3.10/site-packages/heiwa4126_fizzbuzz-0.0.1.dist-info/
- $HOME/.local/lib/python3.10/site-packages/heiwa4126_fizzbuzz/
- $HOME/.local/lib/python3.10/site-packages/tests/

のような場所にインストールされる。

## PyPI への登録

の前に TestPyPI へ登録する。

1. [アカウントを作成する · TestPyPI](https://test.pypi.org/account/register/)
2. 2FA 設定する。やらないと API トークンがもらえない (2024-02 現在)
3. [アカウント設定 · TestPyPI](https://test.pypi.org/manage/account/#api-tokens) で API トークンを 1 つ作る。
4. ↑ の最後に従って `$HOME/.pypirc` 書く。`chmod og= "$HOME/.pypirc"`お忘れなく。この設定ファイル作らなくても twine 実行時に対話的にできるらしい。

ここまで出来たら

```sh
python3 -m build
python3 -m twine upload --repository testpypi dist/*
```

で アップロードすると
[heiwa4126-fizzbuzz · TestPyPI](https://test.pypi.org/project/heiwa4126-fizzbuzz/) が作成/更新される。

TestPyPI からインストールするには

```sh
pip3 install -U --user -i https://test.pypi.org/simple/ heiwa4126-fizzbuzz
```

上記と同じことを PyPI で行う。
