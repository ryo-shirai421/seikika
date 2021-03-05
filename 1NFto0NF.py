# 第1正規形のデータを非正規データに変換するプログラム
# -*- coding: utf-8 -*-
import csv

dict = {}

# 第1正規形のデータを読み込む
with open('1NFdata.tsv', newline='') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        if row[0] in dict.keys():  # キーが存在する場合
            dict[row[0]] = dict[row[0]] + ':' + row[1]
        else:
            dict[row[0]] = row[1]

# 同階層にあるtsvファイルに書き込む
with open('0NFdata.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator="\n")
    for k, v in dict.items():
        writer.writerow([k, v])
