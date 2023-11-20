import streamlit as st
import random

# 音楽のデータベース（例）
music_recommendations = {
    "Happy": ["HappySong1", "HappySong2", "HappySong3"],
    "Sad": ["SadSong1", "SadSong2", "SadSong3"],
    "Energetic": ["EnergeticSong1", "EnergeticSong2", "EnergeticSong3"],
    "Calm": ["CalmSong1", "CalmSong2", "CalmSong3"]
}

# Streamlitアプリケーションの開始
st.title('あなたにおススメの〇〇')
st.write('あなたに合った〇〇を診断します')

# 音楽のデータベース（例）
music_recommendations = {
    "Happy": ["HappySong1", "HappySong2", "HappySong3"],
    "Sad": ["SadSong1", "SadSong2", "SadSong3"],
    "Energetic": ["EnergeticSong1", "EnergeticSong2", "EnergeticSong3"],
    "Calm": ["CalmSong1", "CalmSong2", "CalmSong3"]
}

# Streamlitアプリケーションの開始
mood = st.selectbox("あなたの今の気分は？:", ["うれしい", "悲しい", "元気", "落ち着いている"])

# 選択された気分に基づいて音楽を提案
if mood in music_recommendations:
    st.subheader(f"Recommended songs for {mood}:")
    recommended_songs = music_recommendations[mood]
    random_song = random.choice(recommended_songs)
    st.write(f"🎵 {random_song}")
else:
    st.warning("Invalid mood selection. Please choose a valid mood.")

# コードを実行するには、ターミナルで以下のコマンドを実行します
# streamlit run streamlit_Daichi.py