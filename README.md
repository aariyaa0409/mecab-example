# mecab-example
ここでは形態素解析に必要となるユーザー辞書を作成する。

Mecabのデフォルトではipadic辞書を使用しており、複合語(名詞＋名詞)のような単語は名詞ごとに分割されてしまう。
これを防ぐため、複合語のみの辞書を作成し、形態素解析時に辞書指定すること狙った通りの解析結果を得る。

test.csvは文章中の名詞が連続するパートを「複合語」として取得した結果である。
取得した複合語に対し、makedic.pyにて左右接続ID、コスト値を割り振る。左右接続ID・コスト値とは、その語句の頻出割合を示すパラメータである。
アウトプットとしてdictionary.csvを得る。これがユーザー辞書となる。
