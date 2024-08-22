# -*- coding: utf-8 -*-
"""
@file    : 1_🔴_Grabar.py
@brief   : Handles exam recording
@date    : 2024/08/22
@version : 1.0.0
@author  : Lucas Cortés.
@contact : lucas.cortes@lanek.cl.
"""

import streamlit as st

from source.functions import clear_page, rut_input, set_form

clear_page('Grabar')


def main():
    st.markdown('# 🔴 Grabar Examen')
    rut_input()
    set_form()


if __name__ == '__main__':
    main()
