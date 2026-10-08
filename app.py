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

    /* Основной фон */
    .stApp {
        background-color: #0e1117;
    }

    /* Убираем верхнюю панель Streamlit */
    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    /* Основной заголовок */
    h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        text-align: center;
    }

    /* Заголовки разделов */
    h2 {
        color: #ffcc00 !important;
        font-weight: 800 !important;
    }

    h3 {
        color: #ffffff !important;
        font-weight: 700 !important;
    }

    /* Все подписи элементов */
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

    /* Текст */
    p, span, div {
        opacity: 1;
    }

    /* Поля ввода */
    input {
        color: #ffffff !important;
    }

    /* Selectbox */
    [data-baseweb="select"] {
        color: #ffffff !important;
    }

    [data-baseweb="select"] * {
        color: #ffffff !important;
    }

    /* Радиокнопки */
    [data-testid="stRadio"] label {
        color: #ffffff !important;
    }

    [data-testid="stRadio"] label * {
        color: #ffffff !important;
    }

    /* Разделитель */
    hr {
        border-color: #333333;
    }

    /* Карточка результата */
    .result-box {
        background-color: #161b22;
        border: 1px solid #333333;
        border-radius: 10px;
        padding: 18px;
        margin-top: 12px;
        margin-bottom: 12px;
    }

    .result-title {
        color: #ffcc00;
        font-size: 20px;
        font-weight: 800;
        margin-bottom: 10px;
    }

    .result-text {
        color: #ffffff;
        font-size: 16px;
        line-height: 1.6;
    }

    /* Большое число результата */
    .result-number {
        color: #ffcc00;
        font-size: 28px;
        font-weight: 900;
        margin-top: 10px;
    }

    /* Мобильная версия */
    @media (max-width: 768px) {

        h1 {
            font-size: 28px !important;
        }

        h2 {
            font-size: 22px !important;
        }

        h3 {
            font-size: 19px !important;
        }

        label {
            font-size: 16px !important;
        }

        .result-title {
            font-size: 18px;
        }

        .result-text {
            font-size: 15px;
        }

        .result-number {
            font-size: 24px;
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
# 1. ВОЗМОЖНОСТИ ОДНОГО ОТДЕЛЕНИЯ
# ============================================================

st.header("1. МОЖЛИВОСТІ ОДНОГО ВІДДІЛЕННЯ")


# ------------------------------------------------------------
# РХ РОЗВІДКА
# ------------------------------------------------------------

st.subheader("РХ розвідка")

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
        "Розвідка району, км/год",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="recon_area",
    )


# ------------------------------------------------------------
# САНИТАРНАЯ ОБРАБОТКА
# ------------------------------------------------------------

st.subheader("Санітарна обробка")

sanitary_productivity = st.number_input(
    "Санітарна обробка, осіб/год",
    min_value=0.0,
    value=100.0,
    step=10.0,
    key="sanitary_productivity",
)


# ------------------------------------------------------------
# СПЕЦИАЛЬНАЯ ОБРАБОТКА
# ------------------------------------------------------------

st.subheader("Спеціальна обробка")

st.caption(
    "Вказується фактична можливість одного відділення. "
    "Категорії транспортних засобів не поділяються."
)

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
# 2. ВХОДНЫЕ ДАННЫЕ
# ============================================================

st.header("2. ВХІДНІ ДАНІ ДЛЯ РОЗРАХУНКУ")


# ============================================================
# РХ РОЗВЕДКА
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

recon_volume = st.number_input(
    "Обсяг завдання, км",
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
# САНИТАРНАЯ ОБРАБОТКА
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
# СПЕЦИАЛЬНАЯ ОБРАБОТКА
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
# ОПРЕДЕЛЕНИЕ ПРОИЗВОДИТЕЛЬНОСТИ
# ============================================================

if special_type == "Дезактивація":
    selected_special_productivity = special_deactivation_productivity
else:
    # Дегазація и дезінфекція используют одну возможность
    selected_special_productivity = special_degas_productivity


# ============================================================
# РАСЧЁТ
# ============================================================

# РХ разведка
if recon_type == "Розвідка маршруту":
    recon_productivity = recon_route
else:
    recon_productivity = recon_area

recon_units = calculate_units(
    recon_volume,
    recon_productivity,
    recon_time,
)


# Санитарная обработка
sanitary_units = calculate_units(
    sanitary_people,
    sanitary_productivity,
    sanitary_time,
)


# Специальная обработка
special_units = calculate_units(
    special_volume,
    selected_special_productivity,
    special_time,
)


# ============================================================
# 3. РЕЗУЛЬТАТИ
# ============================================================

st.markdown("---")

st.header("3. РЕЗУЛЬТАТИ РОЗРАХУНКУ")


# ============================================================
# РХ РАЗВЕДКА — РЕЗУЛЬТАТ
# ============================================================

st.subheader("РХ розвідка")

if recon_units is None:

    st.error(
        "Неможливо виконати розрахунок: "
        "можливість одного відділення повинна бути більше 0."
    )

else:

    st.write(
        f"**Вид розвідки:** {recon_type}"
    )

    st.write(
        f"**Обсяг завдання:** {recon_volume:.1f} км"
    )

    st.write(
        f"**Час виконання:** {recon_time:.1f} год"
    )

    st.write(
        f"**Можливість одного відділення:** "
        f"{recon_productivity:.1f} км/год"
    )

    st.metric(
        "Потрібно відділень РХ розвідки",
        recon_units,
    )


# ============================================================
# САНИТАРНАЯ ОБРАБОТКА — РЕЗУЛЬТАТ
# ============================================================

st.subheader("Санітарна обробка")

if sanitary_units is None:

    st.error(
        "Неможливо виконати розрахунок: "
        "можливість одного відділення повинна бути більше 0."
    )

else:

    st.write(
        f"**Кількість людей:** {sanitary_people} осіб"
    )

    st.write(
        f"**Час виконання:** {sanitary_time:.1f} год"
    )

    st.write(
        f"**Можливість одного відділення:** "
        f"{sanitary_productivity:.1f} осіб/год"
    )

    st.metric(
        "Потрібно відділень санітарної обробки",
        sanitary_units,
    )


# ============================================================
# СПЕЦИАЛЬНАЯ ОБРАБОТКА — РЕЗУЛЬТАТ
# ============================================================

st.subheader("Спеціальна обробка")

if special_units is None:

    st.error(
        "Неможливо виконати розрахунок: "
        "можливість одного відділення повинна бути більше 0."
    )

else:

    st.write(
        f"**Вид спеціальної обробки:** {special_type}"
    )

    st.write(
        f"**Кількість техніки:** {special_volume} од."
    )

    st.write(
        f"**Час виконання:** {special_time:.1f} год"
    )

    st.write(
        f"**Можливість одного відділення:** "
        f"{selected_special_productivity:.1f} од./год"
    )

    st.metric(
        "Потрібно відділень спеціальної обробки",
        special_units,
    )


# ============================================================
# 4. ПІДСУМОК
# ============================================================

st.markdown("---")

st.header("4. ПІДСУМОК")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Відділення РХ розвідки",
        recon_units if recon_units is not None else "—",
    )

with col2:
    st.metric(
        "Відділення санітарної обробки",
        sanitary_units if sanitary_units is not None else "—",
    )

with col3:
    st.metric(
        "Відділення спеціальної обробки",
        special_units if special_units is not None else "—",
    )


# ============================================================
# ФОРМУЛА
# ============================================================

st.markdown("---")

st.subheader("Принцип розрахунку")

st.write(
    "N = ceil(Обсяг завдання / "
    "(Можливість одного відділення × Час виконання))"
)

st.caption(
    "Результат округлюється у більшу сторону. "
    "Такий підхід забезпечує консервативне планування сил."
)
