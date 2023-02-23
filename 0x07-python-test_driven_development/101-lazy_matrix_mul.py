#!/usr/bin/python3
# -*- coding: utf-8 -*-
from numpy import matmul

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrix
    Args:
        m_a (lists/floats): First matrix
        m_b (lists/floats): second matrix
    Returns:
        The result of multiply m_a by m_b
    """
    return matmul(m_a, m_b)

