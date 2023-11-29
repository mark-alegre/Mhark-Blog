import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie 
import time

def app():
    
    with st.container():
            col1, col2 = st.columns([1,3])
            with col2:
              st.title(":green[News Report📣]")
               
            with col1:
                def load_lottiefile(filepath: str):
                        with open(filepath, "r") as f:
                                return json.load(f)


                def load_lottieurl(url: str):
                        r = requests.get(url)
                        if r.status_code != 200:
                                return None
                        return r.json()
                

                lottie_coding = load_lottiefile("news.json")  # replace link to local lottie file
                lottie_hello = load_lottieurl("https://lottie.host/f1d4b951-5ba0-40a2-91e5-f7cdede4b750/8RQN7Sxmt4.json")

                st_lottie(
                        lottie_hello,
                        speed=1,
                        reverse=False,
                        loop=True,
                        quality="low", # medium ; high
                        height=None,
                        width=None,
                        key=None,
                )
            st.write("---") 
    with st.container():
            st.subheader(":red[Survival, scandal, a secret cell: how the nail-biting Israel-Hamas hostage deal was done]")
            st.write("---")
            image = 'news1.png'
            st.image(image, caption='📷Hamas militants transport Yaffa Adar, 85, an Israeli civilian kidnapped from Nir Oz, into Gaza in a golf cart on 7 October. Photograph: AP',use_column_width=True)
            st.write("---")
    with st.container():
            st.write(
                    """
                    - ✅ The footage of hostages, many of them teenagers and younger, being seized and driven away crying and pleading with their captors, was as harrowing as the sight of the corpses Hamas left behind.

                    - ✅ The slaughter of Israeli civilians on 7 October was intended to strike terror into the Israeli psyche and inflict a lasting wound. The hostage-taking was done for other reasons: as a brake on Israeli retaliation and to trade for Palestinian prisoners in Israeli jails. Seven weeks later, it has clearly worked better as a bargaining chip than as a deterrent.

                    - ✅ The estimated 240 hostages in Gaza did not stop the intense, relentless bombing of Gaza or the ground offensive on 27 October. Only now, almost a month on, has a four-day lull been agreed, arguably when it suits the Israel Defense Forces (IDF). If Saturday’s crisis, which halted the second round of releases, can be overcome, the ceasefire could be expanded by a few days perhaps, but Israel has left little doubt the war will go on.

                    - ✅ The planned release of as many as 150 Palestinians, on the other hand, is an important gain for the mastermind of the 7 October attack, Yahya Sinwar, who spent more than 23 years in an Israeli prison. It is where he became fluent in Hebrew and acquired an in-depth grasp of Israeli politics and society. It is also where he developed a determination to liberate the thousands of Palestinians held in Israeli jails.
                    """
               )
    with open('news.css') as source_des:
        st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
    social_media = {
         "Read More": "https://www.theguardian.com/world/2023/nov/26/survival-scandal-a-secret-cell-how-the-nail-biting-israel-hamas-hostage-deal-was-done",
        }
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")
    st.write("---")
    
    with st.container():
            st.subheader(":red[📝 U.S.-Philippines Agree to Modernize, Strengthen Alliance]")
            st.write("---")
            image = 'news2.png'
            st.image(image, caption='By Jim Garamone , DOD News',use_column_width=True)
            st.write("---")
    with st.container():
            st.write(
                    """
                    - ✅ The United States and the Philippines will continue the fundamental work needed to modernize and strengthen the alliance between the two nations,
                    said Secretary of Defense Lloyd J. Austin III and Philippine President Ferdinand R. Marcos Jr. today at the Pentagon.
                    """
            )
            st.write("---")
            st.write(
                    """
                   - ✅ The secretary hosted a full-honors ceremony for the close ally on the Pentagon Parade Field — the first such ceremony for more than three years
                    """
            )
            image = 'news2.1.png'
            st.write(
                    """
                        - ✅ The secretary reiterated the United States' ironclad commitment to the Philippines under the Mutual Defense Treaty. The treaty, Austin said, "applies to armed attacks on our armed forces, coast guard vessels, public vessels, or aircraft in the Pacific, including anywhere in the South China Sea. So, make no mistake, Mr. President, we will always have your back in the South China Sea or elsewhere in the region."

                        - ✅ Spotlight: Focus on Indo-Pacific
                        Marcos came to the Pentagon the day after meetings with President Joe Biden at the White House. The visit is the latest in a series of meetings between the two nations. Austin visited Manila in February and met with Marcos at the Malacanang Palace. Last month, the two nations held "two-plus-two" talks with defense and foreign affairs leaders in Washington.

                        - ✅ Marcos said this visit furthers the efforts to strengthen relationships between the two nations. A DOD official said the visit is happening at a historic moment in the alliance. The two militaries are deepening coordination and interoperability at all levels, the official said.
                    """
            )
    with open('news.css') as source_des:
        st.markdown(f'<style>{source_des.read()}</style>', unsafe_allow_html=True)
    social_media = {
         "Read More": "https://www.defense.gov/News/News-Stories/Article/Article/3383809/us-philippines-agree-to-modernize-strengthen-alliance/",
        }
    cols = st.columns(len(social_media))
    for index, (platform, link) in enumerate(social_media.items()):
        cols[index].write(f"[{platform}]({link})")