import streamlit as st
# @st.cache(allow_output_mutation=True)
# 1. add form
# 2. add data caching
# 3. use session state to maintain any variables if needed.

def clean_text(text):
    text = text.replace("'", "").replace("-\n", "").replace("\n", " ").strip()
    return text

def print_hi(name):
    container = st.container()
    # Use a breakpoint in the code line below to debug your script.
    st.title("Cat's App")
    # st.write("Wowzers schmousers this new app is so cool!")
    # button1 = st.button("clickaroo")
    # if button1:
    #     st.write("Clicked zee button.")
    #
    # like = st.checkbox("do you like this app?")
    # button2 = st.button("submit")
    # if button2:
    #     if like:
    #         st.write("cool")
    #     if not like:
    #         st.write("whaaat?")
    # st.header("Start of the Radio Button Section")
    # animal = st.selectbox("what animal is your fav", ("bears", "rams", "mtn lions"))
    # button4 = st.button("submit animal")
    # if button4:
    #     st.write(animal)
    #     if animal == 'mtn lions':
    #         st.write("ROAR!")
    # st.header("multi select")
    # animal2 = st.multiselect("what animals do you like?", ["bears", "rams", "mtn lions"])
    # button5= st.button("submit multiselect")
    # if button5:
    #     st.write(animal2)
    #     if 'mtn lions' in animal2:
    #         st.write("ROAR!")
    # st.header("slider")
    # epochs = st.slider("epochs eh?", 1, 100, 10)
    # button6 = st.button("submit epochs")
    # if button6:
    #     st.write(epochs)
    # user_text = st.text_input("what's your fav?", "starlink")
    # if st.button("toosteroo"):
    #     st.write(user_text + " rinosasaurus!")
    #
    # user_num = st.number_input("que est tu nombre?")
    if 'test' not in st.session_state:
        st.session_state['test'] = 0
    if st.button("up"):
        st.session_state.test += 1
        container.write(st.session_state.test)
    if st.button("down"):
        st.session_state.test -= 1
        container.write(st.session_state.test)
        # st.write(user_num)
    #
    # side_text = st.sidebar.text_area("lutoo?", "gezoinks")
    # if st.sidebar.button("print side text"):
    #     col1, col2 = st.columns(2)
    #     col1.header("orig text")
    #     clean = clean_text(side_text)
    #     col1.write(clean + " alooza!")
    #     col2.header("cleaned text")
    #     col2.write(clean + " alooza!")
    #
    # form1 = st.sidebar.form(key="Options")
    # form1.header("TEST FORM")
    # ent_types = form1.multiselect("Select something", ["TEST_1", "TEST_2", "TEST_3"])
    # form_button = form1.form_submit_button("form submit")
    #
    # if form_button:
    #     form1.write(ent_types)








# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
