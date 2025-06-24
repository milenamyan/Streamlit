import streamlit as st
from time import sleep
#with st.echo(): # For showing cod in bowser
progress_bar = st.progress(0)

for i in range(100):
    sleep(0.005)
    progress_bar.progress(i+1)

st.title('My Streamlit App')
st.header('I am a header')
st.subheader('I am a subheader')
st.text('I am a text')
# st.balloons()
# st.snow()
st.dataframe([{'name': 'first', 'age': 1}, {'name' : 'second', 'age': 2}])
st.json({
    "product": "panir",
    "Type": "Chanax"
})
# st.line_chart([10,12,14,15,20,30,25,20,50])
if st.button('Click me!'):
    st.write("Button clicked!")

if st.checkbox("Check me!"):
    st.write("Checkbox checked!")

option = st.selectbox('Choose an option', ['option1', 'option2','option3'])
st.write('You selected:', option)

slider_value = st.slider('Slide me', 0, 100, step = 5)
st.write('Slider value:', slider_value)

num_input_value = st.number_input('Num input', min_value=0.0, max_value=100., step=5.0)
st.write("Number input value:", num_input_value)

text = st.text_input('Please input text')
st.write('Text input value: ', text)

uploaded_file = st.file_uploader('Upload a file')
if uploaded_file is not None:
    st.write('File uploaded')

st.sidebar.header('Sidebar')
st.sidebar.text('This is a sidebar')


rating1 = st.feedback('stars')
rating2 = st.feedback('faces')
st.write(f'Rating1: {rating1}')
st.write(f'Rating2: {rating2}')

color = st.color_picker('Pick a color')
st.write('Selected color: ', color)

# enable = st.checkbox('Enable camera')
# picture = st.camera_input('Take a pictue', disabled = not enable)
# if picture:
#     st.image(picture)

audio_value = st.audio_input('Record a voice message')
if audio_value:
    st.audio(audio_value)

col1, col2, col3 = st.columns(3)

with col1:
    st.header("A cat")
    st.image("https://static.streamlit.io/examples/cat.jpg")

with col2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg")

with col3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg")

# with col4:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")