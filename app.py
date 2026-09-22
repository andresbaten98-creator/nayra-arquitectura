import streamlit as st
from textwrap import dedent
from html import escape



# ============================================================
# CONFIGURACIÓN
# ============================================================

st.set_page_config(
    page_title="Náyra — Arquitectura",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# FUNCIÓN PARA HTML
# ============================================================

def html(contenido):
    st.html(dedent(contenido).strip())


# ============================================================
# TEMA
# ============================================================

# El tema se guarda en la URL para que no se pierda al cambiar de sección
# ni al recargar la página.
tema_url = st.query_params.get("tema", "claro").lower()

if "modo_oscuro" not in st.session_state:
    st.session_state.modo_oscuro = tema_url == "oscuro"


def cambiar_tema():
    st.query_params["tema"] = "oscuro" if st.session_state.modo_oscuro else "claro"


_, col_tema = st.columns([7.5, 2.5])
with col_tema:
    st.toggle(
        "🌙 Fondo oscuro",
        key="modo_oscuro",
        on_change=cambiar_tema
    )
    st.caption("Tema guardado" if st.session_state.modo_oscuro else "Tema claro")


# ============================================================
# ESTILOS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');


/* ==========================================================
   PALETA
   ========================================================== */

:root {
    --navy: #14253D;
    --navy-light: #294665;

    --beige: #F8F5EF;
    --beige-dark: #EDE6DA;

    --pink: #E9A9C4;
    --pink-light: #F7DDE8;

    --blue: #B9DCE8;
    --blue-light: #E5F3F7;

    --lilac: #C8B8DD;
    --lilac-light: #EEE8F5;

    --red: #C96B6B;
    --red-light: #F5DEDE;

    --black: #252525;

    --text: #3E4650;
    --muted: #727A84;

    --white: #FFFFFF;
    --line: #E3DDD3;
}


/* ==========================================================
   GENERAL
   ========================================================== */

.stApp {
    background: var(--beige);
    color: var(--text);
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

.block-container {
    max-width: 1180px;
    padding-top: 2.5rem;
    padding-bottom: 5rem;
}


/* ==========================================================
   MARCA
   ========================================================== */

.brand {
    text-align: center;
    padding-top: 5px;
    margin-bottom: 35px;
}

.brand-name {
    font-family: 'Playfair Display', serif;
    font-size: 4.5rem;
    font-weight: 600;
    color: var(--navy);
    line-height: 1.1;
    letter-spacing: -2px;
}

.brand-dot {
    color: var(--pink);
}

.brand-subtitle {
    margin-top: 9px;
    color: #718096;
    font-family: 'Inter', sans-serif;
    font-size: 0.78rem;
    letter-spacing: 2.5px;
    text-transform: uppercase;
}


/* ==========================================================
   PALETA DE NÁYRA
   ========================================================== */

.color-palette {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 7px;
    margin-top: 16px;
}

.palette-dot {
    width: 9px;
    height: 9px;
    border-radius: 50%;
    display: inline-block;
}

.palette-beige {
    background: #DCCDB8;
}

.palette-blue {
    background: #B9DCE8;
}

.palette-pink {
    background: #E9A9C4;
}

.palette-lilac {
    background: #C8B8DD;
}

.palette-black {
    background: #252525;
}

.palette-red {
    background: #C96B6B;
}


/* ==========================================================
   HERO
   ========================================================== */

.hero {
    background:
        linear-gradient(
            135deg,
            #14253D 0%,
            #1D3452 55%,
            #294665 100%
        );

    border-radius: 28px;
    padding: 55px;
    color: white;
    margin-bottom: 50px;

    position: relative;
    overflow: hidden;

    box-shadow:
        0 20px 50px rgba(20, 37, 61, 0.18);
}

.hero::after {
    content: "N";

    position: absolute;
    right: 25px;
    bottom: -100px;

    font-family: 'Playfair Display', serif;
    font-size: 290px;

    color: rgba(255,255,255,0.035);
}

.hero-small {
    color: #D9BED0;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 17px;
}

.hero-title {
    position: relative;
    z-index: 2;

    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 600;

    color: white;

    line-height: 1.15;

    margin-bottom: 18px;
}

.hero-text {
    position: relative;
    z-index: 2;

    max-width: 720px;

    color: rgba(255,255,255,0.82);

    font-family: 'Inter', sans-serif;

    font-size: 1rem;
    line-height: 1.8;
}


/* ==========================================================
   TÍTULOS
   ========================================================== */

.section-title {
    font-family: 'Playfair Display', serif;

    font-size: 2rem;

    color: var(--navy);

    margin-bottom: 8px;
}

.section-description {
    color: var(--muted);

    font-size: 0.92rem;

    margin-bottom: 25px;
}


/* ==========================================================
   TARJETAS DE ESTILOS
   ========================================================== */

.arch-card {
    background: var(--white);

    border: 1px solid var(--line);

    border-radius: 22px;

    padding: 28px;

    min-height: 320px;

    box-shadow:
        0 8px 25px rgba(20,37,61,0.045);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease,
        border-color 0.25s ease;
}

.arch-card:hover {
    transform: translateY(-6px);

    box-shadow:
        0 18px 38px rgba(20,37,61,0.11);

    border-color: var(--pink);
}

.arch-icon {
    width: 54px;
    height: 54px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 16px;

    background: var(--blue-light);

    font-size: 1.9rem;

    margin-bottom: 20px;
}

.arch-title {
    font-family: 'Playfair Display', serif;

    color: var(--navy);

    font-size: 1.45rem;

    font-weight: 600;

    margin-bottom: 12px;
}

.arch-description {
    color: var(--muted);

    font-size: 0.9rem;

    line-height: 1.7;
}

.arch-period {
    display: inline-block;

    margin-top: 18px;

    padding: 6px 12px;

    border-radius: 20px;

    background: var(--pink-light);

    color: #85556C;

    font-size: 0.7rem;

    font-weight: 600;
}


/* ==========================================================
   BOTONES
   ========================================================== */

.stButton > button {
    width: 100%;

    min-height: 43px;

    border-radius: 12px;

    border: 1px solid #D9D1C5;

    background: white;

    color: var(--navy);

    font-family: 'Inter', sans-serif;

    font-weight: 600;

    transition: all 0.2s ease;
}

.stButton > button:hover {
    border-color: var(--pink);

    background: #FFF9FB;

    color: var(--navy);
}


/* ==========================================================
   INFORMACIÓN
   ========================================================== */

.info-box {
    background: white;

    border: 1px solid var(--line);

    border-radius: 22px;

    padding: 30px;

    margin-top: 35px;

    box-shadow:
        0 7px 22px rgba(20,37,61,0.035);
}

.info-title {
    font-family: 'Playfair Display', serif;

    color: var(--navy);

    font-size: 1.5rem;

    margin-bottom: 13px;
}

.info-text {
    color: #59636F;

    line-height: 1.8;
}

.info-list {
    color: #59636F;

    line-height: 2;
}


/* ==========================================================
   DETALLE
   ========================================================== */

.detail-header {
    background: white;

    border: 1px solid var(--line);

    border-radius: 25px;

    padding: 40px;

    margin-top: 15px;

    margin-bottom: 35px;

    box-shadow:
        0 8px 25px rgba(20,37,61,0.05);
}

.detail-icon {
    width: 65px;
    height: 65px;

    display: flex;

    align-items: center;
    justify-content: center;

    border-radius: 19px;

    background: var(--lilac-light);

    font-size: 2.4rem;

    margin-bottom: 18px;
}

.detail-title {
    font-family: 'Playfair Display', serif;

    color: var(--navy);

    font-size: 3rem;

    font-weight: 600;

    line-height: 1.15;
}

.detail-period {
    color: var(--red);

    font-size: 0.78rem;

    font-weight: 700;

    letter-spacing: 1.5px;

    text-transform: uppercase;

    margin-top: 10px;
}

.detail-description {
    color: #59636F;

    line-height: 1.8;

    font-size: 1rem;

    margin-top: 20px;

    max-width: 850px;
}


/* ==========================================================
   CARACTERÍSTICAS
   ========================================================== */

.feature {
    background: white;

    border: 1px solid var(--line);

    border-radius: 18px;

    padding: 22px;

    margin-bottom: 15px;

    transition: 0.2s ease;
}

.feature:hover {
    border-color: var(--blue);

    transform: translateY(-2px);
}

.feature-title {
    color: var(--navy);

    font-weight: 700;

    margin-bottom: 7px;
}

.feature-text {
    color: var(--muted);

    line-height: 1.65;

    font-size: 0.91rem;
}


/* ==========================================================
   OBRA REPRESENTATIVA
   ========================================================== */

.work {
    background:
        linear-gradient(
            135deg,
            #14253D,
            #294665
        );

    border-radius: 25px;

    padding: 38px;

    margin: 32px 0;

    box-shadow:
        0 15px 35px rgba(20,37,61,0.16);

    position: relative;

    overflow: hidden;
}

.work::after {
    content: "✦";

    position: absolute;

    right: 30px;
    top: 20px;

    font-size: 90px;

    color: rgba(255,255,255,0.05);
}

.work-label {
    color: var(--pink);

    font-size: 0.72rem;

    font-weight: 700;

    letter-spacing: 2px;

    text-transform: uppercase;
}

.work-title {
    color: white;

    font-family: 'Playfair Display', serif;

    font-size: 2.1rem;

    margin: 9px 0 15px;
}

.work-text {
    color: rgba(255,255,255,0.82);

    line-height: 1.8;

    max-width: 850px;
}


/* ==========================================================
   DATO INTERESANTE
   ========================================================== */

.fact {
    background: var(--pink-light);

    border-left: 5px solid var(--pink);

    border-radius: 18px;

    padding: 25px;

    margin: 32px 0;
}

.fact-title {
    color: #784E62;

    font-weight: 700;

    margin-bottom: 8px;
}

.fact-text {
    color: #66545D;

    line-height: 1.75;
}


/* ==========================================================
   QUIZ
   ========================================================== */

.quiz-header {
    background: var(--blue-light);

    border: 1px solid #D3E8EE;

    border-radius: 20px;

    padding: 25px;

    margin-top: 35px;

    margin-bottom: 18px;
}

.quiz-title {
    font-family: 'Playfair Display', serif;

    color: var(--navy);

    font-size: 1.5rem;

    margin-bottom: 5px;
}

.quiz-description {
    color: var(--muted);

    font-size: 0.9rem;
}


/* ==========================================================
   FUENTES
   ========================================================== */

.sources {
    background: white;

    border: 1px solid var(--line);

    border-radius: 20px;

    padding: 25px;

    margin-top: 35px;
}

.sources-title {
    color: var(--navy);

    font-family: 'Playfair Display', serif;

    font-size: 1.4rem;
}

.sources-text {
    color: var(--muted);

    font-size: 0.88rem;

    line-height: 1.6;
}

.sources a {
    color: #395875;

    text-decoration: none;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.nayra-footer {
    text-align: center;

    color: #8A8E93;

    border-top: 1px solid var(--line);

    margin-top: 65px;

    padding-top: 28px;

    line-height: 1.9;

    font-size: 0.85rem;
}


/* ==========================================================
   MÓVIL
   ========================================================== */

@media (max-width: 700px) {

    .block-container {
        padding-top: 1.5rem;
    }

    .brand-name {
        font-size: 3.3rem;
    }

    .hero {
        padding: 34px 25px;
        border-radius: 22px;
    }

    .hero-title {
        font-size: 2.25rem;
    }

    .detail-header {
        padding: 28px;
    }

    .detail-title {
        font-size: 2.3rem;
    }

}



/* ==========================================================
   CARRUSEL HORIZONTAL
   ========================================================== */

.arch-carousel {
    display: flex;
    gap: 20px;
    overflow-x: auto;
    overflow-y: hidden;
    scroll-snap-type: x mandatory;
    scroll-behavior: smooth;
    padding: 8px 4px 24px;
    margin: 0 -4px;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: thin;
    scrollbar-color: var(--pink) transparent;
    overscroll-behavior-x: contain;
}

.arch-carousel::-webkit-scrollbar { height: 7px; }
.arch-carousel::-webkit-scrollbar-track { background: transparent; }
.arch-carousel::-webkit-scrollbar-thumb { background: var(--pink); border-radius: 20px; }

.arch-card-link {
    flex: 0 0 330px;
    min-height: 320px;
    scroll-snap-align: start;
    display: block;
    box-sizing: border-box;
    padding: 28px;
    border-radius: 22px;
    border: 1px solid var(--line);
    background: var(--white);
    color: inherit !important;
    text-decoration: none !important;
    box-shadow: 0 8px 25px rgba(20,37,61,0.045);
    transition: transform .25s ease, box-shadow .25s ease, border-color .25s ease;
}

.arch-card-link:hover {
    transform: translateY(-6px);
    border-color: var(--pink);
    box-shadow: 0 18px 38px rgba(20,37,61,0.11);
}

.arch-card-link:active { transform: scale(.985); }

.arch-card-link {
    position: relative;
    overflow: hidden;
}

.arch-card-link::before {
    content: "";
    position: absolute;
    width: 160px;
    height: 160px;
    right: -60px;
    top: -70px;
    border-radius: 50%;
    background: var(--pink-light);
    opacity: .55;
    transition: transform .45s ease, opacity .45s ease;
    pointer-events: none;
}

.arch-card-link::after {
    content: "↗";
    position: absolute;
    right: 20px;
    bottom: 18px;
    width: 34px;
    height: 34px;
    display: grid;
    place-items: center;
    border-radius: 50%;
    background: var(--navy);
    color: white;
    font-size: 16px;
    opacity: 0;
    transform: translateY(8px);
    transition: opacity .25s ease, transform .25s ease;
    pointer-events: none;
}

.arch-card-link:hover::before {
    transform: scale(1.45);
    opacity: .8;
}

.arch-card-link:hover::after {
    opacity: 1;
    transform: translateY(0);
}

.arch-card-link:focus-visible {
    outline: 3px solid var(--pink);
    outline-offset: 4px;
}

.carousel-hint {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 12px;
    margin: 2px 0 14px;
    color: var(--muted);
    font-size: .78rem;
}

.carousel-hint strong { color: var(--navy); }

/* ==========================================================
   WIDGETS · VISIBILIDAD EN TEMA CLARO
   ========================================================== */

[data-testid="stRadio"],
[data-testid="stRadio"] label,
[data-testid="stRadio"] label *,
[data-testid="stRadio"] p,
[data-testid="stRadio"] span,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] * {
    color: var(--text) !important;
}

[data-testid="stRadio"] input {
    accent-color: var(--pink) !important;
}
</style>

/* ==========================================================
   MEJORAS VISUALES · NÁYRA 2.0
   ========================================================== */

html {
    scroll-behavior: smooth;
}

.stApp {
    background-image:
        linear-gradient(rgba(20,37,61,.025) 1px, transparent 1px),
        linear-gradient(90deg, rgba(20,37,61,.025) 1px, transparent 1px);
    background-size: 42px 42px;
}

/* Barra superior de navegación */
.nayra-nav {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 9px;
    margin: -8px auto 28px;
    padding: 8px;
    width: fit-content;
    max-width: 100%;
    border: 1px solid var(--line);
    border-radius: 999px;
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(14px);
    box-shadow: 0 8px 24px rgba(20,37,61,.055);
}

.nav-chip {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 9px 15px;
    border-radius: 999px;
    color: var(--navy);
    font-size: .78rem;
    font-weight: 700;
    text-decoration: none !important;
    transition: all .2s ease;
}

.nav-chip:hover {
    background: var(--pink-light);
    transform: translateY(-1px);
}

/* Separador editorial */
.editorial-line {
    display: flex;
    align-items: center;
    gap: 12px;
    margin: 42px 0 24px;
    color: var(--muted);
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.editorial-line::before,
.editorial-line::after {
    content: "";
    height: 1px;
    flex: 1;
    background: var(--line);
}

/* Hero más editorial */
.hero {
    isolation: isolate;
}

.hero::before {
    content: "";
    position: absolute;
    width: 310px;
    height: 310px;
    right: -95px;
    top: -115px;
    border: 1px solid rgba(255,255,255,.10);
    border-radius: 50%;
    box-shadow:
        0 0 0 30px rgba(255,255,255,.018),
        0 0 0 60px rgba(255,255,255,.012);
    pointer-events: none;
}

.hero-building {
    position: absolute;
    right: 54px;
    bottom: 0;
    width: 190px;
    height: 185px;
    opacity: .18;
    pointer-events: none;
}

.hero-building .tower {
    position: absolute;
    bottom: 0;
    width: 54px;
    height: 145px;
    border: 2px solid rgba(255,255,255,.75);
    border-bottom: 0;
}

.hero-building .tower:nth-child(1) { left: 8px; height: 105px; }
.hero-building .tower:nth-child(2) { left: 68px; height: 160px; }
.hero-building .tower:nth-child(3) { right: 8px; height: 125px; }

.hero-building .window {
    position: absolute;
    width: 7px;
    height: 15px;
    border: 1px solid rgba(255,255,255,.7);
    background: rgba(255,255,255,.13);
}

.hero-building .w1 { left: 25px; bottom: 48px; }
.hero-building .w2 { left: 85px; bottom: 92px; }
.hero-building .w3 { left: 85px; bottom: 57px; }
.hero-building .w4 { right: 25px; bottom: 66px; }

/* Mini panel de estadísticas */
.stats-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 14px;
    margin: 28px 0 42px;
}

.stat-card {
    padding: 18px 20px;
    border: 1px solid var(--line);
    border-radius: 18px;
    background: rgba(255,255,255,.72);
    backdrop-filter: blur(8px);
}

.stat-number {
    font-family: 'Playfair Display', serif;
    color: var(--navy);
    font-size: 1.75rem;
    font-weight: 700;
}

.stat-label {
    color: var(--muted);
    font-size: .75rem;
    margin-top: 2px;
}

/* Tarjetas con profundidad */
.arch-card-link {
    transform: translateZ(0);
}

.arch-card-link:hover {
    transform: translateY(-8px) rotateX(1deg);
}

.arch-card-link .arch-icon {
    transition: transform .35s ease;
}

.arch-card-link:hover .arch-icon {
    transform: translateY(-3px) rotate(-3deg) scale(1.04);
}

.arch-card-link .arch-period {
    transition: transform .25s ease;
}

.arch-card-link:hover .arch-period {
    transform: translateX(4px);
}

/* Migas de pan */
.breadcrumb {
    color: var(--muted);
    font-size: .76rem;
    margin: 4px 0 14px;
}

.breadcrumb strong {
    color: var(--navy);
}

/* Barra de progreso */
.progress-wrap {
    margin: 0 0 28px;
}

.progress-meta {
    display: flex;
    justify-content: space-between;
    color: var(--muted);
    font-size: .72rem;
    margin-bottom: 7px;
}

.progress-track {
    width: 100%;
    height: 6px;
    overflow: hidden;
    border-radius: 99px;
    background: var(--beige-dark);
}

.progress-fill {
    height: 100%;
    border-radius: inherit;
    background: linear-gradient(90deg, var(--pink), var(--lilac));
}

/* Caja de navegación entre estilos */
.next-nav {
    margin-top: 34px;
    padding: 20px;
    border: 1px solid var(--line);
    border-radius: 20px;
    background: rgba(255,255,255,.72);
}

.next-nav-title {
    color: var(--muted);
    font-size: .72rem;
    font-weight: 700;
    letter-spacing: 1.5px;
    text-transform: uppercase;
    margin-bottom: 4px;
}

.next-nav-name {
    color: var(--navy);
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
}

/* Inputs */
[data-testid="stTextInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    border-radius: 13px !important;
    border-color: var(--line) !important;
}

[data-testid="stTextInput"] input:focus {
    border-color: var(--pink) !important;
    box-shadow: 0 0 0 2px rgba(233,169,196,.18) !important;
}

/* Botones más modernos */
.stButton > button {
    min-height: 46px;
    box-shadow: 0 4px 12px rgba(20,37,61,.035);
}

.stButton > button:active {
    transform: scale(.985);
}

/* Selección de texto */
::selection {
    background: var(--pink-light);
    color: var(--navy);
}

@media (max-width: 700px) {
    .nayra-nav {
        width: 100%;
        justify-content: space-between;
        overflow-x: auto;
    }

    .nav-chip {
        flex: 0 0 auto;
        padding: 8px 12px;
    }

    .stats-grid {
        grid-template-columns: 1fr;
    }

    .hero-building {
        right: -18px;
        transform: scale(.78);
        transform-origin: bottom right;
    }

    .hero-title,
    .hero-text {
        max-width: 85%;
    }
}

""", unsafe_allow_html=True)

if st.session_state.modo_oscuro:
    st.markdown(r"""
<style>
/* ==========================================================
   NÁYRA · TEMA OSCURO COMPLETO
   ========================================================== */

.stApp,
[data-testid="stAppViewContainer"],
[data-testid="stHeader"],
[data-testid="stToolbar"],
main {
    background: #0D151F !important;
}

[data-testid="stAppViewContainer"],
.block-container {
    color: #EEF2F6 !important;
}

/* Textos propios de Náyra */
.brand-name,
.section-title,
.arch-title,
.info-title,
.detail-title,
.feature-title,
.work-title,
.fact-title,
.quiz-title,
.sources-title {
    color: #F8F5EF !important;
}

.brand-subtitle,
.section-description,
.arch-description,
.detail-description,
.info-text,
.info-list,
.feature-text,
.work-text,
.fact-text,
.quiz-description,
.sources-text,
.carousel-hint {
    color: #C1CCD7 !important;
}

/* Tarjetas */
.arch-card,
.arch-card-link,
.info-box,
.detail-header,
.feature,
.sources,
.quiz-header,
.work,
.fact {
    background: #172433 !important;
    border-color: #304457 !important;
    color: #EAF0F5 !important;
    box-shadow: 0 12px 32px rgba(0,0,0,.24) !important;
}

.arch-card-link:hover,
.feature:hover {
    border-color: #E9A9C4 !important;
    box-shadow: 0 20px 42px rgba(0,0,0,.34) !important;
}

.arch-icon {
    background: #21394C !important;
}

.arch-period {
    background: #453444 !important;
    color: #F4C9DB !important;
}

/* Botones nativos */
.stButton > button {
    background: #172433 !important;
    color: #F4F1EC !important;
    border: 1px solid #40576B !important;
}

.stButton > button p,
.stButton > button span {
    color: #F4F1EC !important;
}

.stButton > button:hover {
    background: #24384B !important;
    color: #FFFFFF !important;
    border-color: #E9A9C4 !important;
}

/* ==========================================================
   QUIZ · TEXTO SIEMPRE VISIBLE
   ========================================================== */

[data-testid="stRadio"],
[data-testid="stRadio"] label,
[data-testid="stRadio"] label *,
[data-testid="stRadio"] p,
[data-testid="stRadio"] span,
[data-testid="stRadio"] div,
[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] * {
    color: #EAF0F5 !important;
}

[data-testid="stRadio"] label[data-baseweb="radio"] > div {
    color: #EAF0F5 !important;
}

[data-testid="stRadio"] input {
    accent-color: #E9A9C4 !important;
}

/* Mensajes del quiz */
[data-testid="stAlert"],
[data-testid="stAlert"] p,
[data-testid="stAlert"] div {
    color: #F4F7FA !important;
}

/* Toggle */
[data-testid="stToggle"],
[data-testid="stToggle"] label,
[data-testid="stToggle"] label *,
[data-testid="stToggle"] p,
[data-testid="stToggle"] span {
    color: #EAF0F5 !important;
}

[data-testid="stToggle"] [role="switch"] {
    background-color: #3A5065 !important;
}

/* Fuentes */
.sources a {
    color: #9ED8EA !important;
}

.sources a:hover {
    color: #F3B7D0 !important;
}

/* Footer */
.nayra-footer {
    color: #8996A3 !important;
    border-color: #304457 !important;
}

/* Mejoras visuales */
.nayra-nav,
.stat-card,
.next-nav {
    background: rgba(23,36,51,.82) !important;
    border-color: #304457 !important;
    box-shadow: 0 10px 30px rgba(0,0,0,.22) !important;
}

.nav-chip,
.stat-number,
.next-nav-name {
    color: #F4F1EC !important;
}

.editorial-line,
.breadcrumb,
.progress-meta,
.stat-label,
.next-nav-title {
    color: #AAB7C4 !important;
}

.progress-track {
    background: #26394A !important;
}

[data-testid="stTextInput"] input,
[data-testid="stSelectbox"] div[data-baseweb="select"] > div {
    background: #172433 !important;
    color: #EEF2F6 !important;
    border-color: #40576B !important;
}

[data-testid="stTextInput"] input::placeholder {
    color: #8E9CAA !important;
}

/* Scrollbar */
.arch-carousel {
    scrollbar-color: #E9A9C4 #182632;
}

.arch-carousel::-webkit-scrollbar-track {
    background: #182632;
}

.arch-carousel::-webkit-scrollbar-thumb {
    background: #E9A9C4;
}
</style>
""", unsafe_allow_html=True)


st.markdown(r"""
<style>
@media (max-width: 700px) {
    .arch-carousel {
        gap: 14px;
        padding-bottom: 18px;
        mask-image: none;
    }

    .arch-card-link {
        flex: 0 0 82vw;
        min-height: 300px;
        padding: 24px;
    }

    .arch-card-link::after {
        opacity: 1;
        transform: none;
    }

    .carousel-hint { font-size: .72rem; }
}
</style>
""", unsafe_allow_html=True)


# ============================================================
# NAVEGACIÓN GLOBAL
# ============================================================

tema_actual = "oscuro" if st.session_state.modo_oscuro else "claro"
html(f"""
<div class="nayra-nav">
    <a class="nav-chip" href="?pagina=inicio&tema={tema_actual}">⌂ Inicio</a>
    <a class="nav-chip" href="?pagina=catalogo&tema={tema_actual}">🏛️ Estilos</a>
    <a class="nav-chip" href="?pagina=Guatemala&tema={tema_actual}">🇬🇹 Guatemala</a>
</div>
""")

# ============================================================
# INFORMACIÓN DE LOS ESTILOS
# ============================================================

estilos = {

    "Clasico": {
        "nombre": "Arquitectura Clásica",
        "icono": "🏛️",
        "periodo": "Grecia y Roma antiguas",
        "descripcion": "Una arquitectura basada en el orden, la proporción, la simetría y el equilibrio.",
        "historia": "La arquitectura clásica tiene sus principales raíces en la antigua Grecia y Roma. Los griegos desarrollaron los órdenes dórico, jónico y corintio, mientras que los romanos adoptaron y transformaron estas ideas. Roma incorporó además soluciones como el arco, la bóveda, la cúpula y el hormigón, permitiendo construir espacios de mayor escala.",
        "materiales": "Piedra y mármol fueron fundamentales en Grecia. Los romanos también utilizaron ladrillo, hormigón, piedra y diferentes revestimientos.",
        "caracteristicas": [
            ("Orden y proporción", "Las diferentes partes del edificio mantienen relaciones proporcionales entre sí."),
            ("Simetría", "La composición suele organizarse mediante ejes y relaciones equilibradas."),
            ("Columnas", "Las columnas son elementos fundamentales y pueden pertenecer a los órdenes dórico, jónico o corintio."),
            ("Frontón", "Elemento triangular situado tradicionalmente sobre la fachada de muchos templos."),
            ("Entablamento", "Conjunto horizontal colocado sobre las columnas y dividido en varias partes."),
            ("Arcos y bóvedas", "La tradición romana amplió enormemente el uso del arco, las bóvedas y las cúpulas.")
        ],
        "obra": "El Partenón",
        "obra_info": "El Partenón fue construido en la Acrópolis de Atenas entre 447 y 432 a. C. y estuvo dedicado a Atenea. Es uno de los ejemplos más estudiados de la arquitectura clásica griega.",
        "arquitectos": "Ictinos y Calícrates son tradicionalmente reconocidos como sus arquitectos; Fidias estuvo relacionado con la dirección de la decoración escultórica.",
        "reconocer": [
            "Busca columnas con capiteles claramente definidos.",
            "Observa si existe una composición simétrica.",
            "Busca frontones y elementos horizontales.",
            "Identifica una sensación general de orden y proporción.",
            "En edificios romanos, busca también arcos, bóvedas o cúpulas."
        ],
        "dato": "Los arquitectos griegos utilizaron pequeñas correcciones ópticas en determinados edificios para mejorar la percepción visual de sus líneas y proporciones.",
        "pregunta": "¿Cuál de estos elementos está directamente relacionado con la arquitectura clásica?",
        "opciones": ["Columnas y capiteles", "Arbotantes", "Vitrales góticos", "Hormigón visto"],
        "respuesta": "Columnas y capiteles",
        "fuentes": [
            ("The Metropolitan Museum of Art — Architecture in Ancient Greece", "https://www.metmuseum.org/toah/hd/grarc/hd_grarc.htm"),
            ("Encyclopaedia Britannica — Classical architecture", "https://www.britannica.com/art/Classical-architecture")
        ]
    },

    "Gotico": {
        "nombre": "Arquitectura Gótica",
        "icono": "⛪",
        "periodo": "Europa medieval · siglos XII–XVI",
        "descripcion": "Una arquitectura caracterizada por la verticalidad, la luz, los vitrales y nuevas soluciones estructurales.",
        "historia": "La arquitectura gótica se desarrolló en Europa a partir del siglo XII, especialmente en Francia, y se extendió posteriormente por otras regiones. El arco apuntado, la bóveda de crucería y los arbotantes permitieron distribuir las cargas de una manera diferente y abrir grandes superficies para ventanas y vitrales.",
        "materiales": "La piedra fue fundamental para muros, pilares y bóvedas. El vidrio coloreado adquirió especial importancia en las grandes ventanas.",
        "caracteristicas": [
            ("Arco apuntado", "También llamado arco ojival. Es uno de los elementos más reconocibles del estilo gótico."),
            ("Bóveda de crucería", "Sistema de nervaduras que ayuda a organizar y transmitir las cargas de la cubierta."),
            ("Arbotantes", "Elementos exteriores que ayudan a transmitir los empujes de las bóvedas hacia apoyos alejados del muro."),
            ("Vitrales", "Grandes ventanas de vidrio coloreado que permiten introducir luz y contenido visual."),
            ("Verticalidad", "Las proporciones buscan enfatizar la altura del edificio."),
            ("Rosetón", "Gran ventana circular decorada que aparece en numerosas catedrales góticas.")
        ],
        "obra": "Catedral de Notre-Dame de París",
        "obra_info": "La construcción de Notre-Dame de París comenzó en 1163. Es uno de los ejemplos más reconocibles del gótico francés y permite observar arcos apuntados, vitrales, rosetones y sistemas de soporte exteriores.",
        "arquitectos": "Su construcción fue un proceso colectivo dirigido por diferentes maestros de obra a lo largo del tiempo, por lo que no se atribuye a un único arquitecto.",
        "reconocer": [
            "Busca arcos apuntados.",
            "Observa grandes vitrales y rosetones.",
            "Busca una marcada sensación de verticalidad.",
            "Identifica arbotantes en el exterior.",
            "Observa bóvedas de crucería en el interior."
        ],
        "dato": "Las soluciones estructurales góticas permitieron reducir parte de las cargas que recaían directamente sobre los muros, facilitando ventanas mucho mayores.",
        "pregunta": "¿Qué elemento es característico de la arquitectura gótica?",
        "opciones": ["Arco apuntado", "Orden dórico", "Frontón clásico", "Pilotis"],
        "respuesta": "Arco apuntado",
        "fuentes": [
            ("The Metropolitan Museum of Art — Gothic Art", "https://www.metmuseum.org/toah/hd/goth/hd_goth.htm"),
            ("Encyclopaedia Britannica — Gothic architecture", "https://www.britannica.com/art/Gothic-architecture")
        ]
    },

    "Renacentista": {
        "nombre": "Arquitectura Renacentista",
        "icono": "🏺",
        "periodo": "Europa · siglos XV–XVI",
        "descripcion": "Una arquitectura que recuperó principios de la Antigüedad clásica y los combinó con nuevas ideas sobre geometría, perspectiva y proporción.",
        "historia": "El Renacimiento surgió en las ciudades italianas durante el siglo XV y se extendió por Europa. Los arquitectos estudiaron edificios y tratados de la Antigüedad y buscaron aplicar sus principios mediante composiciones geométricas, proporciones matemáticas y una nueva valoración del espacio.",
        "materiales": "Se utilizaron piedra, ladrillo, mármol y estuco, junto con sistemas constructivos tradicionales y una decoración inspirada en la Antigüedad.",
        "caracteristicas": [
            ("Simetría", "Las fachadas y plantas suelen organizarse alrededor de ejes y relaciones equilibradas."),
            ("Proporción", "La geometría se utiliza para establecer relaciones entre las diferentes partes del edificio."),
            ("Arco de medio punto", "Se recupera de la tradición clásica y aparece en puertas, ventanas y espacios interiores."),
            ("Cúpulas", "Las cúpulas adquieren un papel protagonista en numerosas obras renacentistas."),
            ("Órdenes clásicos", "Columnas, pilastras y entablamentos retoman modelos de la Antigüedad."),
            ("Perspectiva", "La nueva comprensión de la perspectiva también influyó en la representación y organización del espacio.")
        ],
        "obra": "Cúpula de Santa Maria del Fiore",
        "obra_info": "La gran cúpula de la catedral de Florencia fue diseñada por Filippo Brunelleschi y construida durante el siglo XV. Es una de las obras fundamentales del Renacimiento italiano.",
        "arquitectos": "Filippo Brunelleschi fue una figura central del primer Renacimiento y diseñó la gran cúpula de Florencia.",
        "reconocer": [
            "Busca composiciones muy simétricas.",
            "Identifica arcos de medio punto.",
            "Observa columnas, pilastras y entablamentos clásicos.",
            "Busca cúpulas y formas geométricas claras.",
            "Observa relaciones proporcionales entre las partes."
        ],
        "dato": "Brunelleschi desarrolló una solución constructiva para levantar la enorme cúpula de Florencia sin depender de una cimbra tradicional completa.",
        "pregunta": "¿Qué concepto se relaciona especialmente con el Renacimiento?",
        "opciones": ["Proporción y perspectiva", "Arbotantes", "Hormigón visto", "Pilotis"],
        "respuesta": "Proporción y perspectiva",
        "fuentes": [
            ("The Metropolitan Museum of Art — Renaissance Architecture", "https://www.metmuseum.org/toah/hd/itar/hd_itar.htm"),
            ("Encyclopaedia Britannica — Renaissance architecture", "https://www.britannica.com/art/Renaissance-architecture")
        ]
    },

    "ArtNouveau": {
        "nombre": "Art Nouveau",
        "icono": "🌿",
        "periodo": "Europa y América · c. 1890–1914",
        "descripcion": "Una corriente que buscó integrar arquitectura y artes decorativas mediante líneas curvas, formas orgánicas y motivos inspirados en la naturaleza.",
        "historia": "El Art Nouveau se desarrolló aproximadamente entre finales del siglo XIX y comienzos del XX. Reaccionó contra parte de la repetición histórica de estilos anteriores y aprovechó nuevos materiales y técnicas para unir arquitectura, mobiliario, cerámica, vidrio y decoración.",
        "materiales": "Hierro y vidrio permitieron nuevas posibilidades para balcones, cubiertas y superficies. También fueron frecuentes la cerámica, piedra y madera.",
        "caracteristicas": [
            ("Líneas orgánicas", "Las curvas y formas ondulantes recuerdan tallos, flores y otros elementos naturales."),
            ("Naturaleza", "Plantas, flores e insectos aparecen como fuentes de inspiración decorativa."),
            ("Hierro ornamental", "El hierro se convierte también en un recurso expresivo y no solamente estructural."),
            ("Vidrio", "Se utiliza para introducir luz y crear efectos decorativos."),
            ("Integración de artes", "Arquitectura, mobiliario, cerámica y vidriería podían formar un conjunto."),
            ("Fachada dinámica", "La composición puede evitar la rigidez geométrica de muchas fachadas tradicionales.")
        ],
        "obra": "Casa Batlló",
        "obra_info": "Construida en Barcelona y remodelada por Antoni Gaudí entre 1904 y 1906, presenta formas orgánicas, cerámica, vidrio y una fachada de gran riqueza visual.",
        "arquitectos": "Antoni Gaudí es una de las figuras más conocidas del modernismo catalán, una de las expresiones regionales relacionadas con el Art Nouveau.",
        "reconocer": [
            "Busca líneas curvas y ondulantes.",
            "Observa motivos vegetales o inspirados en la naturaleza.",
            "Identifica hierro trabajado en balcones o detalles.",
            "Busca cerámica y vidrio integrados al diseño.",
            "Observa si arquitectura y decoración parecen formar una sola obra."
        ],
        "dato": "El movimiento recibió nombres distintos según la región, como Modernisme en Cataluña y Jugendstil en los países de lengua alemana.",
        "pregunta": "¿Qué característica ayuda a reconocer el Art Nouveau?",
        "opciones": ["Formas orgánicas", "Arbotantes", "Órdenes dóricos", "Hormigón visto"],
        "respuesta": "Formas orgánicas",
        "fuentes": [
            ("Victoria and Albert Museum — Art Nouveau", "https://www.vam.ac.uk/articles/art-nouveau"),
            ("The Metropolitan Museum of Art — Art Nouveau", "https://www.metmuseum.org/toah/hd/artn/hd_artn.htm")
        ]
    },

    "Brutalista": {
        "nombre": "Arquitectura Brutalista",
        "icono": "▦",
        "periodo": "Siglo XX · especialmente posguerra",
        "descripcion": "Una corriente que destaca por sus volúmenes geométricos, materiales expuestos y expresión directa de la estructura.",
        "historia": "El brutalismo se desarrolló especialmente después de la Segunda Guerra Mundial. El hormigón fue uno de sus materiales más característicos. El término está relacionado con la expresión francesa béton brut, que hace referencia al hormigón en bruto.",
        "materiales": "El hormigón armado es el material más asociado al brutalismo, aunque también se utilizaron acero, vidrio, ladrillo y otros materiales.",
        "caracteristicas": [
            ("Hormigón visto", "El material se deja visible y forma parte importante de la estética del edificio."),
            ("Geometría", "Son frecuentes los volúmenes fuertes, repetitivos y claramente definidos."),
            ("Estructura visible", "Los elementos constructivos pueden convertirse en protagonistas visuales."),
            ("Masividad", "Muchos edificios transmiten una sensación visual de peso y solidez."),
            ("Repetición", "Es común encontrar módulos o elementos estructurales repetidos."),
            ("Funcionalidad", "La organización espacial suele estar relacionada con la función del edificio.")
        ],
        "obra": "Unité d'Habitation de Marsella",
        "obra_info": "Diseñada por Le Corbusier y terminada en 1952, la Unité d'Habitation combina viviendas, circulación, servicios y espacios comunes en una gran estructura de hormigón.",
        "arquitectos": "Le Corbusier fue una figura central de la arquitectura moderna y una referencia fundamental para el desarrollo del brutalismo.",
        "reconocer": [
            "Busca grandes superficies de hormigón expuesto.",
            "Observa grandes volúmenes geométricos.",
            "Identifica repetición de módulos.",
            "Observa si la estructura forma parte importante de la estética.",
            "Busca una expresión directa de los materiales."
        ],
        "dato": "La expresión francesa béton brut significa 'hormigón en bruto' y está relacionada con el origen del término brutalismo.",
        "pregunta": "¿Qué material está especialmente asociado con el brutalismo?",
        "opciones": ["Hormigón", "Papel", "Mármol exclusivamente", "Madera exclusivamente"],
        "respuesta": "Hormigón",
        "fuentes": [
            ("UNESCO — The Architectural Work of Le Corbusier", "https://whc.unesco.org/en/list/1321/"),
            ("Tate — Brutalism", "https://www.tate.org.uk/art/art-terms/b/brutalism")
        ]
    },

    "Moderno": {
        "nombre": "Arquitectura Moderna",
        "icono": "◫",
        "periodo": "Finales del siglo XIX · siglo XX",
        "descripcion": "Una transformación arquitectónica basada en nuevas tecnologías, materiales, funcionalidad y formas más simples.",
        "historia": "A finales del siglo XIX y durante el siglo XX, el desarrollo del acero, el hormigón armado y el vidrio permitió nuevas formas de construir. Los arquitectos modernos cuestionaron muchos elementos tradicionales y buscaron nuevas soluciones espaciales. Movimientos como la Bauhaus y el Estilo Internacional tuvieron gran influencia.",
        "materiales": "Acero, hormigón armado y vidrio fueron fundamentales, acompañados por ladrillo, piedra, aluminio y otros materiales industriales.",
        "caracteristicas": [
            ("Funcionalidad", "El diseño se relaciona directamente con las necesidades y funciones del edificio."),
            ("Hormigón armado", "Permitió nuevas posibilidades estructurales y espaciales."),
            ("Acero y vidrio", "Facilitaron estructuras más ligeras y grandes superficies acristaladas."),
            ("Planta libre", "La estructura puede permitir mayor libertad en la distribución de los espacios interiores."),
            ("Fachada libre", "La fachada puede tener mayor independencia respecto a la estructura interior."),
            ("Formas simples", "Predominan geometrías limpias y una reducción de la ornamentación tradicional.")
        ],
        "obra": "Villa Savoye",
        "obra_info": "La Villa Savoye fue diseñada por Le Corbusier y Pierre Jeanneret y construida entre 1928 y 1931 en Poissy, Francia. Es una obra fundamental para comprender varias ideas de la arquitectura moderna.",
        "arquitectos": "Le Corbusier, Walter Gropius, Ludwig Mies van der Rohe y Frank Lloyd Wright fueron figuras importantes de la arquitectura moderna, aunque pertenecieron a contextos y corrientes diferentes.",
        "reconocer": [
            "Busca geometrías simples.",
            "Observa el uso de hormigón, acero y vidrio.",
            "Busca grandes ventanas horizontales.",
            "Observa si la distribución espacial parece flexible.",
            "Busca poca ornamentación tradicional."
        ],
        "dato": "La Villa Savoye permite observar varios principios asociados con Le Corbusier: pilotis, planta libre, fachada libre, ventanas horizontales y terraza-jardín.",
        "pregunta": "¿Cuál de estos conceptos está asociado con la arquitectura moderna?",
        "opciones": ["Planta libre", "Arbotantes", "Orden corintio", "Rosetón"],
        "respuesta": "Planta libre",
        "fuentes": [
            ("MoMA — Le Corbusier", "https://www.moma.org/artists/3426"),
            ("Bauhaus Dessau Foundation", "https://bauhaus-dessau.de/en/")
        ]
    },

    "Contemporanea": {
        "nombre": "Arquitectura Contemporánea",
        "icono": "◇",
        "periodo": "Finales del siglo XX · siglo XXI",
        "descripcion": "Un campo diverso que utiliza herramientas digitales, nuevas tecnologías, estrategias ambientales y distintas formas de relacionarse con el contexto.",
        "historia": "La arquitectura contemporánea no constituye un único estilo. Desde finales del siglo XX hasta la actualidad conviven propuestas minimalistas, high-tech, deconstructivistas, bioclimáticas, paramétricas y muchas otras. También ha crecido la importancia de la rehabilitación y reutilización de edificios existentes.",
        "materiales": "Además de hormigón, acero, vidrio y madera, se utilizan sistemas prefabricados, materiales compuestos, tecnologías de fachada y soluciones orientadas a reducir impactos ambientales.",
        "caracteristicas": [
            ("Diseño digital", "El modelado y las herramientas computacionales permiten estudiar y fabricar geometrías complejas."),
            ("Sostenibilidad", "Muchos proyectos incorporan estrategias de eficiencia energética, agua, materiales y relación con el clima."),
            ("Nuevos materiales", "La industria ofrece sistemas y materiales con propiedades específicas para estructura y envolvente."),
            ("Adaptación al contexto", "El edificio puede responder al clima, paisaje, cultura y necesidades de sus usuarios."),
            ("Reutilización", "Rehabilitar edificios existentes puede convertirse en una estrategia arquitectónica y ambiental."),
            ("Diversidad formal", "No existe una única apariencia: diferentes corrientes conviven dentro de la arquitectura contemporánea.")
        ],
        "obra": "Heydar Aliyev Center",
        "obra_info": "Diseñado por Zaha Hadid Architects y terminado en 2012 en Bakú, Azerbaiyán. Su envolvente continua y curvilínea muestra las posibilidades del diseño digital y de los sistemas constructivos contemporáneos.",
        "arquitectos": "Zaha Hadid, Norman Foster, Tadao Ando y Frank Gehry representan aproximaciones muy diferentes dentro de la arquitectura contemporánea.",
        "reconocer": [
            "No busques una única forma: la arquitectura contemporánea es muy diversa.",
            "Observa geometrías complejas o soluciones digitales.",
            "Busca estrategias ambientales o bioclimáticas.",
            "Observa nuevos materiales y sistemas de fachada.",
            "Considera cómo el edificio responde a su contexto."
        ],
        "dato": "La arquitectura contemporánea no debe entenderse como un solo estilo: es un campo donde conviven muchas ideas, tecnologías y posiciones de diseño.",
        "pregunta": "¿Cuál es una característica frecuente en proyectos contemporáneos?",
        "opciones": ["Uso de herramientas digitales", "Arbotantes medievales", "Orden dórico obligatorio", "Frontón triangular obligatorio"],
        "respuesta": "Uso de herramientas digitales",
        "fuentes": [
            ("Zaha Hadid Architects — Heydar Aliyev Center", "https://www.zaha-hadid.com/architecture/heydar-aliyev-center/"),
            ("Royal Institute of British Architects", "https://www.architecture.com/")
        ]
    }
}


# ============================================================
# GUATEMALA
# ============================================================

guatemala = {
    "titulo": "Arquitectura de Guatemala",
    "descripcion": "Patrimonio, historia e identidad guatemalteca.",
    "intro": "Guatemala reúne expresiones arquitectónicas muy distintas: arquitectura maya prehispánica, patrimonio colonial, edificios neoclásicos, arquitectura moderna y propuestas contemporáneas. Sus formas también han estado condicionadas por el clima, los materiales disponibles, los terremotos y las transformaciones sociales.",
    "secciones": [
        ("🏛️", "Arquitectura maya", "Antes de la llegada de los españoles",
         "Las ciudades mayas desarrollaron grandes conjuntos ceremoniales, plazas, templos, palacios y sistemas urbanos. Tikal es uno de los sitios arqueológicos más conocidos y muestra la escala y complejidad alcanzadas por la arquitectura maya."),
        ("⛪", "Arquitectura colonial", "Siglos XVI–XVIII",
         "Antigua Guatemala conserva iglesias, conventos, viviendas y otros edificios vinculados a la época colonial. La arquitectura de la ciudad también refleja adaptaciones relacionadas con la actividad sísmica."),
        ("🏛️", "Arquitectura neoclásica", "Ciudad de Guatemala",
         "Después del traslado de la capital al valle de la Ermita, la nueva ciudad incorporó edificios y espacios urbanos con influencias neoclásicas. El Centro Histórico conserva ejemplos importantes de esta etapa."),
        ("🎭", "Arquitectura moderna", "Siglo XX",
         "Durante el siglo XX aparecieron nuevas formas, materiales y soluciones estructurales. El Centro Cultural Miguel Ángel Asturias es una de las obras más reconocibles de este periodo."),
        ("🌎", "Arquitectura contemporánea", "Siglo XXI",
         "En Guatemala también existen proyectos contemporáneos que combinan concreto, vidrio, acero, madera, estrategias ambientales y nuevas formas de relación con el paisaje y la ciudad.")
    ],
    "fuentes": [
        ("UNESCO — Antigua Guatemala", "https://whc.unesco.org/en/list/65/"),
        ("UNESCO — Tikal National Park", "https://whc.unesco.org/en/list/64/"),
        ("Ministerio de Cultura y Deportes de Guatemala", "https://mcd.gob.gt/")
    ]
}


# ============================================================
# ESTADO DE LA APP
# ============================================================

paginas_validas = {"inicio", "catalogo", "Guatemala", *estilos.keys()}

pagina_url = st.query_params.get("pagina", "inicio")
if pagina_url not in paginas_validas:
    pagina_url = "inicio"

if "pagina" not in st.session_state:
    st.session_state.pagina = pagina_url
elif pagina_url != "inicio" and st.session_state.pagina != pagina_url:
    st.session_state.pagina = pagina_url

if "resultado" not in st.session_state:
    st.session_state.resultado = None

if "estilos_visitados" not in st.session_state:
    st.session_state.estilos_visitados = set()

if "quiz_correctos" not in st.session_state:
    st.session_state.quiz_correctos = set()


def ir_a(nombre):
    st.session_state.pagina = nombre
    st.session_state.resultado = None
    st.query_params["pagina"] = nombre
    st.rerun()


# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

if st.session_state.pagina == "inicio":

    html("""
    <div class="brand">
        <div class="brand-name">
            Náyra<span class="brand-dot">.</span>
        </div>

        <div class="brand-subtitle">
            Explorando la arquitectura a través del tiempo
        </div>

        <div class="color-palette">
            <span class="palette-dot palette-beige"></span>
            <span class="palette-dot palette-blue"></span>
            <span class="palette-dot palette-pink"></span>
            <span class="palette-dot palette-lilac"></span>
            <span class="palette-dot palette-black"></span>
            <span class="palette-dot palette-red"></span>
        </div>
    </div>
    """)

    html("""
    <div class="hero">
        <div class="hero-small">
            Una mirada a la arquitectura
        </div>

        <div class="hero-title">
            Construir también es contar una historia.
        </div>

        <div class="hero-text">
            Náyra es un espacio para descubrir cómo distintas épocas,
            culturas, materiales e ideas transformaron la manera en que
            construimos nuestros espacios.
        </div>

        <div class="hero-building" aria-hidden="true">
            <div class="tower"></div><div class="tower"></div><div class="tower"></div>
            <div class="window w1"></div><div class="window w2"></div>
            <div class="window w3"></div><div class="window w4"></div>
        </div>
    </div>
    """)

    html(f"""
    <div class="stats-grid">
        <div class="stat-card"><div class="stat-number">7</div><div class="stat-label">estilos para explorar</div></div>
        <div class="stat-card"><div class="stat-number">{len(st.session_state.estilos_visitados)}/7</div><div class="stat-label">estilos visitados en esta sesión</div></div>
        <div class="stat-card"><div class="stat-number">{len(st.session_state.quiz_correctos)}/7</div><div class="stat-label">mini retos resueltos correctamente</div></div>
    </div>

    <div class="section-title">
        Explora cuatro grandes estilos
    </div>

    <div class="section-description">
        Empieza por algunos de los estilos fundamentales y después
        continúa explorando otras épocas y corrientes.
    </div>
    """)

    claves = ["Clasico", "Gotico", "Brutalista", "Moderno"]

    html("""
    <div class="carousel-hint">
        <span><strong>Desliza</strong> para explorar</span>
        <span>← &nbsp; arrastra &nbsp; →</span>
    </div>
    """)

    tarjetas = []
    for clave in claves:
        datos = estilos[clave]
        tarjetas.append(f"""
        <a class="arch-card-link" href="?pagina={clave}">
            <div class="arch-icon">{datos["icono"]}</div>
            <div class="arch-title">{datos["nombre"]}</div>
            <div class="arch-description">{datos["descripcion"]}</div>
            <div class="arch-period">{datos["periodo"]}</div>
            <div style="margin-top:18px;color:var(--navy);font-size:.82rem;font-weight:700;">Explorar →</div>
        </a>
        """)

    html('<div class="arch-carousel">' + ''.join(tarjetas) + '</div>')

    html("""
    <div class="info-box">
        <div class="info-title">
            🏗️ ¿Qué encontrarás en Náyra?
        </div>

        <div class="info-text">
            La arquitectura no consiste solamente en observar edificios
            bonitos. Cada construcción refleja una época, una cultura,
            una tecnología y una manera de entender el espacio.
        </div>

        <br>

        <div class="info-list">
            ✓ Historia y contexto<br>
            ✓ Elementos arquitectónicos<br>
            ✓ Materiales y técnicas<br>
            ✓ Obras representativas<br>
            ✓ Arquitectos importantes<br>
            ✓ Guías para reconocer cada estilo<br>
            ✓ Datos interesantes<br>
            ✓ Mini retos para comprobar lo aprendido
        </div>
    </div>
    """)

    col1, col2 = st.columns(2)

    with col1:
        if st.button("✨ Explorar otros estilos", use_container_width=True):
            ir_a("catalogo")

    with col2:
        if st.button("🇬🇹 Conocer la arquitectura de Guatemala", use_container_width=True):
            ir_a("Guatemala")


# ============================================================
# CATÁLOGO DE LOS 7 ESTILOS
# ============================================================

elif st.session_state.pagina == "catalogo":

    if st.button("← Volver a Náyra", key="volver_catalogo"):
        ir_a("inicio")

    html("""
    <div class="section-title">
        🏛️ Explora los 7 estilos
    </div>

    <div class="section-description">
        Una ruta más completa por diferentes momentos de la historia
        de la arquitectura.
    </div>
    """)

    filtro = st.text_input(
        "🔎 Buscar un estilo",
        placeholder="Ej. gótico, moderno, brutalista...",
        key="buscar_estilo"
    ).strip().lower()

    estilos_catalogo = {
        k: v for k, v in estilos.items()
        if not filtro or filtro in v["nombre"].lower() or filtro in v["descripcion"].lower() or filtro in v["periodo"].lower()
    }

    html(f"""
    <div class="carousel-hint">
        <span><strong>{len(estilos_catalogo)}</strong> estilos encontrados</span>
        <span>← &nbsp; desliza &nbsp; →</span>
    </div>
    """)

    if not estilos_catalogo:
        html("""<div class="info-box"><div class="info-title">No encontramos ese estilo</div><div class="info-text">Prueba con palabras como clásico, gótico, renacentista, brutalista, moderno o contemporáneo.</div></div>""")
    else:
        html("""
        <div class="carousel-hint">
            <span><strong>Desliza</strong> para explorar</span>
            <span>← &nbsp; arrastra &nbsp; →</span>
        </div>
        """)

        tarjetas = []
        for clave, datos in estilos_catalogo.items():
            tarjetas.append(f"""
            <a class="arch-card-link" href="?pagina={clave}">
                <div class="arch-icon">{datos["icono"]}</div>
                <div class="arch-title">{datos["nombre"]}</div>
                <div class="arch-description">{datos["descripcion"]}</div>
                <div class="arch-period">{datos["periodo"]}</div>
                <div style="margin-top:18px;color:var(--navy);font-size:.82rem;font-weight:700;">Explorar →</div>
            </a>
            """)

        html('<div class="arch-carousel">' + ''.join(tarjetas) + '</div>')


# ============================================================
# GUATEMALA
# ============================================================

elif st.session_state.pagina == "Guatemala":

    if st.button("← Volver a Náyra", key="volver_guatemala"):
        ir_a("inicio")

    html(f"""
    <div class="detail-header">
        <div class="detail-icon">🇬🇹</div>

        <div class="detail-title">
            {guatemala["titulo"]}
        </div>

        <div class="detail-period">
            {guatemala["descripcion"]}
        </div>

        <div class="detail-description">
            {guatemala["intro"]}
        </div>
    </div>
    """)

    html("""
    <div class="section-title">
        🏛️ Un patrimonio diverso
    </div>

    <div class="section-description">
        Desde las ciudades mayas hasta la arquitectura contemporánea.
    </div>
    """)

    columnas = st.columns(2)

    for i, (icono, titulo, periodo, texto) in enumerate(guatemala["secciones"]):
        with columnas[i % 2]:
            html(f"""
            <div class="feature">
                <div class="arch-icon">{icono}</div>
                <div class="feature-title">{titulo}</div>
                <div class="arch-period">{periodo}</div>
                <div class="feature-text" style="margin-top:12px;">
                    {texto}
                </div>
            </div>
            """)

    html("""
    <div class="info-box">
        <div class="info-title">
            🎭 Una obra que une arquitectura y arte
        </div>

        <div class="info-text">
            El Centro Cultural Miguel Ángel Asturias, inaugurado en 1978,
            es una de las obras modernas más reconocibles de Guatemala.
            Su diseño de Efraín Recinos integra arquitectura, escultura,
            color y referencias a la cultura guatemalteca.
        </div>
    </div>
    """)

    html("""
    <div class="sources">
        <div class="sources-title">📚 Fuentes de consulta</div>
        <div class="sources-text">
            Información histórica y patrimonial basada en fuentes
            institucionales y de organismos culturales.
        </div>
        <br>
    """)

    for nombre, url in guatemala["fuentes"]:
        st.markdown(
            f'• <a href="{url}" target="_blank">{nombre}</a>',
            unsafe_allow_html=True
        )

    html("</div>")


# ============================================================
# PÁGINAS DE LOS ESTILOS
# ============================================================

elif st.session_state.pagina in estilos:

    datos = estilos[st.session_state.pagina]
    orden_estilos = list(estilos.keys())
    indice_estilo = orden_estilos.index(st.session_state.pagina)
    progreso = int(((indice_estilo + 1) / len(orden_estilos)) * 100)
    st.session_state.estilos_visitados.add(st.session_state.pagina)

    html(f"""
    <div class="breadcrumb">Náyra / <strong>{datos["nombre"]}</strong></div>
    <div class="progress-wrap">
        <div class="progress-meta"><span>Ruta de exploración</span><span>{indice_estilo + 1} de {len(orden_estilos)}</span></div>
        <div class="progress-track"><div class="progress-fill" style="width:{progreso}%;"></div></div>
    </div>
    """)

    if st.button("← Volver a Náyra", key="volver"):
        ir_a("inicio")

    html(f"""
    <div class="detail-header">

        <div class="detail-icon">
            {datos["icono"]}
        </div>

        <div class="detail-title">
            {datos["nombre"]}
        </div>

        <div class="detail-period">
            {datos["periodo"]}
        </div>

        <div class="detail-description">
            {datos["descripcion"]}
        </div>

    </div>
    """)

    html("""
    <div class="section-title">
        📜 Historia y contexto
    </div>

    <div class="section-description">
        Conoce el contexto en el que apareció este estilo y por qué
        llegó a tener importancia.
    </div>
    """)

    html(f"""
    <div class="info-box">
        <div class="info-title">
            ¿De dónde viene este estilo?
        </div>

        <div class="info-text">
            {datos["historia"]}
        </div>
    </div>
    """)

    html("""
    <br>

    <div class="section-title">
        🧱 Materiales y construcción
    </div>

    <div class="section-description">
        Los materiales disponibles y las técnicas constructivas
        también influyen en la forma de un edificio.
    </div>
    """)

    html(f"""
    <div class="info-box">
        <div class="info-title">
            ¿Con qué se construía?
        </div>

        <div class="info-text">
            {datos["materiales"]}
        </div>
    </div>
    """)

    html("""
    <br>

    <div class="section-title">
        📐 Características principales
    </div>

    <div class="section-description">
        Estos elementos ayudan a identificar el estilo arquitectónico.
    </div>
    """)

    columnas = st.columns(2)

    for i, (titulo, descripcion) in enumerate(datos["caracteristicas"]):
        with columnas[i % 2]:
            html(f"""
            <div class="feature">
                <div class="feature-title">{titulo}</div>
                <div class="feature-text">{descripcion}</div>
            </div>
            """)

    html(f"""
    <div class="work">

        <div class="work-label">
            Obra representativa
        </div>

        <div class="work-title">
            {datos["obra"]}
        </div>

        <div class="work-text">
            {datos["obra_info"]}
        </div>

        <div class="work-text" style="margin-top:14px;">
            <strong>Arquitectos:</strong> {datos["arquitectos"]}
        </div>

    </div>
    """)

    html("""
    <div class="section-title">
        🔎 ¿Cómo reconocerlo?
    </div>

    <div class="section-description">
        Algunas pistas que puedes buscar cuando observes un edificio.
    </div>
    """)

    for elemento in datos["reconocer"]:
        html(f"""
        <div class="feature">
            <div class="feature-text">
                ✓ &nbsp; {elemento}
            </div>
        </div>
        """)

    html(f"""
    <div class="fact">

        <div class="fact-title">
            💡 ¿Sabías que?
        </div>

        <div class="fact-text">
            {datos["dato"]}
        </div>

    </div>
    """)

    html("""
    <div class="quiz-header">

        <div class="quiz-title">
            🧠 Mini reto
        </div>

        <div class="quiz-description">
            Comprueba cuánto aprendiste sobre este estilo.
        </div>

    </div>
    """)

    respuesta = st.radio(
        datos["pregunta"],
        datos["opciones"],
        key=f"pregunta_{st.session_state.pagina}"
    )

    if st.button(
        "Comprobar respuesta",
        key=f"comprobar_{st.session_state.pagina}"
    ):
        if respuesta == datos["respuesta"]:
            st.session_state.resultado = "correcto"
            st.session_state.quiz_correctos.add(st.session_state.pagina)
        else:
            st.session_state.resultado = "incorrecto"
            st.session_state.quiz_correctos.discard(st.session_state.pagina)

    if st.session_state.resultado == "correcto":
        st.success(
            "✓ ¡Correcto! Has identificado una característica importante de este estilo."
        )

    elif st.session_state.resultado == "incorrecto":
        st.error(
            f"✕ No exactamente. La respuesta correcta es: {datos['respuesta']}"
        )

    html("""
    <div class="sources">

        <div class="sources-title">
            📚 Fuentes de consulta
        </div>

        <div class="sources-text">
            Información histórica y arquitectónica basada en
            fuentes institucionales, museísticas y educativas.
        </div>

        <br>
    """)

    for nombre, url in datos["fuentes"]:
        st.markdown(
            f'• <a href="{url}" target="_blank">{nombre}</a>',
            unsafe_allow_html=True
        )

    html("</div>")

    anterior = orden_estilos[indice_estilo - 1] if indice_estilo > 0 else None
    siguiente = orden_estilos[indice_estilo + 1] if indice_estilo < len(orden_estilos) - 1 else None

    html(f"""
    <div class="next-nav">
        <div class="next-nav-title">Continúa explorando</div>
        <div class="next-nav-name">{estilos[siguiente]["icono"] + " " + estilos[siguiente]["nombre"] if siguiente else "Has llegado al final de la ruta"}</div>
    </div>
    """)

    nav_cols = st.columns(2)
    with nav_cols[0]:
        if anterior and st.button(f"← {estilos[anterior]["nombre"]}", key=f"prev_{st.session_state.pagina}", use_container_width=True):
            ir_a(anterior)
    with nav_cols[1]:
        if siguiente and st.button(f"{estilos[siguiente]["nombre"]} →", key=f"next_{st.session_state.pagina}", use_container_width=True):
            ir_a(siguiente)


# ============================================================
# FOOTER
# ============================================================

html("""
<div class="nayra-footer">
    <strong>Náyra.</strong>
    <br>
    Arquitectura · Historia · Diseño · Conocimiento
    <br><br>
    Donde cada espacio cuenta una historia.
</div>
""")
