import discord
from discord.ext import commands
from datetime import datetime

intents = discord.Intents.default()
intents.guilds = True
intents.voice_states = True

bot = commands.Bot(command_prefix="!", intents=intents)

# 設定
NOTIFY_CHANNEL_ID = 12345678910111213  # ここに通知を送信したいチャンネルIDを張り付ける
voice_session_data = {}  # ボイスチャンネル入退室の情報を保持

@bot.event
async def on_voice_state_update(member, before, after):
    notify_channel = bot.get_channel(NOTIFY_CHANNEL_ID)
    
    # ユーザーがボイスチャンネルに入室
    if before.channel is None and after.channel is not None:
        voice_session_data[member.id] = datetime.now()
        
        # 入室の埋め込みメッセージ
        embed = discord.Embed(
            title="入室通知",
            description=f"{member.display_name} が {after.channel.name} に入室しました。",
            color=discord.Color.green()
        )
        embed.set_thumbnail(url=member.avatar.url)
        
        await notify_channel.send(embed=embed)
    
    # ユーザーがボイスチャンネルから退室
    elif before.channel is not None and after.channel is None:
        enter_time = voice_session_data.pop(member.id, None)
        
        if enter_time:
            exit_time = datetime.now()
            duration = exit_time - enter_time
            days, remainder = divmod(duration.total_seconds(), 86400)  # 1日の秒数86400で分割
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)
            
            # 通話時間の表示
            duration_str = f"{int(days)}日 {int(hours)}時間 {int(minutes)}分 {int(seconds)}秒" if days > 0 else f"{int(hours)}時間 {int(minutes)}分 {int(seconds)}秒"
            
            embed = discord.Embed(
                title="退室通知",
                description=f"{member.display_name} が {before.channel.name} から退室しました。",
                color=discord.Color.red()
            )
            embed.set_thumbnail(url=member.avatar.url)
            embed.add_field(name="入室時刻", value=enter_time.strftime('%m月%d日 %H時%M分'), inline=False)
            embed.add_field(name="退室時刻", value=exit_time.strftime('%m月%d日 %H時%M分'), inline=False)
            embed.add_field(name="通話時間", value=duration_str, inline=False)
            
            await notify_channel.send(embed=embed)

# Bot起動
bot.run("abcdefgh123456789ijkl") #ここにbotのTokenを張り付ける
