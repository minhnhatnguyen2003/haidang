from wordcloud import WordCloud, STOPWORDS
import imageio
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image


st.title("Hello Đăng :point_right: :point_left:")

# Import packages
import numpy as np
from PIL import Image

text = 'HaiDang,Confident,Smart,Talented,Passionate,Humble,LowkeyCrazy,Horny,Caring,FutureDoctor,Kind,Memelord,Uvuvwevwevwe onyetenyevwe ugwemuhwem osas, 1_Kilo_of_feathers, Why_are_u_gay'

# Import packages
import matplotlib.pyplot as plt
# Define a function to plot word cloud
def plot_cloud(wordcloud):
    # Set figure size
    plt.figure(figsize=(40, 30))
    # Display image
    plt.imshow(wordcloud) 
    # No axis details
    plt.axis("off");


# Import package
from wordcloud import WordCloud, STOPWORDS
# Generate word cloud
wordcloud = WordCloud(width = 300, height = 200, random_state=1, background_color='salmon', colormap='Pastel1', collocations=False, stopwords = STOPWORDS).generate(text)
# Plot

if st.button("A random button I made 4 u" ):
        with st.spinner("Appreciation post :eyes:"):
          st.subheader("One: I admire your light and your warmth; they make everyday brighter.")
          st.subheader("Two: I admire your drive and intelligence. I have no doubt that you'll achieve great things.")
          st.subheader("Three: I love your energy.How the hell can you do a morning class, basketball and football? You amaze me in every way :blush:")
          st.text("I made this 'WordCloud' abt what I think of you")
          st.pyplot(plot_cloud(wordcloud))
          st.subheader("I want to be better with you, and I know that I can help you too. So let me... ask this corny question: ")
          st.subheader('Will you be my mập địt? Send your answer on Messenger :))')
          st.write('If yes, send me :pig_nose:')
          st.write('If no, send me :japanese_ogre:')
          st.write("If you need more time, send me :clock1: but you'll have max 3hours")

