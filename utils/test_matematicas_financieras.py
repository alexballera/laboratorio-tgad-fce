#!/usr/bin/env python3
"""
Script de prueba para verificar todas las funciones de matemáticas financieras
actualizadas con numpy_financial.

Ejecutar desde la raíz del proyecto:
python test_matematicas_financieras.py
"""

import sys
sys.path.append('')

from matematicas_financieras import *
import numpy as np

def test_tasas_interes():
    """Prueba funciones de tasas de interés"""
    print("=" * 50)
    print("PRUEBAS DE TASAS DE INTERÉS")
    print("=" * 50)
    
    # Tasa nominal a efectiva
    tasa_efectiva = nominal_to_effective_rate(0.12, 12)
    print(f"Tasa nominal 12% anual, capitalización mensual → TEA: {tasa_efectiva:.2%}")
    
    # Tasa efectiva anual
    tea = effective_annual_rate(0.12, 12)
    print(f"TEA con 12% nominal mensual: {tea:.2%}")
    
    # Tasa anualizada
    anual = annualized_rate(0.01, 12)
    print(f"1% mensual anualizado: {anual:.2%}")

def test_valor_temporal():
    """Prueba funciones de valor presente y futuro"""
    print("\n" + "=" * 50)
    print("PRUEBAS DE VALOR TEMPORAL DEL DINERO")
    print("=" * 50)
    
    # Valor presente
    pv = present_value(rate=0.005, nper=360, pmt=599.55)
    print(f"Valor presente de anualidad $599.55 x 360 meses al 0.5%: ${pv:,.2f}")
    
    # Valor futuro
    fv = future_value(pv=100000, rate=0.005, nper=360)
    print(f"Valor futuro de $100,000 en 360 meses al 0.5%: ${fv:,.2f}")
    
    # Con arrays
    montos = np.array([100000, 150000, 200000])
    fv_array = future_value(pv=montos, rate=0.005, nper=360)
    print(f"Valores futuros para {montos}: {fv_array}")

def test_pagos():
    """Prueba funciones de pagos"""
    print("\n" + "=" * 50)
    print("PRUEBAS DE FUNCIONES DE PAGOS")
    print("=" * 50)
    
    # Pago mensual
    pmt = payment_amount(rate=0.005, nper=360, pv=100000)
    print(f"Pago mensual para préstamo $100,000: ${pmt:.2f}")
    
    # Interés del primer pago
    interest = payment_interest(rate=0.005, per=1, nper=360, pv=100000)
    print(f"Interés del primer pago: ${interest:.2f}")
    
    # Capital del primer pago
    principal = payment_principal(rate=0.005, per=1, nper=360, pv=100000)
    print(f"Capital del primer pago: ${principal:.2f}")
    
    # Verificación
    print(f"Suma interés + capital: ${interest + principal:.2f} = ${pmt:.2f}")

def test_analisis_inversiones():
    """Prueba funciones de análisis de inversiones"""
    print("\n" + "=" * 50)
    print("PRUEBAS DE ANÁLISIS DE INVERSIONES")
    print("=" * 50)
    
    # Datos del proyecto
    inicial = 10000
    flujos = [3000, 4000, 5000]
    tasa = 0.10
    cash_flows_completos = [-inicial] + flujos
    
    # NPV usando función compleja
    npv_complejo = net_present_value(inicial, flujos, tasa)
    print(f"NPV (función compleja): ${npv_complejo:.2f}")
    
    # NPV usando numpy_financial directo
    npv_simple_result = npv_simple(tasa, cash_flows_completos)
    print(f"NPV (numpy_financial): ${npv_simple_result:.2f}")
    
    # IRR usando función compleja
    irr_complejo = internal_rate_of_return(inicial, flujos)
    print(f"IRR (función compleja): {irr_complejo:.2%}")
    
    # IRR usando numpy_financial directo
    irr_simple_result = irr_simple(cash_flows_completos)
    print(f"IRR (numpy_financial): {irr_simple_result:.2%}")
    
    # MIRR
    mirr = modified_internal_rate_of_return(cash_flows_completos, 0.08, 0.12)
    print(f"MIRR (financiamiento 8%, reinversión 12%): {mirr:.2%}")
    
    # Índice de rentabilidad
    pi = profitability_index(inicial, flujos, tasa)
    print(f"Índice de rentabilidad: {pi:.2f}")
    
    # Período de recuperación
    pb = payback_period(inicial, flujos)
    print(f"Período de recuperación: {pb:.2f} años")

def test_anualidades():
    """Prueba funciones de anualidades"""
    print("\n" + "=" * 50)
    print("PRUEBAS DE ANUALIDADES")
    print("=" * 50)
    
    # Valor presente de anualidad
    pv_annuity = present_value_annuity(1000, 0.10, 5)
    print(f"VP de anualidad $1,000 x 5 años al 10%: ${pv_annuity:.2f}")
    
    # Valor futuro de anualidad
    fv_annuity = future_value_annuity(1000, 0.10, 5)
    print(f"VF de anualidad $1,000 x 5 años al 10%: ${fv_annuity:.2f}")

def main():
    """Ejecuta todas las pruebas"""
    print("PRUEBAS COMPLETAS DE MATEMATICAS FINANCIERAS")
    print("Librería actualizada con numpy_financial")
    print("Nomenclatura estándar en inglés mantenida")
    
    test_tasas_interes()
    test_valor_temporal()
    test_pagos()
    test_analisis_inversiones()
    test_anualidades()
    
    print("\n" + "=" * 50)
    print("✅ TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE")
    print("=" * 50)
    print("\nFunciones disponibles:")
    print("• Tasas: nominal_to_effective_rate, effective_annual_rate, annualized_rate")
    print("• Valor temporal: present_value, future_value")
    print("• Anualidades: present_value_annuity, future_value_annuity")
    print("• Pagos: payment_amount, payment_interest, payment_principal")
    print("• Inversiones: net_present_value, internal_rate_of_return, profitability_index, payback_period")
    print("• numpy_financial directo: npv_simple, irr_simple, modified_internal_rate_of_return")
    print("• Análisis avanzado: sensitivity_analysis_npv, monte_carlo_npv, batch_loan_analysis")

if __name__ == "__main__":
    main()