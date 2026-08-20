import streamlit as sl
from PIL import Image

sl.title("La app de Juan José López Patinno")

sl.header("I Gave up for Lent")
sl.write("I'm not even going for the bronze!")
image = Image.open("Give_Up!.webp")
sl.image(image, caption="I'm staying right here, man.")

text = sl.text_input("What are you giving up on today?", "I'm giving up on...")
sl.write("Nice! I would give up on ", text, " too!")

col1, col2 = sl.columns(2)

with col1:
  sl.subheader("I'm giving up on this column!")
  sl.write("There's no point in still trying if you're not going anywhere!")
  resp = sl.checkbox("So true, bestie.")
  if resp:
    sl.write("You totes get me, bro.")

with col2:
  sl.subheader("Also this one!")
  mode = sl.radio("What do you wanna do after giving up?", ("Pick up something else.", "Give up some more.", "Die."))
  if mode == "Pick up something else.":
    sl.write("I should probably do that too.")
  if mode == "Give up some more.":
    sl.write("That is so based.")
  if mode == "Die.":
    sl.write("Maybe don't...")
  
