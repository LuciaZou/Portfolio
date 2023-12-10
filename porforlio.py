import streamlit as st

def main():
    st.title('Lucia Zou Data Science Portfolio')
    st.header('About Me')
    st.text('Welcome! I am Lucia Zou, a fresh graduate from BrainStation Data Science Bootcamp.')
    st.text('I am excited to have new opportunities in the data science field.')
    st.text('I am eager to bring my analytical skills to a great team.')
    st.text('If you are looking for a data scientist, I would love to connect!')
    st.text('Feel free to contact me for potential job opportunities or collaborative projects.')
    st.text('Thank you!')

    # Project
    st.subheader('Liquor Store Profits Prediction')
    st.markdown("[capstone](https://github.com/LuciaZou/capstone)",unsafe_allow_html=True)
    st.markdown('Used machine learning models to forecast future profits of liquor stores in Iowa')
    # Add images, links, code snippets as needed
    st.image('d60309127f7dd4dd05ec3e21e4b5673c.jpg', width=200)

st.sidebar.title("Contact Me")

# Now let's add the QR code to the sidebar
# Add LinkedIn link
st.sidebar.markdown("[LinkedIn](https://www.linkedin.com/in/luciazouyue)", unsafe_allow_html=True)
qr_code_image = 'image_6483441.JPG'
st.sidebar.image(qr_code_image, caption='Scan the QR Code', width=200)

# Add Github link
st.sidebar.markdown("[Github](https://github.com/LuciaZou/capstone)", unsafe_allow_html=True)

# Add Email link
st.sidebar.markdown("[Email](mailto:lucia.zouyuebca@gmail.com)", unsafe_allow_html=True)

#https://github.com/LuciaZou/capstone/blob/main/Screenshot%20Capstone.png

st.markdown(
    """
    <style>
    .main {
        background: url("https://getwallpapers.com/wallpaper/full/0/6/b/1418311-gradient-wallpapers-1920x1200-mobile.jpg");
        background-size: 100% 100%;
        display: flex;
        align-items: center;
        text-color: white;
        min-height: 100vh;
    }
    </style>
    """,
    unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
