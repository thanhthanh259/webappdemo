import streamlit as st
import random
import time

# --- CẤU HÌNH TRANG ---
st.set_page_config(
    page_title="Kho Tool Bán Hàng Online",
    page_icon="🔥",
    layout="centered"
)

# --- CSS TÙY CHỈNH (GIAO DIỆN SHOPEE) ---
st.markdown("""
    <style>
    .main {background-color: #f8f9fa;}
    .stButton>button {
        background-color: #ee4d2d;
        color: white;
        font-weight: bold;
        border-radius: 5px;
        width: 100%;
        height: 50px;
    }
    .stButton>button:hover {background-color: #d73211; border-color: #d73211; color: white;}
    .shopee-box {
        padding: 20px;
        border: 2px dashed #ee4d2d;
        border-radius: 10px;
        background-color: #fff5f5;
        text-align: center;
        margin-bottom: 20px;
    }
    h1, h2, h3 {color: #ee4d2d;}
    </style>
""", unsafe_allow_html=True)

# --- SIDEBAR (MENU BÊN TRÁI) ---
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/f/fe/Shopee.svg/1200px-Shopee.svg.png", width=150)
    st.title("MENU CÔNG CỤ")

    choice = st.radio("Chọn chức năng:", ["🏠 Trang Chủ", "💰 Tính Giá Bán", "🎡 Vòng Quay Random"])

    st.markdown("---")
    st.info("💡 Mẹo: Đây là bản Web dùng thử. Để dùng ổn định, lưu dữ liệu và bảo mật hơn, hãy mua bản Desktop.")
    st.link_button("🛒 MUA BẢN PRO TRÊN SHOPEE (29K)",
                   "https://shopee.vn/link-shop-cua-ban")  # THAY LINK SHOPEE CỦA BẠN VÀO ĐÂY

# =========================================================
# 🏠 TRANG CHỦ
# =========================================================
if choice == "🏠 Trang Chủ":
    st.title("🔥 GIẢI PHÁP BÁN HÀNG TỰ ĐỘNG")
    st.write("Chào mừng bạn đến với kho công cụ hỗ trợ Nhà bán hàng Shopee/TikTok.")

    st.markdown("""
    <div class="shopee-box">
        <h3>🚀 TOP SẢN PHẨM BÁN CHẠY</h3>
        <p>Sở hữu bộ công cụ vĩnh viễn chỉ với giá cốc trà đá!</p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        st.image("https://img.icons8.com/color/480/calculator--v1.png", width=100)
        st.subheader("Tool Tính Giá Lãi/Lỗ")
        st.write("✅ Cập nhật phí sàn tự động")
        st.write("✅ Cảnh báo cắt lỗ")
        st.write("✅ Thay thế Excel")

    with col2:
        st.image("https://img.icons8.com/color/480/roulette.png", width=100)
        st.subheader("Tool Vòng Quay Livestream")
        st.write("✅ Quay số công bằng")
        st.write("✅ Hiển thị đẹp mắt")
        st.write("✅ Tăng tương tác Livestream")

# =========================================================
# 💰 TOOL TÍNH GIÁ BÁN
# =========================================================
elif choice == "💰 Tính Giá Bán":
    st.title("💰 TÍNH GIÁ BÁN KHÔNG LỖ")
    st.caption("Phiên bản Web Lite (Dùng thử)")

    with st.form("calc_form"):
        gia_nhap = st.number_input("Giá nhập hàng (VNĐ)", min_value=0, value=100000, step=1000)
        lai_mong_muon = st.number_input("Lợi nhuận mong muốn (VNĐ)", min_value=0, value=50000, step=1000)

        col_phi1, col_phi2 = st.columns(2)
        with col_phi1:
            phi_san = st.number_input("Phí sàn cố định (%)", value=12.0)
        with col_phi2:
            phi_qc = st.number_input("Chi phí Quảng cáo/Gói (%)", value=5.0)

        submit = st.form_submit_button("TÍNH TOÁN NGAY")

    if submit:
        tong_phi_phantram = phi_san + phi_qc
        # Công thức: Giá Bán = (Giá Nhập + Lãi) / (1 - %Phí)
        if tong_phi_phantram >= 100:
            st.error("Tổng phí quá 100%, không thể tính toán!")
        else:
            gia_ban = (gia_nhap + lai_mong_muon) / (1 - (tong_phi_phantram / 100))
            phi_phai_tra = gia_ban * (tong_phi_phantram / 100)

            st.markdown("---")
            st.success(f"### 💵 GIÁ CẦN BÁN: {gia_ban:,.0f} VNĐ")

            c1, c2, c3 = st.columns(3)
            c1.metric("Giá vốn", f"{gia_nhap:,.0f}")
            c2.metric("Phí sàn phải trả", f"{phi_phai_tra:,.0f}", f"-{tong_phi_phantram}%")
            c3.metric("Lợi nhuận thực", f"{lai_mong_muon:,.0f}")

# =========================================================
# 🎡 TOOL VÒNG QUAY RANDOM
# =========================================================
elif choice == "🎡 Vòng Quay Random":
    st.title("🎡 VÒNG QUAY MAY MẮN")

    tab1, tab2 = st.tabs(["Quay Tên", "Quay Số"])

    with tab1:
        st.write("Nhập danh sách tên (Mỗi tên 1 dòng):")
        text_input = st.text_area("Danh sách", "Nguyễn Văn A\nTrần Thị B\nLê Văn C\nQuà Bí Mật")

        if st.button("QUAY NGAY (SPIN)"):
            lines = [x.strip() for x in text_input.split('\n') if x.strip()]
            if not lines:
                st.warning("Danh sách trống!")
            else:
                with st.spinner("Đang quay..."):
                    time.sleep(2)  # Giả vờ quay

                winner = random.choice(lines)
                st.balloons()  # Hiệu ứng bóng bay
                st.markdown(f"""
                <div style="background-color:#d4edda; padding:20px; border-radius:10px; text-align:center;">
                    <h2 style="color:#155724; margin:0;">🎉 CHÚC MỪNG: {winner} 🎉</h2>
                </div>
                """, unsafe_allow_html=True)

    with tab2:
        c_min, c_max = st.columns(2)
        with c_min:
            min_val = st.number_input("Từ số", value=1)
        with c_max:
            max_val = st.number_input("Đến số", value=100)

        if st.button("QUAY SỐ NGẪU NHIÊN"):
            if min_val > max_val:
                st.error("Số nhỏ phải nhỏ hơn số lớn!")
            else:
                with st.spinner("Đang chọn số..."):
                    time.sleep(1)
                res = random.randint(min_val, max_val)
                st.title(f"SỐ MAY MẮN: {res}")
                st.balloons()