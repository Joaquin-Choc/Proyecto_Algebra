import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Tuple

class NetworkOptimizer:
    """Clase para modelar y optimizar el sistema de redes de comunicaciones"""

    def __init__(self, num_nodes: int = 3):
        """Inicializar el optimizador de red
        Args:
            num_nodes (int): Número de nodos en la red.
        """
        self.num_nodes = num_nodes
        self.A = None  
        self.B = None  
        self.X = None  
        self.A_inv = None
    
    def create_connectivity_matrix(self, connections: List[Tuple[int, int, float]] = None) -> np.ndarray:
        """
        Crea la matriz A de conectividad basada en las conexiones entre nodos.
        
        Args:
            connections: Lista de tuplas (nodo_origen, nodo_destino, flujo)
                        Si es None, usa la configuración por defecto del proyecto
        
        Returns:
            Matriz A de conectividad
        """
        # Inicializar matriz con ceros
        A = np.zeros((self.num_nodes, self.num_nodes))

        if connections is None:
            # Configuración por defecto
            A = np.array([
                [-2, 1, 1],
                [1, -2, 1],
                [1, 1, -2]
            ], dtype=float)
        else:
            #Contruir matriz basada en conexiones proporcionadas
            for i in range(self.num_nodes):
            