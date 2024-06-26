import streamlit as st
from os import path

dir = path.dirname(path.abspath(__file__))
image_path = path.join(dir, "../assets/profile2.jpeg")


def show_member(member: dict):
    for person in member:
        columns = st.columns((0.3, 0.7), vertical_alignment="center")
        with columns[0]:
            st.image(path.join(dir, member.get(person)[0]))
        with columns[1]:
            with st.container(border=True):
                st.subheader(person)
                for i, info in enumerate(member.get(person)):
                    if i == 0:
                        pass
                    elif i == 2:
                        st.page_link(info, label="Linkedin")
                    else:
                        st.write(info)


st.set_page_config(page_title="About Us", page_icon="😊")

st.markdown(
    """
    <p style='text-align: center; font-size: 2.5rem;'>
    <strong>
    ABOUT US
    </strong>
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown("# OUR MISSION")

st.markdown(
    """
    <blockquote style='text-align: center; font-size: 1.50rem; font-family: serif'>
    <i>
    Misi kami adalah menyediakan akses yang mudah dan terjangkau bagi seluruh lapisan
    masyarakat untuk memantau dan meningkatkan kesehatan gigi mereka secara mandiri,
    didukung oleh teknologi AI terdepan yang revolusioner dan inovatif.
    </i>
    </blockquote>
    """,
    unsafe_allow_html=True,
)

st.divider()
st.markdown("# OUR TEAM")

team_ai = {
    "Gunung Pambudi Wibisono": [
        "../assets/gunung.png",
        "gunungpambudiw@gmail.com",
        "https://www.linkedin.com/in/gunungpw/",
    ],
    "Wisnu Eka Saputra. S": [
        "../assets/wisnu.png",
        "wisnuekasaputra@hotmail.com",
        "https://id.linkedin.com/in/wisnuekasaputra",
    ],
    "Vauwez Sam El Fareez": [
        "../assets/vauwez.png",
        "vsefareez@outlook.com",
        "https://www.linkedin.com/in/samfareez/",
    ],
    "Aisyah Amalia Al Fitri": [
        "../assets/amalia.png",
        "arsyah291200@gmail.com",
        "https://www.linkedin.com/in/aisyahamaliaalfitri/",
    ],
    "Irvan Achmad Ashari": [
        "../assets/irfan.png",
        "irvanachmadashari@gmail.com",
        "https://www.linkedin.com/in/maragopan",
    ],
}

team_data = {
    "Adi Kurniawan": [
        "../assets/adi.png",
        "adikurniawan917@gmail.com",
        "https://www.linkedin.com/in/adi-kurniawan-b65a2579/",
    ],
    "Gishelawati": [
        "../assets/ghiselawati.png",
        "gishelawati01@gmail.com",
        "https://www.linkedin.com/in/gishelawati-129982201/",
    ],
    "Nibras Alfaruqiyah": [
        "../assets/nibras.png",
        "alfaruqiyah.nibras@gmail.com",
        "https://www.linkedin.com/in/nibras-alfaruqiyah-web-developer-data/",
    ],
    "Bagus Akhlaq": [
        "../assets/bagus.png",
        "bagusakhlaq@gmail.com",
        "https://www.linkedin.com/in/bagus-akhlaq",
    ],
}

st.write("## Team AI")
show_member(team_ai)

st.write("## Team Data")
show_member(team_data)
