# -*- coding: utf-8 -*-
"""
@file    : 👋_Inicio.py
@brief   : Handles welcome page and code update
@date    : 2024/08/22
@version : 1.0.0
@author  : Lucas Cortés.
@contact : lucas.cortes@lanek.cl.
"""

import streamlit as st

from source.functions import (clear_page, run_git_pull, run_pip_install, set_session)

clear_page('Inicio')
set_session()

st.write('# Bienvenido! 👋')

st.sidebar.warning('Selecciona una opción.')

st.markdown("""
    En este programa podrás subir tus **exámenes de EMG**.

    ### Funcionalidades
    - Grabar: Podras iniciar y detener la grabación de exámenes de EMG, TobbyPro y AVM en simultáneo.
    - Buscar: Buscar estos exámenes por RUT y fecha.
    - Procesar: Procesar exámenes de EMG.

""")

verbose = st.sidebar.toggle('Verbose', False)

if st.sidebar.button('Buscar actualizaciones'):
    update = run_git_pull(verbose)
    #if update:
    #    reqs = run_pip_install(verbose)
