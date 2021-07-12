from altair.utils.schemapi import SchemaValidationError
import streamlit as st
import numpy as np 
import pandas as pd
import altair as alt
from PIL import Image
import time

st.title("Streamlit 超入門") #タイトルつける

st.write("Dataframe") #表を作る

df = pd.DataFrame({
    "1列目":[500,501,502,503],
    "2列目":[623,624,635,661]
 })

st.dataframe(df.style.highlight_max(axis=0),width=300,height=300) #表の幅と高さ、表の表示,最大値にハイライト
#"""これを使うとテキストを表示できる　#で段落分け,```pythonコードを書くためのモノ **で太字に
"""
# 章
Streamlit is **really cool**
## 節

### 項

```python
import streamlit as st
import numpy as np 
import pandas as pd

```

"""
st.latex(r''' 
a + ar + a r^2 +a r^3 +\cdots +a r^{(n-1)} =
\sum_{k=0}^{n-1} a r^k =
a\left(\frac{1-r^{n}}{1-r}\right)''') #式も入れられる

df = pd.DataFrame(
    np.random.rand(20,3),
    columns = ["a","b","c"] #20行3列の乱数の行数を作る
)

st.dataframe(df.style.highlight_max(axis=0),width=300,height=300)
st.line_chart(df) #折れ線グラフ
st.bar_chart(df) #棒グラフ

c =alt.Chart(df).mark_circle().encode(
    x="a",y="b",size="c",color="c",tooltip=["a","b","c"] #x軸をa,y軸をb,値をcとしている
)
st.altair_chart(c) #散布図

df = pd.DataFrame(
    np.random.rand(100,2)/[50,50]+[35.33,139.26],
    columns = ["lat","lon",] #緯度、経度、店の緯度と経度がわかれば、簡単にマッピングできる
)

st.map(df) #マッピング


st.write("Display Image")

if st.checkbox("Show Image"): #Checkboxにチェックを入れると表示できるように
    img = Image.open("000001.jpg")
    st.image(img,caption="光ピンセット",use_column_width =True) #画像の表示

st.write("Interactive Widgets")

option = st.selectbox(
    "あなたが好きな数字を教えてください",
    list(range(1,11)) #セレクトボックスに数字を入れると表示
)
"あなたの好きな数字は、",option,"です"

text = st.text_input("あなたの趣味を教えて下さい") #言葉の挿入
"あなたの趣味は",text,"です。間違いありませんか？"

slider = st.slider("あなたの今の調子は？",0,100,50) #最小値が0,最大値が10,最初の位置50
"コンディション:",slider

st.sidebar.write("スライドバーの作成")
text2 =st.sidebar.text_input("あなたの好きなゲームは？") #sidebarの中に横の質問事項
university =st.sidebar.slider("大学の志望度は？",0,100,50)

"あなたの好きなゲームは",text2,"です"
"大学の志望度は",university,"です"

left_column, right_column = st.beta_columns(2) #ボタンの使い方と2カラムレイアウト
button = left_column.button("右カラムに文字を表字")
if button:
    right_column.write("ありがとうございます。")

expander = st.beta_expander("問い合わせ") #問い合わせをクリックすると問い合わせ内容を表示できる。
expander.text_input("問い合わせ内容をお書きください。")
st.write("お電話の場合は0120-00-1120まで")


st.write("プレグレスバーの表示")
"Start!!!!!"

latest_iteration = st.empty() #プログレスバーの作成
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"進行中{i+1}") #どのように変化させるか記入
    bar.progress(i + 1)
    time.sleep(0.1)
"終了です"






