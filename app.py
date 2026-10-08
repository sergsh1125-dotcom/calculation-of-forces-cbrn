```python
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

    /* ========================================================
       ОСНОВНИЙ ІНТЕРФЕЙС
       ======================================================== */

    .stApp {
        background-color: #0e1117;
    }

    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 2rem;
    }


    /* ========================================================
       ПРИБРАТИ СЛУЖБОВУ ВЕРХНЮ ПАНЕЛЬ STREAMLIT
       ПК + СМАРТФОН
       ======================================================== */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ========================================================
       ЗАГОЛОВКИ
       ======================================================== */

    h1 {
        color: #ffffff !important;
        font-weight: 800 !important;
        letter-spacing: 0.2px;
        line-height: 1.2 !important;
        text-rendering: geometricPrecision;
        -webkit-font-smoothing: antialiased;
    }

    h2,
    h3 {
        color: #ffffff !important;
        font-weight: 800 !important;
        line-height: 1.25 !important;
        text-rendering: geometricPrecision;
        -webkit-font-smoothing: antialiased;
    }


    /* ========================================================
       НАЗВИ РОЗДІЛІВ
       ======================================================== */

    .section-title {
        background-color: #ffcc00;
        color: #000000 !important;
        padding: 12px 15px;
        border-radius: 6px;
        font-weight: 800;
        font-size: 18px;
        line-height: 1.3;
        margin-top: 16px;
        margin-bottom: 18px;
        text-rendering: geometricPrecision;
        -webkit-font-smoothing: antialiased;
    }


    /* ========================================================
       ПІДПИСИ НАД ПОЛЯМИ STREAMLIT
       БІЛІ — У Т.Ч. НА СМАРТФОНІ
       ======================================================== */

    label {
        color: #ffffff !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }

    label p {
        color: #ffffff !important;
        font-weight: 600 !important;
        opacity: 1 !important;
    }

    [data-testid="stWidgetLabel"] {
        color: #ffffff !important;
    }

    [data-testid="stWidgetLabel"] * {
        color: #ffffff !important;
        opacity: 1 !important;
    }

    [data-testid="stMarkdownContainer"] p {
        color: #ffffff;
    }


    /* ========================================================
       ПОЛЯ ВВЕДЕННЯ
       ======================================================== */

    input,
    textarea,
    select {
        font-size: 16px !important;
    }


    /* ========================================================
       INFO / ПОВІДОМЛЕННЯ
       ======================================================== */

    [data-testid="stAlert"] {
        color: #ffffff !important;
    }

    [data-testid="stAlert"] p {
        color: #ffffff !important;
    }


    /* ========================================================
       КНОПКА
       ======================================================== */

    div.stButton > button {
        width: 100%;
        min-height: 50px;
        font-weight: 800;
        font-size: 16px;
    }


    /* ========================================================
       РЕЗУЛЬТАТИ
       ======================================================== */

    .result-card {
        background-color: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 16px;
        margin-bottom: 12px;
    }

    .result-title {
        color: #ffcc00;
        font-size: 19px;
        font-weight: 800;
        line-height: 1.3;
    }

    .result-number {
        color: #ffffff;
        font-size: 30px;
        font-weight: 800;
        margin-top: 10px;
        line-height: 1.2;
    }

    .result-details {
        color: #ffffff;
        font-size: 15px;
        line-height: 1.6;
        margin-top: 9px;
    }


    /* ========================================================
       METRIC
       ======================================================== */

    [data-testid="stMetricLabel"] {
        color: #ffffff !important;
    }

    [data-testid="stMetricValue"] {
        color: #ffffff !important;
    }


    /* ========================================================
       МОБІЛЬНА ВЕРСІЯ
       ======================================================== */

    @media (max-width: 768px) {

        .block-container {
            padding-left: 0.75rem;
            padding-right: 0.75rem;
            padding-top: 1rem;
        }

        h1 {
            font-size: 1.65rem !important;
            font-weight: 800 !important;
            line-height: 1.2 !important;
        }

        h2 {
            font-size: 1.35rem !important;
            font-weight: 800 !important;
        }

        h3 {
            font-size: 1.15rem !important;
            font-weight: 800 !important;
        }

        .section-title {
            font-size: 17px;
            padding: 12px 13px;
            line-height: 1.35;
            margin-top: 14px;
            margin-bottom: 16px;
        }

        .result-title {
            font-size: 18px;
        }

        .result-number {
            font-size: 27px;
        }

        .result-details {
            font-size: 15px;
            line-height: 1.6;
        }

        label,
        label p,
        [data-testid="stWidgetLabel"],
        [data-testid="stWidgetLabel"] * {
            color: #ffffff !important;
            opacity: 1 !important;
            font-weight: 600 !important;
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
    "РХ розвідки, санітарної та спеціальної обробки."
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


# ============================================================
# РХ РОЗВІДКА
# ============================================================

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


# ============================================================
# САНІТАРНА ОБРОБКА
# ============================================================

st.subheader("Санітарна обробка людей")

san_people = st.number_input(
    "Санітарна обробка, осіб/год",
    min_value=0.0,
    value=50.0,
    step=5.0,
    key="san_people"
)


# ============================================================
# СПЕЦІАЛЬНА ОБРОБКА
# ============================================================

st.subheader("Спеціальна обробка техніки")

col1, col2, col3 = st.columns(3)

with col1:
    special_total = st.number_input(
        "Всього техніки, од./год",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="special_total"
    )

with col2:
    special_light = st.number_input(
        "У тому числі — легкові автомобілі, од./год",
        min_value=0.0,
        value=10.0,
        step=1.0,
        key="special_light"
    )

with col3:
    special_heavy = st.number_input(
        "У тому числі — вантажні автомобілі (автобуси), од./год",
        min_value=0.0,
        value=5.0,
        step=1.0,
        key="special_heavy"
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
# СПЕЦІАЛЬНА ОБРОБКА ТЕХНІКИ
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

st.markdown("**Тип техніки та кількість**")

col1, col2, col3 = st.columns(3)

with col1:
    special_light_volume = st.number_input(
        "Легкові автомобілі",
        min_value=0,
        value=0,
        step=1,
        key="special_light_volume"
    )

with col2:
    special_truck_volume = st.number_input(
        "Вантажні автомобілі",
        min_value=0,
        value=0,
        step=1,
        key="special_truck_volume"
    )

with col3:
    special_bus_volume = st.number_input(
        "Автобуси",
        min_value=0,
        value=0,
        step=1,
        key="special_bus_volume"
    )

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

    # ========================================================
    # РХ РОЗВІДКА
    # ========================================================

    if rhr_type == "Розвідка маршруту":
        rhr_productivity = rhr_route
    else:
        rhr_productivity = rhr_area

    rhr_result = calculate_units(
        rhr_volume,
        rhr_productivity,
        rhr_time
    )

    if rhr_result is None:

        st.error(
            "Для РХ розвідки необхідно вказати можливість "
            "одного відділення більше 0 км/год."
        )

    else:

        st.markdown(
            f"""
            <div class="result-card">
                <div class="result-title">РХ РОЗВІДКА</div>
                <div class="result-details">
                    Вид: {rhr_type}<br>
                    Обсяг: {rhr_volume:.1f} км<br>
                    Час виконання: {rhr_time:.1f} год<br>
                    Можливість одного відділення: {rhr_productivity:.1f} км/год
                </div>
                <div class="result-number">
                    {rhr_result} відділення РХ розвідки
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # САНІТАРНА ОБРОБКА
    # ========================================================

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
                    Можливість одного відділення: {san_people:.1f} осіб/год
                </div>

                <div class="result-number">
                    {san_result} відділення санітарної обробки
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )


    # ========================================================
    # СПЕЦІАЛЬНА ОБРОБКА
    # ========================================================

    special_results = []


    # --------------------------------------------------------
    # ЛЕГКОВІ АВТОМОБІЛІ
    # --------------------------------------------------------

    if special_light_volume > 0:

        result = calculate_units(
            special_light_volume,
            special_light,
            special_time
        )

        if result is None:

            st.error(
                "Для легкових автомобілів необхідно вказати "
                "можливість більше 0 од./год."
            )

        else:

            special_results.append(
                (
                    "Легкові автомобілі",
                    special_light_volume,
                    special_light,
                    result
                )
            )


    # --------------------------------------------------------
    # ВАНТАЖНІ АВТОМОБІЛІ
    # --------------------------------------------------------

    if special_truck_volume > 0:

        result = calculate_units(
            special_truck_volume,
            special_heavy,
            special_time
        )

        if result is None:

            st.error(
                "Для вантажних автомобілів необхідно вказати "
                "можливість більше 0 од./год."
            )

        else:

            special_results.append(
                (
                    "Вантажні автомобілі",
                    special_truck_volume,
                    special_heavy,
                    result
                )
            )


    # --------------------------------------------------------
    # АВТОБУСИ
    # --------------------------------------------------------

    if special_bus_volume > 0:

        result = calculate_units(
            special_bus_volume,
            special_heavy,
            special_time
        )

        if result is None:

            st.error(
                "Для автобусів необхідно вказати "
                "можливість більше 0 од./год."
            )

        else:

            special_results.append(
                (
                    "Автобуси",
                    special_bus_volume,
                    special_heavy,
                    result
                )
            )


    # ========================================================
    # ВИВЕДЕННЯ РЕЗУЛЬТАТІВ СПЕЦІАЛЬНОЇ ОБРОБКИ
    # ========================================================

    if special_results:

        for vehicle_name, volume, productivity, result in special_results:

            st.markdown(
                f"""
                <div class="result-card">
                    <div class="result-title">
                        СПЕЦІАЛЬНА ОБРОБКА ТЕХНІКИ
                    </div>

                    <div class="result-details">
                        Вид обробки: {special_type}<br>
                        Тип техніки: {vehicle_name}<br>
                        Кількість: {volume} од.<br>
                        Час виконання: {special_time:.1f} год<br>
                        Можливість одного відділення: {productivity:.1f} од./год
                    </div>

                    <div class="result-number">
                        {result} відділення спеціальної обробки
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        st.info(
            "Для спеціальної обробки не задано кількість техніки."
        )


    # ========================================================
    # ПІДСУМОК
    # ========================================================

    st.subheader("Підсумок")

    summary_col1, summary_col2, summary_col3 = st.columns(3)

    with summary_col1:

        st.metric(
            "Відділення РХ розвідки",
            rhr_result if rhr_result is not None else "-"
        )

    with summary_col2:

        st.metric(
            "Відділення санітарної обробки",
            san_result if san_result is not None else "-"
        )

    with summary_col3:

        if special_results:
            special_total = max(
                item[3] for item in special_results
            )
        else:
            special_total = 0

        st.metric(
            "Відділення спеціальної обробки",
            special_total
        )
```

### Что конкретно изменено

* Серые подписи полей теперь принудительно **белые**, в том числе на мобильном.
* Скрыта верхняя служебная панель Streamlit:

  * меню;
  * `Deploy`;
  * служебный header;
  * footer.
* Результаты оставлены в виде нормальных карточек без вывода служебных HTML-тегов пользователю.
* В «Можливості одного відділення» теперь:

  1. **Всього техніки, од./год**
  2. **У тому числі — легкові автомобілі, од./год**
  3. **У тому числі — вантажні автомобілі (автобуси), од./год**
* Для расчёта:

  * легковые используют своё значение;
  * грузовые используют значение «вантажні автомобілі (автобуси)»;
  * автобусы используют то же значение.
* Остальная логика расчёта и отдельное время выполнения каждой задачи сохранены.

**Важный момент:** поле **«Всього техніки» пока информационное** и не участвует непосредственно в формуле. Это логично, если оно нужно как общая характеристика возможности отделения, а расчёт производится по конкретному типу техники.
