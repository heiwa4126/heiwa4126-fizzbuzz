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

# (オプション)./.venv に venv環境作成
inv setup

# とりあえずサンプル実行
inv example

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

## 他にもいろいろあるので tasks.py を見てください
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
