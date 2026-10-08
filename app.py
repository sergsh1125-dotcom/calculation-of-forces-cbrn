import math
import streamlit as st


# ============================================================
# НАЛАШТУВАННЯ СТОРІНКИ
# ============================================================

st.set_page_config(
    page_title="Розрахунок сил РХБ захисту",
    page_icon="☢️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# СТИЛІ
# ============================================================

st.markdown("""
<style>

    /* Основний фон */
    .stApp {
        background-color: #0e1117;
    }

    /* Заголовки */
    h1, h2, h3 {
        color: #ffffff;
    }

    /* Жовті заголовки блоків */
    .section-title {
        background-color: #ffcc00;
        color: #000000;
        padding: 10px 14px;
        border-radius: 6px;
        font-weight: 700;
        margin-top: 12px;
        margin-bottom: 15px;
    }

    /* Картка результату */
    .result-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .result-title {
        color: #ffcc00;
        font-size: 18px;
        font-weight: 700;
    }

    .result-number {
        color: #ffffff;
        font-size: 30px;
        font-weight: 700;
        margin-top: 8px;
    }

    .result-details {
        color: #c9d1d9;
        font-size: 14px;
        margin-top: 8px;
    }

    /* Кнопка */
    div.stButton > button {
        width: 100%;
        min-height: 48px;
        font-weight: 700;
    }

    /* Підписи */
    label {
        color: #ffffff !important;
    }

    /* Мобільна адаптація */
    @media (max-width: 768px) {

        .block-container {
            padding-left: 0.8rem;
            padding-right: 0.8rem;
            padding-top: 1rem;
        }

        h1 {
            font-size: 1.55rem;
        }

        h2 {
            font-size: 1.3rem;
        }

        h3 {
            font-size: 1.1rem;
        }

        .result-number {
            font-size: 26px;
        }

    }

</style>
""", unsafe_allow_html=True)


# ============================================================
# ЗАГОЛОВОК
# ============================================================

st.title("Розрахунок сил РХБ захисту")

st.caption(
    "Розрахунок необхідної кількості відділень для виконання завдань "
    "РХБ розвідки, санітарної та спеціальної обробки."
)


# ============================================================
# БЛОК 1. МОЖЛИВОСТІ ОДНОГО ВІДДІЛЕННЯ
# ============================================================

st.markdown(
    '<div class="section-title">1. МОЖЛИВОСТІ ОДНОГО ВІДДІЛЕННЯ</div>',
    unsafe_allow_html=True
)

st.info(
    "Оператор самостійно встановлює продуктивність одного відділення "
    "залежно від наявної спеціальної техніки та умов виконання завдання."
)


# ---------- РХ РОЗВІДКА ----------

st.subheader("РХ розвідка")

col1, col2 = st.columns(2)

with col1:
    rhr_route = st.number_input(
        "Розвідка маршруту, км/год",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="rhr_route"
    )

with col2:
    rhr_area = st.number_input(
        "Розвідка району, км/год",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="rhr_area"
    )


# ---------- САНІТАРНА ОБРОБКА ----------

st.subheader("Санітарна обробка людей")

san_people = st.number_input(
    "Санітарна обробка, осіб/год",
    min_value=0.0,
    value=50.0,
    step=5.0,
    key="san_people"
)


# ---------- СПЕЦІАЛЬНА ОБРОБКА ----------

st.subheader("Спеціальна обробка техніки")

col1, col2, col3 = st.columns(3)

with col1:
    special_light = st.number_input(
        "Легкові автомобілі, од./год",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="special_light"
    )

with col2:
    special_truck = st.number_input(
        "Вантажні автомобілі, од./год",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="special_truck"
    )

with col3:
    special_bus = st.number_input(
        "Автобуси, од./год",
        min_value=0.0,
        value=3.0,
        step=1.0,
        key="special_bus"
    )


# ============================================================
# БЛОК 2. ВХІДНІ ДАНІ
# ============================================================

st.markdown(
    '<div class="section-title">2. ВХІДНІ ДАНІ ДЛЯ РОЗРАХУНКУ</div>',
    unsafe_allow_html=True
)


# ============================================================
# РХ РОЗВІДКА
# ============================================================

st.subheader("РХ розвідка")

rhr_type = st.selectbox(
    "Вид РХ розвідки",
    [
        "Розвідка маршруту",
        "Розвідка району"
    ],
    key="rhr_type"
)

col1, col2 = st.columns(2)

with col1:

    rhr_volume = st.number_input(
        "Обсяг завдання, км",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="rhr_volume"
    )

with col2:

    rhr_time = st.number_input(
        "ЧАС НА ВИКОНАННЯ ЗАВДАННЯ, год",
        min_value=0.1,
        value=1.0,
        step=0.5,
        key="rhr_time"
    )


# ============================================================
# САНІТАРНА ОБРОБКА
# ============================================================

st.subheader("Санітарна обробка людей")

col1, col2 = st.columns(2)

with col1:

    san_volume = st.number_input(
        "Кількість людей, осіб",
        min_value=0,
        value=100,
        step=10,
        key="san_volume"
    )

with col2:

    san_time = st.number_input(
        "ЧАС НА ВИКОНАННЯ ЗАВДАННЯ, год",
        min_value=0.1,
        value=1.0,
        step=0.5,
        key="san_time"
    )


# ============================================================
# СПЕЦІАЛЬНА ОБРОБКА
# ============================================================

st.subheader("Спеціальна обробка техніки")

special_type = st.selectbox(
    "Вид спеціальної обробки",
    [
        "Дегазація",
        "Дезактивація",
        "Дезінфекція"
    ],
    key="special_type"
)

vehicle_type = st.selectbox(
    "Тип техніки",
    [
        "Легкові автомобілі",
        "Вантажні автомобілі",
        "Автобуси"
    ],
    key="vehicle_type"
)

col1, col2 = st.columns(2)

with col1:

    special_volume = st.number_input(
        "Кількість техніки, од.",
        min_value=0,
        value=10,
        step=1,
        key="special_volume"
    )

with col2:

    special_time = st.number_input(
        "ЧАС НА ВИКОНАННЯ ЗАВДАННЯ, год",
        min_value=0.1,
        value=1.0,
        step=0.5,
        key="special_time"
    )


# ============================================================
# КНОПКА РОЗРАХУНКУ
# ============================================================

st.markdown("---")

calculate = st.button(
    "РОЗРАХУВАТИ КІЛЬКІСТЬ СИЛ",
    type="primary",
    use_container_width=True
)


# ============================================================
# ФУНКЦІЯ РОЗРАХУНКУ
# ============================================================

def calculate_units(volume, productivity, time):
    """
    Розрахунок необхідної кількості відділень.

    volume       - обсяг завдання
    productivity - можливість одного відділення за годину
    time         - заданий час виконання
    """

    if volume <= 0:
        return 0

    if productivity <= 0:
        return None

    if time <= 0:
        return None

    return math.ceil(volume / (productivity * time))


# ============================================================
# БЛОК 3. РЕЗУЛЬТАТИ
# ============================================================

if calculate:

    st.markdown(
        '<div class="section-title">3. РЕЗУЛЬТАТИ РОЗРАХУНКУ</div>',
        unsafe_allow_html=True
    )

    results = []


    # --------------------------------------------------------
    # РХ РОЗВІДКА
    # --------------------------------------------------------

    if rhr_type == "Розвідка маршруту":

        productivity = rhr_route

    else:

        productivity = rhr_area


    rhr_result = calculate_units(
        rhr_volume,
        productivity,
        rhr_time
    )


    if rhr_result is None:

        st.error(
            "Для РХ розвідки необхідно вказати можливість "
            "одного відділення більше 0 км/год."
        )

    else:

        if rhr_type == "Розвідка маршруту":
            unit_name = "відділення РХР"
        else:
            unit_name = "відділення РХР"

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">РХ РОЗВІДКА</div>

                <div class="result-details">
                    Вид: {rhr_type}<br>
                    Обсяг: {rhr_volume:.1f} км<br>
                    Час виконання: {rhr_time:.1f} год<br>
                    Можливість 1 відділення: {productivity:.1f} км/год
                </div>

                <div class="result-number">
                    {rhr_result} {unit_name}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        results.append(rhr_result)


    # --------------------------------------------------------
    # САНІТАРНА ОБРОБКА
    # --------------------------------------------------------

    san_result = calculate_units(
        san_volume,
        san_people,
        san_time
    )


    if san_result is None:

        st.error(
            "Для санітарної обробки необхідно вказати "
            "можливість одного відділення більше 0 осіб/год."
        )

    else:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">
                    САНІТАРНА ОБРОБКА ЛЮДЕЙ
                </div>

                <div class="result-details">
                    Кількість людей: {san_volume} осіб<br>
                    Час виконання: {san_time:.1f} год<br>
                    Можливість 1 відділення: {san_people:.1f} осіб/год
                </div>

                <div class="result-number">
                    {san_result} відділення
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        results.append(san_result)


    # --------------------------------------------------------
    # СПЕЦІАЛЬНА ОБРОБКА
    # --------------------------------------------------------

    if vehicle_type == "Легкові автомобілі":

        productivity = special_light

    elif vehicle_type == "Вантажні автомобілі":

        productivity = special_truck

    else:

        productivity = special_bus


    special_result = calculate_units(
        special_volume,
        productivity,
        special_time
    )


    if special_result is None:

        st.error(
            "Для спеціальної обробки необхідно вказати "
            "можливість одного відділення більше 0 од./год."
        )

    else:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">
                    СПЕЦІАЛЬНА ОБРОБКА ТЕХНІКИ
                </div>

                <div class="result-details">
                    Вид обробки: {special_type}<br>
                    Тип техніки: {vehicle_type}<br>
                    Кількість: {special_volume} од.<br>
                    Час виконання: {special_time:.1f} год<br>
                    Можливість 1 відділення: {productivity:.1f} од./год
                </div>

                <div class="result-number">
                    {special_result} відділення
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        results.append(special_result)


    # ========================================================
    # ПІДСУМКОВА ТАБЛИЦЯ
    # ========================================================

    st.subheader("Підсумок")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:

        st.metric(
            "Відділення РХР",
            rhr_result if rhr_result is not None else "-"
        )

    with summary_col2:

        st.metric(
            "Санітарна обробка",
            san_result if san_result is not None else "-"
        )

    with summary_col3:

        st.metric(
            "Спеціальна обробка",
            special_result if special_result is not None else "-"
        )


    # Загальна кількість
    if results:

        total = sum(results)

        st.markdown("---")

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">
                    ЗАГАЛЬНА КІЛЬКІСТЬ ВІДДІЛЕНЬ
                </div>

                <div class="result-number">
                    {total}
                </div>

                <div class="result-details">
                    РХР: {rhr_result if rhr_result is not None else 0}<br>
                    Санітарна обробка: {san_result if san_result is not None else 0}<br>
                    Спеціальна обробка: {special_result if special_result is not None else 0}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
