-- Análisis de crecimiento promedio por temperatura
SELECT 
    Temperatura, 
    AVG(Crecimiento) AS Promedio_Crecimiento
FROM Tabla_Lechugas
GROUP BY Temperatura
ORDER BY Promedio_Crecimiento DESC;