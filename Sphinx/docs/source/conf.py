# -- Path setup --------------------------------------------------------------
import os
import sys
sys.path.insert( 0, os.path.abspath("./") ) # conf.pyが格納されているディレクトリを，PYthonモジュール検索パスに追加する


# -- Project information -----------------------------------------------------
project = "sampleSphinx"
copyright = "2025, YANAKA Shunsuke"
author = "YANAKA Shunsuke"
release = "1.0.0"


# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc", # docstring形式コメントを自動でドキュメント化するためのもの
    "sphinx.ext.napoleon" # googleスタイルのdocstringに対応させるためのもの
]

templates_path = ["_templates"]
exclude_patterns = []

language = "ja"

# Pythonコード内のimport文が原因で，Sphinxによるドキュメント出力にWARNINGとなった場合，対象ライブラリをモックとして扱い回避する
autodic_mock_imports = [
    "pandas",
    "pycaret"
]


# -- Options for HTML output -------------------------------------------------
# html_theme = "alabaster" # Webサイト形式のドキュメントにおける，デフォルトのテーマ
html_theme = "sphinx_rtd_theme" # Tips 第1章でインストールしたテーマ
html_static_path = ["_static"]
html_css_files = ["sampleCSS.css"] # CSSの適用（複数のCSSファイルを適用する場合は，カンマ区切りで可能）