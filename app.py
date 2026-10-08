import math
import streamlit as st


# ============================================================
# НАСТРОЙКИ СТРАНИЦЫ
# ============================================================

st.set_page_config(
    page_title="Розрахунок сил РХБ захисту",
    page_icon="☢️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ======================================================
       ОСНОВНОЙ ФОН
       ====================================================== */

    .stApp {
        background-color: #0e1117;
    }


    /* ======================================================
       СЛУЖЕБНЫЕ ЭЛЕМЕНТЫ STREAMLIT
       ====================================================== */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ======================================================
       НАЗВАНИЕ СКРИПТА И ЗАГОЛОВКИ — ЖЁЛТЫЕ
       ====================================================== */

    h1 {
        color: #ffcc00 !important;
        font-weight: 800 !important;
        text-align: center;
    }

    h2 {
        color: #ffcc00 !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #ffcc00 !important;
        font-weight: 800 !important;
    }


    /* ======================================================
       ОБЫЧНЫЙ ТЕКСТ — БЕЛЫЙ
       ====================================================== */

    p {
        color: #ffffff !important;
    }

    label {
        color: #ffffff !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }

    [data-testid="stWidgetLabel"] {
        color: #ffffff !important;
        opacity: 1 !important;
    }

    [data-testid="stWidgetLabel"] * {
        color: #ffffff !important;
        opacity: 1 !important;
    }


    /* ======================================================
       ПОЛЯ ВВОДА — СЕРЫЙ ФОН
       ЦИФРЫ — ТЁМНЫЕ
       ====================================================== */

    [data-testid="stNumberInput"] input {
        background-color: #d9d9d9 !important;
        color: #111111 !important;
        -webkit-text-fill-color: #111111 !important;
        opacity: 1 !important;

        border: 1px solid #777777 !important;
        border-radius: 6px !important;
    }

    [data-testid="stNumberInput"] input:focus {
        background-color: #eeeeee !important;
        color: #111111 !important;
        -webkit-text-fill-color: #111111 !important;
    }


    /* ======================================================
   SELECTBOX — БЕЛОЕ ОКНО, ТЁМНЫЙ ТЕКСТ
   ====================================================== */

[data-testid="stSelectbox"] [data-baseweb="select"] {
    background-color: #ffffff !important;
    border-radius: 6px !important;
}

[data-testid="stSelectbox"] [data-baseweb="select"] * {
    color: #111111 !important;
}

[data-testid="stSelectbox"] input {
    color: #111111 !important;
    -webkit-text-fill-color: #111111 !important;
}


    /* ======================================================
       ВЫПАДАЮЩЕЕ МЕНЮ
       ====================================================== */

    [data-baseweb="popover"] {
        background-color: #d9d9d9 !important;
    }

    [data-baseweb="menu"] {
        background-color: #d9d9d9 !important;
    }

    [data-baseweb="menu"] * {
        color: #111111 !important;
    }


    /* ======================================================
       RADIO
       ====================================================== */

    [data-testid="stRadio"] label {
        color: #ffffff !important;
    }

    [data-testid="stRadio"] label p {
        color: #ffffff !important;
    }

    [data-testid="stRadio"] label span {
        color: #ffffff !important;
    }


    /* ======================================================
       ПОДПИСИ ПОЛЕЙ
       ====================================================== */

    [data-testid="stNumberInput"] label {
        color: #ffffff !important;
    }

    [data-testid="stSelectbox"] label {
        color: #ffffff !important;
    }


    /* ======================================================
       РЕЗУЛЬТАТЫ
       ====================================================== */

    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
    }

    [data-testid="stMetricLabel"] * {
        color: #ffffff !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffcc00 !important;
    }

    [data-testid="stMetricValue"] * {
        color: #ffcc00 !important;
    }


    /* ======================================================
       ОШИБКИ
       ====================================================== */

    [data-testid="stAlert"] {
        color: #ffffff !important;
    }

    [data-testid="stAlert"] * {
        color: #ffffff !important;
    }


    /* ======================================================
       МОБИЛЬНАЯ ВЕРСИЯ
       ====================================================== */

    @media (max-width: 768px) {

        h1 {
            color: #ffcc00 !important;
            font-size: 27px !important;
        }

        h2 {
            color: #ffcc00 !important;
            font-size: 22px !important;
        }

        h3 {
            color: #ffcc00 !important;
            font-size: 19px !important;
        }

        p {
            color: #ffffff !important;
        }

        label {
            color: #ffffff !important;
        }

        /* Цифры в полях */
        [data-testid="stNumberInput"] input {
            background-color: #d9d9d9 !important;
            color: #111111 !important;
            -webkit-text-fill-color: #111111 !important;
            font-size: 17px !important;
            font-weight: 600 !important;
        }

        /* Выбор */
        [data-testid="stSelectbox"] [data-baseweb="select"] {
            background-color: #d9d9d9 !important;
        }

        [data-testid="stSelectbox"] [data-baseweb="select"] * {
            color: #111111 !important;
        }

        /* Radio */
        [data-testid="stRadio"] label {
            color: #ffffff !important;
        }

        /* Результаты */
        [data-testid="stMetricLabel"] {
            color: #ffffff !important;
        }

        [data-testid="stMetricValue"] {
            color: #ffcc00 !important;
            font-size: 28px !important;
        }

    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# ФУНКЦИЯ РАСЧЁТА
# ============================================================

def calculate_units(volume, productivity, time):
    """
    Расчёт необходимого количества отделений.

    N = ceil(volume / (productivity * time))
    """

    if volume <= 0:
        return 0

    if productivity <= 0:
        return None

    if time <= 0:
        return None

    return math.ceil(volume / (productivity * time))


# ============================================================
# ЗАГОЛОВОК
# ============================================================

st.title("РОЗРАХУНОК СИЛ РХБ ЗАХИСТУ")

st.markdown("---")


# ============================================================
# 1. МОЖЛИВОСТІ ОДНОГО ВІДДІЛЕННЯ
# ============================================================

st.header("1. МОЖЛИВОСТІ ОДНОГО ВІДДІЛЕННЯ (заповнюється оператором)")


# ------------------------------------------------------------
# РХ РОЗВІДКА
# ------------------------------------------------------------

st.subheader("Відділення РХ розвідки (1 СМРХР)")

col1, col2 = st.columns(2)

with col1:
    recon_route = st.number_input(
        "Розвідка маршруту, км/год",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="recon_route",
    )

with col2:
    recon_area = st.number_input(
        "Розвідка району, км.кв./год",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="recon_area",
    )


# ------------------------------------------------------------
# САНІТАРНА ОБРОБКА
# ------------------------------------------------------------

st.subheader("Відділення санітарної обробки (1 комплект сан. обробки)")

sanitary_productivity = st.number_input(
    "Санітарна обробка, осіб/год",
    min_value=0.0,
    value=100.0,
    step=10.0,
    key="sanitary_productivity",
)


# ------------------------------------------------------------
# СПЕЦІАЛЬНА ОБРОБКА
# ------------------------------------------------------------

st.subheader("Відділення спеціальної обробки (1 СМРХЗ)")

col1, col2 = st.columns(2)

with col1:
    special_degas_productivity = st.number_input(
        "Дегазація (дезінфекція), од./год",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="special_degas_productivity",
    )

with col2:
    special_deactivation_productivity = st.number_input(
        "Дезактивація, од./год",
        min_value=0.0,
        value=3.0,
        step=1.0,
        key="special_deactivation_productivity",
    )


st.markdown("---")


# ============================================================
# 2. ВХІДНІ ДАНІ ДЛЯ РОЗРАХУНКУ
# ============================================================

st.header("2. ВХІДНІ ДАНІ ДЛЯ РОЗРАХУНКУ")


# ============================================================
# РХ РОЗВІДКА
# ============================================================

st.subheader("РХ розвідка")

recon_type = st.selectbox(
    "Вид РХ розвідки",
    [
        "Розвідка маршруту",
        "Розвідка району",
    ],
    key="recon_type",
)

recon_volume_unit = (
    "км"
    if recon_type == "Розвідка маршруту"
    else "км.кв."
)

recon_volume = st.number_input(
    f"Обсяг завдання, {recon_volume_unit}",
    min_value=0.0,
    value=10.0,
    step=1.0,
    key="recon_volume",
)

recon_time = st.number_input(
    "ЧАС НА ВИКОНАННЯ ЗАВДАННЯ, год",
    min_value=0.1,
    value=1.0,
    step=0.5,
    key="recon_time",
)


# ============================================================
# САНІТАРНА ОБРОБКА
# ============================================================

st.subheader("Санітарна обробка")

sanitary_people = st.number_input(
    "Кількість людей, осіб",
    min_value=0,
    value=100,
    step=10,
    key="sanitary_people",
)

sanitary_time = st.number_input(
    "ЧАС НА ВИКОНАННЯ ЗАВДАННЯ, год",
    min_value=0.1,
    value=1.0,
    step=0.5,
    key="sanitary_time",
)


# ============================================================
# СПЕЦІАЛЬНА ОБРОБКА
# ============================================================

st.subheader("Спеціальна обробка")

special_type = st.radio(
    "Вид спеціальної обробки",
    [
        "Дегазація",
        "Дезактивація",
        "Дезінфекція",
    ],
    horizontal=True,
    key="special_type",
)

special_volume = st.number_input(
    "Кількість техніки, од.",
    min_value=0,
    value=20,
    step=1,
    key="special_volume",
)

special_time = st.number_input(
    "ЧАС НА ВИКОНАННЯ ЗАВДАННЯ, год",
    min_value=0.1,
    value=1.0,
    step=0.5,
    key="special_time",
)


# ============================================================
# ВИБОР ПРОДУКТИВНОСТІ СПЕЦІАЛЬНОЇ ОБРОБКИ
# ============================================================

if special_type == "Дезактивація":
    selected_special_productivity = special_deactivation_productivity
else:
    selected_special_productivity = special_degas_productivity


# ============================================================
# РОЗРАХУНОК
# ============================================================

# РХ розвідка
if recon_type == "Розвідка маршруту":
    recon_productivity = recon_route
    recon_volume_unit = "км"
    recon_productivity_unit = "км/год"
else:
    recon_productivity = recon_area
    recon_volume_unit = "км.кв."
    recon_productivity_unit = "км.кв./год"


recon_units = calculate_units(
    recon_volume,
    recon_productivity,
    recon_time,
)


# Санітарна обробка
sanitary_units = calculate_units(
    sanitary_people,
    sanitary_productivity,
    sanitary_time,
)


# Спеціальна обробка
special_units = calculate_units(
    special_volume,
    selected_special_productivity,
    special_time,
)


# ============================================================
# 3. РЕЗУЛЬТАТИ РОЗРАХУНКУ
# ============================================================

st.markdown("---")

st.header("3. РЕЗУЛЬТАТИ РОЗРАХУНКУ")


# ============================================================
# РХ РОЗВІДКА
# ============================================================

st.subheader("РХ розвідка")

if recon_units is None:

    st.error(
        "Неможливо виконати розрахунок: "
        "можливість одного відділення повинна бути більше 0."
    )

else:

    st.write(
        f"Вид розвідки: {recon_type}"
    )

    st.write(
        f"Обсяг завдання: "
        f"{recon_volume:.1f} {recon_volume_unit}"
    )

    st.write(
        f"Час виконання: {recon_time:.1f} год"
    )

    st.write(
        f"Можливість одного відділення: "
        f"{recon_productivity:.1f} {recon_productivity_unit}"
    )

    st.metric(
        "Потрібно відділень РХ розвідки",
        recon_units,
    )


# ============================================================
# САНІТАРНА ОБРОБКА
# ============================================================

st.subheader("Санітарна обробка")

if sanitary_units is None:

    st.error(
        "Неможливо виконати розрахунок: "
        "можливість одного відділення повинна бути більше 0."
    )

else:

    st.write(
        f"Кількість людей: {sanitary_people} осіб"
    )

    st.write(
        f"Час виконання: {sanitary_time:.1f} год"
    )

    st.write(
        f"Можливість одного відділення: "
        f"{sanitary_productivity:.1f} осіб/год"
    )

    st.metric(
        "Потрібно відділень санітарної обробки",
        sanitary_units,
    )


# ============================================================
# СПЕЦІАЛЬНА ОБРОБКА
# ============================================================

st.subheader("Спеціальна обробка")

if special_units is None:

    st.error(
        "Неможливо виконати розрахунок: "
        "можливість одного відділення повинна бути більше 0."
    )

else:

    st.write(
        f"Вид спеціальної обробки: {special_type}"
    )

    st.write(
        f"Кількість техніки: {special_volume} од."
    )

    st.write(
        f"Час виконання: {special_time:.1f} год"
    )

    st.write(
        f"Можливість одного відділення: "
        f"{selected_special_productivity:.1f} од./год"
    )

    st.metric(
        "Потрібно відділень спеціальної обробки",
        special_units,
    )
