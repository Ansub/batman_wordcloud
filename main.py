from wordcloud import WordCloud, STOPWORDS ,ImageColorGenerator
import matplotlib.pyplot as plt  #to display the wordcloud
from PIL import Image            #to load our image
import numpy as np               #to get the color of our image

#content
text = open("batman.txt", "r").read()
stopwords = set(STOPWORDS)

#appearance-related
custom_mask = np.array(Image.open("batman.png"))
wc = WordCloud(background_color="white",
               stopwords= stopwords,
               mask = custom_mask
               )
wc.generate(text)
image_colors = ImageColorGenerator(custom_mask)
wc.recolor(color_func = image_colors)


# #plotting
# plt.imshow(wc, interpolation  = "bilinear")
# plt.axis("off")
# plt.show()

#save
wc.to_file("batmanwordcloud.png")