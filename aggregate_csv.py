# csvファイルを読み書きするcsvモジュールをインポート!
import csv

# csvファイルを受け取り、集計する関数
def aggregate_csv(file_name):
    try:
        # ファイルを開く
        with open(file_name,newline='', encoding='utf-8') as csvfile:
            # csvリーダーでファイルを読み取る
            reader = csv.reader(csvfile)
            total = 0
            # ヘッダー行をスキップ
            next(reader)
            # 各行を読み取って処理
            for row in reader:
            #データが不完全な行
                if len(row) < 2:
                    print(f"警告: 不完全な行がありました {row}")
                    continue
                try:
                    # 数量の数値に変換
                    value = float(row[1])
                    # 合計に加算
                    total += value
                except ValueError:
                    print(f"警告: '{row[1]}'は数値に変換できません")
            # 合計を表示
            print(f"合計:{total}")

            # 合計結果をoutput.csvに保存する
            try:
                with open('output.csv','w',newline='',encoding='utf-8') as outputfile:
                    writer = csv.writer(outputfile)
                    # ヘッダー行を追加
                    writer.writerow(["合計"])
                    # 合計を追加
                    writer.writerow([total])
                    print("集計結果をoutput.csvに保存しました。")
            except Exception as e:
                print(f"ファイル書き込みエラー：{e}")

    except FileNotFoundError:
        # 指定されたファイルが見つからない場合にエラーメッセージを表示
        print("エラー:指定したcsvファイルが見つかりません")
    except Exception as e:
        # その他の予期しないエラーが発生した場合、エラーメッセージを表示
        print(f"予期しないエラーが発生しました:{e}")

# ユーザーがファイル名を入力、そのファイルを処理する
file_name = input("読み込むcsvファイル名を入力してください:")
# 上記の関数を呼び出して、指定されたファイルを集計
aggregate_csv(file_name)
