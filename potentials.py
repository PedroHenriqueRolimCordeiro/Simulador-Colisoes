# Funções para calcular forças de interação
import numpy as np

def lennard_jones_force(r, epsilon, sigma):
    """
    Calcula a magnitude da força de Lennard-Jones entre duas partículas.

    Parâmetros:
    r (float): Distância entre as duas partículas.
    epsilon (float): Profundidade do poço de potencial (parâmetro de energia).
    sigma (float): Distância onde o potencial é zero (parâmetro de distância).

    Retorna:
    float: A magnitude da força de Lennard-Jones.
    """
    if r == 0:     #Evitar divisão por zero se as partículas estiverem na mesma direção
        return 0.0
    
    # A fórmula é F = 24 * epsilon * (2 * (sigma**12 / r**13) - (sigma**6 / r**7)) 
    
    # Termos intermediarios
    sigma_over_r = sigma / r
    sigma_over_r_6 = sigma_over_r**6
    sigma_over_r_12 = sigma_over_r**12

    # Calculo da magnitude da força
    force_magnitude = 24 * epsilon * (2 * sigma_over_r_12 / r - sigma_over_r_6 / r)

    return force_magnitude

# --- teste ---
if __name__ == "__main__":
    # Constantes de exemplo para teste
    epsilon_val = 0.0103 # eV
    sigma_val = 3.4      # Angstrom

    distances = np.linspace(2.0, 5.0, 100) # Distâncias de 2.0 a 5.0 Angstroms
    forces = [lennard_jones_force(d, epsilon_val, sigma_val) for d in distances]

    import matplotlib.pyplot as plt
    plt.figure(figsize=(8, 6))
    plt.plot(distances, forces, label='Força de Lennard-Jones')
    plt.axhline(0, color='gray', linestyle='--', linewidth=0.8) # Linha zero
    plt.xlabel('Distância (r)')
    plt.ylabel('Força (F)')
    plt.title('Força de Lennard-Jones vs. Distância')
    plt.grid(True)
    plt.legend()
    plt.show()

    test_r = 3.8
    force_at_test_r = lennard_jones_force(test_r, epsilon_val, sigma_val)
    print(f"\nForça de LJ em r={test_r:.2f} Å: {force_at_test_r:.4f} eV/Å")
    # Lembrete
    # Se a força for positiva, é repulsiva; se negativa, é atrativa.
    # Para r < sigma (3.4), a força deve ser repulsiva (positiva).
    # Para r > sigma, a força deve ser atrativa (negativa), até um certo ponto.