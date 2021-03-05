# 正規形出ないデータをtsvファイルから読み取り、第1正規形へと変換するプログラム
# -*- coding: utf-8 -*-

import csv, itertools

# 2次元データを1次元にする関数 -> ((o,o),o)などを(o,o,o)に変換
def flatten(data):
    flatten_data = []
    for i in range(len(data)):
        if isinstance(data[i], tuple) or isinstance(data[i], list):
            for j in range(len(data[i])):
                flatten_data.append(data[i][j])
        else:
            flatten_data.append(data[i])
    return flatten_data

# tsvファイルからデータをリストとして読み込む(ファイルは同じ階層にあるとする)
with open('data.tsv') as f:
    reader = csv.reader(f, delimiter='\t')
    rows = [row for row in reader]

result_data = []

for row in rows:   
    prev_col_data = []
    
    for i in range(len(row)):
        splited_data = row[i].split(':')
        # 最初の1列目はprev_col_dataが空なので処理を分ける。
        if(i==0):
            prev_col_data = splited_data
            continue

        # 前の列から順に直積を取ることで全ての組み合わせを求める。
        present_data = list(itertools.product(prev_col_data, splited_data))
        
        for j in range(len(present_data)):
            present_data[j] = flatten(present_data[j])
        # 今まで見た列のデータを代入
        prev_col_data = present_data
            
    for data in present_data:
        result_data.append(data)

# 整形されたデータを同階層のtsvファイルへと書き込む。
with open('1NFdata.tsv', 'w') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator="\n")
    writer.writerows(result_data)

