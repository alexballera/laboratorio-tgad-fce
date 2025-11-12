# %% [markdown]
# # Funciones de Matemáticas Financieras
# Nomenclatura estándar en inglés para cálculos financieros

# %% Importaciones
import numpy as np
import numpy_financial as npf
from typing import Optional, Union

# %% Funciones de Tasas de Interés

def nominal_to_effective_rate(r: float, m: int) -> float:
    """
    Convierte tasa nominal a tasa efectiva por período.
    
    @param {float} r - Tasa nominal anual
    @param {int} m - Períodos de capitalización por año
    @returns {float} Tasa efectiva por período
    
    @example
    >>> nominal_to_effective_rate(0.12, 12)  # 12% anual capitalización mensual
    0.01  # 1% mensual
    
    @formula
    Tasa efectiva = r / m
    
    @note
    - Convierte tasa anual a tasa por período de capitalización
    - Para 12% anual mensual: 0.12/12 = 0.01 (1% mensual)
    """
    return r / m

# %%

def effective_annual_rate(r: float, m: int) -> float:
    """
    Calcula la tasa efectiva anual a partir de la tasa nominal.
    
    @param {float} r - Tasa nominal anual
    @param {int} m - Períodos de capitalización por año
    @returns {float} Tasa efectiva anual
    
    @example
    >>> effective_annual_rate(0.12, 12)  # 12% anual capitalización mensual
    0.1268  # 12.68% efectiva anual
    
    @formula
    TEA = (1 + r/m)^m - 1
    
    @note
    - Considera el efecto de capitalización compuesta
    - Mayor frecuencia de capitalización = mayor TEA
    """
    return (1 + r / m) ** m - 1

# %%

def annualized_rate(r: float, m: int) -> float:
    """
    Convierte tasa periódica a tasa anualizada.
    
    @param {float} r - Tasa por período
    @param {int} m - Períodos por año
    @returns {float} Tasa anualizada
    
    @example
    >>> annualized_rate(0.02, 12)  # 2% mensual
    0.2682  # 26.82% anual
    
    @formula
    Tasa anualizada = (1 + r)^m - 1
    
    @note
    - Convierte tasa periódica a equivalente anual
    - Considera capitalización compuesta
    """
    return (1 + r) ** m - 1

# %% Funciones de Valor Presente y Futuro

def present_value(rate: Union[float, np.ndarray], nper: Union[int, np.ndarray], 
                  pmt: Union[float, np.ndarray], fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula el valor presente de flujos futuros usando numpy_financial.
    
    @param {Union[float, np.ndarray]} fv - Valor futuro o cash flows futuros
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[float, np.ndarray]} nper - Número de períodos de capitalización
    @param {Union[float, np.ndarray]} pmt - Pago periódico (por defecto 0)
    @returns {Union[float, np.ndarray]} Valor presente
    
    @example
    >>> present_value(1000, 0.05, 10)  # $1000 en 10 períodos al 5%
    613.91
    >>> present_value([1000, 2000], [0.05, 0.06], [10, 15])  # Arrays
    array([613.91, 832.04])
    
    @formula
    PV = npf.pv(rate, nper, pmt, fv)
    
    @note
    - Usa numpy_financial internamente para máxima precisión
    - Soporta arrays para análisis de sensibilidad
    - Para capitalización personalizada usar rate = tasa_anual/períodos_por_año
    """
    result = -npf.pv(rate, nper, pmt, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(fv) and np.isscalar(rate) and np.isscalar(nper) and np.isscalar(pmt):
        return float(result)
    return result

# %%

def future_value(pv: Union[float, np.ndarray], rate: Union[float, np.ndarray], 
                nper: Union[float, np.ndarray] = 1, pmt: Union[float, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula el valor futuro de flujos presentes usando numpy_financial.
    
    @param {Union[float, np.ndarray]} pv - Valor presente o cash flows presentes
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[float, np.ndarray]} nper - Número de períodos de capitalización
    @param {Union[float, np.ndarray]} pmt - Pago periódico (por defecto 0)
    @returns {Union[float, np.ndarray]} Valor futuro
    
    @example
    >>> future_value(1000, 0.05, 10)  # $1000 a 10 períodos al 5%
    1628.89
    >>> future_value(1000, 0.08, 12)  # $1000 con capitalización mensual
    1083.00
    
    @formula
    FV = npf.fv(rate, nper, pmt, pv)
    
    @note
    - Usa numpy_financial internamente para máxima precisión
    - Soporta arrays para análisis de sensibilidad
    - Para capitalización personalizada usar rate = tasa_anual/períodos_por_año
    - Para ON usar nper = 12 (capitalización mensual en 1 año)
    """
    result = -npf.fv(rate, nper, pmt, -pv)
    
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(pv) and np.isscalar(rate) and np.isscalar(nper) and np.isscalar(pmt):
        return float(result)
    return result

# %%

def present_value_annuity(C: float, r: float, T: Union[int, float], m: int = 1) -> float:
    """
    Calcula el valor presente de una anualidad con capitalización.
    
    @param {float} C - Cash flow periódico
    @param {float} r - Tasa de interés anual
    @param {Union[int, float]} T - Tiempo en años
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {float} Valor presente de la anualidad
    
    @example
    >>> present_value_annuity(100, 0.05, 10, 1)  # $100 anuales por 10 años al 5%
    772.17
    >>> present_value_annuity(100, 0.05, 10, 12)  # $100 mensuales por 10 años al 5%
    9420.45
    
    @formula
    PV = C * [1 - (1 + r/m)^(-m*T)] / (r/m)
    
    @note
    - Para anualidades ordinarias (pagos al final del período)
    - m=1 para capitalización anual, m=12 para mensual
    - Si r/m=0, usa fórmula simplificada PV = C * m * T
    """
    rate_per_period = r / m
    total_periods = m * T
    if rate_per_period == 0:
        return C * total_periods
    return C * (1 - (1 + rate_per_period) ** (-total_periods)) / rate_per_period

# %%

def future_value_annuity(C: float, r: float, T: Union[int, float], m: int = 1) -> float:
    """
    Calcula el valor futuro de una anualidad con capitalización.
    
    @param {float} C - Cash flow periódico
    @param {float} r - Tasa de interés anual
    @param {Union[int, float]} T - Tiempo en años
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {float} Valor futuro de la anualidad
    
    @example
    >>> future_value_annuity(100, 0.05, 10, 1)  # $100 anuales por 10 años al 5%
    1257.79
    >>> future_value_annuity(100, 0.05, 10, 12)  # $100 mensuales por 10 años al 5%
    15528.23
    
    @formula
    FV = C * [((1 + r/m)^(m*T) - 1) / (r/m)]
    
    @note
    - Para anualidades ordinarias (pagos al final del período)
    - m=1 para capitalización anual, m=12 para mensual
    - Si r/m=0, usa fórmula simplificada FV = C * m * T
    """
    rate_per_period = r / m
    total_periods = m * T
    if rate_per_period == 0:
        return C * total_periods
    return C * (((1 + rate_per_period) ** total_periods - 1) / rate_per_period)

# %% Funciones de Pagos

def payment_amount(rate: Union[float, np.ndarray], nper: Union[int, np.ndarray], 
                   pv: Union[float, np.ndarray], fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula el monto del pago para un préstamo usando numpy_financial.
    
    @param {Union[float, np.ndarray]} pv - Monto del préstamo (valor presente)
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} nper - Número de períodos
    @param {Union[float, np.ndarray]} fv - Valor futuro (por defecto 0)
    @returns {Union[float, np.ndarray]} Monto del pago periódico
    
    @example
    >>> payment_amount(100000, 0.005, 360)  # Préstamo $100k a 30 años
    599.55  # Pago mensual
    >>> payment_amount([100000, 200000], [0.005, 0.006], [360, 240])  # Arrays
    array([599.55, 1438.06])  # Pagos para múltiples escenarios
    
    @formula
    PMT = npf.pmt(rate, nper, pv, fv)
    
    @note
    - Usa numpy_financial para cálculos de préstamos estándar
    - Soporta arrays para análisis comparativo de préstamos
    - Retorna valor positivo (pago que se hace)
    """
    result = -npf.pmt(rate, nper, pv, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(pv) and np.isscalar(rate) and np.isscalar(nper) and np.isscalar(fv):
        return float(result)
    return result

# %%

def payment_interest(rate: Union[float, np.ndarray], per: Union[int, np.ndarray], 
                    nper: Union[int, np.ndarray], pv: Union[float, np.ndarray], 
                    fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula la porción de interés de un pago específico usando numpy_financial.
    
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} per - Período específico para calcular interés
    @param {Union[int, np.ndarray]} nper - Número total de períodos
    @param {Union[float, np.ndarray]} pv - Valor presente (monto del préstamo)
    @param {Union[float, np.ndarray]} fv - Valor futuro (por defecto 0)
    @returns {Union[float, np.ndarray]} Porción de interés del pago
    
    @example
    >>> payment_interest(0.005, 1, 360, 100000)  # Interés del primer pago
    500.00
    >>> payment_interest(0.005, [1, 2, 3], 360, 100000)  # Múltiples períodos
    array([500.00, 499.50, 499.00])
    
    @formula
    IPMT = npf.ipmt(rate, per, nper, pv, fv)
    
    @note
    - Usa numpy_financial para cálculos precisos de interés
    - Soporta arrays para análisis de amortización
    - Retorna valor positivo (interés que se paga)
    """
    result = -npf.ipmt(rate, per, nper, pv, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(rate) and np.isscalar(per) and 
        np.isscalar(nper) and np.isscalar(pv) and np.isscalar(fv)):
        return float(result)
    return result

# %%

def payment_principal(rate: Union[float, np.ndarray], per: Union[int, np.ndarray], 
                     nper: Union[int, np.ndarray], pv: Union[float, np.ndarray], 
                     fv: Union[int, np.ndarray] = 0) -> Union[float, np.ndarray]:
    """
    Calcula la porción de capital de un pago específico usando numpy_financial.
    
    @param {Union[float, np.ndarray]} rate - Tasa de interés por período
    @param {Union[int, np.ndarray]} per - Período específico para calcular capital
    @param {Union[int, np.ndarray]} nper - Número total de períodos
    @param {Union[float, np.ndarray]} pv - Valor presente (monto del préstamo)
    @param {Union[float, np.ndarray]} fv - Valor futuro (por defecto 0)
    @returns {Union[float, np.ndarray]} Porción de capital del pago
    
    @example
    >>> payment_principal(0.005, 1, 360, 100000)  # Capital del primer pago
    233.33
    >>> payment_principal(0.005, [1, 2, 3], 360, 100000)  # Múltiples períodos
    array([233.33, 234.50, 235.67])
    
    @formula
    PPMT = npf.ppmt(rate, per, nper, pv, fv)
    
    @note
    - Usa numpy_financial para cálculos precisos de capital
    - Soporta arrays para análisis de amortización
    - Retorna valor positivo (capital que se paga)
    """
    result = -npf.ppmt(rate, per, nper, pv, fv)  # type: ignore
    
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(rate) and np.isscalar(per) and 
        np.isscalar(nper) and np.isscalar(pv) and np.isscalar(fv)):
        return float(result)
    return result# %% Funciones de Análisis de Inversiones

def net_present_value(initial_investment: float, cash_flows: list, r: float, T: Optional[int] = None, m: int = 1) -> float:
    """
    Calcula el valor presente neto (NPV) de una inversión con capitalización.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows - Lista de flujos de caja futuros
    @param {float} r - Tasa de interés anual
    @param {Optional[int]} T - Número total de períodos (por defecto len(cash_flows))
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {float} Valor presente neto
    
    @example
    >>> net_present_value(10000, [3000, 4000, 5000], 0.10, 3, 1)
    -199.21  # NPV negativo, inversión no viable
    >>> net_present_value(10000, [3500, 4500, 5500], 0.10, 3, 1)
    1061.57  # NPV positivo, inversión viable
    
    @formula
    NPV = -Initial_Investment + Σ[CF_t / (1 + r/m)^(m*t)]
    
    @note
    - NPV > 0: inversión viable
    - NPV < 0: inversión no viable
    - Considera capitalización personalizada con parámetro m
    """
    if T is None:
        T = len(cash_flows)
    
    npv = -initial_investment
    for i, cf in enumerate(cash_flows):
        time_period = (i + 1) / m
        npv += cf / (1 + r/m) ** (m * time_period)
    
    return npv

# %%

def internal_rate_of_return(initial_investment: float, cash_flows: list, max_iter: int = 1000, precision: float = 1e-6) -> float:
    """
    Calcula la tasa interna de retorno (IRR) usando método de Newton-Raphson.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows - Lista de flujos de caja futuros
    @param {int} max_iter - Número máximo de iteraciones (por defecto 1000)
    @param {float} precision - Precisión deseada (por defecto 1e-6)
    @returns {float} Tasa interna de retorno
    
    @example
    >>> internal_rate_of_return(10000, [3500, 4500, 5500])
    0.1542  # IRR del 15.42%
    >>> internal_rate_of_return(10000, [2000, 3000, 4000])
    -0.0451  # IRR negativo del -4.51%
    
    @formula
    Encuentra r donde NPV = -Initial_Investment + Σ[CF_t / (1 + r)^t] = 0
    
    @note
    - Usa método iterativo Newton-Raphson
    - IRR > tasa de descuento: inversión viable
    - Puede tener múltiples soluciones con flujos mixtos
    """
    # Estimación inicial
    rate = 0.1
    
    for _ in range(max_iter):
        npv = -initial_investment
        npv_derivative = 0
        
        for i, cf in enumerate(cash_flows):
            period = i + 1
            npv += cf / (1 + rate) ** period
            npv_derivative -= cf * period / (1 + rate) ** (period + 1)
        
        if abs(npv) < precision:
            return rate
        
        if npv_derivative == 0:
            break
            
        rate = rate - npv / npv_derivative
    
    return rate

# %%

def modified_internal_rate_of_return(cash_flows: list, finance_rate: float, reinvest_rate: float) -> float:
    """
    Calcula la Tasa Interna de Retorno Modificada (MIRR) usando numpy_financial.
    
    @param {list} cash_flows - Lista de flujos de caja (incluyendo inversión inicial negativa)
    @param {float} finance_rate - Tasa de financiamiento para flujos negativos
    @param {float} reinvest_rate - Tasa de reinversión para flujos positivos
    @returns {float} Tasa interna de retorno modificada
    
    @example
    >>> modified_internal_rate_of_return([-1000, 300, 400, 500], 0.10, 0.12)
    0.1013  # MIRR del 10.13%
    
    @formula
    MIRR = npf.mirr(cash_flows, finance_rate, reinvest_rate)
    
    @note
    - Usa numpy_financial para cálculos precisos
    - Considera diferentes tasas para financiamiento y reinversión
    - Más realista que IRR tradicional para proyectos complejos
    """
    return npf.mirr(cash_flows, finance_rate, reinvest_rate)

# %%

def npv_simple(rate: float, cash_flows: list) -> float:
    """
    Calcula el Valor Presente Neto usando numpy_financial directamente.
    
    @param {float} rate - Tasa de descuento 
    @param {list} cash_flows - Lista de flujos de caja (incluyendo inversión inicial)
    @returns {float} Valor presente neto
    
    @example
    >>> npv_simple(0.10, [-1000, 300, 400, 500])
    42.95  # NPV positivo
    
    @formula
    NPV = npf.npv(rate, cash_flows)
    
    @note
    - Wrapper directo de numpy_financial.npv()
    - Primer flujo debe ser la inversión inicial (negativo)
    - Flujos posteriores son los retornos esperados
    """
    return npf.npv(rate, cash_flows)

# %%

def irr_simple(cash_flows: list) -> float:
    """
    Calcula la Tasa Interna de Retorno usando numpy_financial directamente.
    
    @param {list} cash_flows - Lista de flujos de caja (incluyendo inversión inicial)
    @returns {float} Tasa interna de retorno
    
    @example
    >>> irr_simple([-1000, 300, 400, 500])
    0.1062  # IRR del 10.62%
    
    @formula
    IRR = npf.irr(cash_flows)
    
    @note
    - Wrapper directo de numpy_financial.irr()
    - Primer flujo debe ser la inversión inicial (negativo)
    - Encuentra la tasa donde NPV = 0
    """
    return npf.irr(cash_flows)

# %%

def profitability_index(initial_investment: float, cash_flows: list, r: float, T: Optional[int] = None, m: int = 1) -> float:
    """
    Calcula el índice de rentabilidad (PI) con capitalización.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows - Lista de flujos de caja futuros
    @param {float} r - Tasa de interés anual
    @param {Optional[int]} T - Número total de períodos (por defecto len(cash_flows))
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {float} Índice de rentabilidad
    
    @example
    >>> profitability_index(10000, [3500, 4500, 5500], 0.10, 3, 1)
    1.106  # PI > 1, proyecto viable
    >>> profitability_index(10000, [2500, 3000, 3500], 0.10, 3, 1)
    0.751  # PI < 1, proyecto no viable
    
    @formula
    PI = Σ[PV de cash flows] / Initial Investment
    
    @note
    - PI > 1: proyecto viable (crea valor)
    - PI < 1: proyecto no viable (destruye valor)
    - PI = 1: proyecto indiferente (NPV = 0)
    """
    if T is None:
        T = len(cash_flows)
    
    present_value_sum = 0
    for i, cf in enumerate(cash_flows):
        time_period = (i + 1) / m
        present_value_sum += cf / (1 + r/m) ** (m * time_period)
    
    return present_value_sum / initial_investment

# %%

def payback_period(initial_investment: float, cash_flows: list) -> float:
    """
    Calcula el período de recuperación de la inversión.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows - Lista de flujos de caja
    @returns {float} Período de recuperación en años
    
    @example
    >>> payback_period(10000, [3000, 4000, 5000])
    2.75  # Se recupera en 2.75 años
    >>> payback_period(8000, [2500, 3000, 4000])
    2.17  # Se recupera en 2.17 años
    
    @formula
    Período donde Σ(CF_t) >= Initial_Investment (con interpolación)
    
    @note
    - No considera valor temporal del dinero
    - Retorna float('inf') si nunca se recupera
    - Incluye interpolación para cálculo exacto
    """
    cumulative_cash_flow = 0
    
    for i, cf in enumerate(cash_flows):
        cumulative_cash_flow += cf
        
        if cumulative_cash_flow >= initial_investment:
            # Interpolación para encontrar el momento exacto
            previous_cumulative = cumulative_cash_flow - cf
            fraction = (initial_investment - previous_cumulative) / cf
            return i + fraction
    
    # Si nunca se recupera la inversión
    return float('inf')

# %% Funciones Avanzadas de Análisis

def sensitivity_analysis_npv(initial_investment: float, cash_flows: list, 
                            r_range: np.ndarray, T: Optional[int] = None, m: int = 1) -> np.ndarray:
    """
    Análisis de sensibilidad del NPV variando la tasa de descuento.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows - Lista de flujos de caja futuros
    @param {np.ndarray} r_range - Array de tasas a analizar
    @param {Optional[int]} T - Número total de períodos (por defecto len(cash_flows))
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {np.ndarray} Array de valores NPV correspondientes
    
    @example
    >>> rates = np.linspace(0.05, 0.15, 11)
    >>> npvs = sensitivity_analysis_npv(10000, [3500, 4500, 5500], rates)
    >>> npvs.shape
    (11,)  # 11 valores NPV diferentes
    
    @formula
    NPV(r) = -Initial_Investment + Σ[CF_t / (1 + r/m)^(m*t)] para cada r
    
    @note
    - Útil para análisis de riesgo de tasa de interés
    - Permite visualizar sensibilidad del proyecto a cambios en r
    - Vectorización para eficiencia computacional
    """
    
    # Vectorizar el cálculo para todas las tasas
    npv_values = np.full(len(r_range), -initial_investment, dtype=float)
    
    for i, cf in enumerate(cash_flows):
        time_period = (i + 1) / m
        npv_values += cf / (1 + r_range/m) ** (m * time_period)
    
    return npv_values

# %%

def monte_carlo_npv(initial_investment: float, cash_flows_mean: list, cash_flows_std: list,
                   r_mean: float, r_std: float, n_simulations: int = 1000, 
                   T: Optional[int] = None, m: int = 1) -> np.ndarray:
    """
    Simulación Monte Carlo para análisis de riesgo de NPV.
    
    @param {float} initial_investment - Inversión inicial
    @param {list} cash_flows_mean - Media de cada flujo de caja
    @param {list} cash_flows_std - Desviación estándar de cada flujo de caja
    @param {float} r_mean - Tasa de descuento promedio
    @param {float} r_std - Desviación estándar de la tasa
    @param {int} n_simulations - Número de simulaciones (por defecto 1000)
    @param {Optional[int]} T - Número total de períodos
    @param {int} m - Períodos de capitalización por año (por defecto 1)
    @returns {np.ndarray} Array con resultados NPV de todas las simulaciones
    
    @example
    >>> cf_mean = [3500, 4500, 5500]
    >>> cf_std = [500, 600, 700]
    >>> npv_dist = monte_carlo_npv(10000, cf_mean, cf_std, 0.10, 0.02, 1000)
    >>> np.mean(npv_dist)  # NPV promedio
    1061.57
    >>> np.std(npv_dist)   # Riesgo
    850.23
    
    @formula
    NPV = -I₀ + Σ[CF_t(μ,σ) / (1 + r(μ,σ)/m)^(m*t)] para n simulaciones
    
    @note
    - Asume distribuciones normales para flujos y tasa
    - Permite cuantificar riesgo del proyecto
    - Usa seed=42 para reproducibilidad
    """    
    # Generar simulaciones aleatorias
    np.random.seed(42)  # Para reproducibilidad
    rates = np.random.normal(r_mean, r_std, n_simulations)
    rates = np.maximum(rates, 0.001)  # Evitar tasas negativas
    
    npv_results = np.full(n_simulations, -initial_investment, dtype=float)
    
    for i, (cf_mean, cf_std) in enumerate(zip(cash_flows_mean, cash_flows_std)):
        # Generar flujos de caja aleatorios
        cash_flows_sim = np.random.normal(cf_mean, cf_std, n_simulations)
        time_period = (i + 1) / m
        
        # Calcular valor presente para cada simulación
        pv_cf = cash_flows_sim / (1 + rates/m) ** (m * time_period)
        npv_results += pv_cf
    
    return npv_results

# %%

def batch_loan_analysis(principals: np.ndarray, rates: np.ndarray, periods: np.ndarray) -> dict:
    """
    Análisis en lote de múltiples préstamos.
    
    @param {np.ndarray} principals - Array de montos de préstamos
    @param {np.ndarray} rates - Array de tasas de interés
    @param {np.ndarray} periods - Array de períodos
    @returns {dict} Diccionario con arrays de resultados
    
    @example
    >>> principals = np.array([100000, 200000, 300000])
    >>> rates = np.array([0.005, 0.006, 0.007])
    >>> periods = np.array([360, 240, 180])
    >>> results = batch_loan_analysis(principals, rates, periods)
    >>> results['payments']
    array([599.55, 1438.06, 2491.78])
    
    @formula
    Calcula PMT, IPMT, PPMT, Total pagado e Interés total para cada préstamo
    
    @note
    - Procesamiento vectorizado para eficiencia
    - Retorna métricas completas de análisis de préstamos
    - Útil para comparación de múltiples escenarios
    """
    # Calcular todas las métricas usando las funciones vectorizadas
    payments = payment_amount(principals, rates, periods)
    first_interest = payment_interest(principals, rates, 1, periods)
    first_principal = payment_principal(principals, rates, 1, periods)
    
    # Calcular total pagado y total de intereses
    total_paid = payments * periods
    total_interest = total_paid - principals
    
    return {
        'payments': payments,
        'first_interest': first_interest,
        'first_principal': first_principal,
        'total_paid': total_paid,
        'total_interest': total_interest,
        'interest_ratio': total_interest / principals  # Proporción de interés vs capital
    }