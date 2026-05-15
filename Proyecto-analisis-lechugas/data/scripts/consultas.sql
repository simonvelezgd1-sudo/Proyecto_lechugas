CREATE TABLE staging_lechugas (
    plant_id VARCHAR(50),
    fecha_raw VARCHAR(50),
    temp_c VARCHAR(50),
    humedad_pct VARCHAR(50),
    tds_ppm VARCHAR(50),
    ph_nivel VARCHAR(50),
    dias_crecimiento VARCHAR(50),
    temp_f VARCHAR(50),
    humedad_raw VARCHAR(50)
);

INSERT INTO staging_lechugas (
    plant_id, 
    fecha_raw, 
    temp_c, 
    humedad_pct, 
    tds_ppm, 
    ph_nivel, 
    dias_crecimiento, 
    temp_f, 
    humedad_raw
)
SELECT 
    CAST("Plant_ID" AS VARCHAR), 
    CAST("Date" AS VARCHAR), 
    CAST("Temperature (°C)" AS VARCHAR), 
    CAST("Humidity (%)" AS VARCHAR), 
    CAST("TDS Value (ppm)" AS VARCHAR), 
    CAST("pH Level" AS VARCHAR), 
    CAST("Growth Days" AS VARCHAR), 
    CAST("Temperature (F)" AS VARCHAR), 
    CAST("Humidity" AS VARCHAR)
FROM lechuga_dataset_update;
SELECT *,
row_number() OVER(
	PARTITION BY plant_id, fecha_raw, temp_c, humedad_pct, tds_ppm, ph_nivel
) AS numero_fila
FROM staging_lechugas;
update staging_lechugas 
set plant_id =TRIM(plant_id),
	fecha_raw=TRIM(fecha_raw),
	temp_c=TRIM(temp_c),
	ph_nivel=TRIM(ph_nivel);
select fecha_raw
from staging_lechugas 
limit 10;
select temp_c,
	cast(temp_c as decimal(10,2)) as temp_sumerica
from staging_lechugas 
limit 10;
create table lechugas_clean as 
select
	plant_id,
	cast(fecha_raw as date) fecha,
	cast( temp_c as decimal(10,2)) as temperature_c,
	cast(ph_nivel as decimal(10,2)) as ph,
	cast(dias_crecimiento as int) as dias_vida
from staging_lechugas;
select * from lechugas_clean limit 10;
select 
	count(*) as total_registros,
	round(avg(temperature_c), 2) as temperatura_promedio,
	min(ph) as ph_minimo,
	max(ph) as ph_maximo
from lechugas_clean;
SELECT 
    humedad_raw, 
    humedad_pct, 
    dias_crecimiento 
FROM staging_lechugas 
LIMIT 10;
SELECT 
    ROUND((humedad_raw::numeric * 100), 0) AS humedad_porcentaje_real, 
    AVG(dias_crecimiento::numeric) AS promedio_dias,
    COUNT(*) AS total_muestras
FROM staging_lechugas
GROUP BY humedad_porcentaje_real
ORDER BY promedio_dias ASC;
CREATE OR REPLACE VIEW reporte_crecimiento_lechugas AS
SELECT 
    ROUND((humedad_raw::numeric * 100), 0) AS humedad_entera, 
    AVG(dias_crecimiento::numeric) AS promedio_crecimiento,   
    COUNT(*) AS numero_muestras                             
FROM staging_lechugas 
GROUP BY humedad_entera
ORDER BY promedio_crecimiento ASC;
select 
	round(humedad_raw::numeric *100,0) as hum,
	avg(temp_c::numeric) as prom_temp
from staging_lechugas 
where round(humedad_raw::numeric * 100,0) in (73,74)
group by hum;
select
	FLOOR(temp_c::numeric) as rango_temp,
	avg(dias_crecimiento::numeric) as crecimiento_prom,
	avg(humedad_raw::numeric * 100) as hum_prom,
	count(*) as total_muestras
from staging_lechugas sl 
group by rango_temp 
order by rango_temp asc;
create table lecguhas_promedio(
	id serial primary key,
	temperature_c float,
	humedad_raw float,
	ph_nivel float,
	tds_ppm float
	);
INSERT INTO lecguhas_promedio (temperature_c, humedad_raw, ph_nivel, tds_ppm)
SELECT 
    temp_c::FLOAT, 
    humedad_raw::FLOAT, 
    ph_nivel::FLOAT, 
    tds_ppm::FLOAT
FROM staging_lechugas;
SELECT 
    COUNT(*) AS total_mediciones,
    ROUND(AVG(temperature_c), 2) AS temp_promedio,
    ROUND(AVG(ph_nivel), 2) AS ph_promedio,
    MIN(ph_nivel) AS ph_mi
    MAX(ph_nivel) AS ph_maximo
FROM lecguhas_promedio;SELECT 
    COUNT(*) AS total_mediciones,
    ROUND(AVG(temperature_c)::numeric, 2) AS temp_promedio,
    ROUND(AVG(ph_nivel)::numeric, 2) AS ph_promedio,
    MIN(ph_nivel) AS ph_minimo,
    MAX(ph_nivel) AS ph_maximo
FROM lecguhas_promedio;
select count(*) as alertas_de_calor
from lecguhas_promedio
where temperature_c >25;
select 
	round(avg(tds_ppm)::numeric,2) as nutrientes_sueltos,
	min(tds_ppm) as nutrientes_min,
	max(tds_ppm)as nutrientes_max  
	from lecguhas_promedio;
select 
	COUNT(*) as Total_registros,
	date(fecha_raw) as fecha_Cultivo,
	cast(dias_crecimiento as integer) as list_day,
	MIN(humedad_pct) as pct_hum_min,
	MAX(humedad_pct) as pct_hum_max
from staging_lechugas sl 
group by
	date(fecha_raw),
	cast(dias_crecimiento as integer);
select
	count(*) as total_muestras,
	cast(AVG(ph_nivel) as DECIMAL (10,2)) as PH_LIMIT,
	floor(ph_nivel / 6.5) as limite
from staging_lechugas sl 
where cantidad > 6.5
group by 	
	floor(ph_nivel /6.5)

order by PH_LIMIT desc;
