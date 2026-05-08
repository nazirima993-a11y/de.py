import streamlit as st
import datetime
import urllib.parse

# --- 1. SETUP SISTEM ---
if 'halaman' not in st.session_state:
    st.session_state.halaman = "Page 1"
def navigasi(nama_page):
    st.session_state.halaman = nama_page
    st.rerun()

# ==========================================
# PAGE 1: MENU UTAMA
# ==========================================
if st.session_state.halaman == "Page 1":
    st.title("PAGE 1")
    st.subheader("📦 PELANGGAN")
    if st.button("GO TO PAGE 2", use_container_width=True):
        navigasi("Page 2")
    
    st.write("---")
    st.subheader("🛵 monitor job")
    if st.button("GO TO PAGE 7", use_container_width=True):
        navigasi("Page 7")

# ==========================================
# PAGE 2: BORANG TEMPAHAN (IKUT NOTA SEBIJI)
# ==========================================
elif st.session_state.halaman == "Page 2":
    st.title("PAGE 2")
    nama = st.text_input("NAMA :")
    kategori = st.selectbox("kategori", ["motor", "kereta", "4x4"])
    tarikh = st.text_input("TARIKH / MASA")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("*Pick Up*")
        addr1 = st.text_input("Alamat", key="p1")
        tel1 = st.text_input("no tel", key="p2")
        kaw1 = st.text_input("kawasan", key="p3")
    with col2:
        st.write("*DROP*")
        addr2 = st.text_input("Alamat ", key="d1")
        tel2 = st.text_input("no tel ", key="d2")
        kaw2 = st.text_input("kawasan ", key="d3")

    st.write("---")
    # GOOGLE MAP PINTAR
    if addr1 and addr2:
        asal = urllib.parse.quote(f"{addr1} {kaw1}")
        tuju = urllib.parse.quote(f"{addr2} {kaw2}")
        link = f"https://www.google.com/maps/dir/?api=1&origin={asal}&destination={tuju}"
        st.link_button("🌐 LIHAT JARAK DI GOOGLE MAPS", link)

    jarak = st.number_input("jarak = (google map)", min_value=0.0)
    
    # FORMULA KADAR NOTA KAK EMI
    harga = 0.0
    if kategori == "motor": harga = 5.0 + (1.0 * jarak)
    elif kategori == "kereta":
        base = 7.5 if jarak <= 10 else 5.0
        harga = base + (1.5 * jarak)
    elif kategori == "4x4":
        base = 15.0 if jarak <= 10 else 10.0
        harga = base + (2.3 * jarak)

    st.subheader(f"HARGA = RM {harga:.2f}")
    st.write("* pembayaran ketika sampai item")
    st.write("* saya bersetuju dengan harga di atas")
    
    id_auto = f"{kategori.upper()}-{datetime.datetime.now().strftime('%M%S')}"
    st.write(f"ID Job : {id_auto}")

    if st.button("SUBMIT"):
        st.session_state.job = {'id': id_auto, 'nama': nama, 'harga': harga, 'kategori': kategori}
        st.success("simpan Page 3")
    if st.button("⬅️ Back to Page 1"):
        navigasi("Page 1")



# ==========================================
# PAGE 7: DASHBOARD RIDER
# ==========================================
elif st.session_state.halaman == "Page 7":
    st.title("PAGE 7: DASHBOARD RIDER")
    st.subheader(f"STATUS JOB: {st.session_state.job['id']}")
    status = st.radio("KEMASKINI:", ["TOL", "TIBA", "AMBIL", "SAMPAI", "DROP"])
    if status == "DROP":
        if st.button("SELESAI & SIMPAN"):
            navigasi("Page 1")

