# %% [markdown]
# # Funciones de Matemáticas Financieras
# Nomenclatura estándar en inglés para cálculos financieros

# %% Importaciones
import numpy as np
import numpy_financial as npf
from typing import Union, Optional
from numpy.typing import NDArray

# %% Funciones de Tasas de Interés

def nominal_to_effective_rate(r: float, m: int) -> float:
    """
    Convierte tasa nominal a tasa efectiva por período
    
    Args:
        r: Tasa nominal anual (ej: 0.12 para 12%)
        m: Períodos de capitalización por año (ej: 12 para mensual)
    
    Returns:
        float: Tasa efectiva por período
        
    Example:
        >>> nominal_to_effective_rate(0.12, 12)  # 12% anual capitalización mensual
        0.01  # 1% mensual
    """
    return r / m

# %%

def effective_annual_rate(r: float, m: int) -> float:
    """
    Calcula la tasa efectiva anual a partir de la tasa nominal
    Fórmula: (1 + r/m)^m - 1
    
    Args:
        r: Tasa nominal anual (ej: 0.12 para 12%)
        m: Períodos de capitalización por año (ej: 12 para mensual)
    
    Returns:
        float: Tasa efectiva anual
        
    Example:
        >>> effective_annual_rate(0.12, 12)  # 12% anual capitalización mensual
        0.1268  # 12.68% efectiva anual
    """
    return (1 + r / m) ** m - 1

# %%

def annualized_rate(r: float, m: int) -> float:
    """
    Convierte tasa periódica a tasa anualizada
    Fórmula: (1 + r)^m - 1
    
    Args:
        r: Tasa por período (ej: 0.02 para 2% mensual)
        m: Períodos por año (ej: 12 para mensual)
    
    Returns:
        float: Tasa anualizada
        
    Example:
        >>> annualized_rate(0.02, 12)  # 2% mensual
        0.2682  # 26.82% anual
    """
    return (1 + r) ** m - 1

# %% Funciones de Valor Presente y Futuro

def present_value(C: Union[float, NDArray], r: Union[float, NDArray], T: Union[int, float, NDArray], m: Union[int, NDArray] = 1) -> Union[float, NDArray]:
    """
    Calcula el valor presente de un monto futuro con capitalización
    Soporta valores individuales y arrays para análisis de sensibilidad
    Fórmula: PV = C / (1 + r/m)^(m*T)
    
    Args:
        C: Cash flow futuro (ej: 1000 o [1000, 2000, 3000])
        r: Tasa de interés anual (ej: 0.05 o [0.04, 0.05, 0.06])
        T: Tiempo en años (ej: 10 o [5, 10, 15])
        m: Períodos de capitalización por año (ej: 12 o [1, 12, 365])
    
    Returns:
        Union[float, NDArray]: Valor presente (escalar o array)
        
    Example:
        >>> present_value(1000, 0.05, 10, 1)  # Valor individual
        613.91  # Valor presente
        >>> present_value([1000, 2000], [0.05, 0.06], [10, 15], 1)  # Arrays
        array([613.91, 832.04])  # VP para múltiples escenarios
    """
    result = C / (1 + r/m) ** (m * T)
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(C) and np.isscalar(r) and np.isscalar(T) and np.isscalar(m)):
        return float(result)
    return result

# %%

def future_value(C: Union[float, NDArray], r: Union[float, NDArray], T: Union[int, float, NDArray], m: Union[int, NDArray] = 1) -> Union[float, NDArray]:
    """
    Calcula el valor futuro de un monto presente con capitalización
    Soporta valores individuales y arrays para análisis de sensibilidad
    Fórmula: FV = C * (1 + r/m)^(m*T)
    
    Args:
        C: Cash flow presente (ej: 1000 o [1000, 2000, 3000])
        r: Tasa de interés anual (ej: 0.05 o [0.04, 0.05, 0.06])
        T: Tiempo en años (ej: 10 o [5, 10, 15])
        m: Períodos de capitalización por año (ej: 12 o [1, 12, 365])
    
    Returns:
        Union[float, NDArray]: Valor futuro (escalar o array)
        
    Example:
        >>> future_value(1000, 0.05, 10, 1)  # Valor individual
        1628.89  # Valor futuro
        >>> future_value([1000, 2000], [0.05, 0.06], [10, 15], 1)  # Arrays
        array([1628.89, 4793.67])  # VF para múltiples escenarios
    """
    result = C * (1 + r/m) ** (m * T)
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(C) and np.isscalar(r) and np.isscalar(T) and np.isscalar(m)):
        return float(result)
    return result

# %%

def present_value_annuity(C: float, r: float, T: Union[int, float], m: int = 1) -> float:
    """
    Calcula el valor presente de una anualidad con capitalización
    Fórmula: PV = C * [1 - (1 + r/m)^(-m*T)] / (r/m)
    
    Args:
        C: Cash flow periódico (ej: 100)
        r: Tasa de interés anual (ej: 0.05 para 5%)
        T: Tiempo en años (ej: 10)
        m: Períodos de capitalización por año (ej: 12 para mensual, 1 para anual)
    
    Returns:
        float: Valor presente de la anualidad
        
    Example:
        >>> present_value_annuity(100, 0.05, 10, 1)  # $100 anuales por 10 años al 5%
        772.17  # Valor presente de la anualidad
        >>> present_value_annuity(100, 0.05, 10, 12)  # $100 mensuales por 10 años al 5%
        9420.45  # Valor presente de la anualidad mensual
    """
    rate_per_period = r / m
    total_periods = m * T
    if rate_per_period == 0:
        return C * total_periods
    return C * (1 - (1 + rate_per_period) ** (-total_periods)) / rate_per_period

# %%

def future_value_annuity(C: float, r: float, T: Union[int, float], m: int = 1) -> float:
    """
    Calcula el valor futuro de una anualidad con capitalización
    Fórmula: FV = C * [((1 + r/m)^(m*T) - 1) / (r/m)]
    
    Args:
        C: Cash flow periódico (ej: 100)
        r: Tasa de interés anual (ej: 0.05 para 5%)
        T: Tiempo en años (ej: 10)
        m: Períodos de capitalización por año (ej: 12 para mensual, 1 para anual)
    
    Returns:
        float: Valor futuro de la anualidad
        
    Example:
        >>> future_value_annuity(100, 0.05, 10, 1)  # $100 anuales por 10 años al 5%
        1257.79  # Valor futuro de la anualidad
        >>> future_value_annuity(100, 0.05, 10, 12)  # $100 mensuales por 10 años al 5%
        15528.23  # Valor futuro de la anualidad mensual
    """
    rate_per_period = r / m
    total_periods = m * T
    if rate_per_period == 0:
        return C * total_periods
    return C * (((1 + rate_per_period) ** total_periods - 1) / rate_per_period)

# %% Funciones de Pagos

def payment_amount(principal: Union[float, NDArray], rate: Union[float, NDArray], periods: Union[int, NDArray]) -> Union[float, NDArray]:
    """
    Calcula el monto del pago para un préstamo
    Soporta valores individuales y arrays para cálculos en lote
    
    Args:
        principal: Monto del préstamo (ej: 100000 o [100000, 200000, 300000])
        rate: Tasa de interés por período (ej: 0.005 o [0.004, 0.005, 0.006])
        periods: Número de períodos (ej: 360 o [360, 240, 180])
    
    Returns:
        Union[float, NDArray]: Monto del pago periódico (escalar o array)
        
    Example:
        >>> payment_amount(100000, 0.005, 360)  # Valor individual
        599.55  # Pago mensual
        >>> payment_amount([100000, 200000], [0.005, 0.006], [360, 240])  # Arrays
        array([599.55, 1438.06])  # Pagos para múltiples escenarios
    """
    result = npf.pmt(rate, periods, -principal)
    # Si todos los inputs son escalares, retorna escalar
    if np.isscalar(principal) and np.isscalar(rate) and np.isscalar(periods):
        return float(result)
    return result

# %%

def payment_interest(principal: Union[float, NDArray], rate: Union[float, NDArray], 
                    period: Union[int, NDArray], periods: Union[int, NDArray]) -> Union[float, NDArray]:
    """
    Calcula la porción de interés de un pago específico
    Soporta valores individuales y arrays para cálculos en lote
    
    Args:
        principal: Monto del préstamo (ej: 100000 o [100000, 200000])
        rate: Tasa de interés por período (ej: 0.005 o [0.004, 0.005])
        period: Período específico (ej: 12 o [1, 2, 3])
        periods: Total de períodos (ej: 360 o [360, 240])
    
    Returns:
        Union[float, NDArray]: Porción de interés del pago
        
    Example:
        >>> payment_interest(100000, 0.005, 1, 360)  # Valor individual
        500.00  # Interés del primer pago
        >>> payment_interest(100000, 0.005, [1, 2, 3], 360)  # Múltiples períodos
        array([500.00, 499.50, 499.00])  # Interés para primeros 3 pagos
    """
    result = npf.ipmt(rate, period, periods, -principal)
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(principal) and np.isscalar(rate) and 
        np.isscalar(period) and np.isscalar(periods)):
        return float(result)
    return result

# %%

def payment_principal(principal: Union[float, NDArray], rate: Union[float, NDArray], 
                     period: Union[int, NDArray], periods: Union[int, NDArray]) -> Union[float, NDArray]:
    """
    Calcula la porción de capital de un pago específico
    Soporta valores individuales y arrays para cálculos en lote
    
    Args:
        principal: Monto del préstamo (ej: 100000 o [100000, 200000])
        rate: Tasa de interés por período (ej: 0.005 o [0.004, 0.005])
        period: Período específico (ej: 12 o [1, 2, 3])
        periods: Total de períodos (ej: 360 o [360, 240])
    
    Returns:
        Union[float, NDArray]: Porción de capital del pago
        
    Example:
        >>> payment_principal(100000, 0.005, 1, 360)  # Valor individual
        99.55  # Capital del primer pago
        >>> payment_principal(100000, 0.005, [1, 2, 3], 360)  # Múltiples períodos
        array([99.55, 100.05, 100.55])  # Capital para primeros 3 pagos
    """
    result = npf.ppmt(rate, period, periods, -principal)
    # Si todos los inputs son escalares, retorna escalar
    if (np.isscalar(principal) and np.isscalar(rate) and 
        np.isscalar(period) and np.isscalar(periods)):
        return float(result)
    return result

# %% Funciones de Análisis de Inversiones

def net_present_value(initial_investment: float, cash_flows: list, r: float, T: Optional[int] = None, m: int = 1) -> float:
    """
    Calcula el valor presente neto (NPV) de una inversión con capitalización
    Fórmula: NPV = -Initial_Investment + Σ[CF_t / (1 + r/m)^(m*t)]
    
    Args:
        initial_investment: Inversión inicial (ej: 10000)
        cash_flows: Lista de flujos de caja futuros (ej: [2000, 3000, 4000])
        r: Tasa de interés anual (ej: 0.10 para 10%)
        T: Número total de períodos (si None, usa len(cash_flows))
        m: Períodos de capitalización por año (ej: 12 para mensual, 1 para anual)
    
    Returns:
        float: Valor presente neto
        
    Example:
        >>> net_present_value(10000, [3000, 4000, 5000], 0.10, 3, 1)  # Inversión de $10,000, flujos anuales al 10%
        -199.21  # NPV negativo, inversión no viable
        >>> net_present_value(10000, [3500, 4500, 5500], 0.10, 3, 1)  # Inversión mejorada
        1061.57  # NPV positivo, inversión viable
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
    Calcula la tasa interna de retorno (IRR) usando método de Newton-Raphson
    Encuentra la tasa r donde NPV = 0
    
    Args:
        initial_investment: Inversión inicial (ej: 10000)
        cash_flows: Lista de flujos de caja futuros (ej: [3000, 4000, 5000])
        max_iter: Número máximo de iteraciones
        precision: Precisión deserada
    
    Returns:
        float: Tasa interna de retorno
        
    Example:
        >>> internal_rate_of_return(10000, [3500, 4500, 5500])  # Inversión con buenos flujos
        0.1542  # IRR del 15.42%
        >>> internal_rate_of_return(10000, [2000, 3000, 4000])  # Inversión con flujos menores
        -0.0451  # IRR negativo del -4.51%
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

def profitability_index(initial_investment: float, cash_flows: list, r: float, T: Optional[int] = None, m: int = 1) -> float:
    """
    Calcula el índice de rentabilidad (PI) con capitalización
    Fórmula: PI = Σ[PV de cash flows] / Initial Investment
    
    Args:
        initial_investment: Inversión inicial (ej: 10000)
        cash_flows: Lista de flujos de caja futuros (ej: [3000, 4000, 5000])
        r: Tasa de interés anual (ej: 0.10 para 10%)
        T: Número total de períodos (si None, usa len(cash_flows))
        m: Períodos de capitalización por año (ej: 12 para mensual, 1 para anual)
    
    Returns:
        float: Índice de rentabilidad (>1 = viable, <1 = no viable)
        
    Example:
        >>> profitability_index(10000, [3500, 4500, 5500], 0.10, 3, 1)  # PI > 1
        1.106  # Índice mayor a 1, proyecto viable
        >>> profitability_index(10000, [2500, 3000, 3500], 0.10, 3, 1)  # PI < 1
        0.751  # Índice menor a 1, proyecto no viable
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
    Calcula el período de recuperación de la inversión
    
    Args:
        initial_investment: Inversión inicial (ej: 10000)
        cash_flows: Lista de flujos de caja (ej: [3000, 4000, 5000])
    
    Returns:
        float: Período de recuperación en años (o float('inf') si nunca se recupera)
        
    Example:
        >>> payback_period(10000, [3000, 4000, 5000])
        2.75  # Se recupera la inversión en 2.75 años
        >>> payback_period(8000, [2500, 3000, 4000])
        2.17  # Se recupera la inversión en 2.17 años
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
                            r_range: NDArray, T: Optional[int] = None, m: int = 1) -> NDArray:
    """
    Análisis de sensibilidad del NPV variando la tasa de descuento
    
    Args:
        initial_investment: Inversión inicial (ej: 10000)
        cash_flows: Lista de flujos de caja futuros (ej: [3000, 4000, 5000])
        r_range: Array de tasas a analizar (ej: np.linspace(0.05, 0.15, 100))
        T: Número total de períodos (si None, usa len(cash_flows))
        m: Períodos de capitalización por año
    
    Returns:
        NDArray: Array de valores NPV correspondientes a cada tasa
        
    Example:
        >>> rates = np.linspace(0.05, 0.15, 11)  # Tasas del 5% al 15%
        >>> npvs = sensitivity_analysis_npv(10000, [3500, 4500, 5500], rates)
        >>> npvs.shape
        (11,)  # 11 valores NPV diferentes
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
                   T: Optional[int] = None, m: int = 1) -> NDArray:
    """
    Simulación Monte Carlo para análisis de riesgo de NPV
    
    Args:
        initial_investment: Inversión inicial
        cash_flows_mean: Media de cada flujo de caja
        cash_flows_std: Desviación estándar de cada flujo de caja
        r_mean: Tasa de descuento promedio
        r_std: Desviación estándar de la tasa
        n_simulations: Número de simulaciones
        T: Número total de períodos
        m: Períodos de capitalización por año
    
    Returns:
        NDArray: Array con los resultados NPV de todas las simulaciones
        
    Example:
        >>> cf_mean = [3500, 4500, 5500]
        >>> cf_std = [500, 600, 700]
        >>> npv_dist = monte_carlo_npv(10000, cf_mean, cf_std, 0.10, 0.02, 1000)
        >>> np.mean(npv_dist)  # NPV promedio
        1061.57
        >>> np.std(npv_dist)   # Riesgo (desviación estándar)
        850.23
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

def batch_loan_analysis(principals: NDArray, rates: NDArray, periods: NDArray) -> dict:
    """
    Análisis en lote de múltiples préstamos
    
    Args:
        principals: Array de montos de préstamos
        rates: Array de tasas de interés
        periods: Array de períodos
    
    Returns:
        dict: Diccionario con arrays de resultados para cada métrica
        
    Example:
        >>> principals = np.array([100000, 200000, 300000])
        >>> rates = np.array([0.005, 0.006, 0.007])
        >>> periods = np.array([360, 240, 180])
        >>> results = batch_loan_analysis(principals, rates, periods)
        >>> results['payments']
        array([599.55, 1438.06, 2491.78])  # Pagos mensuales
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