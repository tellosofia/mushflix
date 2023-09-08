import streamlit as st
from PIL import Image

st.title('Welcome back to :red[Mushflix] :mushroom:, Ahmed!')
st.header('We hope you enjoy movies as much as we do!', divider = 'red')
st.subheader("Take a look at this film we think you'll love!")

youtube_url = 'https://youtu.be/bxABOiay6oA?si=ioh9wO1e3CpRVJqD'
st.video(youtube_url)

# ***First row*** Can we actually turn this into a row?
st.header('Check out the TOP movies!', divider = 'gray')
st.subheader(":sunglasses: best ratings and popularity :sunglasses:")

col1, col2, col3 = st.columns(3)

with col1:
    st.image('https://image.tmdb.org/t/p/original/tDGOyLbrNj47wFN0H7nmtHoEfN0.jpg', caption = 'Body Heat')
    st.image('https://image.tmdb.org/t/p/original/h68ilwiTesb5wmDgy2mHYkVuOBP.jpg', caption = 'The General')
    st.image('https://image.tmdb.org/t/p/original/vNXGrknx4GjWLgmuNTftWZluIUl.jpg', caption = 'Whiplash')
                
with col2:           
    st.image('https://image.tmdb.org/t/p/original/tilClWjFZeUTGJu0pxgF72fvUmN.jpg', caption = 'All about my mother')
    st.image('https://image.tmdb.org/t/p/original/ysKahAEPP8h6MInuLjr0xuZOTjh.jpg', caption = 'Snatch')
    st.image('https://image.tmdb.org/t/p/original/uLtVbjvS1O7gXL8lUOwsFOH4man.jpg', caption = 'Guardians of the Galaxy')

with col3:
    st.image('https://image.tmdb.org/t/p/original/e1rPzkIcBEJiAd3piGirt7qVux7.jpg', caption = 'Hot Fuzz')
    st.image('https://image.tmdb.org/t/p/original/mYnU5LqkCjWJLGSp9Oabbdq1GlI.jpg', caption = 'The longest day')
    st.image('https://image.tmdb.org/t/p/original/lJxtMpsFyWINiXqV0ZW0LgwtAWE.jpg', caption = 'Lois C.K.: Live at the Beacon Theater')


# *** Second row***

st.header("Since you enjoyed 'Dolores Clairbone' we custom-made this list for you", divider = 'gray')
st.subheader(":heart: :green_heart: :heart: :green_heart: :heart: :green_heart: :heart: :green_heart: :heart: :green_heart: :heart: :green_heart: :heart: :green_heart: :heart: :green_heart:")

col4, col5, col6 = st.columns(3)

with col4:
    st.image('https://image.tmdb.org/t/p/original/5GCUPT3yRkVjJ0uXJ66lR9Lrs1e.jpg', caption = 'Rob Roy')
    st.image('https://image.tmdb.org/t/p/original/6sV6PNt3Oi2GMSvsMzZpkXv1vSQ.jpg', caption = 'Quiz Show')
    st.image('https://image.tmdb.org/t/p/original/ogKegWajhtkFUmDbCqsa2rJLwbn.jpg', caption = 'Legends of the Fall')
                
with col5:           
    st.image('https://image.tmdb.org/t/p/original/ka6np2LONtAElZOVeebb3mwSTBs.jpg', caption = 'Dead Man Walking')
    st.image('https://image.tmdb.org/t/p/original/fYER1mVSnBVsPBSC7IAN0bbscGN.jpg', caption = 'Copycat')
    st.image('https://image.tmdb.org/t/p/original/9qkepBLafRQVuMXWgnjqvdefD92.jpg', caption = 'Don Juan DeMarco')

with col6:
    st.image('https://image.tmdb.org/t/p/original/fHuKwcrwltGlWn3510N1YO7vJ4I.jpg', caption = "What's Eating Gilbert Grape")
    st.image('https://image.tmdb.org/t/p/original/mK7yzlKsgFePRs24Eki9XsJYJj7.jpg', caption = 'French Kiss')
    st.image('https://image.tmdb.org/t/p/original/3jrwJiMCe7VZP0DNcywHYOKg0Zu.jpg', caption = 'Ed Wood')

# *** Third and last row ***

st.header("With love, curated just for you!", divider = 'gray')

col7, col8, col9 = st.columns(3)

with col7:
    st.image('https://image.tmdb.org/t/p/original/3Rfvhy1Nl6sSGJwyjb0QiZzZYlB.jpg', caption = 'Toy Story')
    st.image('https://image.tmdb.org/t/p/original/1J4Z7VhdAgtdd97nCxY7dcBpjGT.jpg', caption = 'Grumpier Old Men')
    st.image('https://image.tmdb.org/t/p/original/xKsnZDERG1dk95wuZ5q9iks3OL3.jpg', caption = 'Heat')
                
with col8:           
    st.image('https://image.tmdb.org/t/p/original/9JcMUzQy9gPqDmJJGH3AcL145mv.jpg', caption = 'From Dusk Till Dawn')
    st.image('https://image.tmdb.org/t/p/original/yTDwyUEYHZTK35z7Iyp4QHxvVj9.jpg', caption = 'Bottle Rocket')
    st.image('https://image.tmdb.org/t/p/original/c4vkEcwWiRAg5TAb4sbuIElSR4T.jpg', caption = 'Canadian Bacon')

with col9:
    st.image('https://image.tmdb.org/t/p/original/kjFYGZLDGWMIp3tV4nuWQ4oWDar.jpg', caption = "Desperado")
    st.image('https://image.tmdb.org/t/p/original/5ESLsrW33Kw2c3GeLNHrG4Ef9M5.jpg', caption = 'Billy Madison')
    st.image('https://image.tmdb.org/t/p/original/2zU6nh8h9WS4aiwoaxgAEv7QPCm.jpg', caption = 'Clerks')

st.balloons()
