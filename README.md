# VC-Notice-Discord-Bot
VCの入退室と退出時に入退室時刻と通話時間を通知する

![Image](https://github.com/llenn7711/VC-Notice-Discord-Bot/blob/main/image.png?raw=true)
## 仕様
### Discord Botアカウントの作成
- [Discord Developer Portal](https://discord.com/developers/applications)よりBotアカウントを作成します。

### コードの書き換え
- 12行目：```NOTIFY_CHANNEL_ID```入退室通知のメッセージを送信したいチャンネルのチャンネルIDに置き換えます。
- 60行目：```bot.run```を使用したいBotのTokenに置き換えます。
  
### インストール
- Python 3.x
- 必要なライブラリのインストール
- discord.py
   詳しくは[Discord.py](https://github.com/Rapptz/discord.py)
  
```
py -3 -m pip install -U discord.py
```

### プログラムの実行

```
python vc.py
```
