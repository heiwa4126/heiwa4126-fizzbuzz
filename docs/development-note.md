# 煩雑な開発メモ

## 開発関連

タスクランナーに [invoke](https://pypi.org/project/invoke/) を使っています。事前に

```sh
pip install invoke -g
```

で invoke をインストールしてください。

```sh
# このレポジトリをクローン
git clone https://github.com/heiwa4126/heiwa4126-fizzbuzz.git
cd heiwa4126-fizzbuzz

# (推奨)./.venv に venv環境作成
inv setup

# (オプション)とりあえずサンプル実行
inv example
```

開発は

```sh
# ソースを ./srcの下にいろいろ書く
# テストを ./testの下にいろいろ書く

# ユニットテスト実施
inv test

# ビルド
inv build

# インストール
inv install

# アンインストール
inv uninstall

# 再インストール (アンインストールしてビルドしてインストール)
inv reinstall

# Ruffによる自動修正
inv fix

## inv xxx は他にもいろいろあるので tasks.py を見てください
## または `inv -l`

#-- 上記手順をくりかえす
```

ここまでできたら

```sh
git add --all
git commit -am 'any messages'
inv release  # build & `npm versin patch` みたいなもの
```

で発行の準備完了

### PyPI への登録

**の前に TestPyPI へ登録する。**

1. [アカウントを作成する · TestPyPI](https://test.pypi.org/account/register/)
2. 2FA 設定する。やらないと API トークンがもらえない (2024-02 現在)
3. [アカウント設定 · TestPyPI](https://test.pypi.org/manage/account/#api-tokens) で API トークンを 1 つ作る。
4. ↑ の最後に従って `$HOME/.pypirc` 書く。`chmod og= "$HOME/.pypirc"`お忘れなく。この設定ファイル作らなくても twine 実行時に対話的にできるらしい。

ここまで出来たら

```sh
python3 -m twine upload --repository testpypi dist/*
# or
inv upload_testpypi
```

で アップロードすると
[heiwa4126-fizzbuzz · TestPyPI](https://test.pypi.org/project/heiwa4126-fizzbuzz/) が作成/更新される。

TestPyPI からインストールするには

```sh
pip3 install -U --user -i https://test.pypi.org/simple/ heiwa4126-fizzbuzz
```

オプション `-U` と `--user` はお好みで。

次に
上記と同じことを PyPI で行う。

## 古い開発メモ

(invoke を使う前のメモ。一部間違いあり)

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

### PyPI への登録(古い)

**の前に TestPyPI へ登録する。**

1. [アカウントを作成する · TestPyPI](https://test.pypi.org/account/register/)
2. 2FA 設定する。やらないと API トークンがもらえない (2024-02 現在)
3. [アカウント設定 · TestPyPI](https://test.pypi.org/manage/account/#api-tokens) で API トークンを 1 つ作る。
4. ↑ の最後に従って `$HOME/.pypirc` 書く。`chmod og= "$HOME/.pypirc"`お忘れなく。この設定ファイル作らなくても twine 実行時に対話的にできるらしい。

ここまで出来たら

```sh
rm -rf dist
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

## namespace 付き(風)の pip のモジュール名は heiwa4126.fizzbuzz と heiwa4126-fizzbuzz のどちらがいいですか?

いろいろ調べたけど

- Python でのパッケージ名はアンダースコアで
- pip でのパッケージ名はハイフンで

という「風習」しかないみたい。

---

Python のパッケージ名を規定しているのは、PEP 8 (Python Style Guide) です。

PEP 8 には、Python のコーディングスタイルに関する様々な規約が定められています。
その中の 1 つに、パッケージ名の命名規則が含まれています。

具体的には、以下のようになっています。

- パッケージ名は短くて、Python の単語にするのが理想的
- パッケージ名は小文字で、単語の区切りには underscore を使う
- パッケージ名の prefix (django* や app*)の使用は避ける

つまり、推奨されるパッケージ名は例えば以下のようになります。

```
mypackage
my_package
```

PEP 8 は Python コミュニティで広く支持され、
Python のコーディングスタイルの事実上の標準となっているため、
パッケージ名もこの規約に従うことが推奨されています。
コードの読みやすさと一貫性を保つためです。

---

PIP のパッケージ名を規定している公式文書は PEP 508 です。

PEP 508 は「Dependency specification for Python Software Packages」と題されており、
Python パッケージの依存関係の指定方法について定めています。その中で、パッケージ名の命名規則も明記されています。

PEP 508 によると、パッケージ名は以下の規則に従う必要があります。

- ASCII 文字のみを使用し、大文字小文字を区別する
- アンダースコア(\_)、ハイフン(-)、ピリオド(.)が使用可能
- 先頭文字はアンダースコアまたは ASCII 文字
- Python のキーワードは使用不可

さらに、以下のようなベストプラクティスも推奨されています。

- ハイフン(-)は OS 間の移植性のために避ける
- ピリオド(.)は名前空間パッケージを表すために避ける
- アンダースコア(\_)は内部的な意味を持つので避ける

つまり、PIP のパッケージ名としては"simple-name"や"simple.name"よりも"simplename"のようなフラットな名前が推奨されているということになります。

この PEP 508 の規則に従うことで、パッケージ名の曖昧さを避け、異なるパッケージ間で名前が衝突するリスクを低減できます。

---

今回は「名前空間パッケージ」なので heiwa4126.fizzbuzz にする。
