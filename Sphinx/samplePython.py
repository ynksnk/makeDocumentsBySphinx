#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""samplePython.pyの概要
docstiling形式のコメント記述に関する，サンプルプログラム

2025.1.19　YANAKA Shunsuke
"""


class sampleClass:
    """クラスsampleClassの概要
        クラスにおけるdocstling形式コメントの表記を例示するためのクラス
    
    Attributes:
        sample_value(int): 任意の整数値を格納する変数
        sample_string(str): 任意の文字列を格納する変数
    
    .. figure:: ./images/図の挿入例.jpg
	:width: 100%
	:align: center
	:alt: 図　figureを用いて図を挿入した様子
	
	図 figureを用いて図を挿入した様子
    """

    def __init__(self, sample_value, sample_string = "Hello"):
        """コンストラクタの概要

        Args:
            sample_value(int): 任意の整数
            sample_string(str, optional): 任意の文字列
        """
        self.sample_value = sample_value
        self.sample_string = sample_string

    def set_value(self, value):
        """クラス関数set_valueの概要
            クラス変数sample_valueに値を設定する関数

        Args:
            value (int): 任意の整数
        """
        self.sample_value = value

    def get_value(self):
        """クラス関数get_valueの概要
            クラス変数sample_valueの値を取得する関数

        Returns:
            int: クラス変数sample_valueの値
        """
        return self.sample_value

    def get_string(self):
        """クラス関数get_stringの概要
            クラス変数sample_stringの値を取得する関数

        Returns:
            str: クラス変数sample_stringの値
        """
        return self.sample_string


sc = sampleClass(100, "hogehoge")
sc.set_value(200)
print("sample_valueの値: ", sc.get_value())
print("sample_stringの値: ", sc.get_string())