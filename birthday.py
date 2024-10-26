import tkinter as tk

# グローバル変数（配列）の宣言
# 保存用の配列　本当はハッシュとキーで管理したいが、今回は配列で管理
namae = []
eat = []
seibetu = []
yaruki = []

# 削除用の配列
namesakujyo = []
sukisakujyo = []
seibetusakujyo = []
yarukisakujyo = []

# データを登録し、下部に表示する関数
def regist():
    # GUIの各入力値を変数に取得。GUIと内部の橋渡しのコード
    ans1 = entry1.get()
    ans2 = entry2.get()
    ans3 = selected_option.get()

    # チェックボックスの値を取得
    check = var.get()
    # if文の真偽チェックで格納する値を変更
    if check:
        ans4 = "やる気あり"
    else:
        ans4 = "ぷぅ～"

    # データをリストに追加
    namae.append(ans1)
    eat.append(ans2)
    seibetu.append(ans3)
    yaruki.append(ans4)  

    # 登録済のデータを下部に表示する。配列の数に応じて表示数を増加。iは0からスタート
    for i in range(len(namae)):
        # 名前の表示
        name_label = tk.Label(root, text=namae[i])
        name_label.grid(row=i + 6, column=0, padx=5, pady=5)
        namesakujyo.append(name_label)

        # 好きな食べ物の表示
        eat_label = tk.Label(root, text=eat[i])
        eat_label.grid(row=i + 6, column=1, padx=5, pady=5)
        sukisakujyo.append(eat_label)

        # 性別の表示
        seibetu_label = tk.Label(root, text=seibetu[i])
        seibetu_label.grid(row=i + 6, column=2, padx=5, pady=5)
        seibetusakujyo.append(seibetu_label)

        # やる気の表示
        yaruki_label = tk.Label(root, text=yaruki[i])
        yaruki_label.grid(row=i + 6, column=3, padx=5, pady=5)
        yarukisakujyo.append(yaruki_label)
def delete():
    # 配列を合体させて、一気に削除しようとする。
    for label in namesakujyo + sukisakujyo + seibetusakujyo + yarukisakujyo:
    # destroy()は、tkinterウィジェット（ここではラベルオブジェクト）を画面上から削除
        label.destroy()
    # 保存用配列の削除　for文が分かりにくいときは、上のコードもぶっちゃけ個別にdestroyでいい。
    namae.clear()
    eat.clear()
    seibetu.clear()
    yaruki.clear()
    # 削除用配列自体の削除
    namesakujyo.clear()
    sukisakujyo.clear()
    seibetusakujyo.clear()
    yarukisakujyo.clear()

# メインウィンドウのセットアップ
root = tk.Tk()
root.geometry("400x400")

# GUIパーツの作成
label1 = tk.Label(root, text='名前')
label2 = tk.Label(root, text='好きな食べ物')

# Entry（ユーザー入力部分）のインスタンス化
entry1 = tk.Entry(root)
entry2 = tk.Entry(root)

# ラジオボタンの作成
# tk.StringVar()はラジオボタンの選択値を格納する変数
selected_option = tk.StringVar(value="男")
# variable=selected_optionで選択された値がselected_option変数に保存
radiobutton1 = tk.Radiobutton(root, text="男", variable=selected_option, value="男")
radiobutton2 = tk.Radiobutton(root, text="女", variable=selected_option, value="女")
radiobutton3 = tk.Radiobutton(root, text="未回答", variable=selected_option, value="不明")

# チェックボックスの作成
# TrueまたはFalseを格納するための変数varを作成
var = tk.BooleanVar()
checkbox = tk.Checkbutton(root, text='やる気', variable=var)

# 登録ボタンを作成。登録ボタン押下でregist関数を実行
btn1 = tk.Button(root, text="登録", command=regist)
btn2 = tk.Button(root, text="データ削除", command=delete)

# GUIに作った部品を配置(起動時にセッティング)
label1.grid(row=0, column=0, padx=5, pady=5)
entry1.grid(row=0, column=1, padx=5, pady=5)
label2.grid(row=1, column=0, padx=5, pady=5)
entry2.grid(row=1, column=1, padx=5, pady=5)
radiobutton1.grid(row=3, column=0, pady=5)
radiobutton2.grid(row=3, column=1, pady=5)
radiobutton3.grid(row=3, column=2, pady=5)
checkbox.grid(row=4, column=1, padx=5, pady=5)
btn1.grid(row=5, column=1)
btn2.grid(row=5, column=2)

# メインループの開始
root.mainloop()
