import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly_express as px

st.set_page_config(
    page_title="Kemiskinan dan Tingkat Stunting pada Balita: Tren, Wawasan, dan Korelasi di Jawa Barat (2015-2020)",
)

pp, name = st.columns([1, 10])
pp.image("data/profile/pp.jpg", width=60)
name.markdown(
    """
        <style>
            .name {
                margin-top: -15px;
            }
            .sub {
                margin-top: -20px;
            }
            .date {
                margin-top: -20px;
                font-size: 12px;
            }
        </style>
    """,
    unsafe_allow_html=True,
)
name.markdown("<h6 class='name'>Bagas Shalahuddin Wahid</h6>", unsafe_allow_html=True)
name.markdown("<p class='sub'>TETRIS III: The CEO Project</p>", unsafe_allow_html=True)
name.markdown("<p class='date'>12 Juni 2023</p>", unsafe_allow_html=True)

"---"

st.title("Kemiskinan dan Tingkat Stunting pada Balita: Tren, Wawasan, dan Korelasi di Jawa Barat (2015-2020)")

st.write(
    """
    Stunting, yang ditandai oleh pertumbuhan fisik yang terhambat pada bayi dan anak-anak, 
    merupakan masalah kesehatan yang serius dan kompleks di banyak negara berkembang, termasuk Indonesia. 
    Stunting dapat memiliki konsekuensi jangka panjang terhadap kesehatan dan perkembangan anak, 
    termasuk penurunan kemampuan kognitif, rendahnya produktivitas di masa dewasa, serta meningkatkan risiko penyakit kronis.

    Salah satu faktor yang dapat mempengaruhi tingkat stunting pada bayi adalah kemiskinan. 
    Kemiskinan merupakan masalah sosial yang melibatkan kekurangan akses terhadap sumber daya dan kesempatan yang mendasar, 
    termasuk pangan yang bergizi, akses ke layanan kesehatan, sanitasi yang memadai, dan pendidikan.

    Jawa Barat, sebagai salah satu provinsi terpadat di Indonesia, tidak luput dari permasalahan kemiskinan dan stunting pada bayi. 
    Provinsi ini memiliki keberagaman sosial-ekonomi yang signifikan, dengan sebagian penduduknya masih hidup di bawah garis kemiskinan. 
    Oleh karena itu, penting untuk menganalisis hubungan antara kemiskinan dan tingkat stunting pada bayi di Jawa Barat 
    guna memahami faktor-faktor yang berkontribusi terhadap prevalensi stunting dan merumuskan langkah-langkah intervensi yang tepat.

    Melalui analisis tersebut, dapat diharapkan pemangku kebijakan, organisasi kesehatan, dan masyarakat dapat memahami 
    hubungan antara kemiskinan dan stunting pada bayi di Jawa Barat, serta mengevaluasi kebijakan yang ada dan merancang strategi baru 
    untuk mengurangi angka stunting di wilayah tersebut. Dengan demikian, upaya pencegahan dan penanggulangan stunting pada bayi 
    dapat dilakukan secara lebih efektif dan terarah, guna memastikan generasi muda Jawa Barat tumbuh dengan potensi optimal dan memiliki masa depan yang cerah.
    """
)
st.markdown(
    "<h3>Tren Kemiskinan dan Balita Stunting di Jawa Barat Beserta Wawasan</h3>", unsafe_allow_html=True
)
kemiskinan, stunting = st.tabs(["Kemiskinan", "Tingkat Stunting"])

with kemiskinan:
    pers_kemiskinan = pd.read_csv("data/cleaned-data/Persentase Kemiskinan 2015-2020.csv")

    pers_kemiskinan['tahun'] = pd.to_datetime(pers_kemiskinan['tahun']).dt.year
    pers_kemiskinan.set_index('tahun', inplace=True)

    fig = px.line(pers_kemiskinan, x=pers_kemiskinan.index, y="JAWA BARAT", title="Persentase Kemiskinan di Provinsi Jawa Barat")
    fig.update_traces(mode="lines+markers", marker=dict(size=5))
    
    fig.update_layout(
        xaxis=dict(title="Tahun"),
        yaxis=dict(title="Persentase Kemiskinan", range=[0, 20]),
        hovermode="x",
        legend=dict(title="Kabupaten/Kota"),
        annotations=[
            dict(
                text="Sumber: Badan Pusat Statistik (BPS)",
                xref="paper",
                yref="paper",
                x=0,
                y=-0.2,
                showarrow=False,
                font=dict(size=10),
            )
        ],
    )

    st.plotly_chart(fig)

    st.write(
    """Dari data yang diberikan mengenai tingkat kemiskinan di Jawa Barat dari tahun 2015 hingga 2020, 
    berikut adalah beberapa insight yang dapat diperoleh:
    """
    )
    st.markdown("- Trend Penurunan: Terdapat tren penurunan tingkat kemiskinan di Jawa Barat selama periode yang diamati. Pada tahun 2015, tingkat kemiskinan mencapai 9.496%, dan secara bertahap mengalami penurunan hingga mencapai 6.893% pada tahun 2019 sebelum naik sedikit menjadi 7.851% pada tahun 2020.")
    st.markdown("- Terdapat penurunan yang signifikan dalam tingkat kemiskinan dari tahun 2017 hingga tahun 2018, dengan penurunan sebesar 1.251%. Hal ini menunjukkan adanya upaya yang dilakukan untuk mengurangi tingkat kemiskinan di Jawa Barat.")
    st.markdown("- Meskipun terjadi penurunan secara keseluruhan, terjadi peningkatan sedikit pada tingkat kemiskinan di tahun 2020 dibandingkan dengan tahun sebelumnya. Peningkatan ini mungkin dipengaruhi oleh faktor-faktor seperti perubahan kondisi sosial-ekonomi dan dampak pandemi COVID-19.")

    
with stunting:
    pers_stunting =  pd.read_csv("data/cleaned-data/Persentase Stunting 2015-2020.csv")
    #Persentase Stunting di Provinsi Jawa Barat
    pers_stunting['tahun'] = pd.to_datetime(pers_stunting['tahun']).dt.year
    pers_stunting.set_index('tahun', inplace=True)

    fig = px.line(pers_stunting, x=pers_stunting.index, y="JAWA BARAT", title="Persentase Balita Stunting di Provinsi Jawa Barat")
    fig.update_traces(mode="lines+markers", marker=dict(size=5))
    
    fig.update_layout(
        xaxis=dict(title="Tahun"),
        yaxis=dict(title="Persentase Balita Stunting", range=[0, 20]),
        hovermode="x",
        legend=dict(title="Kabupaten/Kota"),
        annotations=[
            dict(
                text="Sumber: Badan Pusat Statistik (BPS)",
                xref="paper",
                yref="paper",
                x=0,
                y=-0.2,
                showarrow=False,
                font=dict(size=10),
            )
        ],
    )

    st.plotly_chart(fig)
    
    st.write(
    """Dari data yang diberikan mengenai tingkat stunting pada balita di Jawa Barat dari tahun 2015 hingga 2020, 
    beberapa insight yang dapat diperoleh adalah sebagai berikut:
    """
    )
    st.markdown("- Trend Penurunan: Terdapat tren penurunan tingkat stunting pada balita di Jawa Barat selama periode yang diamati. Pada tahun 2015, tingkat stunting mencapai 9.974%, namun secara bertahap mengalami penurunan hingga mencapai 6.922% pada tahun 2019 sebelum naik lagi menjadi 9.441% pada tahun 2020.")
    st.markdown("- Penurunan yang Signifikan: Terdapat penurunan yang signifikan dalam tingkat stunting dari tahun 2017 hingga tahun 2018, dengan penurunan sebesar 2.149%. Hal ini menunjukkan adanya upaya yang dilakukan untuk mengatasi masalah stunting di Jawa Barat.")
    st.markdown("- Perbedaan Tren: Meskipun terjadi penurunan secara keseluruhan, terdapat variasi dalam tren tingkat stunting pada balita di Jawa Barat. Setelah mencapai titik terendah pada tahun 2019, tingkat stunting mengalami peningkatan pada tahun 2020.")
    st.markdown("- Peningkatan tingkat stunting pada tahun 2020 menunjukkan adanya faktor-faktor yang mempengaruhi seperti perubahan kondisi sosial-ekonomi, pandemi COVID-19, atau faktor lainnya yang perlu dianalisis lebih lanjut untuk memahami penyebabnya.")

st.markdown(
    "<h3>Tren Kemiskinan dan Balita Stunting di Jawa Barat Berdasarkan Kabupaten/Kota</h3>", unsafe_allow_html=True
)

kemiskinan, stunting = st.tabs(["Kemiskinan", "Tingkat Stunting"])

with kemiskinan:
    kabupaten_kota = pers_kemiskinan.columns.tolist()

    show_all1 = st.checkbox("Show All Kabupaten/Kota",  key="show_all_kemiskinan")

    if show_all1:
        selected_kabupaten_kota = kabupaten_kota
    else:
        selected_kabupaten_kota = st.multiselect("Pilih Kabupaten/Kota", kabupaten_kota, key="select_kab_kemiskinan", default="KABUPATEN BANDUNG")

    filtered_data = pers_kemiskinan[selected_kabupaten_kota]

    filtered_data = filtered_data.reset_index()

    fig = px.line(filtered_data, x="tahun", y=selected_kabupaten_kota)

    fig.update_layout(
        xaxis_title="Tahun",
        yaxis_title="Persentase Kemiskinan",
        title="Grafik Persentase Kemiskinan Berdasarkan Kabupaten/Kota"
    )

    st.plotly_chart(fig)
    
    st.write(
    """Dari data yang diberikan mengenai tingkat stunting pada balita di Jawa Barat dari tahun 2015 hingga 2020 berdasarkan kabupaten/kota, 
    beberapa insight yang dapat diperoleh adalah sebagai berikut:
    """
    )
    st.markdown("- Secara umum, di semua kabupaten/kota tingkat kemiskinan di Jawa Barat mengalami penurunan di rentang 2015-2019, tapi mengalami peningkatan di tahun 2020")
    st.markdown("- Kota Tasikmalaya menjadi kota dengan persentase tingkat kemiskinan paling tinggi di sepanjang tahun, berbeda dengan Kota Depok yang memiliki persentase tingkat kemiskinan yang paling rendah")

with stunting:
    kabupaten_kota = pers_stunting.columns.tolist()

    show_all2 = st.checkbox("Show All Kabupaten/Kota", key="show_all_stunting")

    if show_all2:
        selected_kabupaten_kota = kabupaten_kota
    else:
        selected_kabupaten_kota = st.multiselect("Pilih Kabupaten/Kota", kabupaten_kota, key="select_kab_stunting", default="KABUPATEN BANDUNG")

    filtered_data = pers_stunting[selected_kabupaten_kota]

    filtered_data = filtered_data.reset_index()

    fig = px.line(filtered_data, x="tahun", y=selected_kabupaten_kota)

    fig.update_layout(
        xaxis_title="Tahun",
        yaxis_title="Persentase Stunting pada Balita",
        title="Grafik Persentase Stunting pada Balita Berdasarkan Kabupaten/Kota"
    )

    st.plotly_chart(fig)
    
    st.write(
    """Dari data yang diberikan mengenai tingkat stunting pada balita di Jawa Barat dari tahun 2015 hingga 2020 berdasarkan kabupaten/kota, 
    beberapa insight yang dapat diperoleh adalah sebagai berikut:
    """
    )
    st.markdown("- Secara umum, di semua kabupaten/kota tingkat stunting pada balita di Jawa Barat mengalami penurunan di rentang 2015-2019, tapi mengalami peningkatan di tahun 2020")
    st.markdown("- Kota Tasikmalaya menjadi kota dengan persentase tingkat stunting pada balita paling tinggi di sepanjang tahun, berbeda dengan Kota Depok yang memiliki persentase tingkat stunting pada balita paling rendah")
st.markdown(
    "<h3>Analisis Korelasi Kemiskinan dan Balita Stunting di Jawa Barat</h3>", unsafe_allow_html=True
)

# Create a Streamlit selectbox for choosing the Kabupaten
selected_kabupaten = st.selectbox('Select Kabupaten', pers_kemiskinan.columns)

# Get the Kemiskinan and Stunting data for the selected Kabupaten
kemiskinan_data = pers_kemiskinan[selected_kabupaten]
stunting_data = pers_stunting[selected_kabupaten]

# Calculate the correlation coefficient (r)
r = np.corrcoef(kemiskinan_data, stunting_data)[0, 1]

# Create a Streamlit scatter plot
st.pyplot(plt.figure(figsize=(8, 6)))
plt.scatter(kemiskinan_data, stunting_data)

# Set the plot title and labels
plt.title(f'Kemiskinan vs Stunting di {selected_kabupaten}')
plt.xlabel('Kemiskinan')
plt.ylabel('Stunting')

# Show the plot
st.pyplot(plt)

# Create a table to display the correlation coefficient
table_data = {'Correlation Coefficient (r)': [r]}
correlation_table = pd.DataFrame(table_data)
st.table(correlation_table)

# Calculate the average correlation coefficient for all Kabupaten
avg_r = np.mean(np.corrcoef(pers_kemiskinan, pers_stunting))

# Display the average correlation coefficient
st.write(f'Average Correlation Coefficient: {avg_r}')

st.write(
    """Kesimpulan : 
    """
    )
st.markdown("- Korelasi tingkat kemiskinan dan tingkat balita yang stunting adalah berkorelasi sedang")
st.markdown("- Terjadi peningkatan untuk kemiskinan dan balita yang stunting di tahun 2020, yang mungkin dipengaruhi oleh perubahan sosial-ekonomi akibat pandemi COVID-19")
