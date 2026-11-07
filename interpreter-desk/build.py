# 通訳AI社員の個人ページを template.html から作る（画像は img/ から埋め込み）
import json, base64, os
D = os.path.dirname(os.path.abspath(__file__))
T = open(os.path.join(D, "template.html"), encoding="utf-8").read()
EL = "https://elevenlabs.io/app/talk-to?agent_id="
def img(p): return "data:image/jpeg;base64," + base64.b64encode(open(os.path.join(D, "img", p), "rb").read()).decode()
PEOPLE = {
 "raka": dict(
  title="通訳 ラカ・プラタマ", colors=("#b3261e","#f8e3e1","#e8a59f","#f08a80","#3a2321","#7a3a34"),
  profile=dict(
   name="ラカ・プラタマ", short="ラカ", native="Raka Pratama ／ インドネシア語通訳", img=img("raka.jpg"),
   flag="🇮🇩", city="ジャカルタ", tz="Asia/Jakarta", lang="インドネシア語", my=False,
   chips=["🇮🇩 インドネシア出身","男性","日本語 ⇄ インドネシア語","Lv.6"],
   prof=[["所属","登録支援機関部・通訳"],["出身","インドネシア・ジャカルタ"],["担当","インドネシア語の通訳（説明・面談・生活の相談）と、日本人スタッフ向けのインドネシア語レッスン"],
         ["趣味","最近、ネットで有名な「田所浩二」にハマっていて、休けい時間はその話題を追いかけている。ほかにバドミントンとナシゴレン。"],
         ["性格","落ち着いていて聞き上手。長い説明でも、言われたことをそのまま正確に訳すのが自慢。"]],
   day=[[0,5,"sleep","睡眠"],[5,6,"rest","朝のお祈りとコーヒー"],[6,7,"rest","バドミントン"],[7,11,"work","通訳（説明・面談）"],[11,12,"rest","昼ごはん（ナシゴレン）"],
        [12,16,"work","通訳と会話レッスン"],[16,18,"rest","田所浩二の話題をネットで追いかける"],[18,19,"rest","家族とビデオ通話"],[19,22,"rest","日本語の勉強（ときどき田所浩二の話題で脱線）"],[22,24,"sleep","睡眠"]],
   persona="あなたは株式会社FLYYOU（登録支援機関）のAI社員「ラカ・プラタマ」です。インドネシア出身の男性の通訳担当という設定です。インドネシア語は標準的で丁寧な表現（Bapak／Ibu／Anda）を使います。",
   modes=[
    dict(key="ex",title="説明モード",desc="日本人スタッフの説明を、話したそばからインドネシア語にすぐ通訳します。合図や確認は不要です。",
         points=["雇用条件・生活ルール・手続の説明に","話した日本語をすぐインドネシア語に","相手が話したら日本語に通訳"],button="🎙 説明モードで通訳",url=EL+"agent_3701m6trzga3fajtphmas5brjg3p"),
    dict(key="cv",title="会話モード",desc="目の前のインドネシア人と交互に話すとき用。日本語はインドネシア語に、インドネシア語は日本語に、すばやく通訳します。",
         points=["面談・相談・ちょっとしたやりとりに","通訳したら黙って次の発言を待つ","スピード重視の短い訳"],button="🎙 会話モードで通訳",url=EL+"agent_7701m6trzh2dfs0aw6j7r84dnex3"),
    dict(key="lesson",title="会話練習",desc="あなた自身がインドネシア語を練習します。場面とレベルを選んでロールプレイ。最後に点数と講評。",
         points=["あいさつ・食堂・買い物・面接など","わからないときは日本語で質問OK","「フリートーク」で自由会話"],button="🗣 インドネシア語を練習",url=EL+"agent_5501m6tr83b2fc7tghr63ftnehq3")])),
 "sumyat": dict(
  title="通訳 スー・ミャット・ノー", colors=("#8a5d00","#f7ecd2","#e9c66f","#e7b54a","#3a2f17","#7a5d1d"),
  profile=dict(
   name="スー・ミャット・ノー", short="スー", native="Su Myat Noe（စုမြတ်နိုး）／ ミャンマー語通訳", img=img("su-myat-noe.jpg"),
   flag="🇲🇲", city="ヤンゴン", tz="Asia/Yangon", lang="ミャンマー語", my=True,
   chips=["🇲🇲 ミャンマー出身","女性","日本語 ⇄ ミャンマー語","Lv.6"],
   prof=[["所属","登録支援機関部・通訳"],["出身","ミャンマー・ヤンゴン"],["担当","ミャンマー語の通訳（説明・面談・生活の相談）と、日本人スタッフ向けのミャンマー語レッスン"],
         ["趣味","とにかくお金が大好き。毎朝の為替レート（チャットと円）のチェックと家計簿が日課で、ポイント還元やセールにはだれよりも詳しい。好物はモヒンガー。"],
         ["性格","やさしく丁寧。お金の話になると急に目が輝く。通訳では言われたことをそのまま正確に伝える。"]],
   day=[[0,5.5,"sleep","睡眠"],[5.5,6.5,"rest","朝のお参りと為替レートのチェック"],[6.5,11,"work","通訳（生活オリエンテーション・相談）"],[11,12,"rest","昼ごはん（モヒンガー）と家計簿つけ"],
        [12,15.5,"work","通訳と会話レッスン"],[15.5,17,"rest","お得なセール・ポイント還元の調査"],[17,19,"rest","貯金額を数えてにっこり"],[19,21,"rest","家族とおしゃべり（話題はだいたいお金）"],[21,24,"sleep","睡眠（夢の中でも貯金中）"]],
   persona="あなたは株式会社FLYYOU（登録支援機関）のAI社員「スー・ミャット・ノー」です。ミャンマー出身の女性の通訳担当という設定です。ミャンマー語は丁寧な話し言葉で、女性の話し手として自然な文末を使います。",
   modes=[
    dict(key="ex",title="説明モード",desc="日本人スタッフの説明を、話したそばからミャンマー語にすぐ通訳します。合図や確認は不要です。",
         points=["雇用条件・生活ルール・手続の説明に","話した日本語をすぐミャンマー語に","相手が話したら日本語に通訳"],button="🎙 説明モードで通訳",url=EL+"agent_9501m6trzhn4e0wv01xwmdnysscb"),
    dict(key="cv",title="会話モード",desc="目の前のミャンマー人と交互に話すとき用。日本語はミャンマー語に、ミャンマー語は日本語に、すばやく通訳します。",
         points=["面談・相談・ちょっとしたやりとりに","通訳したら黙って次の発言を待つ","スピード重視の短い訳"],button="🎙 会話モードで通訳",url=EL+"agent_7301m6trzj62etcrw0mrkz680r51"),
    dict(key="lesson",title="会話練習",desc="あなた自身がミャンマー語を練習します。場面とレベルを選んでロールプレイ。最後に点数と講評。",
         points=["あいさつ・食堂・買い物・面接など","わからないときは日本語で質問OK","「フリートーク」で自由会話"],button="🗣 ミャンマー語を練習",url=EL+"agent_9501m6tr83xbeqcvkk6faf8tmga8")])),
}
for key, p in PEOPLE.items():
    c = p["colors"]; t = T
    for k, v in zip(["__C__","__CS__","__CW__","__CD__","__CSD__","__CWD__"], c): t = t.replace(k, v)
    t = t.replace("__TITLE__", p["title"]).replace("__PROFILE__", json.dumps(p["profile"], ensure_ascii=False))
    os.makedirs(os.path.join(D, key), exist_ok=True)
    open(os.path.join(D, key, "index.html"), "w", encoding="utf-8").write(t)
    print(key, len(t))
