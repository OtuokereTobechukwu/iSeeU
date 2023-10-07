from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os

from wordcloud import WordCloud, STOPWORDS

# get data directory (using getcwd() is needed to support running example in generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

# Read the whole text.
# text = open(path.join(d, "text.txt")).read()
# words = "He is an amazing writer and singer. Such an amazing singer and an accomplished artist. He has won 3 grammys becuase he is so amazing. I never knew he had so much talent. topping world stages"
text = "He is an amazing writer and singer. Such an amazing singer and an accomplished artist. He has won 3 grammys becuase he is so amazing. I never knew he had so much talent. topping world stages"
# read the mask image
# taken from
# http://www.stencilry.org/stencils/movies/alice%20in%20wonderland/255fk.jpg
alice_mask = np.array(Image.open(path.join(d, "head_silhouette.jpeg")))

stopwords = set(STOPWORDS)
stopwords.add("said")

wc = WordCloud(
    background_color="white",
    max_words=2000,
    mask=alice_mask,
    stopwords=stopwords,
    contour_width=2,
    contour_color="#C0C0C0",
)

# generate word cloud
wc.generate(text)

# store to file
# wc.to_file(path.join(d, "alice.png"))

# show
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
fig1 = plt.gcf()
fig1.savefig("tessstttyyy.png", dpi=300)
