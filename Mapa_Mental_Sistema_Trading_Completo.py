import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import numpy as np

# Configuración
plt.figure(figsize=(16, 20))
ax = plt.gca()
ax.set_xlim(0, 10)
ax.set_ylim(0, 24)
ax.axis('off')

# Colores del tema
color_header = '#1e3a8a'  # Azul oscuro
color_component = '#3b82f6'  # Azul medio
color_genai = '#10b981'  # Verde
color_warning = '#f59e0b'  # Naranja
color_text = '#1f2937'  # Gris oscuro

# ============================================================================
# TÍTULO PRINCIPAL
# ============================================================================
ax.text(5, 23, 'SISTEMA DE TRADING ALGORÍTMICO',
        ha='center', va='top', fontsize=20, fontweight='bold', color=color_header)
ax.text(5, 22.5, 'Aumentado con IA Generativa',
        ha='center', va='top', fontsize=14, color=color_header)

# ============================================================================
# COMPONENTE 1: DATA PIPELINE
# ============================================================================
y_start = 20.5

# Box principal
box1 = FancyBboxPatch((0.5, y_start), 9, 3,
                      boxstyle="round,pad=0.1",
                      edgecolor=color_component,
                      facecolor='#eff6ff',
                      linewidth=2)
ax.add_patch(box1)

# Título
ax.text(1, y_start + 2.7, '1️⃣ DATA PIPELINE',
        fontsize=14, fontweight='bold', color=color_component)
ax.text(1, y_start + 2.4, 'Fundación del Sistema',
        fontsize=10, color=color_text, style='italic')

# Inputs
ax.text(1, y_start + 1.8, '📥 INPUTS:', fontsize=10, fontweight='bold')
ax.text(1.2, y_start + 1.5, '• yfinance / Alpaca', fontsize=9)
ax.text(1.2, y_start + 1.2, '• Polygon.io', fontsize=9)
ax.text(1.2, y_start + 0.9, '• Bloomberg', fontsize=9)

# Procesos
ax.text(3.5, y_start + 1.8, '🔧 PROCESOS:', fontsize=10, fontweight='bold')
ax.text(3.7, y_start + 1.5, '• Descarga', fontsize=9)
ax.text(3.7, y_start + 1.2, '• Limpieza', fontsize=9)
ax.text(3.7, y_start + 0.9, '• Validación', fontsize=9)

# GenAI
ax.text(6, y_start + 1.8, '🤖 GENAI AUMENTA:', fontsize=10, fontweight='bold', color=color_genai)
ax.text(6.2, y_start + 1.5, '• Sugiere fuentes', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 1.2, '• Detecta gaps', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 0.9, '• Genera código', fontsize=9, color=color_genai)

# Outputs
ax.text(8.5, y_start + 1.8, '⚙️ OUTPUTS:', fontsize=10, fontweight='bold')
ax.text(8.7, y_start + 1.5, '• DataFrame', fontsize=9)
ax.text(8.7, y_start + 1.2, '• Metadata', fontsize=9)
ax.text(8.7, y_start + 0.9, '• Logs', fontsize=9)

# Conceptos clave
ax.text(1, y_start + 0.4, '📚 OHLCV • Adjusted Data • Gaps • Outliers',
        fontsize=8, style='italic', color='#6b7280')

# ============================================================================
# FLECHA HACIA COMPONENTE 2
# ============================================================================
arrow1 = FancyArrowPatch((5, y_start), (5, y_start - 0.5),
                         arrowstyle='->', mutation_scale=30,
                         linewidth=2, color=color_component)
ax.add_patch(arrow1)

# ============================================================================
# COMPONENTE 2: ESTRATEGIA
# ============================================================================
y_start -= 4

box2 = FancyBboxPatch((0.5, y_start), 9, 3,
                      boxstyle="round,pad=0.1",
                      edgecolor=color_component,
                      facecolor='#eff6ff',
                      linewidth=2)
ax.add_patch(box2)

ax.text(1, y_start + 2.7, '2️⃣ ESTRATEGIA',
        fontsize=14, fontweight='bold', color=color_component)
ax.text(1, y_start + 2.4, 'Cerebro del Sistema',
        fontsize=10, color=color_text, style='italic')

# Contenido
ax.text(1, y_start + 1.8, '📊 Indicadores:', fontsize=10, fontweight='bold')
ax.text(1.2, y_start + 1.5, '• Bollinger Bands', fontsize=9)
ax.text(1.2, y_start + 1.2, '• RSI, MACD', fontsize=9)
ax.text(1.2, y_start + 0.9, '• Machine Learning', fontsize=9)

ax.text(3.5, y_start + 1.8, '📐 Lógica:', fontsize=10, fontweight='bold')
ax.text(3.7, y_start + 1.5, '• Crossover', fontsize=9)
ax.text(3.7, y_start + 1.2, '• Breakout', fontsize=9)
ax.text(3.7, y_start + 0.9, '• Mean Reversion', fontsize=9)

ax.text(6, y_start + 1.8, '🤖 GENAI:', fontsize=10, fontweight='bold', color=color_genai)
ax.text(6.2, y_start + 1.5, '• Genera hipótesis', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 1.2, '• Implementa código', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 0.9, '• Sugiere features', fontsize=9, color=color_genai)

ax.text(8.5, y_start + 1.8, '🚦 SEÑALES:', fontsize=10, fontweight='bold')
ax.text(8.7, y_start + 1.5, '• BUY (1)', fontsize=9)
ax.text(8.7, y_start + 1.2, '• SELL (-1)', fontsize=9)
ax.text(8.7, y_start + 0.9, '• HOLD (0)', fontsize=9)

ax.text(1, y_start + 0.4, '📚 Edge • Alpha • Signals • Momentum',
        fontsize=8, style='italic', color='#6b7280')

# ============================================================================
# COMPONENTE 3: RISK MANAGEMENT
# ============================================================================
arrow2 = FancyArrowPatch((5, y_start), (5, y_start - 0.5),
                         arrowstyle='->', mutation_scale=30,
                         linewidth=2, color=color_component)
ax.add_patch(arrow2)

y_start -= 4

box3 = FancyBboxPatch((0.5, y_start), 9, 3,
                      boxstyle="round,pad=0.1",
                      edgecolor=color_warning,
                      facecolor='#fef3c7',
                      linewidth=2)
ax.add_patch(box3)

ax.text(1, y_start + 2.7, '3️⃣ RISK MANAGEMENT',
        fontsize=14, fontweight='bold', color=color_warning)
ax.text(1, y_start + 2.4, 'Frenos del Sistema',
        fontsize=10, color=color_text, style='italic')

ax.text(1, y_start + 1.8, '🛡️ Protección:', fontsize=10, fontweight='bold')
ax.text(1.2, y_start + 1.5, '• Position Sizing', fontsize=9)
ax.text(1.2, y_start + 1.2, '• Stop Loss', fontsize=9)
ax.text(1.2, y_start + 0.9, '• Circuit Breaker', fontsize=9)

ax.text(3.5, y_start + 1.8, '📊 Métricas:', fontsize=10, fontweight='bold')
ax.text(3.7, y_start + 1.5, '• Max Drawdown', fontsize=9)
ax.text(3.7, y_start + 1.2, '• Sharpe Ratio', fontsize=9)
ax.text(3.7, y_start + 0.9, '• Kelly Criterion', fontsize=9)

ax.text(6, y_start + 1.8, '🤖 GENAI:', fontsize=10, fontweight='bold', color=color_genai)
ax.text(6.2, y_start + 1.5, '• Simula "Black Swans"', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 1.2, '• Explica riesgos', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 0.9, '• Optimiza Sizing', fontsize=9, color=color_genai)

ax.text(1, y_start + 0.4, '📚 Drawdown • Volatility • Risk/Reward Ratio',
        fontsize=8, style='italic', color='#6b7280')

# ============================================================================
# COMPONENTE 4: BACKTESTING
# ============================================================================
arrow3 = FancyArrowPatch((5, y_start), (5, y_start - 0.5),
                         arrowstyle='->', mutation_scale=30,
                         linewidth=2, color=color_component)
ax.add_patch(arrow3)

y_start -= 4

box4 = FancyBboxPatch((0.5, y_start), 9, 3,
                      boxstyle="round,pad=0.1",
                      edgecolor=color_component,
                      facecolor='#eff6ff',
                      linewidth=2)
ax.add_patch(box4)

ax.text(1, y_start + 2.7, '4️⃣ BACKTESTING',
        fontsize=14, fontweight='bold', color=color_component)
ax.text(1, y_start + 2.4, 'Validación del Sistema',
        fontsize=10, color=color_text, style='italic')

ax.text(1, y_start + 1.8, '⚙️ Motores:', fontsize=10, fontweight='bold')
ax.text(1.2, y_start + 1.5, '• Vectorizado (rápido)', fontsize=9)
ax.text(1.2, y_start + 1.2, '• Event-Driven (realista)', fontsize=9)
ax.text(1.2, y_start + 0.9, '• backtrader / Zipline', fontsize=9)

ax.text(3.5, y_start + 1.8, '🔬 Análisis:', fontsize=10, fontweight='bold')
ax.text(3.7, y_start + 1.5, '• Reporte (HTML)', fontsize=9)
ax.text(3.7, y_start + 1.2, '• Gráficos PnL', fontsize=9)
ax.text(3.7, y_start + 0.9, '• Walk-Forward', fontsize=9)

ax.text(6, y_start + 1.8, '🤖 GENAI:', fontsize=10, fontweight='bold', color=color_genai)
ax.text(6.2, y_start + 1.5, '• Analiza reportes', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 1.2, '• Detecta Overfitting', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 0.9, '• Sugiere escenarios', fontsize=9, color=color_genai)

ax.text(1, y_start + 0.4, '📚 Overfitting • Lookahead Bias • Slippage • Commission',
        fontsize=8, style='italic', color='#6b7280')

# ============================================================================
# COMPONENTE 5: EXECUTION
# ============================================================================
arrow4 = FancyArrowPatch((5, y_start), (5, y_start - 0.5),
                         arrowstyle='->', mutation_scale=30,
                         linewidth=2, color=color_component)
ax.add_patch(arrow4)

y_start -= 4

box5 = FancyBboxPatch((0.5, y_start), 9, 3,
                      boxstyle="round,pad=0.1",
                      edgecolor=color_component,
                      facecolor='#eff6ff',
                      linewidth=2)
ax.add_patch(box5)

ax.text(1, y_start + 2.7, '5️⃣ EXECUTION',
        fontsize=14, fontweight='bold', color=color_component)
ax.text(1, y_start + 2.4, 'Interacción con el Mercado',
        fontsize=10, color=color_text, style='italic')

ax.text(1, y_start + 1.8, '📡 Conexión:', fontsize=10, fontweight='bold')
ax.text(1.2, y_start + 1.5, '• Broker API', fontsize=9)
ax.text(1.2, y_start + 1.2, '• Alpaca / IBKR', fontsize=9)
ax.text(1.2, y_start + 0.9, '• Paper vs. Live', fontsize=9)

ax.text(3.5, y_start + 1.8, '📈 Órdenes:', fontsize=10, fontweight='bold')
ax.text(3.7, y_start + 1.5, '• Market, Limit', fontsize=9)
ax.text(3.7, y_start + 1.2, '• Gestión de Posición', fontsize=9)
ax.text(3.7, y_start + 0.9, '• Monitoreo PnL', fontsize=9)

ax.text(6, y_start + 1.8, '🤖 GENAI:', fontsize=10, fontweight='bold', color=color_genai)
ax.text(6.2, y_start + 1.5, '• Monitorea logs', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 1.2, '• Interpreta news feeds', fontsize=9, color=color_genai)
ax.text(6.2, y_start + 0.9, '• Genera alertas', fontsize=9, color=color_genai)

ax.text(1, y_start + 0.4, '📚 Latency • API Keys • WebSockets • FIX Protocol',
        fontsize=8, style='italic', color='#6b7280')

# ============================================================================
# CAPA DE GENAI (abajo)
# ============================================================================
y_genai = 1.5 # Ajustado para dar espacio

box_genai = FancyBboxPatch((0.5, y_genai), 9, 1.5,
                           boxstyle="round,pad=0.1",
                           edgecolor=color_genai,
                           facecolor='#d1fae5',
                           linewidth=3,
                           linestyle='--')
ax.add_patch(box_genai)

ax.text(5, y_genai + 1.2, '🤖 CAPA DE IA GENERATIVA (TRANSVERSAL)',
        ha='center', fontsize=12, fontweight='bold', color=color_genai)

ax.text(1.5, y_genai + 0.7, '💡 Ideación', fontsize=9, color=color_genai)
ax.text(3.5, y_genai + 0.7, '🐛 Debugging', fontsize=9, color=color_genai)
ax.text(5.5, y_genai + 0.7, '🔄 Traducción', fontsize=9, color=color_genai)
ax.text(7.5, y_genai + 0.7, '📝 Documentación', fontsize=9, color=color_genai)

# ============================================================================
# MENSAJE FINAL
# ============================================================================
ax.text(5, 0.5, '⚠️ GenAI = COPILOTO (acelera) | TÚ = PILOTO (decides y validas)',
        ha='center', fontsize=11, fontweight='bold',
        color=color_warning,
        bbox=dict(boxstyle='round', facecolor='#fef3c7', edgecolor=color_warning, linewidth=2))

plt.tight_layout()
plt.savefig('Mapa_Mental_Sistema_Trading_Completo.png', dpi=300, bbox_inches='tight',
            facecolor='white', edgecolor='none')
plt.show()

print("✅ Diagrama completo generado: Mapa_Mental_Sistema_Trading_Completo.png")
