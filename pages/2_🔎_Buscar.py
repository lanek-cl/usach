# -*- coding: utf-8 -*-
"""
@file    : 2_🔎_Buscar.py
@brief   : Handles exam search
@date    : 2024/08/22
@version : 1.0.0
@author  : Lucas Cortés.
@contact : lucas.cortes@lanek.cl.
"""

import streamlit as st

from source.functions import clear_page, rut_input, search_input

clear_page('Buscar')


def main():
    st.markdown('# 🔎 Buscar Examen')
    rut_input(False)
    search_input()


if __name__ == '__main__':
    main()
